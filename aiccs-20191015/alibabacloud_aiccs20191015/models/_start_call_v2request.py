# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartCallV2Request(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        callee: str = None,
        caller: str = None,
        caller_type: int = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # Agent account name (agent logon name).
        # 
        # This parameter is required.
        self.account_name = account_name
        # Callee number for hotline outbound calls.
        # 
        # This parameter is required.
        self.callee = callee
        # Caller number for hotline outbound calls.
        # 
        # This parameter is required.
        self.caller = caller
        # Call type. Valid values:
        # 
        # - **1**: Inbound
        # - **2**: Outbound
        # 
        # This parameter is required.
        self.caller_type = caller_type
        # Unique customer request ID. Used for idempotency validation. You can generate it using UUID.
        self.client_token = client_token
        # AICCS instance ID. You can obtain it from the Artificial Intelligence Cloud Call Service console.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.caller_type is not None:
            result['CallerType'] = self.caller_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

