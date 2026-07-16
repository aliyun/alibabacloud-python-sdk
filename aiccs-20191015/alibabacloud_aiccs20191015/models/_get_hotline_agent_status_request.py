# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotlineAgentStatusRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        instance_id: str = None,
    ):
        # Agent account name, which is the phone number or mailbox entered during account registration. It is unique within the instance.
        # 
        # This parameter is required.
        self.account_name = account_name
        # AICCS instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

