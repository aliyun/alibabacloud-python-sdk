# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployConfigInfo(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        deployment_id: int = None,
        deployment_type: str = None,
        env: str = None,
        finish: bool = None,
        instance_count: int = None,
        is_monitor_enable: int = None,
        is_service_group_enable: int = None,
        memory: int = None,
        pipeline_id: str = None,
        pre_stop: str = None,
        service_group_id: int = None,
        service_id: int = None,
        timeout: int = None,
        times: int = None,
    ):
        self.cpu = cpu
        self.deployment_id = deployment_id
        self.deployment_type = deployment_type
        # This parameter is required.
        self.env = env
        self.finish = finish
        self.instance_count = instance_count
        self.is_monitor_enable = is_monitor_enable
        self.is_service_group_enable = is_service_group_enable
        self.memory = memory
        self.pipeline_id = pipeline_id
        self.pre_stop = pre_stop
        self.service_group_id = service_group_id
        # This parameter is required.
        self.service_id = service_id
        self.timeout = timeout
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.deployment_type is not None:
            result['deploymentType'] = self.deployment_type

        if self.env is not None:
            result['env'] = self.env

        if self.finish is not None:
            result['finish'] = self.finish

        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count

        if self.is_monitor_enable is not None:
            result['isMonitorEnable'] = self.is_monitor_enable

        if self.is_service_group_enable is not None:
            result['isServiceGroupEnable'] = self.is_service_group_enable

        if self.memory is not None:
            result['memory'] = self.memory

        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id

        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('deploymentType') is not None:
            self.deployment_type = m.get('deploymentType')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('finish') is not None:
            self.finish = m.get('finish')

        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')

        if m.get('isMonitorEnable') is not None:
            self.is_monitor_enable = m.get('isMonitorEnable')

        if m.get('isServiceGroupEnable') is not None:
            self.is_service_group_enable = m.get('isServiceGroupEnable')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')

        if m.get('preStop') is not None:
            self.pre_stop = m.get('preStop')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

