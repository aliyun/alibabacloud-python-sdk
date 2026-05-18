# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class ListMountPointsResponseBody(DaraModel):
    def __init__(
        self,
        mount_points: List[main_models.ListMountPointsResponseBodyMountPoints] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.mount_points = mount_points
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.mount_points:
            for v1 in self.mount_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['MountPoints'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k1 in m.get('MountPoints'):
                temp_model = main_models.ListMountPointsResponseBodyMountPoints()
                self.mount_points.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMountPointsResponseBodyMountPoints(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        mount_point_alias: str = None,
        mount_point_domain: str = None,
        mount_point_id: str = None,
        network_type: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.access_group_id = access_group_id
        self.create_time = create_time
        self.description = description
        self.file_system_id = file_system_id
        self.mount_point_alias = mount_point_alias
        self.mount_point_domain = mount_point_domain
        self.mount_point_id = mount_point_id
        self.network_type = network_type
        self.region_id = region_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_point_alias is not None:
            result['MountPointAlias'] = self.mount_point_alias

        if self.mount_point_domain is not None:
            result['MountPointDomain'] = self.mount_point_domain

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountPointAlias') is not None:
            self.mount_point_alias = m.get('MountPointAlias')

        if m.get('MountPointDomain') is not None:
            self.mount_point_domain = m.get('MountPointDomain')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

