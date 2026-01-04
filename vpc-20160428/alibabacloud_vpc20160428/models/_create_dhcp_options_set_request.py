# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateDhcpOptionsSetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dhcp_options_set_description: str = None,
        dhcp_options_set_name: str = None,
        domain_name: str = None,
        domain_name_servers: str = None,
        dry_run: bool = None,
        ipv_6lease_time: str = None,
        lease_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateDhcpOptionsSetRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the DHCP options set.
        # 
        # The description must be 1 to 256 characters in length. It must start with a letter and cannot start with `http://` or `https://`.
        self.dhcp_options_set_description = dhcp_options_set_description
        # The name of the DHCP options set.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        self.dhcp_options_set_name = dhcp_options_set_name
        # The root domain. For example, you can set the value to example.com.
        # 
        # After a DHCP options set is associated with a virtual private cloud (VPC), the root domain in the DHCP options set is automatically synchronized with the ECS instances in the VPC.
        self.domain_name = domain_name
        # The IP address of the DNS server. You can enter at most four DNS server IP addresses. Separate IP addresses with commas (,).
        # 
        # >  If no IP address is specified, the Elastic Compute Service (ECS) instance uses the IP addresses 100.100.2.136 and 100.100.2.138, which are provided by Alibaba Cloud by default.
        self.domain_name_servers = domain_name_servers
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The lease time of the IPv6 addresses for the DHCP options set.
        # 
        # *   If you use hours as the unit, valid values are **24h to 1176h** and **87600h to 175200h**. Default value: **87600h**.
        # *   If you use days as the unit, valid values are **1d to 49d** and **3650d to 7300d**. Default value: **3650d**.
        # 
        # >  When you enter a value, you must also specify the unit.
        self.ipv_6lease_time = ipv_6lease_time
        # The lease time of the IPv4 addresses for the DHCP options set.
        # 
        # *   If you use hours as the unit, valid values are **24h to 1176h** and **87600h to 175200h**. Default value: **87600h**.
        # *   If you use days as the unit, valid values are **1d to 49d** and **3650d to 7300d**. Default value: **3650d**.
        # 
        # >  When you enter a value, you must also specify the unit.
        self.lease_time = lease_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region to which the DHCP options set belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the DHCP options set belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag of the resource.
        self.tag = tag

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dhcp_options_set_description is not None:
            result['DhcpOptionsSetDescription'] = self.dhcp_options_set_description

        if self.dhcp_options_set_name is not None:
            result['DhcpOptionsSetName'] = self.dhcp_options_set_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_servers is not None:
            result['DomainNameServers'] = self.domain_name_servers

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipv_6lease_time is not None:
            result['Ipv6LeaseTime'] = self.ipv_6lease_time

        if self.lease_time is not None:
            result['LeaseTime'] = self.lease_time

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DhcpOptionsSetDescription') is not None:
            self.dhcp_options_set_description = m.get('DhcpOptionsSetDescription')

        if m.get('DhcpOptionsSetName') is not None:
            self.dhcp_options_set_name = m.get('DhcpOptionsSetName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameServers') is not None:
            self.domain_name_servers = m.get('DomainNameServers')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Ipv6LeaseTime') is not None:
            self.ipv_6lease_time = m.get('Ipv6LeaseTime')

        if m.get('LeaseTime') is not None:
            self.lease_time = m.get('LeaseTime')

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
                temp_model = main_models.CreateDhcpOptionsSetRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateDhcpOptionsSetRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be at most 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N to add to the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
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

