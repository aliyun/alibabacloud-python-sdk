# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUserSettingResponseBody(DaraModel):
    def __init__(
        self,
        alert_levels: List[str] = None,
        invalid_warning_keep_days: int = None,
        request_id: str = None,
    ):
        # The severities of alerts. If this parameter is empty, no custom alerts are generated.
        self.alert_levels = alert_levels
        # The number of days during which you want to retain invalid alerts.
        self.invalid_warning_keep_days = invalid_warning_keep_days
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_levels is not None:
            result['AlertLevels'] = self.alert_levels

        if self.invalid_warning_keep_days is not None:
            result['InvalidWarningKeepDays'] = self.invalid_warning_keep_days

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevels') is not None:
            self.alert_levels = m.get('AlertLevels')

        if m.get('InvalidWarningKeepDays') is not None:
            self.invalid_warning_keep_days = m.get('InvalidWarningKeepDays')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

