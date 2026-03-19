# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateLayer7RuleRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_ids: List[str] = None,
        resource_group_id: str = None,
        rs_type: int = None,
        rules: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.instance_ids = instance_ids
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rs_type = rs_type
        # This parameter is required.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self

