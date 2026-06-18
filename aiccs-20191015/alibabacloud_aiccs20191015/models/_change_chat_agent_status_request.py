# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeChatAgentStatusRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        client_token: str = None,
        instance_id: str = None,
        method: str = None,
    ):
        # Agent account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Unique ID for the customer request. Used for idempotency validation. You can generate it using UUID.
        self.client_token = client_token
        # Artificial Intelligence Cloud Call Service (AICCS) instance ID. You can obtain it from the Artificial Intelligence Cloud Call Service console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The target online status to switch to. Currently, only **requestLogout** (request offline) is supported.
        # 
        # This parameter is required.
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.method is not None:
            result['Method'] = self.method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        return self

