# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPublishedAppInfoRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        biz_region_id: str = None,
        category_id: int = None,
        category_type: int = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        order_param: str = None,
        product_type: str = None,
        session_id: str = None,
        sort_type: str = None,
    ):
        self.app_name = app_name
        self.biz_region_id = biz_region_id
        self.category_id = category_id
        self.category_type = category_type
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.order_param = order_param
        self.product_type = product_type
        self.session_id = session_id
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.order_param is not None:
            result['OrderParam'] = self.order_param

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('OrderParam') is not None:
            self.order_param = m.get('OrderParam')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

