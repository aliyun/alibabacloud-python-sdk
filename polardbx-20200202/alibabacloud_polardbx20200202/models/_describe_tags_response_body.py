# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeTagsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tag_infos: List[main_models.DescribeTagsResponseBodyTagInfos] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tag_infos = tag_infos

    def validate(self):
        if self.tag_infos:
            for v1 in self.tag_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TagInfos'] = []
        if self.tag_infos is not None:
            for k1 in self.tag_infos:
                result['TagInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tag_infos = []
        if m.get('TagInfos') is not None:
            for k1 in m.get('TagInfos'):
                temp_model = main_models.DescribeTagsResponseBodyTagInfos()
                self.tag_infos.append(temp_model.from_map(k1))

        return self

class DescribeTagsResponseBodyTagInfos(DaraModel):
    def __init__(
        self,
        dbinstance_ids: List[str] = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.dbinstance_ids = dbinstance_ids
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

