# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class PeriodicSchedulingPolicy(DaraModel):
    def __init__(
        self,
        is_finished: bool = None,
        only_once_trigger_time: int = None,
        only_once_trigger_time_is_expired: bool = None,
        periodic_scheduling_level: str = None,
        periodic_scheduling_values: List[int] = None,
        periodic_trigger_time: int = None,
        resource_setting: main_models.BriefResourceSetting = None,
    ):
        self.is_finished = is_finished
        self.only_once_trigger_time = only_once_trigger_time
        self.only_once_trigger_time_is_expired = only_once_trigger_time_is_expired
        self.periodic_scheduling_level = periodic_scheduling_level
        self.periodic_scheduling_values = periodic_scheduling_values
        self.periodic_trigger_time = periodic_trigger_time
        self.resource_setting = resource_setting

    def validate(self):
        if self.resource_setting:
            self.resource_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_finished is not None:
            result['isFinished'] = self.is_finished

        if self.only_once_trigger_time is not None:
            result['onlyOnceTriggerTime'] = self.only_once_trigger_time

        if self.only_once_trigger_time_is_expired is not None:
            result['onlyOnceTriggerTimeIsExpired'] = self.only_once_trigger_time_is_expired

        if self.periodic_scheduling_level is not None:
            result['periodicSchedulingLevel'] = self.periodic_scheduling_level

        if self.periodic_scheduling_values is not None:
            result['periodicSchedulingValues'] = self.periodic_scheduling_values

        if self.periodic_trigger_time is not None:
            result['periodicTriggerTime'] = self.periodic_trigger_time

        if self.resource_setting is not None:
            result['resourceSetting'] = self.resource_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isFinished') is not None:
            self.is_finished = m.get('isFinished')

        if m.get('onlyOnceTriggerTime') is not None:
            self.only_once_trigger_time = m.get('onlyOnceTriggerTime')

        if m.get('onlyOnceTriggerTimeIsExpired') is not None:
            self.only_once_trigger_time_is_expired = m.get('onlyOnceTriggerTimeIsExpired')

        if m.get('periodicSchedulingLevel') is not None:
            self.periodic_scheduling_level = m.get('periodicSchedulingLevel')

        if m.get('periodicSchedulingValues') is not None:
            self.periodic_scheduling_values = m.get('periodicSchedulingValues')

        if m.get('periodicTriggerTime') is not None:
            self.periodic_trigger_time = m.get('periodicTriggerTime')

        if m.get('resourceSetting') is not None:
            temp_model = main_models.BriefResourceSetting()
            self.resource_setting = temp_model.from_map(m.get('resourceSetting'))

        return self

