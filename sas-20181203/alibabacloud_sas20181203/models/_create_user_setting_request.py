# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserSettingRequest(DaraModel):
    def __init__(
        self,
        alert_levels: str = None,
        invalid_warning_keep_days: int = None,
        source_ip: str = None,
    ):
        # The severities of alerts.
        self.alert_levels = alert_levels
        # The number of days during which you want to retain invalid alerts.
        self.invalid_warning_keep_days = invalid_warning_keep_days
        # The source IP address.
        self.source_ip = source_ip

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

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevels') is not None:
            self.alert_levels = m.get('AlertLevels')

        if m.get('InvalidWarningKeepDays') is not None:
            self.invalid_warning_keep_days = m.get('InvalidWarningKeepDays')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

