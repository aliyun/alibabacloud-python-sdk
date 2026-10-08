# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformClusterMemberRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        password: str = None,
        target_cluster_id: str = None,
    ):
        # The IDs of the ECS instances. Separate multiple IDs with a comma (,).
        # 
        # - The instances must be in the same VPC as the target cluster.
        # 
        # - An instance can belong to only one cluster at a time.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The logon password to set for the instances.
        # 
        # This parameter is required.
        self.password = password
        # The ID of the target cluster.
        # 
        # This parameter is required.
        self.target_cluster_id = target_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.password is not None:
            result['Password'] = self.password

        if self.target_cluster_id is not None:
            result['TargetClusterId'] = self.target_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('TargetClusterId') is not None:
            self.target_cluster_id = m.get('TargetClusterId')

        return self

