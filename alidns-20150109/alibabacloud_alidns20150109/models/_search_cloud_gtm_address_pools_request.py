# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchCloudGtmAddressPoolsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_name: str = None,
        address_pool_type: str = None,
        available_status: str = None,
        client_token: str = None,
        enable_status: str = None,
        health_status: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # Address pool name, supports fuzzy search for the entered address pool name.
        self.address_pool_name = address_pool_name
        # Address pool type, supports precise query for address pool types:
        # - IPv4
        # - IPv6
        # - domain
        self.address_pool_type = address_pool_type
        # Address pool availability status, supporting precise queries for address pool availability:
        # - available: Available
        # - unavailable: Unavailable
        self.available_status = available_status
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Address pool enable status, supports precise query of address pool enable status:
        # - enable: Enabled status
        # - disable: Disabled status
        self.enable_status = enable_status
        # The health state of the address pool. You can enter a health state for exact search. Valid values:
        # 
        # ok: The health state of the address pool is normal and all addresses that are referenced by the address pool are available.
        # 
        # ok_alert: The health state of the address pool is warning and some of the addresses that are referenced by the address pool are unavailable. However, the address pool is deemed normal. In this case, only the available addresses are returned for Domain Name System (DNS) requests.
        # 
        # exceptional: The health state of the address pool is abnormal and some or all of the addresses that are referenced by the address pool are unavailable. In this case, the address pool is deemed abnormal.
        self.health_status = health_status
        # Current page number, starting from 1, default is 1.
        self.page_number = page_number
        # The number of rows per page when paginating queries, with a maximum value of 100 and a default of 20.
        self.page_size = page_size
        # Address pool remarks, supporting fuzzy search for the input remarks.
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

        if self.available_status is not None:
            result['AvailableStatus'] = self.available_status

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

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

        if m.get('AvailableStatus') is not None:
            self.available_status = m.get('AvailableStatus')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

