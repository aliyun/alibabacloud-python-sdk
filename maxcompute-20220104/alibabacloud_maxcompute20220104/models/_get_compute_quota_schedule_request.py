# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetComputeQuotaScheduleRequest(DaraModel):
    def __init__(
        self,
        display_timezone: str = None,
    ):
        # Display time zone.
        self.display_timezone = display_timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_timezone is not None:
            result['displayTimezone'] = self.display_timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayTimezone') is not None:
            self.display_timezone = m.get('displayTimezone')

        return self

