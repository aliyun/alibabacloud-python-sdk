# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudVendorAccountAKListRequest(DaraModel):
    def __init__(
        self,
        auth_ids: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        status: int = None,
        sub_account_name: str = None,
        vendor: str = None,
        vendor_auth_alias: str = None,
    ):
        # The unique ID of the AccessKey pair.
        self.auth_ids = auth_ids
        # The page number. Default value: 1.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The status of the AccessKey pair. Valid values:
        # 
        # *   **0**: enabled
        # *   **1**: disabled
        self.status = status
        # The username of the sub-account of the cloud service provider to which the AccessKey pair belongs.
        self.sub_account_name = sub_account_name
        self.vendor = vendor
        # The name of the AccessKey pair.
        self.vendor_auth_alias = vendor_auth_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_ids is not None:
            result['AuthIds'] = self.auth_ids

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_account_name is not None:
            result['SubAccountName'] = self.sub_account_name

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendor_auth_alias is not None:
            result['VendorAuthAlias'] = self.vendor_auth_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthIds') is not None:
            self.auth_ids = m.get('AuthIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAccountName') is not None:
            self.sub_account_name = m.get('SubAccountName')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorAuthAlias') is not None:
            self.vendor_auth_alias = m.get('VendorAuthAlias')

        return self

