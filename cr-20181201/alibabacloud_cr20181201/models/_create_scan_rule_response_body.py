# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScanRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
        scan_rule_id: str = None,
    ):
        # The returned HTTP or HTTPS status code.
        self.code = code
        # Request Id
        self.request_id = request_id
        # The rule ID.
        self.scan_rule_id = scan_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scan_rule_id is not None:
            result['ScanRuleId'] = self.scan_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScanRuleId') is not None:
            self.scan_rule_id = m.get('ScanRuleId')

        return self

