# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotlineCallActionRequest(DaraModel):
    def __init__(
        self,
        acc: str = None,
        account_name: str = None,
        act: int = None,
        biz: str = None,
        client_token: str = None,
        from_source: str = None,
        instance_id: str = None,
    ):
        # Hotline Custom Parameter in JSON format.
        self.acc = acc
        # Agent account name, which is the phone number or mailbox specified during account registration. It is unique within the instance.
        self.account_name = account_name
        # Operation Type. Valid values:
        # - **1**: Hotline.
        # - **2**: Online.
        # - **3**: Ticket.
        self.act = act
        # Business Custom Parameter in JSON format.
        self.biz = biz
        # Unique ID of the customer request. Used for idempotency validation. You can generate it by using a UUID.
        self.client_token = client_token
        # Source type. Valid values:
        # 
        # - **hotlinebs_out**: Hotline.
        # - **ticket_out**: Ticket.
        # - **other_system_out**: Other system.
        self.from_source = from_source
        # Artificial Intelligence Cloud Call Service (AICCS) instance ID.
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
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.act is not None:
            result['Act'] = self.act

        if self.biz is not None:
            result['Biz'] = self.biz

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.from_source is not None:
            result['FromSource'] = self.from_source

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Act') is not None:
            self.act = m.get('Act')

        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FromSource') is not None:
            self.from_source = m.get('FromSource')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

