# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class SetDesktopGroupScaleTimerRequest(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        region_id: str = None,
        scale_timer_infos: List[main_models.SetDesktopGroupScaleTimerRequestScaleTimerInfos] = None,
    ):
        # The ID of the cloud computer pool.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The information about the scheduled auto scaling task.
        self.scale_timer_infos = scale_timer_infos

    def validate(self):
        if self.scale_timer_infos:
            for v1 in self.scale_timer_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ScaleTimerInfos'] = []
        if self.scale_timer_infos is not None:
            for k1 in self.scale_timer_infos:
                result['ScaleTimerInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.scale_timer_infos = []
        if m.get('ScaleTimerInfos') is not None:
            for k1 in m.get('ScaleTimerInfos'):
                temp_model = main_models.SetDesktopGroupScaleTimerRequestScaleTimerInfos()
                self.scale_timer_infos.append(temp_model.from_map(k1))

        return self

class SetDesktopGroupScaleTimerRequestScaleTimerInfos(DaraModel):
    def __init__(
        self,
        buy_res_amount: int = None,
        cron: str = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_res_amount: int = None,
        min_res_amount: int = None,
        ratio_threshold: float = None,
        type: str = None,
    ):
        # One option for the auto scaling policy. This option specifies the number of cloud computers that you want to create in the cloud computer pool. Valid values: 0 to 200.
        self.buy_res_amount = buy_res_amount
        # The cron expression of the trigger time.
        self.cron = cron
        # The keep-alive duration of a session after the session is disconnected. Unit: milliseconds. Valid values: 180000 (3 minutes) to 345600000 (4 days). A value of 0 indicates that the session always keeps alive.
        # 
        # If a session is disconnected by the end user or accidentally due to a factor and the end user does not re-establish a connection with the session within the keep-alive duration, the session expires and unsaved data is deleted. If the end user successfully re-establishes a connection with the session within the keep-alive duration, the end user returns to the session and can still access the original data.
        self.keep_duration = keep_duration
        # The load balancing policy for the multi-session cloud computer pool.
        # 
        # Valid values:
        # 
        # *   0: depth-first
        # *   1: breadth first.
        self.load_policy = load_policy
        # One option for the auto scaling policy. This option specifies the maximum number of cloud computers that you can create in the cloud computer pool. Valid values: 0 to 200.
        self.max_res_amount = max_res_amount
        # One option for the auto scaling policy. This option specifies the minimum number of cloud computers that you must create in the cloud computer pool. Valid values: 0 to 200.
        self.min_res_amount = min_res_amount
        # The threshold for the ratio of connected sessions. This parameter is the condition that triggers auto scaling in a multi-session cloud computer pool. Formula:
        # 
        # `Ratio of connected sessions = Number of connected sessions/(Total number of cloud computers × Maximum number of sessions allowed for each cloud computer) × 100%`.
        # 
        # When the specified threshold is reached, new cloud computers are automatically created. When the specified threshold is not reached, idle cloud computers are released.
        self.ratio_threshold = ratio_threshold
        # The type of the auto scaling policy.
        # 
        # Valid values:
        # 
        # *   drop
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   normal
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   peak
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   rise
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_res_amount is not None:
            result['BuyResAmount'] = self.buy_res_amount

        if self.cron is not None:
            result['Cron'] = self.cron

        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration

        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy

        if self.max_res_amount is not None:
            result['MaxResAmount'] = self.max_res_amount

        if self.min_res_amount is not None:
            result['MinResAmount'] = self.min_res_amount

        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResAmount') is not None:
            self.buy_res_amount = m.get('BuyResAmount')

        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')

        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')

        if m.get('MaxResAmount') is not None:
            self.max_res_amount = m.get('MaxResAmount')

        if m.get('MinResAmount') is not None:
            self.min_res_amount = m.get('MinResAmount')

        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

