# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListHotViewPointsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListHotViewPointsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListHotViewPointsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHotViewPointsResponseBodyData(DaraModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        news: List[main_models.ListHotViewPointsResponseBodyDataNews] = None,
        ratio: str = None,
        view_points: List[main_models.ListHotViewPointsResponseBodyDataViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.news = news
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()
        if self.view_points:
            for v1 in self.view_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type

        result['News'] = []
        if self.news is not None:
            for k1 in self.news:
                result['News'].append(k1.to_map() if k1 else None)

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        result['ViewPoints'] = []
        if self.view_points is not None:
            for k1 in self.view_points:
                result['ViewPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')

        self.news = []
        if m.get('News') is not None:
            for k1 in m.get('News'):
                temp_model = main_models.ListHotViewPointsResponseBodyDataNews()
                self.news.append(temp_model.from_map(k1))

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k1 in m.get('ViewPoints'):
                temp_model = main_models.ListHotViewPointsResponseBodyDataViewPoints()
                self.view_points.append(temp_model.from_map(k1))

        return self

class ListHotViewPointsResponseBodyDataViewPoints(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.ListHotViewPointsResponseBodyDataViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.ListHotViewPointsResponseBodyDataViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class ListHotViewPointsResponseBodyDataViewPointsOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class ListHotViewPointsResponseBodyDataNews(DaraModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        image_urls: List[str] = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tags: List[str] = None,
        title: str = None,
        topic: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.image_urls = image_urls
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tags = tags
        self.title = title
        self.topic = topic
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

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

