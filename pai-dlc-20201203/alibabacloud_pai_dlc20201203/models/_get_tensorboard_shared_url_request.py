# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTensorboardSharedUrlRequest(DaraModel):
    def __init__(
        self,
        expire_time_seconds: str = None,
    ):
        # The validity period of the shareable link. Unit: seconds. Maximum value: 604800.
        self.expire_time_seconds = expire_time_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time_seconds is not None:
            result['ExpireTimeSeconds'] = self.expire_time_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTimeSeconds') is not None:
            self.expire_time_seconds = m.get('ExpireTimeSeconds')

        return self

