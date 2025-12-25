# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountDelegatedStatusResponseBody(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        delegated_status: bool = None,
        request_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The name of the Alibaba Cloud account. This parameter is returned only if the account is the delegated administrator account.
        self.account_name = account_name
        # Indicates whether the Alibaba Cloud account is the delegated administrator account of the WAF instance.
        # 
        # *   **true**
        # *   **false**
        self.delegated_status = delegated_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.delegated_status is not None:
            result['DelegatedStatus'] = self.delegated_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DelegatedStatus') is not None:
            self.delegated_status = m.get('DelegatedStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

