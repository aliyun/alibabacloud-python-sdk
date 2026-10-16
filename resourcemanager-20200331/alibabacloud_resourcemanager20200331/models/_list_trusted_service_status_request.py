# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTrustedServiceStatusRequest(DaraModel):
    def __init__(
        self,
        admin_account_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The management account or delegated administrator account. Valid values:
        # - Management account (default): Queries the list of trusted services enabled by the management account.
        # - Delegated administrator account: Queries the list of trusted services enabled by the delegated administrator account.
        # 
        # For more information about trusted services and delegated administrator accounts, see [Overview of trusted services](https://help.aliyun.com/document_detail/208133.html) and [Manage delegated administrator accounts](https://help.aliyun.com/document_detail/208117.html).
        self.admin_account_id = admin_account_id
        # The page number.
        # 
        # Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_account_id is not None:
            result['AdminAccountId'] = self.admin_account_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminAccountId') is not None:
            self.admin_account_id = m.get('AdminAccountId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

