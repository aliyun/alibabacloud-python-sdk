# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddLargeModelRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        base_model: List[str] = None,
        model_name: str = None,
        model_url: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        temperature: float = None,
        top_k: int = None,
        top_p: float = None,
    ):
        # The authorization code.
        self.auth_code = auth_code
        # The base model.
        self.base_model = base_model
        # The model name.
        self.model_name = model_name
        # The model URL.
        self.model_url = model_url
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The temperature.
        self.temperature = temperature
        # The `top-k` value.
        self.top_k = top_k
        # The `top-p` value.
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.base_model is not None:
            result['BaseModel'] = self.base_model

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_url is not None:
            result['ModelUrl'] = self.model_url

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.top_p is not None:
            result['TopP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('BaseModel') is not None:
            self.base_model = m.get('BaseModel')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        return self

