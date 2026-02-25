# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagCustomPersonRequest(DaraModel):
    def __init__(
        self,
        category_description: str = None,
        category_id: str = None,
        category_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        person_description: str = None,
        person_id: str = None,
        person_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.category_description = category_description
        self.category_id = category_id
        self.category_name = category_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.person_description = person_description
        self.person_id = person_id
        self.person_name = person_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_description is not None:
            result['CategoryDescription'] = self.category_description

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.person_description is not None:
            result['PersonDescription'] = self.person_description

        if self.person_id is not None:
            result['PersonId'] = self.person_id

        if self.person_name is not None:
            result['PersonName'] = self.person_name

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryDescription') is not None:
            self.category_description = m.get('CategoryDescription')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PersonDescription') is not None:
            self.person_description = m.get('PersonDescription')

        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')

        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

