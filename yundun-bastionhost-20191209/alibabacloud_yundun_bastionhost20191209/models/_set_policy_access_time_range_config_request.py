# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class SetPolicyAccessTimeRangeConfigRequest(DaraModel):
    def __init__(
        self,
        access_time_range_config: main_models.SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        # The logon period limits.
        # 
        # This parameter is required.
        self.access_time_range_config = access_time_range_config
        # The bastion host ID.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The control policy ID.
        # 
        # >  You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to query the control policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        if self.access_time_range_config:
            self.access_time_range_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_time_range_config is not None:
            result['AccessTimeRangeConfig'] = self.access_time_range_config.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTimeRangeConfig') is not None:
            temp_model = main_models.SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfig()
            self.access_time_range_config = temp_model.from_map(m.get('AccessTimeRangeConfig'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfig(DaraModel):
    def __init__(
        self,
        effective_time: List[main_models.SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfigEffectiveTime] = None,
    ):
        # The details about the periods during which users can log on to the assets.
        self.effective_time = effective_time

    def validate(self):
        if self.effective_time:
            for v1 in self.effective_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EffectiveTime'] = []
        if self.effective_time is not None:
            for k1 in self.effective_time:
                result['EffectiveTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.effective_time = []
        if m.get('EffectiveTime') is not None:
            for k1 in m.get('EffectiveTime'):
                temp_model = main_models.SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfigEffectiveTime()
                self.effective_time.append(temp_model.from_map(k1))

        return self

class SetPolicyAccessTimeRangeConfigRequestAccessTimeRangeConfigEffectiveTime(DaraModel):
    def __init__(
        self,
        days: List[int] = None,
        hours: List[int] = None,
    ):
        # The days of the week during which users can log on to the assets.
        self.days = days
        # The time periods of the day during which users can log on to the assets.
        self.hours = hours

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['Days'] = self.days

        if self.hours is not None:
            result['Hours'] = self.hours

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('Hours') is not None:
            self.hours = m.get('Hours')

        return self

