# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListSearchTaskDialogueDatasResponseBody(DaraModel):
    def __init__(
        self,
        articles: List[main_models.ListSearchTaskDialogueDatasResponseBodyArticles] = None,
        audios: List[main_models.ListSearchTaskDialogueDatasResponseBodyAudios] = None,
        code: str = None,
        http_status_code: int = None,
        images: List[main_models.ListSearchTaskDialogueDatasResponseBodyImages] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        realtime_search: bool = None,
        request_id: str = None,
        search_type: str = None,
        success: bool = None,
        total_count: int = None,
        videos: List[main_models.ListSearchTaskDialogueDatasResponseBodyVideos] = None,
    ):
        self.articles = articles
        self.audios = audios
        self.code = code
        self.http_status_code = http_status_code
        self.images = images
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.realtime_search = realtime_search
        self.request_id = request_id
        self.search_type = search_type
        self.success = success
        self.total_count = total_count
        self.videos = videos

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()
        if self.audios:
            for v1 in self.audios:
                 if v1:
                    v1.validate()
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.videos:
            for v1 in self.videos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Articles'] = []
        if self.articles is not None:
            for k1 in self.articles:
                result['Articles'].append(k1.to_map() if k1 else None)

        result['Audios'] = []
        if self.audios is not None:
            for k1 in self.audios:
                result['Audios'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.realtime_search is not None:
            result['RealtimeSearch'] = self.realtime_search

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.search_type is not None:
            result['SearchType'] = self.search_type

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Videos'] = []
        if self.videos is not None:
            for k1 in self.videos:
                result['Videos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.ListSearchTaskDialogueDatasResponseBodyArticles()
                self.articles.append(temp_model.from_map(k1))

        self.audios = []
        if m.get('Audios') is not None:
            for k1 in m.get('Audios'):
                temp_model = main_models.ListSearchTaskDialogueDatasResponseBodyAudios()
                self.audios.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ListSearchTaskDialogueDatasResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RealtimeSearch') is not None:
            self.realtime_search = m.get('RealtimeSearch')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.videos = []
        if m.get('Videos') is not None:
            for k1 in m.get('Videos'):
                temp_model = main_models.ListSearchTaskDialogueDatasResponseBodyVideos()
                self.videos.append(temp_model.from_map(k1))

        return self

class ListSearchTaskDialogueDatasResponseBodyVideos(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class ListSearchTaskDialogueDatasResponseBodyImages(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class ListSearchTaskDialogueDatasResponseBodyAudios(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
    ):
        self.file_url = file_url
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class ListSearchTaskDialogueDatasResponseBodyArticles(DaraModel):
    def __init__(
        self,
        author: str = None,
        category_uuid: str = None,
        content: str = None,
        doc_id: str = None,
        doc_type: str = None,
        doc_uuid: str = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        multimodal_medias: List[main_models.ListSearchTaskDialogueDatasResponseBodyArticlesMultimodalMedias] = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.category_uuid = category_uuid
        self.content = content
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.doc_uuid = doc_uuid
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.multimodal_medias = multimodal_medias
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        if self.multimodal_medias:
            for v1 in self.multimodal_medias:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['Author'] = self.author

        if self.category_uuid is not None:
            result['CategoryUuid'] = self.category_uuid

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        result['MultimodalMedias'] = []
        if self.multimodal_medias is not None:
            for k1 in self.multimodal_medias:
                result['MultimodalMedias'].append(k1.to_map() if k1 else None)

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('CategoryUuid') is not None:
            self.category_uuid = m.get('CategoryUuid')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        self.multimodal_medias = []
        if m.get('MultimodalMedias') is not None:
            for k1 in m.get('MultimodalMedias'):
                temp_model = main_models.ListSearchTaskDialogueDatasResponseBodyArticlesMultimodalMedias()
                self.multimodal_medias.append(temp_model.from_map(k1))

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListSearchTaskDialogueDatasResponseBodyArticlesMultimodalMedias(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

