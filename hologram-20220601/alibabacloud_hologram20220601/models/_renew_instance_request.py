# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
    ):
        # Specifies whether to enable monthly auto-renewal. The default value is false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  If you enable auto-renewal for an instance for which auto-renewal is enabled, an error is reported.
        self.auto_renew = auto_renew
        # The renewal duration. Unit: month.
        # 
        # This parameter is required.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.duration is not None:
            result['duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        return self

