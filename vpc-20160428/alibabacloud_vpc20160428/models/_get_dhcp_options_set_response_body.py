# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetDhcpOptionsSetResponseBody(DaraModel):
    def __init__(
        self,
        associate_vpcs: List[main_models.GetDhcpOptionsSetResponseBodyAssociateVpcs] = None,
        creation_time: str = None,
        dhcp_options: main_models.GetDhcpOptionsSetResponseBodyDhcpOptions = None,
        dhcp_options_set_description: str = None,
        dhcp_options_set_id: str = None,
        dhcp_options_set_name: str = None,
        owner_id: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetDhcpOptionsSetResponseBodyTags] = None,
    ):
        # The information about the virtual private cloud (VPC) that is associated with the DHCP options set.
        self.associate_vpcs = associate_vpcs
        # create time
        self.creation_time = creation_time
        # The configuration information about the DHCP options set.
        self.dhcp_options = dhcp_options
        # The description of the DHCP options set.
        self.dhcp_options_set_description = dhcp_options_set_description
        # The ID of the DHCP options set.
        self.dhcp_options_set_id = dhcp_options_set_id
        # The name of the DHCP options set.
        self.dhcp_options_set_name = dhcp_options_set_name
        # The ID of the Alibaba Cloud account to which the DHCP options set belongs.
        self.owner_id = owner_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the DHCP options set. Valid values:
        # 
        # *   **Available**: available
        # *   **InUse**: in use
        # *   **Deleted**: deleted
        # *   **Pending**: being configured
        self.status = status
        # The tag list.
        self.tags = tags

    def validate(self):
        if self.associate_vpcs:
            for v1 in self.associate_vpcs:
                 if v1:
                    v1.validate()
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
        result['AssociateVpcs'] = []
        if self.associate_vpcs is not None:
            for k1 in self.associate_vpcs:
                result['AssociateVpcs'].append(k1.to_map() if k1 else None)

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
        self.associate_vpcs = []
        if m.get('AssociateVpcs') is not None:
            for k1 in m.get('AssociateVpcs'):
                temp_model = main_models.GetDhcpOptionsSetResponseBodyAssociateVpcs()
                self.associate_vpcs.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DhcpOptions') is not None:
            temp_model = main_models.GetDhcpOptionsSetResponseBodyDhcpOptions()
            self.dhcp_options = temp_model.from_map(m.get('DhcpOptions'))

        if m.get('DhcpOptionsSetDescription') is not None:
            self.dhcp_options_set_description = m.get('DhcpOptionsSetDescription')

        if m.get('DhcpOptionsSetId') is not None:
            self.dhcp_options_set_id = m.get('DhcpOptionsSetId')

        if m.get('DhcpOptionsSetName') is not None:
            self.dhcp_options_set_name = m.get('DhcpOptionsSetName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetDhcpOptionsSetResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetDhcpOptionsSetResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class GetDhcpOptionsSetResponseBodyDhcpOptions(DaraModel):
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
        # The lease time of the IPv6 addresses for the DHCP options set.
        #  
        # *   If you use hours as the unit, Valid values are **24h to 1176h** and **87600h to 175200h**. Default value: **87600h**.
        # *   If you use days as the unit, Valid values are **1d to 49d** and **3650d to 7300d**. Default value: **3650d**.
        self.ipv_6lease_time = ipv_6lease_time
        # The lease time of the IPv4 addresses for the DHCP options set.
        # 
        # *   If you use hours as the unit, valid values are **24h to 1176h** and **87600h to 175200h**. Default value: **87600h**.
        # 
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

class GetDhcpOptionsSetResponseBodyAssociateVpcs(DaraModel):
    def __init__(
        self,
        associate_status: str = None,
        vpc_id: str = None,
    ):
        # The status of the VPC that is associated with the DHCP options set. Valid values:
        #  
        # *   **InUse**: in use
        # *   **Pending**: being configured
        self.associate_status = associate_status
        # The ID of the VPC that is associated with the DHCP options set.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_status is not None:
            result['AssociateStatus'] = self.associate_status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateStatus') is not None:
            self.associate_status = m.get('AssociateStatus')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

