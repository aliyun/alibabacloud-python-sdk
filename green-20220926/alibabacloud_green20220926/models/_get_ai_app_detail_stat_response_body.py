# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiAppDetailStatResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        avg_model_duration: float = None,
        avg_model_duration_dau: float = None,
        model_count: int = None,
        model_count_dau: float = None,
        request_id: str = None,
        risk_event_count: int = None,
        token_count: int = None,
        token_count_dau: float = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The average duration of model calls.
        self.avg_model_duration = avg_model_duration
        # The day-over-day change ratio of average model call duration.
        self.avg_model_duration_dau = avg_model_duration_dau
        # The number of model calls.
        self.model_count = model_count
        # The day-over-day change ratio of model call count.
        self.model_count_dau = model_count_dau
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The number of risk events.
        self.risk_event_count = risk_event_count
        # The number of tokens consumed.
        self.token_count = token_count
        # The day-over-day change ratio of token consumption count.
        self.token_count_dau = token_count_dau

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.avg_model_duration is not None:
            result['AvgModelDuration'] = self.avg_model_duration

        if self.avg_model_duration_dau is not None:
            result['AvgModelDurationDau'] = self.avg_model_duration_dau

        if self.model_count is not None:
            result['ModelCount'] = self.model_count

        if self.model_count_dau is not None:
            result['ModelCountDau'] = self.model_count_dau

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_event_count is not None:
            result['RiskEventCount'] = self.risk_event_count

        if self.token_count is not None:
            result['TokenCount'] = self.token_count

        if self.token_count_dau is not None:
            result['TokenCountDau'] = self.token_count_dau

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AvgModelDuration') is not None:
            self.avg_model_duration = m.get('AvgModelDuration')

        if m.get('AvgModelDurationDau') is not None:
            self.avg_model_duration_dau = m.get('AvgModelDurationDau')

        if m.get('ModelCount') is not None:
            self.model_count = m.get('ModelCount')

        if m.get('ModelCountDau') is not None:
            self.model_count_dau = m.get('ModelCountDau')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskEventCount') is not None:
            self.risk_event_count = m.get('RiskEventCount')

        if m.get('TokenCount') is not None:
            self.token_count = m.get('TokenCount')

        if m.get('TokenCountDau') is not None:
            self.token_count_dau = m.get('TokenCountDau')

        return self

