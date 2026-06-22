# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecurityScoreRuleRequest(DaraModel):
    def __init__(
        self,
        cal_type: str = None,
        lang: str = None,
    ):
        # Specifies whether to query the new or legacy security score rules. If the value is **home_security_score**, the new security score rules are queried. Otherwise, the legacy security score rules are queried by default.
        self.cal_type = cal_type
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cal_type is not None:
            result['CalType'] = self.cal_type

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalType') is not None:
            self.cal_type = m.get('CalType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

