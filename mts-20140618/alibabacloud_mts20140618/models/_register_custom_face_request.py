# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterCustomFaceRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        image_url: str = None,
        owner_account: str = None,
        owner_id: int = None,
        person_id: str = None,
        person_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the figure library in which you want to register a custom face. The ID is used to uniquely identify a figure library. You can specify the ID of a custom figure library. Make sure that the ID is unique and keep the ID for future API operation calls. If you set this parameter to the ID of a system figure library, the custom face is registered in the system figure library. The ID can be up to 120 characters in length and is not case-sensitive.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The URL of the facial image that you want to register for the specified figure. The image must contain only one face.
        # 
        # This parameter is required.
        self.image_url = image_url
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the figure for which you want to register a custom face. The ID is used to uniquely identify a figure. You can specify a figure ID. Make sure that the ID is unique and keep the ID for future API operation calls. The ID can be up to 120 characters in length and is not case-sensitive. The value returned is of the String type.
        # 
        # This parameter is required.
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
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')

        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

