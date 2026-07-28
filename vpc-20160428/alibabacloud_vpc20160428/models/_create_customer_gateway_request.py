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
        # The Autonomous System Number (ASN) of the gateway device in the on-premises data center. This parameter is required if you plan to enable Border Gateway Protocol (BGP) dynamic routing for the IPsec-VPN connection. Valid values: 1 to 4294967295. The value 45104 is not supported.
        # 
        # **Asn** is a 4-byte number that can be entered in the two-segment format: the first 16 bits.the last 16 bits. Each segment is entered in decimal notation.
        # 
        # For example, if you enter 123.456, the ASN is 123 × 65536 + 456 = 8061384.
        # 
        # > - Use a private ASN to establish a BGP connection with Alibaba Cloud. For more information about the range of private ASNs, refer to the relevant documentation.
        # > - 45104 is a unique identity allocated to Alibaba Cloud Computing Co., Ltd. by the Internet Assigned Numbers Authority (IANA). It is used to identify Alibaba Cloud in global Internet routing and data transmission.
        self.asn = asn
        # The authentication key of the BGP routing protocol for the gateway device in the on-premises data center.
        # 
        # The key must be 1 to 64 characters in length and can contain only ASCII characters. Spaces, Chinese characters, and half-width question marks (?) are not supported.
        self.auth_key = auth_key
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the customer gateway.  
        # 
        # The description must be 1 to 100 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The static IP address of the gateway device in the on-premises data center.
        # 
        # - If you want to create an IPsec-VPN connection that uses the public network type, enter a public IP address.
        # 
        # - If you want to create an IPsec-VPN connection that uses the private network type, enter a private IP address.
        # 
        # The following IP addresses are not supported. If you use these IP addresses, the IPsec-VPN connection cannot be established:
        # 
        # - 100.64.0.0 to 100.127.255.255
        # - 127.0.0.0 to 127.255.255.255
        # - 169.254.0.0 to 169.254.255.255
        # - 224.0.0.0 to 239.255.255.255
        # - 255.0.0.0 to 255.255.255.255
        # 
        # This parameter is required.
        self.ip_address = ip_address
        # The name of the customer gateway.  
        # 
        # The name must be 1 to 100 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the customer gateway. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the customer gateway belongs.
        # 
        # - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query the resource group ID.
        # - If you do not specify a resource group, the customer gateway is added to the default resource group after it is created.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags to add to the customer gateway.
        # 
        # You can add up to 20 tags to a customer gateway at a time.
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
        # The tag key. If you specify this parameter, the value cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys at a time.
        self.key = key
        # The tag value.
        # 
        # The tag value can be up to 128 characters in length and can be an empty string. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each tag key corresponds to one tag value. You can specify up to 20 tag values at a time.
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

