# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddCheckResultWhiteListRequest(DaraModel):
    def __init__(
        self,
        check_ids: List[int] = None,
        instance_ids: List[str] = None,
        remark: str = None,
        rule_type: str = None,
    ):
        # The IDs of the check items.
        # 
        # >  You can call the [ListCheckResult](~~ListCheckResult~~) operation to query the IDs of the check items.
        self.check_ids = check_ids
        # IDs of the cloud product instances that need to be whitelisted. Separate multiple IDs with a comma (,).
        self.instance_ids = instance_ids
        # The description. The value of this parameter can be up to 65,535 bytes in length.
        self.remark = remark
        # The type of the rule. Default value: **WHITE**. Valid value:
        # 
        # *   **WHITE**: Add check items to the whitelist.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

