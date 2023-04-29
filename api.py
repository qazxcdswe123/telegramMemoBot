import re

from aiohttp import ClientTimeout, ClientResponse
from aiohttp.formdata import FormData
from aiohttp_retry import RetryClient, ClientSession


class Request:
    def __init__(self, *args, **kwargs):
        self.client_session = ClientSession()
        self.retry_client = RetryClient(client_session=self.client_session)
        self.request = self.retry_client.request(*args, **kwargs)

    async def __aenter__(self) -> ClientResponse:
        return await self.request

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client_session.close()
        await self.retry_client.close()


def request(method, url, data=None, json=None):
    if json is not None:
        return Request(method, url, json=json, timeout=ClientTimeout(total=1000))
    else:
        return Request(method, url, data=data, timeout=ClientTimeout(total=1000))


class Memo:
    def __init__(self, domain, openid):
        self.domain = domain
        self.openid = openid
        self.url = f"{domain}api/memo?openId={openid}"

    async def send_memo(self, content="", visibility="PRIVATE", res_id_list=None):
        if res_id_list is None:
            res_id_list = []
        data = {
            "content": content,
            "visibility": visibility,
            "resourceIdList": res_id_list,
        }
        tags = re.findall(r"#\S+", content)
        if tags:
            tag = Tag(self.domain, self.openid)
            for t in tags:
                t = t.replace("#", "")
                await tag.create_tag(t)
        async with request("POST", url=self.url, json=data) as resp:
            assert resp.status == 200
            resp_data = await resp.json()
            return resp_data["data"]["id"]


class Resource:
    def __init__(self, domain, openid):
        self.url = f"{domain}api/resource/blob?openId={openid}"

    async def create_res(self, file):
        data = FormData()
        data.add_field("file", file, filename="telegram-file.jpg", content_type="image/jpeg")
        async with request("POST", url=self.url, data=data) as resp:
            assert resp.status == 200
            resp_data = await resp.json()
            return resp_data["data"]["id"]


class Tag:
    def __init__(self, domain, openid):
        self.url = f"{domain}api/tag?openId={openid}"

    async def create_tag(self, name):
        data = {"name": name}
        async with request("POST", url=self.url, json=data) as resp:
            assert resp.status == 200
