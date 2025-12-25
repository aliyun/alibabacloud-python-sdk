# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyComputeBurstConfigRequest(DaraModel):
    def __init__(
        self,
        burst_status: str = None,
        client_token: str = None,
        cpu_enlarge_threshold: str = None,
        cpu_shrink_threshold: str = None,
        crontab_job_id: str = None,
        dbinstance_id: str = None,
        memory_enlarge_threshold: str = None,
        memory_shrink_threshold: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        scale_max_cpus: str = None,
        scale_max_memory: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        task_id: str = None,
    ):
        # This parameter is set to **disabled** if the assured serverless feature is disabled.
        self.burst_status = burst_status
        # The client token that is used to ensure the idempotence of requests and prevent repeated requests from being submitted. You can use the client to generate the value, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The CPU utilization threshold for **scale-out**. Valid values: 60 to 90. Unit: %.
        self.cpu_enlarge_threshold = cpu_enlarge_threshold
        # The CPU utilization threshold for **scale-in**. Valid values: 30 to 55. Unit: %.
        self.cpu_shrink_threshold = cpu_shrink_threshold
        # The reserved parameter. This parameter is not supported.
        self.crontab_job_id = crontab_job_id
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The memory usage threshold for **scale-out**. Valid values: 60 to 90. Unit: %.
        self.memory_enlarge_threshold = memory_enlarge_threshold
        # The memory usage threshold for **scale-in**. Valid values: 30 to 55. Unit: %.
        self.memory_shrink_threshold = memory_shrink_threshold
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The maximum number of CPU cores for elastic scaling. The maximum value cannot exceed twice the initial CPU configuration.
        self.scale_max_cpus = scale_max_cpus
        # The maximum memory for elastic scaling. The value cannot exceed twice the instance\\"s initial memory size. Unit: GB. Step size: 2 GB.
        self.scale_max_memory = scale_max_memory
        # The time when the specified entry takes effect. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        # 
        # >  This parameter is required only if **SwitchTimeMode** is set to **2**.
        self.switch_time = switch_time
        # The effective policy. Valid values:
        # 
        # *   **0**: Immediately takes effect.
        # *   **1**: Takes effect within the maintenance window. You can call the **ModifyDBInstanceMaintainTime** operation to change the maintenance window of an instance.
        # *   **2**: Takes effect at a specified point in time.
        self.switch_time_mode = switch_time_mode
        # The reserved parameter. This parameter is not supported.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.burst_status is not None:
            result['BurstStatus'] = self.burst_status

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cpu_enlarge_threshold is not None:
            result['CpuEnlargeThreshold'] = self.cpu_enlarge_threshold

        if self.cpu_shrink_threshold is not None:
            result['CpuShrinkThreshold'] = self.cpu_shrink_threshold

        if self.crontab_job_id is not None:
            result['CrontabJobId'] = self.crontab_job_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.memory_enlarge_threshold is not None:
            result['MemoryEnlargeThreshold'] = self.memory_enlarge_threshold

        if self.memory_shrink_threshold is not None:
            result['MemoryShrinkThreshold'] = self.memory_shrink_threshold

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scale_max_cpus is not None:
            result['ScaleMaxCpus'] = self.scale_max_cpus

        if self.scale_max_memory is not None:
            result['ScaleMaxMemory'] = self.scale_max_memory

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstStatus') is not None:
            self.burst_status = m.get('BurstStatus')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CpuEnlargeThreshold') is not None:
            self.cpu_enlarge_threshold = m.get('CpuEnlargeThreshold')

        if m.get('CpuShrinkThreshold') is not None:
            self.cpu_shrink_threshold = m.get('CpuShrinkThreshold')

        if m.get('CrontabJobId') is not None:
            self.crontab_job_id = m.get('CrontabJobId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('MemoryEnlargeThreshold') is not None:
            self.memory_enlarge_threshold = m.get('MemoryEnlargeThreshold')

        if m.get('MemoryShrinkThreshold') is not None:
            self.memory_shrink_threshold = m.get('MemoryShrinkThreshold')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScaleMaxCpus') is not None:
            self.scale_max_cpus = m.get('ScaleMaxCpus')

        if m.get('ScaleMaxMemory') is not None:
            self.scale_max_memory = m.get('ScaleMaxMemory')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

