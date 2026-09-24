# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartHotlineServiceRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # The name of the agent account, which is the mobile number or email address specified during account registration. The name must be unique within the instance.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The unique ID of the client request. Used for idempotency checks. You can use a UUID to generate this ID.
        self.client_token = client_token
        # The ID of the Artificial Intelligence Cloud Call Service (AICCS) instance.
        # You can obtain the instance ID from **Instance Management** in the left-side navigation pane of the [AICCS console](https://aiccs.console.aliyun.com/overview).
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

