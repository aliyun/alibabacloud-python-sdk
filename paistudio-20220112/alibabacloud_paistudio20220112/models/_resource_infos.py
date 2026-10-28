# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceInfos(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ecs_spec: str = None,
        gpu_card_type: str = None,
        machine_model: str = None,
        max_quota: int = None,
        network_pod_id: str = None,
        region_id: str = None,
        used_quota: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The ECS instance type information.
        self.ecs_spec = ecs_spec
        # The GPU card type.
        self.gpu_card_type = gpu_card_type
        # The machine model.
        self.machine_model = machine_model
        # The maximum quota.
        self.max_quota = max_quota
        # The network pod ID.
        self.network_pod_id = network_pod_id
        # The region ID.
        self.region_id = region_id
        # The used quota.
        self.used_quota = used_quota
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.gpu_card_type is not None:
            result['GpuCardType'] = self.gpu_card_type

        if self.machine_model is not None:
            result['MachineModel'] = self.machine_model

        if self.max_quota is not None:
            result['MaxQuota'] = self.max_quota

        if self.network_pod_id is not None:
            result['NetworkPodId'] = self.network_pod_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('GpuCardType') is not None:
            self.gpu_card_type = m.get('GpuCardType')

        if m.get('MachineModel') is not None:
            self.machine_model = m.get('MachineModel')

        if m.get('MaxQuota') is not None:
            self.max_quota = m.get('MaxQuota')

        if m.get('NetworkPodId') is not None:
            self.network_pod_id = m.get('NetworkPodId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

