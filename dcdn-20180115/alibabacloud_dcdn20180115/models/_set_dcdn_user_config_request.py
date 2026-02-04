# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDcdnUserConfigRequest(DaraModel):
    def __init__(
        self,
        configs: str = None,
        function_id: int = None,
        owner_account: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The configuration parameters of the feature.
        # 
        # This parameter is required.
        self.configs = configs
        # The ID of the feature.
        # 
        # This parameter is required.
        self.function_id = function_id
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
        if self.configs is not None:
            result['Configs'] = self.configs

        if self.function_id is not None:
            result['FunctionId'] = self.function_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

