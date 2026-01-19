# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLogConfigRequest(DaraModel):
    def __init__(
        self,
        log_type: str = None,
        security_token: str = None,
    ):
        # The log type. Valid values: **log** and **survey**.
        self.log_type = log_type
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

