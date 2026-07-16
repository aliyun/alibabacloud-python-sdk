# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateSwitchStatusRequest(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
        status: str = None,
    ):
        # The rule ID.
        # > You can call the [ListSasContainerWebDefenseRule](https://help.aliyun.com/document_detail/2623606.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The status of the container tamper-proofing rule. Valid values:
        # - on: enabled.
        # - off: disabled.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

