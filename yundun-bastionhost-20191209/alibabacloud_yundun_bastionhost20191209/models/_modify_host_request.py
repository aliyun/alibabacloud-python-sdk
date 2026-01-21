# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHostRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        host_id: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        ostype: str = None,
        pref_kex: str = None,
        region_id: str = None,
    ):
        # The new description of the host. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the host.
        # 
        # > You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query the ID of the host.
        # 
        # This parameter is required.
        self.host_id = host_id
        # The new name of the host. The name can be up to 128 characters.
        self.host_name = host_name
        # The new internal endpoint of the host. You can set this parameter to a domain name or an IP address.
        self.host_private_address = host_private_address
        # The new public endpoint of the host. You can set this parameter to a domain name or an IP address.
        self.host_public_address = host_public_address
        # The ID of the bastion host on which you want to modify the information about the host.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the new network domain to which the host belongs.
        # 
        # > You can call the [ListNetworkDomains](https://help.aliyun.com/document_detail/2758827.html) operation to query the network domain ID.
        self.network_domain_id = network_domain_id
        # The new operating system of the host. Valid values:
        # 
        # *   **Linux**
        # *   **Windows**
        self.ostype = ostype
        # The preferred key exchange algorithm of the host. If you set OSType to Linux, you can modify this parameter. Valid values:
        # 
        # *   **default**
        # *   **diffie-hellman-group1-sha1**
        # *   **diffie-hellman-group14-sha1**
        # *   **diffie-hellman-group-exchange-sha1**
        self.pref_kex = pref_kex
        # The region ID of the bastion host on which you want to modify the information about the host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address

        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.pref_kex is not None:
            result['PrefKex'] = self.pref_kex

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')

        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('PrefKex') is not None:
            self.pref_kex = m.get('PrefKex')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

