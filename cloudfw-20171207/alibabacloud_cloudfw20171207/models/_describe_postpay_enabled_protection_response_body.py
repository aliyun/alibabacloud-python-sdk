# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePostpayEnabledProtectionResponseBody(DaraModel):
    def __init__(
        self,
        disabled_days: int = None,
        disabled_type: str = None,
        is_enabled_protection: bool = None,
        is_open_but_disabled: bool = None,
        request_id: str = None,
    ):
        self.disabled_days = disabled_days
        self.disabled_type = disabled_type
        self.is_enabled_protection = is_enabled_protection
        self.is_open_but_disabled = is_open_but_disabled
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled_days is not None:
            result['DisabledDays'] = self.disabled_days

        if self.disabled_type is not None:
            result['DisabledType'] = self.disabled_type

        if self.is_enabled_protection is not None:
            result['IsEnabledProtection'] = self.is_enabled_protection

        if self.is_open_but_disabled is not None:
            result['IsOpenButDisabled'] = self.is_open_but_disabled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisabledDays') is not None:
            self.disabled_days = m.get('DisabledDays')

        if m.get('DisabledType') is not None:
            self.disabled_type = m.get('DisabledType')

        if m.get('IsEnabledProtection') is not None:
            self.is_enabled_protection = m.get('IsEnabledProtection')

        if m.get('IsOpenButDisabled') is not None:
            self.is_open_but_disabled = m.get('IsOpenButDisabled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

