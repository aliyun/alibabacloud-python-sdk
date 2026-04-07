# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ScanSensitiveDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sensitives: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The check result. sensDatas indicates the rules that are used to check the sensitive data. sensDatas includes the following parameters:
        # 
        # *   hitCount: the number of times that the sensitive data hits the rule.
        # *   ruleName: the name of the rule.
        self.sensitives = sensitives

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sensitives is not None:
            result['Sensitives'] = self.sensitives

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sensitives') is not None:
            self.sensitives = m.get('Sensitives')

        return self

