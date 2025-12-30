# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ReplaceCloudGtmInstanceConfigAddressPoolRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address_pools: List[main_models.ReplaceCloudGtmInstanceConfigAddressPoolRequestAddressPools] = None,
        client_token: str = None,
        config_id: str = None,
        instance_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The address pools.
        self.address_pools = address_pools
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The configuration ID of the access domain name. Two configuration IDs exist when the access domain name is bound to the same GTM instance but an A record and an AAAA record are configured for the access domain name. The configuration ID uniquely identifies a configuration.
        # 
        # You can call the [ListCloudGtmInstanceConfigs](~~ListCloudGtmInstanceConfigs~~) operation to query the configuration ID of the access domain name.
        self.config_id = config_id
        # The ID of the GTM 3.0 instance for which you want to change address pools.
        self.instance_id = instance_id

    def validate(self):
        if self.address_pools:
            for v1 in self.address_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        result['AddressPools'] = []
        if self.address_pools is not None:
            for k1 in self.address_pools:
                result['AddressPools'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        self.address_pools = []
        if m.get('AddressPools') is not None:
            for k1 in m.get('AddressPools'):
                temp_model = main_models.ReplaceCloudGtmInstanceConfigAddressPoolRequestAddressPools()
                self.address_pools.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class ReplaceCloudGtmInstanceConfigAddressPoolRequestAddressPools(DaraModel):
    def __init__(
        self,
        address_pool_id: str = None,
        request_source: List[str] = None,
        serial_number: int = None,
        weight_value: int = None,
    ):
        # The ID of the address pool. This ID uniquely identifies the address pool.
        # 
        # *   If you specify this parameter, the address pools that are associated with the desired instance are removed and the instance is associated with new address pools.
        # *   If this parameter is left empty, the address pools that are associated with the desired instance are removed and no address pool is associated with the instance.
        self.address_pool_id = address_pool_id
        # The DNS request sources.
        self.request_source = request_source
        # The sequence number of the new address pool. The address pool with the smallest sequence number is preferentially returned for DNS requests from any source. The sequence number specifies the priority for returning the address pool. A smaller sequence number specifies a higher priority.
        self.serial_number = serial_number
        # The weight value of the new address pool. You can set a different weight value for each address pool. This way, address pools are returned based on the weight values for Domain Name System (DNS) requests. A weight value must be an integer that ranges from 1 to 100.
        self.weight_value = weight_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.weight_value is not None:
            result['WeightValue'] = self.weight_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('WeightValue') is not None:
            self.weight_value = m.get('WeightValue')

        return self

