# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteScanRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        scan_rule_id: str = None,
    ):
        # The instance ID
        self.instance_id = instance_id
        # The rule ID
        self.scan_rule_id = scan_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scan_rule_id is not None:
            result['ScanRuleId'] = self.scan_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScanRuleId') is not None:
            self.scan_rule_id = m.get('ScanRuleId')

        return self

