# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateCustomerGatewayRequest(DaraModel):
    def __init__(
        self,
        asn: str = None,
        auth_key: str = None,
        client_token: str = None,
        description: str = None,
        ip_address: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.CreateCustomerGatewayRequestTags] = None,
    ):
        # The autonomous system number (ASN) of the gateway device in your data center. This parameter is required If you want to use Border Gateway Protocol (BGP) for the IPsec-VPN connection. Valid values: 1 to 4294967295. 45104 is not supported.
        # 
        # **Asn** is a 4-byte number. You can enter it in two segments and separate the first 16 bits from the following 16 bits with a period (.). Enter the number in each segment in decimal format.
        # 
        # For example, if you enter 123.456, the ASN is 8061384. The ASN is calculated by using the following formula: 123 × 65536 + 456 = 8061384.
        # 
        # > - We recommend that you use a private ASN to establish BGP connections to Alibaba Cloud. For information about the range of private ASNs, see the relevant documentation.
        # > - 45104 is a unique identifier assigned by IANA to Alibaba Cloud. It is used to identify Alibaba Cloud during route selection and data transmission over the Internet.
        self.asn = asn
        # The authentication key of the BGP routing protocol for the gateway device in the data center.
        # 
        # The key must be 1 to 64 characters in length. It can contain only ASCII characters and cannot contain spaces or question marks (?).
        self.auth_key = auth_key
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the customer gateway.
        # 
        # The description must be 1 to 100 characters in length, and cannot start with `http://` or `https://`.
        self.description = description
        # The static IP address of the gateway device in the data center.
        # 
        # *   If you want to create a public IPsec-VPN connection, enter a public IP address.
        # *   If you want to create a private IPsec-VPN connection, enter a private IP address.
        # 
        # You cannot use the following IP addresses. Otherwise, a IPsec-VPN connection cannot be established:
        # 
        # *   100.64.0.0~100.127.255.255
        # *   127.0.0.0~127.255.255.255
        # *   169.254.0.0~169.254.255.255
        # *   224.0.0.0~239.255.255.255
        # *   255.0.0.0~255.255.255.255
        # 
        # This parameter is required.
        self.ip_address = ip_address
        # The name of the customer gateway.
        # 
        # The name must be 1 to 100 characters in length, and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the customer gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the customer gateway belongs.
        # 
        # - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query the resource group list.
        # 
        # - If you do not specify a resource group, the customer gateway will belong to the default resource group after being created.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag value.
        # 
        # The tag value can be an empty string and cannot exceed 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # Each tag key corresponds to one tag value. You can specify up to 20 tag values in each call.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asn is not None:
            result['Asn'] = self.asn

        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asn') is not None:
            self.asn = m.get('Asn')

        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateCustomerGatewayRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateCustomerGatewayRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key cannot be an empty string.
        # 
        # It can be at most 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # You can specify at most 20 tag keys in each call.
        self.key = key
        # The tag value.
        # 
        # The tag value can be an empty string and cannot exceed 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # Each tag key corresponds to one tag value. You can specify at most 20 tag values in each call.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

