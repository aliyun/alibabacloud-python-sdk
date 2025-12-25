# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListHotNewsWithTypeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListHotNewsWithTypeResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListHotNewsWithTypeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListHotNewsWithTypeResponseBodyData(DaraModel):
    def __init__(
        self,
        news: List[main_models.ListHotNewsWithTypeResponseBodyDataNews] = None,
        news_type: str = None,
        news_type_name: str = None,
        total_pages: int = None,
    ):
        self.news = news
        self.news_type = news_type
        self.news_type_name = news_type_name
        self.total_pages = total_pages

    def validate(self):
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['News'] = []
        if self.news is not None:
            for k1 in self.news:
                result['News'].append(k1.to_map() if k1 else None)

        if self.news_type is not None:
            result['NewsType'] = self.news_type

        if self.news_type_name is not None:
            result['NewsTypeName'] = self.news_type_name

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.news = []
        if m.get('News') is not None:
            for k1 in m.get('News'):
                temp_model = main_models.ListHotNewsWithTypeResponseBodyDataNews()
                self.news.append(temp_model.from_map(k1))

        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')

        if m.get('NewsTypeName') is not None:
            self.news_type_name = m.get('NewsTypeName')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListHotNewsWithTypeResponseBodyDataNews(DaraModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_uuid: str = None,
        image_urls: List[str] = None,
        pub_time: str = None,
        search_source: str = None,
        search_source_name: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        update_time: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_uuid = doc_uuid
        self.image_urls = image_urls
        self.pub_time = pub_time
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.update_time = update_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['Author'] = self.author

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

