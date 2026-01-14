# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetConsumeOffsetRequest(DaraModel):
    def __init__(
        self,
        reset_time: str = None,
        reset_type: str = None,
    ):
        # The time when the consumer offset is reset.
        self.reset_time = reset_time
        # The method that is used to reset the consumer offset. Valid values: LATEST_OFFSET and SPECIFIED_TIME.
        self.reset_type = reset_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reset_time is not None:
            result['resetTime'] = self.reset_time

        if self.reset_type is not None:
            result['resetType'] = self.reset_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resetTime') is not None:
            self.reset_time = m.get('resetTime')

        if m.get('resetType') is not None:
            self.reset_type = m.get('resetType')

        return self

