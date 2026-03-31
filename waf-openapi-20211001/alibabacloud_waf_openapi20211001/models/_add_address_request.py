# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddAddressRequest(DaraModel):
    def __init__(
        self,
        address_list: List[str] = None,
        instance_id: str = None,
        resource_manager_resource_group_id: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.address_list = address_list
        # This parameter is required.
        self.instance_id = instance_id
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_list is not None:
            result['AddressList'] = self.address_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

