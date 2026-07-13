# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudGtmAddressPoolsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_name: str = None,
        address_pool_type: str = None,
        client_token: str = None,
        enable_status: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English. This is the default value.
        self.accept_language = accept_language
        # The name of the address pool.
        self.address_pool_name = address_pool_name
        # The type of the address pool. Valid values:
        # 
        # - IPv4: The address pool contains IPv4 addresses.
        # 
        # - IPv6: The address pool contains IPv6 addresses.
        # 
        # - domain: The address pool contains domain names.
        self.address_pool_type = address_pool_type
        # A client-generated token that is used to ensure the idempotence of the request. Make sure that the token is unique among different requests. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The status of the address pool. Valid values:
        # 
        # - enable: The address pool is enabled.
        # 
        # - disable: The address pool is disabled.
        self.enable_status = enable_status
        # The page number. The value starts from **1**. The default value is **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is **100**. The default value is **20**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The remarks for the address pool.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address_pool_name is not None:
            result['AddressPoolName'] = self.address_pool_name

        if self.address_pool_type is not None:
            result['AddressPoolType'] = self.address_pool_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolName') is not None:
            self.address_pool_name = m.get('AddressPoolName')

        if m.get('AddressPoolType') is not None:
            self.address_pool_type = m.get('AddressPoolType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

