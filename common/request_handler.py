import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RequestHandler:
    def __init__(self, base_url=""):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, **kwargs):
        """发送 GET 请求"""
        url = self.base_url + path
        logging.info(f"GET {url}")
        return self.session.get(url, **kwargs)

    def post(self, path, **kwargs):
        """发送 POST 请求"""
        url = self.base_url + path
        logging.info(f"POST {url}")
        return self.session.post(url, **kwargs)