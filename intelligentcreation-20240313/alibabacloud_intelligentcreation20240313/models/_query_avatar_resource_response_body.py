# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class QueryAvatarResourceResponseBody(DaraModel):
    def __init__(
        self,
        query_resource_info_list: List[main_models.QueryAvatarResourceResponseBodyQueryResourceInfoList] = None,
        request_id: str = None,
    ):
        self.query_resource_info_list = query_resource_info_list
        self.request_id = request_id

    def validate(self):
        if self.query_resource_info_list:
            for v1 in self.query_resource_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['queryResourceInfoList'] = []
        if self.query_resource_info_list is not None:
            for k1 in self.query_resource_info_list:
                result['queryResourceInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_resource_info_list = []
        if m.get('queryResourceInfoList') is not None:
            for k1 in m.get('queryResourceInfoList'):
                temp_model = main_models.QueryAvatarResourceResponseBodyQueryResourceInfoList()
                self.query_resource_info_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryAvatarResourceResponseBodyQueryResourceInfoList(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        type: str = None,
        valid_period_time: str = None,
    ):
        self.resource_id = resource_id
        self.type = type
        self.valid_period_time = valid_period_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.type is not None:
            result['type'] = self.type

        if self.valid_period_time is not None:
            result['validPeriodTime'] = self.valid_period_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('validPeriodTime') is not None:
            self.valid_period_time = m.get('validPeriodTime')

        return self

