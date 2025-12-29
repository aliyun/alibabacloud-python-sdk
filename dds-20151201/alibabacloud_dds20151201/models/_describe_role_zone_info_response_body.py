# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeRoleZoneInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zone_infos: main_models.DescribeRoleZoneInfoResponseBodyZoneInfos = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information of nodes in the zone.
        self.zone_infos = zone_infos

    def validate(self):
        if self.zone_infos:
            self.zone_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.zone_infos is not None:
            result['ZoneInfos'] = self.zone_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ZoneInfos') is not None:
            temp_model = main_models.DescribeRoleZoneInfoResponseBodyZoneInfos()
            self.zone_infos = temp_model.from_map(m.get('ZoneInfos'))

        return self

class DescribeRoleZoneInfoResponseBodyZoneInfos(DaraModel):
    def __init__(
        self,
        zone_info: List[main_models.DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo] = None,
    ):
        self.zone_info = zone_info

    def validate(self):
        if self.zone_info:
            for v1 in self.zone_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ZoneInfo'] = []
        if self.zone_info is not None:
            for k1 in self.zone_info:
                result['ZoneInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_info = []
        if m.get('ZoneInfo') is not None:
            for k1 in m.get('ZoneInfo'):
                temp_model = main_models.DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo()
                self.zone_info.append(temp_model.from_map(k1))

        return self

class DescribeRoleZoneInfoResponseBodyZoneInfosZoneInfo(DaraModel):
    def __init__(
        self,
        ins_name: str = None,
        node_type: str = None,
        role_id: str = None,
        role_type: str = None,
        zone_id: str = None,
    ):
        # The ID of the node.
        self.ins_name = ins_name
        # The type of the node. Valid values:
        # 
        # *   **normal**
        # *   **configServer**
        # *   **shard**
        # *   **mongos**
        # 
        # > Valid value for replica set instances: **normal**. Valid values for sharded cluster instances: **configServer**, **shard**, and **mongos**.
        self.node_type = node_type
        # The role ID.
        self.role_id = role_id
        # The role of the node. Valid values:
        # 
        # *   **Primary**
        # *   **Secondary**
        # *   **Hidden**
        self.role_type = role_type
        # The zone ID of the node.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

