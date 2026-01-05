# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterServerlessConfRequest(DaraModel):
    def __init__(
        self,
        allow_shut_down: str = None,
        crontab_job_id: str = None,
        dbcluster_id: str = None,
        from_time_service: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_ap_ro_num_max: str = None,
        scale_ap_ro_num_min: str = None,
        scale_max: str = None,
        scale_min: str = None,
        scale_ro_num_max: str = None,
        scale_ro_num_min: str = None,
        seconds_until_auto_pause: str = None,
        serverless_rule_cpu_enlarge_threshold: str = None,
        serverless_rule_cpu_shrink_threshold: str = None,
        serverless_rule_mode: str = None,
        task_id: str = None,
    ):
        # Specifies whether to enable No-activity Suspension. Default value: false. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.allow_shut_down = allow_shut_down
        # Cycle policy ID.
        self.crontab_job_id = crontab_job_id
        # The ID of the serverless cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies an immediate or scheduled task to modify parameters and restart the cluster. Valid values:
        # 
        # *   false: scheduled task
        # *   true: immediate task
        self.from_time_service = from_time_service
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The latest start time for upgrading the specifications within the scheduled time period. Specify the time in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # > * The value of this parameter must be at least 30 minutes later than the value of PlannedStartTime.
        # >*   If you specify PlannedStartTime but do not specify PlannedEndTime, the latest start time of the task is set to a value that is calculated by using the following formula: `PlannedEndTime value + 30 minutes`. For example, if you set PlannedStartTime to `2021-01-14T09:00:00Z` and you do not specify PlannedEndTime, the latest start time of the task is set to `2021-01-14T09:30:00Z`.
        self.planned_end_time = planned_end_time
        # The earliest start time of the scheduled task for adding the read-only node. The scheduled task specifies that the task is run in the required period. Specify the time in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # 
        # > *   The earliest start time of the scheduled task can be a point in time within the next 24 hours. For example, if the current time is `2021-01-14T09:00:00Z`, you can specify a point in time between `2021-01-14T09:00:00Z` and `2021-01-15T09:00:00Z`.
        # >*   If you leave this parameter empty, the task for adding the read-only node is immediately run by default.
        self.planned_start_time = planned_start_time
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum number of stable AP read-only nodes. Valid values: 0 to 7.
        self.scale_ap_ro_num_max = scale_ap_ro_num_max
        # The minimum number of stable AP read-only nodes. Valid values: 0 to 7.
        self.scale_ap_ro_num_min = scale_ap_ro_num_min
        # The maximum number of PCUs per node for scaling. Valid values: 1 PCU to 32 PCUs.
        self.scale_max = scale_max
        # The minimum number of PCUs per node for scaling. Valid values: 1 PCU to 31 PCUs.
        self.scale_min = scale_min
        # The maximum number of read-only nodes for scaling. Valid values: 0 to 15.
        self.scale_ro_num_max = scale_ro_num_max
        # The minimum number of read-only nodes for scaling. Valid values: 0 to 15.
        self.scale_ro_num_min = scale_ro_num_min
        # The detection period for No-activity Suspension. Valid values: 5 to 1440. Unit: minutes. The detection duration must be a multiple of 5 minutes.
        self.seconds_until_auto_pause = seconds_until_auto_pause
        # CPU burst threshold
        self.serverless_rule_cpu_enlarge_threshold = serverless_rule_cpu_enlarge_threshold
        # CPU downscale threshold
        self.serverless_rule_cpu_shrink_threshold = serverless_rule_cpu_shrink_threshold
        # Elastic sensitivity. Values: - normal: standard - flexible: sensitive
        self.serverless_rule_mode = serverless_rule_mode
        # Asynchronous task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_shut_down is not None:
            result['AllowShutDown'] = self.allow_shut_down

        if self.crontab_job_id is not None:
            result['CrontabJobId'] = self.crontab_job_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.from_time_service is not None:
            result['FromTimeService'] = self.from_time_service

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_ap_ro_num_max is not None:
            result['ScaleApRoNumMax'] = self.scale_ap_ro_num_max

        if self.scale_ap_ro_num_min is not None:
            result['ScaleApRoNumMin'] = self.scale_ap_ro_num_min

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        if self.scale_ro_num_max is not None:
            result['ScaleRoNumMax'] = self.scale_ro_num_max

        if self.scale_ro_num_min is not None:
            result['ScaleRoNumMin'] = self.scale_ro_num_min

        if self.seconds_until_auto_pause is not None:
            result['SecondsUntilAutoPause'] = self.seconds_until_auto_pause

        if self.serverless_rule_cpu_enlarge_threshold is not None:
            result['ServerlessRuleCpuEnlargeThreshold'] = self.serverless_rule_cpu_enlarge_threshold

        if self.serverless_rule_cpu_shrink_threshold is not None:
            result['ServerlessRuleCpuShrinkThreshold'] = self.serverless_rule_cpu_shrink_threshold

        if self.serverless_rule_mode is not None:
            result['ServerlessRuleMode'] = self.serverless_rule_mode

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowShutDown') is not None:
            self.allow_shut_down = m.get('AllowShutDown')

        if m.get('CrontabJobId') is not None:
            self.crontab_job_id = m.get('CrontabJobId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FromTimeService') is not None:
            self.from_time_service = m.get('FromTimeService')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleApRoNumMax') is not None:
            self.scale_ap_ro_num_max = m.get('ScaleApRoNumMax')

        if m.get('ScaleApRoNumMin') is not None:
            self.scale_ap_ro_num_min = m.get('ScaleApRoNumMin')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        if m.get('ScaleRoNumMax') is not None:
            self.scale_ro_num_max = m.get('ScaleRoNumMax')

        if m.get('ScaleRoNumMin') is not None:
            self.scale_ro_num_min = m.get('ScaleRoNumMin')

        if m.get('SecondsUntilAutoPause') is not None:
            self.seconds_until_auto_pause = m.get('SecondsUntilAutoPause')

        if m.get('ServerlessRuleCpuEnlargeThreshold') is not None:
            self.serverless_rule_cpu_enlarge_threshold = m.get('ServerlessRuleCpuEnlargeThreshold')

        if m.get('ServerlessRuleCpuShrinkThreshold') is not None:
            self.serverless_rule_cpu_shrink_threshold = m.get('ServerlessRuleCpuShrinkThreshold')

        if m.get('ServerlessRuleMode') is not None:
            self.serverless_rule_mode = m.get('ServerlessRuleMode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

