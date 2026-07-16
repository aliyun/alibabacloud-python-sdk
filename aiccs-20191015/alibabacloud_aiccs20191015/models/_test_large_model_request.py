# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TestLargeModelRequest(DaraModel):
    def __init__(
        self,
        base_model: List[str] = None,
        model_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_dialog_content: str = None,
    ):
        # The base models.
        self.base_model = base_model
        # The ID of the test scenario.
        self.model_code = model_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The user dialog content.
        self.user_dialog_content = user_dialog_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_model is not None:
            result['BaseModel'] = self.base_model

        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_dialog_content is not None:
            result['UserDialogContent'] = self.user_dialog_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseModel') is not None:
            self.base_model = m.get('BaseModel')

        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserDialogContent') is not None:
            self.user_dialog_content = m.get('UserDialogContent')

        return self

