# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CollectorDeployMachine(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        group_id: str = None,
        instance_id: str = None,
        machines: List[main_models.CollectorDeployMachineMachines] = None,
        success_pods_count: str = None,
        total_pods_count: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.config_type = config_type
        self.group_id = group_id
        self.instance_id = instance_id
        self.machines = machines
        self.success_pods_count = success_pods_count
        self.total_pods_count = total_pods_count
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.machines:
            for v1 in self.machines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        result['machines'] = []
        if self.machines is not None:
            for k1 in self.machines:
                result['machines'].append(k1.to_map() if k1 else None)

        if self.success_pods_count is not None:
            result['successPodsCount'] = self.success_pods_count

        if self.total_pods_count is not None:
            result['totalPodsCount'] = self.total_pods_count

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.machines = []
        if m.get('machines') is not None:
            for k1 in m.get('machines'):
                temp_model = main_models.CollectorDeployMachineMachines()
                self.machines.append(temp_model.from_map(k1))

        if m.get('successPodsCount') is not None:
            self.success_pods_count = m.get('successPodsCount')

        if m.get('totalPodsCount') is not None:
            self.total_pods_count = m.get('totalPodsCount')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self



class CollectorDeployMachineMachines(DaraModel):
    def __init__(
        self,
        agent_status: str = None,
        instance_id: str = None,
    ):
        self.agent_status = agent_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

