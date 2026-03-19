# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class ListValueAddedResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        value_added_list: List[main_models.ListValueAddedResponseBodyValueAddedList] = None,
    ):
        self.request_id = request_id
        self.value_added_list = value_added_list

    def validate(self):
        if self.value_added_list:
            for v1 in self.value_added_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ValueAddedList'] = []
        if self.value_added_list is not None:
            for k1 in self.value_added_list:
                result['ValueAddedList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.value_added_list = []
        if m.get('ValueAddedList') is not None:
            for k1 in m.get('ValueAddedList'):
                temp_model = main_models.ListValueAddedResponseBodyValueAddedList()
                self.value_added_list.append(temp_model.from_map(k1))

        return self

class ListValueAddedResponseBodyValueAddedList(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        gmt_create: int = None,
        instance_id: str = None,
        log_size: int = None,
        status: int = None,
        store_region: str = None,
    ):
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.log_size = log_size
        self.status = status
        self.store_region = store_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_size is not None:
            result['LogSize'] = self.log_size

        if self.status is not None:
            result['Status'] = self.status

        if self.store_region is not None:
            result['StoreRegion'] = self.store_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoreRegion') is not None:
            self.store_region = m.get('StoreRegion')

        return self

