# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ImportOneTaskPhoneNumberRequest(DaraModel):
    def __init__(
        self,
        out_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
        variables: Dict[str, Any] = None,
    ):
        self.out_id = out_id
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.task_id = task_id
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self

