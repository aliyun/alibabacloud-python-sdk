# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetBaselineConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetBaselineConfigResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the baseline.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.GetBaselineConfigResponseBodyData()
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

class GetBaselineConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        baseline_name: str = None,
        baseline_type: str = None,
        exp_hour: int = None,
        exp_minu: int = None,
        hour_exp_detail: str = None,
        hour_sla_detail: str = None,
        is_default: bool = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        sla_hour: int = None,
        sla_minu: int = None,
        use_flag: bool = None,
    ):
        # The ID of the baseline.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values: DAILY (daily baseline) and HOURLY (hourly baseline).
        self.baseline_type = baseline_type
        # The alert hour of the daily baseline. Valid values: [0, 47\\].
        self.exp_hour = exp_hour
        # The alert minute of the daily baseline. Valid values: [0, 59\\].
        self.exp_minu = exp_minu
        # The alert time configuration of the hourly baseline in JSON format. The key is the cycle number, and the value is in hh:mm format. Valid values of hh: [0,47\\]. Valid values of mm: [0,59\\].
        self.hour_exp_detail = hour_exp_detail
        # The committed time configuration of the hourly baseline in JSON format. The key is the cycle number, and the value is in hh:mm format. Valid values of hh: [0,47\\]. Valid values of mm: [0,59\\].
        self.hour_sla_detail = hour_sla_detail
        # Indicates whether this is the default baseline of the workspace. Valid values: true and false.
        self.is_default = is_default
        # The Alibaba Cloud UID of the baseline owner. If multiple owners exist, they are separated by commas (,).
        self.owner = owner
        # The priority of the baseline. Valid values: 1, 3, 5, 7, and 8.
        self.priority = priority
        # The ID of the workspace.
        self.project_id = project_id
        # The committed hour of the daily baseline. Valid values: [0, 47\\].
        self.sla_hour = sla_hour
        # The committed minute of the daily baseline. Valid values: [0, 59\\].
        self.sla_minu = sla_minu
        # Indicates whether the baseline is enabled. Valid values: true (enabled) and false (disabled).
        self.use_flag = use_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_type is not None:
            result['BaselineType'] = self.baseline_type

        if self.exp_hour is not None:
            result['ExpHour'] = self.exp_hour

        if self.exp_minu is not None:
            result['ExpMinu'] = self.exp_minu

        if self.hour_exp_detail is not None:
            result['HourExpDetail'] = self.hour_exp_detail

        if self.hour_sla_detail is not None:
            result['HourSlaDetail'] = self.hour_sla_detail

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sla_hour is not None:
            result['SlaHour'] = self.sla_hour

        if self.sla_minu is not None:
            result['SlaMinu'] = self.sla_minu

        if self.use_flag is not None:
            result['UseFlag'] = self.use_flag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineType') is not None:
            self.baseline_type = m.get('BaselineType')

        if m.get('ExpHour') is not None:
            self.exp_hour = m.get('ExpHour')

        if m.get('ExpMinu') is not None:
            self.exp_minu = m.get('ExpMinu')

        if m.get('HourExpDetail') is not None:
            self.hour_exp_detail = m.get('HourExpDetail')

        if m.get('HourSlaDetail') is not None:
            self.hour_sla_detail = m.get('HourSlaDetail')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SlaHour') is not None:
            self.sla_hour = m.get('SlaHour')

        if m.get('SlaMinu') is not None:
            self.sla_minu = m.get('SlaMinu')

        if m.get('UseFlag') is not None:
            self.use_flag = m.get('UseFlag')

        return self

