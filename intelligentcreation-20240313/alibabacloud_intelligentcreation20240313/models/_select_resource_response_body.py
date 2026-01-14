# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class SelectResourceResponseBody(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        request_id: str = None,
        resource_info_list: List[main_models.SelectResourceResponseBodyResourceInfoList] = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.request_id = request_id
        self.resource_info_list = resource_info_list

    def validate(self):
        if self.resource_info_list:
            for v1 in self.resource_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['aliyunUid'] = self.aliyun_uid

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resourceInfoList'] = []
        if self.resource_info_list is not None:
            for k1 in self.resource_info_list:
                result['resourceInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunUid') is not None:
            self.aliyun_uid = m.get('aliyunUid')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.resource_info_list = []
        if m.get('resourceInfoList') is not None:
            for k1 in m.get('resourceInfoList'):
                temp_model = main_models.SelectResourceResponseBodyResourceInfoList()
                self.resource_info_list.append(temp_model.from_map(k1))

        return self

class SelectResourceResponseBodyResourceInfoList(DaraModel):
    def __init__(
        self,
        expire_time: str = None,
        last_expire: int = None,
        remain_count: int = None,
        resource_type: int = None,
        unit: str = None,
    ):
        self.expire_time = expire_time
        self.last_expire = last_expire
        self.remain_count = remain_count
        self.resource_type = resource_type
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.last_expire is not None:
            result['lastExpire'] = self.last_expire

        if self.remain_count is not None:
            result['remainCount'] = self.remain_count

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('lastExpire') is not None:
            self.last_expire = m.get('lastExpire')

        if m.get('remainCount') is not None:
            self.remain_count = m.get('remainCount')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

