# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListBaselinesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListBaselinesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListBaselinesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBaselinesResponseBodyData(DaraModel):
    def __init__(
        self,
        baselines: List[main_models.ListBaselinesResponseBodyDataBaselines] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The baselines.
        self.baselines = baselines
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of baselines returned.
        self.total_count = total_count

    def validate(self):
        if self.baselines:
            for v1 in self.baselines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Baselines'] = []
        if self.baselines is not None:
            for k1 in self.baselines:
                result['Baselines'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baselines = []
        if m.get('Baselines') is not None:
            for k1 in m.get('Baselines'):
                temp_model = main_models.ListBaselinesResponseBodyDataBaselines()
                self.baselines.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBaselinesResponseBodyDataBaselines(DaraModel):
    def __init__(
        self,
        alert_enabled: bool = None,
        alert_margin_threshold: int = None,
        baseline_id: int = None,
        baseline_name: str = None,
        baseline_type: str = None,
        enabled: bool = None,
        over_time_settings: List[main_models.ListBaselinesResponseBodyDataBaselinesOverTimeSettings] = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
    ):
        # Indicates whether the alerting feature is enabled. Valid values: true and false.
        self.alert_enabled = alert_enabled
        # The alert margin threshold for the baseline instance. Unit: minutes.
        self.alert_margin_threshold = alert_margin_threshold
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values: DAILY and HOURLY.
        self.baseline_type = baseline_type
        # Indicates whether the baseline is enabled. Valid values: true and false.
        self.enabled = enabled
        # The settings of the committed completion time of the baseline.
        self.over_time_settings = over_time_settings
        # The ID of the Alibaba Cloud account used by the baseline owner. Multiple IDs can be specified. The IDs are separated by commas (,).
        self.owner = owner
        # The priority of the baseline. Valid values: {1,2,5,7,8}.
        self.priority = priority
        # The ID of the workspace to which the baseline belongs.
        self.project_id = project_id

    def validate(self):
        if self.over_time_settings:
            for v1 in self.over_time_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_enabled is not None:
            result['AlertEnabled'] = self.alert_enabled

        if self.alert_margin_threshold is not None:
            result['AlertMarginThreshold'] = self.alert_margin_threshold

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_type is not None:
            result['BaselineType'] = self.baseline_type

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['OverTimeSettings'] = []
        if self.over_time_settings is not None:
            for k1 in self.over_time_settings:
                result['OverTimeSettings'].append(k1.to_map() if k1 else None)

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEnabled') is not None:
            self.alert_enabled = m.get('AlertEnabled')

        if m.get('AlertMarginThreshold') is not None:
            self.alert_margin_threshold = m.get('AlertMarginThreshold')

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineType') is not None:
            self.baseline_type = m.get('BaselineType')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.over_time_settings = []
        if m.get('OverTimeSettings') is not None:
            for k1 in m.get('OverTimeSettings'):
                temp_model = main_models.ListBaselinesResponseBodyDataBaselinesOverTimeSettings()
                self.over_time_settings.append(temp_model.from_map(k1))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ListBaselinesResponseBodyDataBaselinesOverTimeSettings(DaraModel):
    def __init__(
        self,
        cycle: int = None,
        time: str = None,
    ):
        # The cycle that corresponds to the committed completion time. For a day-level baseline, the value of this parameter is 1. For an hour-level baseline, the value of this parameter cannot exceed 24.
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

