# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class ListAclGroupsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.ListAclGroupsResponseBodyData] = None,
        http_status_code: int = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id

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
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAclGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListAclGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        cidrs: List[str] = None,
        create_time: str = None,
        group_name: str = None,
        id: int = None,
        instance_id: str = None,
        uid: int = None,
    ):
        self.cidrs = cidrs
        self.create_time = create_time
        self.group_name = group_name
        self.id = id
        self.instance_id = instance_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidrs is not None:
            result['cidrs'] = self.cidrs

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.id is not None:
            result['id'] = self.id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cidrs') is not None:
            self.cidrs = m.get('cidrs')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

