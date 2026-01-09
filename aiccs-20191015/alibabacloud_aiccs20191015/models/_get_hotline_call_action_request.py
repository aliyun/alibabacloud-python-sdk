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
        self.acc = acc
        self.account_name = account_name
        self.act = act
        self.biz = biz
        self.client_token = client_token
        self.from_source = from_source
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

