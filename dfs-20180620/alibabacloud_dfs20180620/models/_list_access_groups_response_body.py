# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class ListAccessGroupsResponseBody(DaraModel):
    def __init__(
        self,
        access_groups: List[main_models.ListAccessGroupsResponseBodyAccessGroups] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.access_groups = access_groups
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.access_groups:
            for v1 in self.access_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessGroups'] = []
        if self.access_groups is not None:
            for k1 in self.access_groups:
                result['AccessGroups'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_groups = []
        if m.get('AccessGroups') is not None:
            for k1 in m.get('AccessGroups'):
                temp_model = main_models.ListAccessGroupsResponseBodyAccessGroups()
                self.access_groups.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAccessGroupsResponseBodyAccessGroups(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_group_name: str = None,
        create_time: str = None,
        description: str = None,
        is_default: bool = None,
        mount_point_count: int = None,
        network_type: str = None,
        region_id: str = None,
        rule_count: int = None,
    ):
        self.access_group_id = access_group_id
        self.access_group_name = access_group_name
        self.create_time = create_time
        self.description = description
        self.is_default = is_default
        self.mount_point_count = mount_point_count
        self.network_type = network_type
        self.region_id = region_id
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

