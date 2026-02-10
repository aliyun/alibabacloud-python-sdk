# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExposedInstanceCriteriaRequest(DaraModel):
    def __init__(
        self,
        resource_directory_account_id: str = None,
        value: str = None,
    ):
        # The ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to query the account ID.
        self.resource_directory_account_id = resource_directory_account_id
        # The value of the search condition. Fuzzy match is supported.
        # 
        # >  You can specify the name, ID, public IP address, private IP address, component, port, or IP address of an exposed asset.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

