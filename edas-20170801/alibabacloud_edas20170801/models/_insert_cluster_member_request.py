# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertClusterMemberRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_ids: str = None,
        password: str = None,
    ):
        # The ID of the cluster into which you want to import ECS instances.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the ECS instance that you want to import into the cluster. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The logon password of the ECS instance that you want to import into the cluster.
        # 
        # This parameter is required.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids

        if self.password is not None:
            result['password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')

        if m.get('password') is not None:
            self.password = m.get('password')

        return self

