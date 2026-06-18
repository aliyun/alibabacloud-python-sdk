# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNumLocationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        phone_num: str = None,
    ):
        # Unique ID for the customer request. Used for idempotency validation and can be generated using a UUID.
        self.client_token = client_token
        # Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it in the <b>Instance Management</b> section of the left-side navigation pane in the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Phone number to query.
        # 
        # This parameter is required.
        self.phone_num = phone_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        return self

