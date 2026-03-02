# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeploymentRevertCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cpu: int = None,
        deployment_id: int = None,
        description: str = None,
        instance_count: int = None,
        is_monitor_enable: int = None,
        is_service_group_enable: int = None,
        memory: int = None,
        timeout: int = None,
        times: int = None,
        type: str = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
        self.deployment_id = deployment_id
        self.description = description
        # This parameter is required.
        self.instance_count = instance_count
        self.is_monitor_enable = is_monitor_enable
        self.is_service_group_enable = is_service_group_enable
        # This parameter is required.
        self.memory = memory
        self.timeout = timeout
        # This parameter is required.
        self.times = times
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.description is not None:
            result['description'] = self.description

        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count

        if self.is_monitor_enable is not None:
            result['isMonitorEnable'] = self.is_monitor_enable

        if self.is_service_group_enable is not None:
            result['isServiceGroupEnable'] = self.is_service_group_enable

        if self.memory is not None:
            result['memory'] = self.memory

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.times is not None:
            result['times'] = self.times

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')

        if m.get('isMonitorEnable') is not None:
            self.is_monitor_enable = m.get('isMonitorEnable')

        if m.get('isServiceGroupEnable') is not None:
            self.is_service_group_enable = m.get('isServiceGroupEnable')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('times') is not None:
            self.times = m.get('times')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

