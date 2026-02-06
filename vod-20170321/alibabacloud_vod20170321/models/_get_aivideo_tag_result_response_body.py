# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetAIVideoTagResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        video_tag_result: main_models.GetAIVideoTagResultResponseBodyVideoTagResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.video_tag_result = video_tag_result

    def validate(self):
        if self.video_tag_result:
            self.video_tag_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.video_tag_result is not None:
            result['VideoTagResult'] = self.video_tag_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VideoTagResult') is not None:
            temp_model = main_models.GetAIVideoTagResultResponseBodyVideoTagResult()
            self.video_tag_result = temp_model.from_map(m.get('VideoTagResult'))

        return self

class GetAIVideoTagResultResponseBodyVideoTagResult(DaraModel):
    def __init__(
        self,
        category: List[main_models.GetAIVideoTagResultResponseBodyVideoTagResultCategory] = None,
        keyword: List[main_models.GetAIVideoTagResultResponseBodyVideoTagResultKeyword] = None,
        location: List[main_models.GetAIVideoTagResultResponseBodyVideoTagResultLocation] = None,
        person: List[main_models.GetAIVideoTagResultResponseBodyVideoTagResultPerson] = None,
        time: List[main_models.GetAIVideoTagResultResponseBodyVideoTagResultTime] = None,
    ):
        # The video categories.
        self.category = category
        # The keyword tags.
        self.keyword = keyword
        # The location tags.
        self.location = location
        # The figure tags.
        self.person = person
        # The time tags.
        self.time = time

    def validate(self):
        if self.category:
            for v1 in self.category:
                 if v1:
                    v1.validate()
        if self.keyword:
            for v1 in self.keyword:
                 if v1:
                    v1.validate()
        if self.location:
            for v1 in self.location:
                 if v1:
                    v1.validate()
        if self.person:
            for v1 in self.person:
                 if v1:
                    v1.validate()
        if self.time:
            for v1 in self.time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Category'] = []
        if self.category is not None:
            for k1 in self.category:
                result['Category'].append(k1.to_map() if k1 else None)

        result['Keyword'] = []
        if self.keyword is not None:
            for k1 in self.keyword:
                result['Keyword'].append(k1.to_map() if k1 else None)

        result['Location'] = []
        if self.location is not None:
            for k1 in self.location:
                result['Location'].append(k1.to_map() if k1 else None)

        result['Person'] = []
        if self.person is not None:
            for k1 in self.person:
                result['Person'].append(k1.to_map() if k1 else None)

        result['Time'] = []
        if self.time is not None:
            for k1 in self.time:
                result['Time'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category = []
        if m.get('Category') is not None:
            for k1 in m.get('Category'):
                temp_model = main_models.GetAIVideoTagResultResponseBodyVideoTagResultCategory()
                self.category.append(temp_model.from_map(k1))

        self.keyword = []
        if m.get('Keyword') is not None:
            for k1 in m.get('Keyword'):
                temp_model = main_models.GetAIVideoTagResultResponseBodyVideoTagResultKeyword()
                self.keyword.append(temp_model.from_map(k1))

        self.location = []
        if m.get('Location') is not None:
            for k1 in m.get('Location'):
                temp_model = main_models.GetAIVideoTagResultResponseBodyVideoTagResultLocation()
                self.location.append(temp_model.from_map(k1))

        self.person = []
        if m.get('Person') is not None:
            for k1 in m.get('Person'):
                temp_model = main_models.GetAIVideoTagResultResponseBodyVideoTagResultPerson()
                self.person.append(temp_model.from_map(k1))

        self.time = []
        if m.get('Time') is not None:
            for k1 in m.get('Time'):
                temp_model = main_models.GetAIVideoTagResultResponseBodyVideoTagResultTime()
                self.time.append(temp_model.from_map(k1))

        return self

class GetAIVideoTagResultResponseBodyVideoTagResultTime(DaraModel):
    def __init__(
        self,
        tag: str = None,
        times: List[str] = None,
    ):
        # The tag string.
        self.tag = tag
        # The points in time when the tags are displayed. Unit: milliseconds.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag is not None:
            result['Tag'] = self.tag

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class GetAIVideoTagResultResponseBodyVideoTagResultPerson(DaraModel):
    def __init__(
        self,
        face_url: str = None,
        tag: str = None,
        times: List[str] = None,
    ):
        # The URL of the profile photo.
        # 
        # > This parameter is returned only when a figure tag was used.
        self.face_url = face_url
        # The tag string.
        self.tag = tag
        # The points in time when the tags are displayed. Unit: milliseconds.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class GetAIVideoTagResultResponseBodyVideoTagResultLocation(DaraModel):
    def __init__(
        self,
        tag: str = None,
        times: List[str] = None,
    ):
        # The tag string.
        self.tag = tag
        # The points in time when the tags are displayed. Unit: milliseconds.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag is not None:
            result['Tag'] = self.tag

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class GetAIVideoTagResultResponseBodyVideoTagResultKeyword(DaraModel):
    def __init__(
        self,
        tag: str = None,
        times: List[str] = None,
    ):
        # The tag string.
        self.tag = tag
        # The points in time when the tags are displayed. Unit: milliseconds.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag is not None:
            result['Tag'] = self.tag

        if self.times is not None:
            result['Times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        return self

class GetAIVideoTagResultResponseBodyVideoTagResultCategory(DaraModel):
    def __init__(
        self,
        tag: str = None,
    ):
        # The tag string.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

