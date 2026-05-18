# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class DetachVscFromMountPointsRequest(DaraModel):
    def __init__(
        self,
        detach_infos: List[main_models.DetachVscFromMountPointsRequestDetachInfos] = None,
        input_region_id: str = None,
        use_assume_role_chk_server_perm: bool = None,
    ):
        self.detach_infos = detach_infos
        # This parameter is required.
        self.input_region_id = input_region_id
        self.use_assume_role_chk_server_perm = use_assume_role_chk_server_perm

    def validate(self):
        if self.detach_infos:
            for v1 in self.detach_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetachInfos'] = []
        if self.detach_infos is not None:
            for k1 in self.detach_infos:
                result['DetachInfos'].append(k1.to_map() if k1 else None)

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.use_assume_role_chk_server_perm is not None:
            result['UseAssumeRoleChkServerPerm'] = self.use_assume_role_chk_server_perm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detach_infos = []
        if m.get('DetachInfos') is not None:
            for k1 in m.get('DetachInfos'):
                temp_model = main_models.DetachVscFromMountPointsRequestDetachInfos()
                self.detach_infos.append(temp_model.from_map(k1))

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('UseAssumeRoleChkServerPerm') is not None:
            self.use_assume_role_chk_server_perm = m.get('UseAssumeRoleChkServerPerm')

        return self

class DetachVscFromMountPointsRequestDetachInfos(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mount_point_id: str = None,
        vsc_id: str = None,
        vsc_name: str = None,
        vsc_type: str = None,
    ):
        self.instance_id = instance_id
        self.mount_point_id = mount_point_id
        self.vsc_id = vsc_id
        self.vsc_name = vsc_name
        self.vsc_type = vsc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name

        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')

        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')

        return self

