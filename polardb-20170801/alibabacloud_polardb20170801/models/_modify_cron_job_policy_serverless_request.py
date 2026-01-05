# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCronJobPolicyServerlessRequest(DaraModel):
    def __init__(
        self,
        allow_shut_down: str = None,
        cron_expression: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        job_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
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
        start_time: str = None,
    ):
        self.allow_shut_down = allow_shut_down
        # This parameter is required.
        self.cron_expression = cron_expression
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.end_time = end_time
        self.job_id = job_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scale_ap_ro_num_max = scale_ap_ro_num_max
        self.scale_ap_ro_num_min = scale_ap_ro_num_min
        self.scale_max = scale_max
        self.scale_min = scale_min
        self.scale_ro_num_max = scale_ro_num_max
        self.scale_ro_num_min = scale_ro_num_min
        self.seconds_until_auto_pause = seconds_until_auto_pause
        self.serverless_rule_cpu_enlarge_threshold = serverless_rule_cpu_enlarge_threshold
        self.serverless_rule_cpu_shrink_threshold = serverless_rule_cpu_shrink_threshold
        self.serverless_rule_mode = serverless_rule_mode
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_shut_down is not None:
            result['AllowShutDown'] = self.allow_shut_down

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowShutDown') is not None:
            self.allow_shut_down = m.get('AllowShutDown')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

