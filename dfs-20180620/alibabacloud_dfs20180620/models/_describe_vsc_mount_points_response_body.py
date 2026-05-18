# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class DescribeVscMountPointsResponseBody(DaraModel):
    def __init__(
        self,
        mount_points: List[main_models.DescribeVscMountPointsResponseBodyMountPoints] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.mount_points = mount_points
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
                temp_model = main_models.DescribeVscMountPointsResponseBodyMountPoints()
                self.mount_points.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVscMountPointsResponseBodyMountPoints(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_total_count: int = None,
        instances: List[main_models.DescribeVscMountPointsResponseBodyMountPointsInstances] = None,
        mount_point_alias: str = None,
        mount_point_id: str = None,
    ):
        self.description = description
        self.instance_total_count = instance_total_count
        self.instances = instances
        self.mount_point_alias = mount_point_alias
        self.mount_point_id = mount_point_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_total_count is not None:
            result['InstanceTotalCount'] = self.instance_total_count

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.mount_point_alias is not None:
            result['MountPointAlias'] = self.mount_point_alias

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceTotalCount') is not None:
            self.instance_total_count = m.get('InstanceTotalCount')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeVscMountPointsResponseBodyMountPointsInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('MountPointAlias') is not None:
            self.mount_point_alias = m.get('MountPointAlias')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        return self

class DescribeVscMountPointsResponseBodyMountPointsInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        status: str = None,
        vscs: List[main_models.DescribeVscMountPointsResponseBodyMountPointsInstancesVscs] = None,
    ):
        self.instance_id = instance_id
        self.status = status
        self.vscs = vscs

    def validate(self):
        if self.vscs:
            for v1 in self.vscs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        result['Vscs'] = []
        if self.vscs is not None:
            for k1 in self.vscs:
                result['Vscs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.vscs = []
        if m.get('Vscs') is not None:
            for k1 in m.get('Vscs'):
                temp_model = main_models.DescribeVscMountPointsResponseBodyMountPointsInstancesVscs()
                self.vscs.append(temp_model.from_map(k1))

        return self

class DescribeVscMountPointsResponseBodyMountPointsInstancesVscs(DaraModel):
    def __init__(
        self,
        vsc_id: str = None,
        vsc_name: str = None,
        vsc_status: str = None,
        vsc_type: str = None,
    ):
        self.vsc_id = vsc_id
        self.vsc_name = vsc_name
        self.vsc_status = vsc_status
        self.vsc_type = vsc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name

        if self.vsc_status is not None:
            result['VscStatus'] = self.vsc_status

        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')

        if m.get('VscStatus') is not None:
            self.vsc_status = m.get('VscStatus')

        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')

        return self

