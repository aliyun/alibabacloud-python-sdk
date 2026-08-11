# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetDataAgentTaskModelUsageMetricsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetDataAgentTaskModelUsageMetricsResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of TPM time series metrics for model usage, returned in chronological order with usage at each time point.
        self.data = data
        # The error code returned when the request is abnormal.
        self.error_code = error_code
        # The error message returned when the call fails.
        self.error_message = error_message
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetDataAgentTaskModelUsageMetricsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataAgentTaskModelUsageMetricsResponseBodyData(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        tpm: int = None,
    ):
        # The start time of the statistical interval for this time series point. The value is a UNIX timestamp in seconds.
        self.begin_time = begin_time
        # The end time of the statistical interval for this time series point. The value is a UNIX timestamp in seconds.
        self.end_time = end_time
        # The TPM for this time series point, which is the number of tokens consumed within the statistical interval.
        self.tpm = tpm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.tpm is not None:
            result['Tpm'] = self.tpm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Tpm') is not None:
            self.tpm = m.get('Tpm')

        return self

