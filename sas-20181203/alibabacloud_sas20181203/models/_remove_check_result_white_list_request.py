# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveCheckResultWhiteListRequest(DaraModel):
    def __init__(
        self,
        check_group_id: str = None,
        check_ids: List[int] = None,
        instance_ids: List[str] = None,
        rule_id: int = None,
        type: str = None,
    ):
        # This parameter is deprecated.
        self.check_group_id = check_group_id
        # The IDs of the check items.
        self.check_ids = check_ids
        # A set of cloud product instance IDs that require validation.
        self.instance_ids = instance_ids
        # The ID of the whitelist rule.
        # 
        # >  You can call the [ListCheckResult](~~ListCheckResult~~) operation to query the IDs of whitelist rules.
        self.rule_id = rule_id
        # This parameter is deprecated.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_group_id is not None:
            result['CheckGroupId'] = self.check_group_id

        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckGroupId') is not None:
            self.check_group_id = m.get('CheckGroupId')

        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

