# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityCheckScheduleConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_check_job_config: main_models.DescribeSecurityCheckScheduleConfigResponseBodyRiskCheckJobConfig = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The configurations of custom check tasks.
        self.risk_check_job_config = risk_check_job_config

    def validate(self):
        if self.risk_check_job_config:
            self.risk_check_job_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_check_job_config is not None:
            result['RiskCheckJobConfig'] = self.risk_check_job_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskCheckJobConfig') is not None:
            temp_model = main_models.DescribeSecurityCheckScheduleConfigResponseBodyRiskCheckJobConfig()
            self.risk_check_job_config = temp_model.from_map(m.get('RiskCheckJobConfig'))

        return self

class DescribeSecurityCheckScheduleConfigResponseBodyRiskCheckJobConfig(DaraModel):
    def __init__(
        self,
        days_of_week: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The day of the week when the check tasks are performed. Multiple days can be specified. Multiple days are separated by commas (,).
        # 
        # *   **1**: Monday
        # *   **2**: Tuesday
        # *   **3**: Wednesday
        # *   **4**: Thursday
        # *   **5**: Friday
        # *   **6**: Saturday
        # *   **7**: Sunday
        self.days_of_week = days_of_week
        # The time range during which check tasks end. Valid values:
        # 
        # *   **6**: 00:00 to 06:00
        # *   **12**: 06:00 to 12:00
        # *   **18**: 12:00 to 18:00
        # *   **24**: 18:00 to 24:00
        self.end_time = end_time
        # The time range during which check tasks start. Valid values:
        # 
        # *   **0**: 00:00 to 06:00
        # *   **6**: 06:00 to 12:00
        # *   **12**: 12:00 to 18:00
        # *   **18**: 18:00 to 24:00
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

