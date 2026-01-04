# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkAclsResponseBody(DaraModel):
    def __init__(
        self,
        network_acls: main_models.DescribeNetworkAclsResponseBodyNetworkAcls = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The details of the network ACLs.
        self.network_acls = network_acls
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.network_acls:
            self.network_acls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_acls is not None:
            result['NetworkAcls'] = self.network_acls.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAcls') is not None:
            temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAcls()
            self.network_acls = temp_model.from_map(m.get('NetworkAcls'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkAclsResponseBodyNetworkAcls(DaraModel):
    def __init__(
        self,
        network_acl: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAcl] = None,
    ):
        self.network_acl = network_acl

    def validate(self):
        if self.network_acl:
            for v1 in self.network_acl:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkAcl'] = []
        if self.network_acl is not None:
            for k1 in self.network_acl:
                result['NetworkAcl'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_acl = []
        if m.get('NetworkAcl') is not None:
            for k1 in m.get('NetworkAcl'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAcl()
                self.network_acl.append(temp_model.from_map(k1))

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAcl(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        egress_acl_entries: main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclEgressAclEntries = None,
        ingress_acl_entries: main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclIngressAclEntries = None,
        network_acl_id: str = None,
        network_acl_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        resources: main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclResources = None,
        status: str = None,
        tags: main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclTags = None,
        vpc_id: str = None,
    ):
        # The time when the network ACL was created.
        self.creation_time = creation_time
        # The description of the network ACL.
        self.description = description
        # The outbound rules.
        self.egress_acl_entries = egress_acl_entries
        # The configurations of the inbound rules.
        self.ingress_acl_entries = ingress_acl_entries
        # The ID of the network ACL.
        self.network_acl_id = network_acl_id
        # The name of the network ACL.
        self.network_acl_name = network_acl_name
        # The ID of the Alibaba Cloud account to which the network ACL belongs.
        self.owner_id = owner_id
        # The region ID of the network ACL.
        self.region_id = region_id
        # The resources that are associated with the network ACL.
        self.resources = resources
        # The status of the network ACL. Valid values:
        # 
        # *   **Available**
        # *   **Modifying**
        self.status = status
        # The information about the tags.
        self.tags = tags
        # The ID of the associated VPC.
        self.vpc_id = vpc_id

    def validate(self):
        if self.egress_acl_entries:
            self.egress_acl_entries.validate()
        if self.ingress_acl_entries:
            self.ingress_acl_entries.validate()
        if self.resources:
            self.resources.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_acl_entries is not None:
            result['EgressAclEntries'] = self.egress_acl_entries.to_map()

        if self.ingress_acl_entries is not None:
            result['IngressAclEntries'] = self.ingress_acl_entries.to_map()

        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.network_acl_name is not None:
            result['NetworkAclName'] = self.network_acl_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressAclEntries') is not None:
            temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclEgressAclEntries()
            self.egress_acl_entries = temp_model.from_map(m.get('EgressAclEntries'))

        if m.get('IngressAclEntries') is not None:
            temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclIngressAclEntries()
            self.ingress_acl_entries = temp_model.from_map(m.get('IngressAclEntries'))

        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('NetworkAclName') is not None:
            self.network_acl_name = m.get('NetworkAclName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resources') is not None:
            temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclTagsTag(DaraModel):
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

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclResources(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclResourcesResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclResourcesResource(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        # The ID of the associated resource.
        self.resource_id = resource_id
        # The type of resource with which you want to associate the network ACL.
        self.resource_type = resource_type
        # The association status of the resource. Valid values:
        # 
        # *   **BINDED**
        # *   **BINDING**
        # *   **UNBINDING**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclIngressAclEntries(DaraModel):
    def __init__(
        self,
        ingress_acl_entry: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclIngressAclEntriesIngressAclEntry] = None,
    ):
        self.ingress_acl_entry = ingress_acl_entry

    def validate(self):
        if self.ingress_acl_entry:
            for v1 in self.ingress_acl_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IngressAclEntry'] = []
        if self.ingress_acl_entry is not None:
            for k1 in self.ingress_acl_entry:
                result['IngressAclEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ingress_acl_entry = []
        if m.get('IngressAclEntry') is not None:
            for k1 in m.get('IngressAclEntry'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclIngressAclEntriesIngressAclEntry()
                self.ingress_acl_entry.append(temp_model.from_map(k1))

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclIngressAclEntriesIngressAclEntry(DaraModel):
    def __init__(
        self,
        description: str = None,
        entry_type: str = None,
        ip_version: str = None,
        network_acl_entry_id: str = None,
        network_acl_entry_name: str = None,
        policy: str = None,
        port: str = None,
        protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The description of the inbound rule.
        self.description = description
        # The type of the inbound rule.
        # 
        # - **custom**
        # 
        # - **system**
        self.entry_type = entry_type
        # The IP version. 
        # 
        # *   **IPv4**
        # *   **IPv6**
        self.ip_version = ip_version
        # The ID of the inbound rule.
        self.network_acl_entry_id = network_acl_entry_id
        # The name of the inbound rule.
        self.network_acl_entry_name = network_acl_entry_name
        # The action to be performed on network traffic that matches the rule. Valid values:
        # 
        # *   **accept**
        # *   **drop**
        self.policy = policy
        # The destination port range of the inbound traffic.
        # 
        # *   If the **protocol** of the inbound rule is set to **all**, **icmp**, or **gre**, the port range is -1/-1, which specifies all ports.
        # *   If the **protocol** of the inbound rule is set to **tcp** or **udp**, set the port range in the following format: **1/200** or **80/80**, which specifies port 1 to port 200 or port 80. Valid ports: **1** to **65535**.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   **icmp**
        # *   **gre**
        # *   **tcp**
        # *   **udp**
        # *   **all**
        self.protocol = protocol
        # The source CIDR block.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.entry_type is not None:
            result['EntryType'] = self.entry_type

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.network_acl_entry_id is not None:
            result['NetworkAclEntryId'] = self.network_acl_entry_id

        if self.network_acl_entry_name is not None:
            result['NetworkAclEntryName'] = self.network_acl_entry_name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntryType') is not None:
            self.entry_type = m.get('EntryType')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('NetworkAclEntryId') is not None:
            self.network_acl_entry_id = m.get('NetworkAclEntryId')

        if m.get('NetworkAclEntryName') is not None:
            self.network_acl_entry_name = m.get('NetworkAclEntryName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclEgressAclEntries(DaraModel):
    def __init__(
        self,
        egress_acl_entry: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclEgressAclEntriesEgressAclEntry] = None,
    ):
        self.egress_acl_entry = egress_acl_entry

    def validate(self):
        if self.egress_acl_entry:
            for v1 in self.egress_acl_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EgressAclEntry'] = []
        if self.egress_acl_entry is not None:
            for k1 in self.egress_acl_entry:
                result['EgressAclEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.egress_acl_entry = []
        if m.get('EgressAclEntry') is not None:
            for k1 in m.get('EgressAclEntry'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclEgressAclEntriesEgressAclEntry()
                self.egress_acl_entry.append(temp_model.from_map(k1))

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsNetworkAclEgressAclEntriesEgressAclEntry(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_ip: str = None,
        entry_type: str = None,
        ip_version: str = None,
        network_acl_entry_id: str = None,
        network_acl_entry_name: str = None,
        policy: str = None,
        port: str = None,
        protocol: str = None,
    ):
        # The description of the outbound rule.
        self.description = description
        # The destination CIDR block.
        self.destination_cidr_ip = destination_cidr_ip
        # The type of the inbound rule.
        # 
        # - **custom**
        # 
        # - **system**
        self.entry_type = entry_type
        # The IP version. 
        # 
        # *   **IPv4**
        # *   **IPv6**
        self.ip_version = ip_version
        # The ID of the outbound rule.
        self.network_acl_entry_id = network_acl_entry_id
        # The name of the outbound rule.
        self.network_acl_entry_name = network_acl_entry_name
        # The action to be performed on network traffic that matches the rule. Valid values:
        # 
        # *   **accept**
        # *   **drop**
        self.policy = policy
        # The destination port range of the outbound traffic.
        # 
        # *   If the **protocol** of the outbound rule is set to **all**, **icmp**, or **gre**, the port range is -1/-1, which specified all ports.
        # *   If the **protocol** of the outbound rule is set to **tcp** or **udp**, set the port range in the following format: **1/200** or **80/80**, which specifies port 1 to port 200 or port 80. Valid values for a port: **1** to **65535**.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   **icmp**
        # *   **gre**
        # *   **tcp**
        # *   **udp**
        # *   **all**
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_ip is not None:
            result['DestinationCidrIp'] = self.destination_cidr_ip

        if self.entry_type is not None:
            result['EntryType'] = self.entry_type

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.network_acl_entry_id is not None:
            result['NetworkAclEntryId'] = self.network_acl_entry_id

        if self.network_acl_entry_name is not None:
            result['NetworkAclEntryName'] = self.network_acl_entry_name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrIp') is not None:
            self.destination_cidr_ip = m.get('DestinationCidrIp')

        if m.get('EntryType') is not None:
            self.entry_type = m.get('EntryType')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('NetworkAclEntryId') is not None:
            self.network_acl_entry_id = m.get('NetworkAclEntryId')

        if m.get('NetworkAclEntryName') is not None:
            self.network_acl_entry_name = m.get('NetworkAclEntryName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

