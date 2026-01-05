# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeCronJobPolicyServerlessResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeCronJobPolicyServerlessResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeCronJobPolicyServerlessResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeCronJobPolicyServerlessResponseBodyItems(DaraModel):
    def __init__(
        self,
        action: str = None,
        allow_shut_down: str = None,
        cron_expression: str = None,
        dbcluster_id: str = None,
        end_time: str = None,
        job_id: str = None,
        order_id: str = None,
        region_id: str = None,
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
        status: str = None,
    ):
        self.action = action
        self.allow_shut_down = allow_shut_down
        self.cron_expression = cron_expression
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.job_id = job_id
        self.order_id = order_id
        self.region_id = region_id
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
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

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

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

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

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

