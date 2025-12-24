# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchDeleteLiveDomainConfigsRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        function_names: str = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ingest domain or streaming domain. Separate multiple domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The names of the features. Separate multiple features with commas (,). For more information, see **Features specified by the Functions parameter**.
        # 
        # This parameter is required.
        self.function_names = function_names
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.function_names is not None:
            result['FunctionNames'] = self.function_names

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

