# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class CreateBaselineRequest(DaraModel):
    def __init__(
        self,
        alert_margin_threshold: int = None,
        baseline_name: str = None,
        baseline_type: str = None,
        node_ids: str = None,
        overtime_settings: List[main_models.CreateBaselineRequestOvertimeSettings] = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
    ):
        # The alert margin threshold of the baseline. Unit: minutes.
        self.alert_margin_threshold = alert_margin_threshold
        # The name of the baseline.
        # 
        # This parameter is required.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values: DAILY and HOURLY.
        # 
        # This parameter is required.
        self.baseline_type = baseline_type
        # The ancestor nodes of nodes in the baseline.
        self.node_ids = node_ids
        # The settings of the committed completion time of the baseline.
        # 
        # This parameter is required.
        self.overtime_settings = overtime_settings
        # The ID of the Alibaba Cloud account used by the baseline owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The priority of the baseline. Valid values: {1,3,5,7,8}.
        # 
        # This parameter is required.
        self.priority = priority
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.overtime_settings:
            for v1 in self.overtime_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_margin_threshold is not None:
            result['AlertMarginThreshold'] = self.alert_margin_threshold

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_type is not None:
            result['BaselineType'] = self.baseline_type

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        result['OvertimeSettings'] = []
        if self.overtime_settings is not None:
            for k1 in self.overtime_settings:
                result['OvertimeSettings'].append(k1.to_map() if k1 else None)

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertMarginThreshold') is not None:
            self.alert_margin_threshold = m.get('AlertMarginThreshold')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineType') is not None:
            self.baseline_type = m.get('BaselineType')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        self.overtime_settings = []
        if m.get('OvertimeSettings') is not None:
            for k1 in m.get('OvertimeSettings'):
                temp_model = main_models.CreateBaselineRequestOvertimeSettings()
                self.overtime_settings.append(temp_model.from_map(k1))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self



class CreateBaselineRequestOvertimeSettings(DaraModel):
    def __init__(
        self,
        cycle: int = None,
        time: str = None,
    ):
        # The cycle that corresponds to the committed completion time. For a day-level baseline, set this parameter to 1. For an hour-level baseline, set this parameter to a value that is no more than 24.
        self.cycle = cycle
        # The committed completion time in the hh:mm format. Valid values of hh: [0,47]. Valid values of mm: [0,59].
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

