# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTempFileTaskRequest(DaraModel):
    def __init__(
        self,
        gmt_expired_time: str = None,
    ):
        self.gmt_expired_time = gmt_expired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_expired_time is not None:
            result['GmtExpiredTime'] = self.gmt_expired_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtExpiredTime') is not None:
            self.gmt_expired_time = m.get('GmtExpiredTime')

        return self

