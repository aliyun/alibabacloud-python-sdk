# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryTagsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tag_infos: main_models.QueryTagsResponseBodyTagInfos = None,
    ):
        self.request_id = request_id
        self.tag_infos = tag_infos

    def validate(self):
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagInfos') is not None:
            temp_model = main_models.QueryTagsResponseBodyTagInfos()
            self.tag_infos = temp_model.from_map(m.get('TagInfos'))

        return self

class QueryTagsResponseBodyTagInfos(DaraModel):
    def __init__(
        self,
        tag_info: List[main_models.QueryTagsResponseBodyTagInfosTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for v1 in self.tag_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k1 in self.tag_info:
                result['TagInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k1 in m.get('TagInfo'):
                temp_model = main_models.QueryTagsResponseBodyTagInfosTagInfo()
                self.tag_info.append(temp_model.from_map(k1))

        return self

class QueryTagsResponseBodyTagInfosTagInfo(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
    ):
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

