# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountParameterRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        instance_id: str = None,
        parameters: str = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.parameters = parameters
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

