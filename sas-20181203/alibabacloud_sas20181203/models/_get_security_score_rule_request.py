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
        # The old or new version of the security score rule. If you set this parameter to **home_security_score**, the new version of the security score rule is returned. Otherwise, the old version of the security score rule is returned by default.
        self.cal_type = cal_type
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
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

