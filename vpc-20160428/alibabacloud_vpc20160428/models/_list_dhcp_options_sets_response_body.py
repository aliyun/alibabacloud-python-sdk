# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListDhcpOptionsSetsResponseBody(DaraModel):
    def __init__(
        self,
        dhcp_options_sets: List[main_models.ListDhcpOptionsSetsResponseBodyDhcpOptionsSets] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of the DHCP options sets.
        self.dhcp_options_sets = dhcp_options_sets
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is used to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries.
        self.total_count = total_count

    def validate(self):
        if self.dhcp_options_sets:
            for v1 in self.dhcp_options_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DhcpOptionsSets'] = []
        if self.dhcp_options_sets is not None:
            for k1 in self.dhcp_options_sets:
                result['DhcpOptionsSets'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dhcp_options_sets = []
        if m.get('DhcpOptionsSets') is not None:
            for k1 in m.get('DhcpOptionsSets'):
                temp_model = main_models.ListDhcpOptionsSetsResponseBodyDhcpOptionsSets()
                self.dhcp_options_sets.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDhcpOptionsSetsResponseBodyDhcpOptionsSets(DaraModel):
    def __init__(
        self,
        associate_vpc_count: int = None,
        creation_time: str = None,
        dhcp_options: main_models.ListDhcpOptionsSetsResponseBodyDhcpOptionsSetsDhcpOptions = None,
        dhcp_options_set_description: str = None,
        dhcp_options_set_id: str = None,
        dhcp_options_set_name: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListDhcpOptionsSetsResponseBodyDhcpOptionsSetsTags] = None,
    ):
        # The number of VPCs with which the DHCP options set is associated.
        self.associate_vpc_count = associate_vpc_count
        # The creation time of the DHCP options sets.
        self.creation_time = creation_time
        # The details of DHCP options.
        self.dhcp_options = dhcp_options
        # The description of the DHCP options set.
        self.dhcp_options_set_description = dhcp_options_set_description
        # The ID of the DHCP options set.
        self.dhcp_options_set_id = dhcp_options_set_id
        # The name of the DHCP options set.
        self.dhcp_options_set_name = dhcp_options_set_name
        # The ID of the Alibaba Cloud account to which the DHCP options set belongs.
        self.owner_id = owner_id
        # The ID of the resource group to which the DHCP options set belongs.
        self.resource_group_id = resource_group_id
        # The status of the DHCP options set. Valid values:
        # 
        # *   **Available**
        # *   **InUse**
        # *   **Pending**
        # *   **Deleted**
        self.status = status
        # The tag list.
        self.tags = tags

    def validate(self):
        if self.dhcp_options:
            self.dhcp_options.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_vpc_count is not None:
            result['AssociateVpcCount'] = self.associate_vpc_count

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dhcp_options is not None:
            result['DhcpOptions'] = self.dhcp_options.to_map()

        if self.dhcp_options_set_description is not None:
            result['DhcpOptionsSetDescription'] = self.dhcp_options_set_description

        if self.dhcp_options_set_id is not None:
            result['DhcpOptionsSetId'] = self.dhcp_options_set_id

        if self.dhcp_options_set_name is not None:
            result['DhcpOptionsSetName'] = self.dhcp_options_set_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateVpcCount') is not None:
            self.associate_vpc_count = m.get('AssociateVpcCount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DhcpOptions') is not None:
            temp_model = main_models.ListDhcpOptionsSetsResponseBodyDhcpOptionsSetsDhcpOptions()
            self.dhcp_options = temp_model.from_map(m.get('DhcpOptions'))

        if m.get('DhcpOptionsSetDescription') is not None:
            self.dhcp_options_set_description = m.get('DhcpOptionsSetDescription')

        if m.get('DhcpOptionsSetId') is not None:
            self.dhcp_options_set_id = m.get('DhcpOptionsSetId')

        if m.get('DhcpOptionsSetName') is not None:
            self.dhcp_options_set_name = m.get('DhcpOptionsSetName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListDhcpOptionsSetsResponseBodyDhcpOptionsSetsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListDhcpOptionsSetsResponseBodyDhcpOptionsSetsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N added to the resource.
        self.key = key
        # The value of tag N added to the resource.
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

class ListDhcpOptionsSetsResponseBodyDhcpOptionsSetsDhcpOptions(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_name_servers: str = None,
        ipv_6lease_time: str = None,
        lease_time: str = None,
    ):
        # The suffix of the hostname.
        self.domain_name = domain_name
        # The IP address of the DNS server.
        self.domain_name_servers = domain_name_servers
        # The lease time of the IPv6 DHCP options set.
        # 
        # *   If you use hours as the unit, Unit: h. Valid values are **24h to 1176h** and **87600h to 175200h**. Default value: **24h**.
        # 
        # *   If you use days as the unit, Unit: d. Valid values are **1d to 49d** and **3650d to 7300d**. Default value: **1d**.
        self.ipv_6lease_time = ipv_6lease_time
        # The lease time of the IPv4 addresses for the DHCP options set.
        # 
        # *   If you use hours as the unit, valid values are **24h to 1176h** and **87600h to 175200h**. Default value: **87600h**.
        # *   If you use days as the unit, valid values are **1d to 49d** and **3650d to 7300d**. Default value: **3650d**.
        self.lease_time = lease_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_servers is not None:
            result['DomainNameServers'] = self.domain_name_servers

        if self.ipv_6lease_time is not None:
            result['Ipv6LeaseTime'] = self.ipv_6lease_time

        if self.lease_time is not None:
            result['LeaseTime'] = self.lease_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameServers') is not None:
            self.domain_name_servers = m.get('DomainNameServers')

        if m.get('Ipv6LeaseTime') is not None:
            self.ipv_6lease_time = m.get('Ipv6LeaseTime')

        if m.get('LeaseTime') is not None:
            self.lease_time = m.get('LeaseTime')

        return self

