# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiTokenRateLimitConfigRule(DaraModel):
    def __init__(
        self,
        limit_mode: str = None,
        limit_type: str = None,
        limit_value: int = None,
        match_key: str = None,
        match_type: str = None,
        match_value: str = None,
    ):
        self.limit_mode = limit_mode
        self.limit_type = limit_type
        self.limit_value = limit_value
        self.match_key = match_key
        self.match_type = match_type
        self.match_value = match_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit_mode is not None:
            result['limitMode'] = self.limit_mode

        if self.limit_type is not None:
            result['limitType'] = self.limit_type

        if self.limit_value is not None:
            result['limitValue'] = self.limit_value

        if self.match_key is not None:
            result['matchKey'] = self.match_key

        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.match_value is not None:
            result['matchValue'] = self.match_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limitMode') is not None:
            self.limit_mode = m.get('limitMode')

        if m.get('limitType') is not None:
            self.limit_type = m.get('limitType')

        if m.get('limitValue') is not None:
            self.limit_value = m.get('limitValue')

        if m.get('matchKey') is not None:
            self.match_key = m.get('matchKey')

        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('matchValue') is not None:
            self.match_value = m.get('matchValue')

        return self

