# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetDataAgentTaskModelUsageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataAgentTaskModelUsageResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The summary data of model usage for DataAgent analysis tasks.
        self.data = data
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # - **false**: The request fails.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDataAgentTaskModelUsageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataAgentTaskModelUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        acceleration_ratio: float = None,
        rate_limited_session_count: int = None,
        total_llm_wait_duration: float = None,
        total_session_count: int = None,
        peak_tpm: int = None,
        total_call_count: int = None,
        total_token_consumed: int = None,
        used_models: int = None,
    ):
        self.acceleration_ratio = acceleration_ratio
        self.rate_limited_session_count = rate_limited_session_count
        self.total_llm_wait_duration = total_llm_wait_duration
        self.total_session_count = total_session_count
        # The peak TPM (tokens per minute) within the query time range, which is the maximum number of tokens consumed per minute.
        self.peak_tpm = peak_tpm
        # The total number of model calls within the query time range.
        self.total_call_count = total_call_count
        # The total number of tokens consumed within the query time range.
        self.total_token_consumed = total_token_consumed
        # The number of models used within the query time range.
        self.used_models = used_models

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceleration_ratio is not None:
            result['AccelerationRatio'] = self.acceleration_ratio

        if self.rate_limited_session_count is not None:
            result['RateLimitedSessionCount'] = self.rate_limited_session_count

        if self.total_llm_wait_duration is not None:
            result['TotalLlmWaitDuration'] = self.total_llm_wait_duration

        if self.total_session_count is not None:
            result['TotalSessionCount'] = self.total_session_count

        if self.peak_tpm is not None:
            result['peakTpm'] = self.peak_tpm

        if self.total_call_count is not None:
            result['totalCallCount'] = self.total_call_count

        if self.total_token_consumed is not None:
            result['totalTokenConsumed'] = self.total_token_consumed

        if self.used_models is not None:
            result['usedModels'] = self.used_models

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerationRatio') is not None:
            self.acceleration_ratio = m.get('AccelerationRatio')

        if m.get('RateLimitedSessionCount') is not None:
            self.rate_limited_session_count = m.get('RateLimitedSessionCount')

        if m.get('TotalLlmWaitDuration') is not None:
            self.total_llm_wait_duration = m.get('TotalLlmWaitDuration')

        if m.get('TotalSessionCount') is not None:
            self.total_session_count = m.get('TotalSessionCount')

        if m.get('peakTpm') is not None:
            self.peak_tpm = m.get('peakTpm')

        if m.get('totalCallCount') is not None:
            self.total_call_count = m.get('totalCallCount')

        if m.get('totalTokenConsumed') is not None:
            self.total_token_consumed = m.get('totalTokenConsumed')

        if m.get('usedModels') is not None:
            self.used_models = m.get('usedModels')

        return self

