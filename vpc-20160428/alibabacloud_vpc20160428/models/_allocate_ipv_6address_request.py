# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class AllocateIpv6AddressRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ipv_6address: str = None,
        ipv_6address_description: str = None,
        ipv_6address_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.AllocateIpv6AddressRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The type of the IPv6 address. Valid values:
        # 
        # * IPv6Address (default): The instance is a single IPv6 address.
        # * IPv6Prefix: The instance is an IPv6 prefix CIDR block.
        self.address_type = address_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - true: performs a dry run. The system checks the required parameters, request syntax, and business restrictions. If the check fails, the corresponding error is returned. If the check succeeds, the error code DryRunOperation is returned.
        # 
        # - false (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The IPv6 address to allocate. The specified IPv6 address must be an idle address within the CIDR block of the vSwitch.
        self.ipv_6address = ipv_6address
        # The description of the IPv6 address instance.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.ipv_6address_description = ipv_6address_description
        # The name of the IPv6 address instance.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipv_6address_name = ipv_6address_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. For more information about resource groups, see [What is a resource group?](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags for the resource.
        self.tag = tag
        # The ID of the vSwitch to which the IPv6 address belongs.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_description is not None:
            result['Ipv6AddressDescription'] = self.ipv_6address_description

        if self.ipv_6address_name is not None:
            result['Ipv6AddressName'] = self.ipv_6address_name

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressDescription') is not None:
            self.ipv_6address_description = m.get('Ipv6AddressDescription')

        if m.get('Ipv6AddressName') is not None:
            self.ipv_6address_name = m.get('Ipv6AddressName')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.AllocateIpv6AddressRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class AllocateIpv6AddressRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. Do not pass in an empty string.
        # 
        # A tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. You can pass in an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with aliyun or acs:, or contain http:// or https://.
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

