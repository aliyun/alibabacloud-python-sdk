# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendHotlineHeartBeatRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        client_token: str = None,
        instance_id: str = None,
        token: str = None,
    ):
        # Agent account name, which is the phone number or mailbox specified during account registration. It is unique within the instance.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Unique ID for the customer request. Used for idempotency validation. You can generate it using UUID.
        self.client_token = client_token
        # Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it in the <b>Instance Management</b> section of the left-side navigation pane in the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Heartbeat signature.  
        # 
        # You can obtain the token by invoking the [StartHotlineService](https://help.aliyun.com/document_detail/2718045.html) API.
        # 
        # This parameter is required.
        self.token = token

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

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

