# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class DescribeMountPointsVscAttachInfoRequest(DaraModel):
    def __init__(
        self,
        input_region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        query_infos: List[main_models.DescribeMountPointsVscAttachInfoRequestQueryInfos] = None,
        use_assume_role_chk_server_perm: bool = None,
    ):
        # This parameter is required.
        self.input_region_id = input_region_id
        self.max_results = max_results
        self.next_token = next_token
        self.query_infos = query_infos
        self.use_assume_role_chk_server_perm = use_assume_role_chk_server_perm

    def validate(self):
        if self.query_infos:
            for v1 in self.query_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['QueryInfos'] = []
        if self.query_infos is not None:
            for k1 in self.query_infos:
                result['QueryInfos'].append(k1.to_map() if k1 else None)

        if self.use_assume_role_chk_server_perm is not None:
            result['UseAssumeRoleChkServerPerm'] = self.use_assume_role_chk_server_perm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.query_infos = []
        if m.get('QueryInfos') is not None:
            for k1 in m.get('QueryInfos'):
                temp_model = main_models.DescribeMountPointsVscAttachInfoRequestQueryInfos()
                self.query_infos.append(temp_model.from_map(k1))

        if m.get('UseAssumeRoleChkServerPerm') is not None:
            self.use_assume_role_chk_server_perm = m.get('UseAssumeRoleChkServerPerm')

        return self

class DescribeMountPointsVscAttachInfoRequestQueryInfos(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mount_point_id: str = None,
        vsc_id: str = None,
    ):
        self.instance_id = instance_id
        self.mount_point_id = mount_point_id
        self.vsc_id = vsc_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        return self

