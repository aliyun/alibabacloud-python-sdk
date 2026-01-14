# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAICoachTaskSessionResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        audio_usage: int = None,
        deduction_status: int = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        token_usage: int = None,
    ):
        self.audio_usage = audio_usage
        self.deduction_status = deduction_status
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.token_usage = token_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_usage is not None:
            result['audioUsage'] = self.audio_usage

        if self.deduction_status is not None:
            result['deductionStatus'] = self.deduction_status

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.token_usage is not None:
            result['tokenUsage'] = self.token_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioUsage') is not None:
            self.audio_usage = m.get('audioUsage')

        if m.get('deductionStatus') is not None:
            self.deduction_status = m.get('deductionStatus')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('tokenUsage') is not None:
            self.token_usage = m.get('tokenUsage')

        return self

