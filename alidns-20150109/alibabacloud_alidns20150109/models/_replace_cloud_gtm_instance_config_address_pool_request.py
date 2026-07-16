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
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # A list of address pools.
        self.address_pools = address_pools
        # A client-generated token that you use to ensure the idempotence of the request. Make sure that the token is unique among different requests. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The ID of the instance configuration. For the same access domain name and GTM instance, you can configure both A and AAAA records. In this case, the GTM instance has two instance configurations. The ConfigId parameter uniquely identifies an instance configuration.
        # 
        # Call the [ListCloudGtmInstanceConfigs](https://help.aliyun.com/document_detail/2797349.html) operation to query the ConfigId of the instance configuration.
        self.config_id = config_id
        # The ID of the GTM 3.0 instance for which you want to replace address pools.
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
        # The unique ID of the address pool.
        # 
        # - If you specify this parameter, the existing address pools associated with the target instance are deleted and replaced with the address pools that you specify.
        # 
        # - If you leave this parameter empty, all address pools associated with the target instance are deleted.
        self.address_pool_id = address_pool_id
        # A list of request sources.
        self.request_source = request_source
        # The ordinal number. For DNS requests from any source, address pools with smaller ordinal numbers are returned first. A smaller ordinal number indicates a higher priority. This parameter takes effect for the updated address pools.
        self.serial_number = serial_number
        # The weight of the address pool. Valid values are integers from 1 to 100. You can set a different weight for each address pool. DNS queries are resolved based on the specified weights. This parameter takes effect for the updated address pools.
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

