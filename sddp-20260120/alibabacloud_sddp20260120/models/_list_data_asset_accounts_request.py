# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAssetAccountsRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        auth_db: str = None,
        auth_role: str = None,
        biz_type: str = None,
        current_page: int = None,
        instance_id: str = None,
        lang: str = None,
        page_size: int = None,
        product_code: str = None,
        product_ids: str = None,
    ):
        # The database account name. The system filters accounts by the exact account name.
        self.account_name = account_name
        # The authentication database of the MongoDB account. This parameter is used to distinguish accounts with the same name in different authentication databases.
        self.auth_db = auth_db
        # The column encryption access permissions. Valid values:
        # - fullAccess: plaintext access
        # - restrictedAccess: restricted access
        # - noneAccess: decryption prohibited. This value applies only to ApsaraDB RDS for MySQL instances whose current effective key mode is client_key.
        self.auth_role = auth_role
        # The business scenario for the query. Set this parameter to DataMasking for the column encryption scenario. Note that the value is case-sensitive.
        self.biz_type = biz_type
        # The page number of the current page. Pages start from 1.
        self.current_page = current_page
        # The database instance ID. You can obtain this value from the Items[].InstanceId parameter in the response of the ListDataMaskingInstances operation.
        self.instance_id = instance_id
        # The language of the response message. Valid values:
        # - zh: Chinese
        # - en: English
        self.lang = lang
        # The number of entries to return on each page. Keep other filter conditions consistent when querying the next page.
        self.page_size = page_size
        # The cloud service code. Column encryption supports RDS, POLARDB, and PolarDBX2. If ProductId is also specified, the two parameters must match.
        self.product_code = product_code
        # The list of cloud service type IDs. Separate multiple values with commas (,). For the column encryption scenario, the valid values are 5 (RDS), 8 (POLARDB), and 27 (PolarDBX2).
        self.product_ids = product_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.auth_db is not None:
            result['AuthDb'] = self.auth_db

        if self.auth_role is not None:
            result['AuthRole'] = self.auth_role

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AuthDb') is not None:
            self.auth_db = m.get('AuthDb')

        if m.get('AuthRole') is not None:
            self.auth_role = m.get('AuthRole')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')

        return self

