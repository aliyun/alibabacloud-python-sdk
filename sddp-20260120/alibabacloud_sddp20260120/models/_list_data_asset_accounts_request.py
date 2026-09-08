# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAssetAccountsRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        auth_role: str = None,
        biz_type: str = None,
        current_page: int = None,
        instance_id: str = None,
        lang: str = None,
        page_size: int = None,
        product_code: str = None,
        product_ids: str = None,
    ):
        self.account_name = account_name
        self.auth_role = auth_role
        self.biz_type = biz_type
        self.current_page = current_page
        self.instance_id = instance_id
        self.lang = lang
        self.page_size = page_size
        self.product_code = product_code
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

