# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountResponseBody(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        acount_name: str = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.account_name = account_name
        # The name of the account.
        self.acount_name = acount_name
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.acount_name is not None:
            result['AcountName'] = self.acount_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AcountName') is not None:
            self.acount_name = m.get('AcountName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

