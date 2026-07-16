# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ReplaceCloudGtmAddressPoolAddressRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pool_id: str = None,
        addresses: List[main_models.ReplaceCloudGtmAddressPoolAddressRequestAddresses] = None,
        client_token: str = None,
    ):
        # The response language. Valid values:
        # 
        # - **zh-CN**: Chinese
        # 
        # - **en-US** (Default): English
        self.accept_language = accept_language
        # The unique ID of the address pool to update.
        self.address_pool_id = address_pool_id
        # The list of addresses.
        self.addresses = addresses
        # The client token that is used to ensure the idempotence of the request. Ensure the client token is unique for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        self.addresses = []
        if m.get('Addresses') is not None:
            for k1 in m.get('Addresses'):
                temp_model = main_models.ReplaceCloudGtmAddressPoolAddressRequestAddresses()
                self.addresses.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

class ReplaceCloudGtmAddressPoolAddressRequestAddresses(DaraModel):
    def __init__(
        self,
        address_id: str = None,
        request_source: List[str] = None,
        serial_number: int = None,
        weight_value: int = None,
    ):
        # The unique ID of the address.
        # 
        # - If you specify this parameter, all existing addresses in the address pool are deleted and replaced with the specified addresses.
        # 
        # - If you leave this parameter empty, all existing addresses in the address pool are deleted.
        self.address_id = address_id
        # The list of DNS request sources.
        self.request_source = request_source
        # The serial number, which determines the priority of the address. A smaller number indicates a higher priority. This setting applies to the updated addresses.
        self.serial_number = serial_number
        # The weight of the address. Valid values: 1 to 100. You can set a different weight for each address. DNS queries are then resolved based on the weight ratio. This setting applies to the updated addresses.
        self.weight_value = weight_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.weight_value is not None:
            result['WeightValue'] = self.weight_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('WeightValue') is not None:
            self.weight_value = m.get('WeightValue')

        return self

