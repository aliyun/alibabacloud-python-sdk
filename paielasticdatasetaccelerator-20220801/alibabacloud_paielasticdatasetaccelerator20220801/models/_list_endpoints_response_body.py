# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paielasticdatasetaccelerator20220801 import models as main_models
from darabonba.model import DaraModel

class ListEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        endpoints: List[main_models.ListEndpointsResponseBodyEndpoints] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.endpoints = endpoints
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEndpointsResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        instance_id: str = None,
        name: str = None,
        owner_id: str = None,
        status: main_models.EndpointStatus = None,
        type: str = None,
        user_id: str = None,
        uuid: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        # 所属加速实例的ID。
        self.instance_id = instance_id
        self.name = name
        self.owner_id = owner_id
        self.status = status
        self.type = type
        self.user_id = user_id
        self.uuid = uuid
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Status') is not None:
            temp_model = main_models.EndpointStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

