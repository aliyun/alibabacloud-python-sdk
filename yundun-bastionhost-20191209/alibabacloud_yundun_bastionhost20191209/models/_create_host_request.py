# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHostRequest(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        host_name: str = None,
        host_private_address: str = None,
        host_public_address: str = None,
        instance_id: str = None,
        instance_member_id: int = None,
        instance_region_id: str = None,
        network_domain_id: str = None,
        ostype: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
    ):
        # The endpoint type of the host that you want to create. Valid values:
        # 
        # *   **Public**: public endpoint
        # *   **Private**: internal endpoint
        # 
        # This parameter is required.
        self.active_address_type = active_address_type
        # The description of the host that you want to create. The value can be up to 500 characters in length.
        self.comment = comment
        # The name of the host that you want to create. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.host_name = host_name
        # The internal endpoint of the host that you want to create. You can set this parameter to a domain name or an IP address.
        # 
        # > This parameter is required if the **ActiveAddressType** parameter is set to **Private**.
        self.host_private_address = host_private_address
        # The public endpoint of the host that you want to create. You can set this parameter to a domain name or an IP address.
        # 
        # > This parameter is required if the **ActiveAddressType** parameter is set to **Public**.
        self.host_public_address = host_public_address
        # The ID of the bastion host in which you want to create the host.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_member_id = instance_member_id
        # The ID of the region to which the ECS instance or the host in an ApsaraDB MyBase dedicated cluster belongs.
        # 
        # > This parameter is required if the **Source** parameter is set to **Ecs** or **Rds**.
        self.instance_region_id = instance_region_id
        # The ID of the network domain to which the host to be imported belongs.
        # 
        # > You can call the [ListNetworkDomains](https://help.aliyun.com/document_detail/2758827.html) operation to query the network domain ID.
        self.network_domain_id = network_domain_id
        # The operating system of the host that you want to create. Valid values:
        # 
        # *   **Linux**
        # *   **Windows**
        # 
        # This parameter is required.
        self.ostype = ostype
        # The region ID of the bastion host to which you want to import the host.
        # 
        # > For information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The source of the host that you want to create. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        # 
        # This parameter is required.
        self.source = source
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster.
        # 
        # > This parameter is required if the **Source** parameter is set to **Ecs** or **Rds**.
        self.source_instance_id = source_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address

        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_member_id is not None:
            result['InstanceMemberId'] = self.instance_member_id

        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')

        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceMemberId') is not None:
            self.instance_member_id = m.get('InstanceMemberId')

        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        return self

