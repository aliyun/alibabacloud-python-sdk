# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkAclsResponseBody(DaraModel):
    def __init__(
        self,
        network_acls: List[main_models.DescribeNetworkAclsResponseBodyNetworkAcls] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # Details of the network ACLs.
        self.network_acls = network_acls
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.network_acls:
            for v1 in self.network_acls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkAcls'] = []
        if self.network_acls is not None:
            for k1 in self.network_acls:
                result['NetworkAcls'].append(k1.to_map() if k1 else None)

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
        self.network_acls = []
        if m.get('NetworkAcls') is not None:
            for k1 in m.get('NetworkAcls'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAcls()
                self.network_acls.append(temp_model.from_map(k1))

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
        creation_time: str = None,
        description: str = None,
        egress_acl_entries: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsEgressAclEntries] = None,
        ingress_acl_entries: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsIngressAclEntries] = None,
        network_acl_id: str = None,
        network_acl_name: str = None,
        resources: List[main_models.DescribeNetworkAclsResponseBodyNetworkAclsResources] = None,
        status: str = None,
    ):
        # The time when the network ACL was created. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the network ACL.
        self.description = description
        # Details of the outbound rules.
        self.egress_acl_entries = egress_acl_entries
        # Details of the inbound rules.
        self.ingress_acl_entries = ingress_acl_entries
        # The ID of the network ACL.
        self.network_acl_id = network_acl_id
        # The name of the network ACL.
        self.network_acl_name = network_acl_name
        # Details of the associated resources.
        self.resources = resources
        # The status of the network ACL. Valid values:
        # 
        # *   **Available**: The network ACL is available.
        # *   **Modifying**: The network ACL is being configured.
        self.status = status

    def validate(self):
        if self.egress_acl_entries:
            for v1 in self.egress_acl_entries:
                 if v1:
                    v1.validate()
        if self.ingress_acl_entries:
            for v1 in self.ingress_acl_entries:
                 if v1:
                    v1.validate()
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        result['EgressAclEntries'] = []
        if self.egress_acl_entries is not None:
            for k1 in self.egress_acl_entries:
                result['EgressAclEntries'].append(k1.to_map() if k1 else None)

        result['IngressAclEntries'] = []
        if self.ingress_acl_entries is not None:
            for k1 in self.ingress_acl_entries:
                result['IngressAclEntries'].append(k1.to_map() if k1 else None)

        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.network_acl_name is not None:
            result['NetworkAclName'] = self.network_acl_name

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.egress_acl_entries = []
        if m.get('EgressAclEntries') is not None:
            for k1 in m.get('EgressAclEntries'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsEgressAclEntries()
                self.egress_acl_entries.append(temp_model.from_map(k1))

        self.ingress_acl_entries = []
        if m.get('IngressAclEntries') is not None:
            for k1 in m.get('IngressAclEntries'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsIngressAclEntries()
                self.ingress_acl_entries.append(temp_model.from_map(k1))

        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('NetworkAclName') is not None:
            self.network_acl_name = m.get('NetworkAclName')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.DescribeNetworkAclsResponseBodyNetworkAclsResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsResources(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The ID of the associated resource.
        self.resource_id = resource_id
        # The type of the associated resource.
        self.resource_type = resource_type
        # The association status of the resource. Valid values:
        # 
        # *   **BINDED**: The resource is associated with the network ACL.
        # *   **BINDING**: The resource is being associated with the network ACL.
        # *   **UNBINDING**: The resource is being disassociated from the network ACL.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsIngressAclEntries(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        network_acl_entry_id: str = None,
        network_acl_entry_name: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        protocol: str = None,
        type: str = None,
    ):
        # The source CIDR block.
        self.cidr_block = cidr_block
        # The description of the inbound rule.
        self.description = description
        self.destination_cidr_block = destination_cidr_block
        # The ID of the inbound rule.
        self.network_acl_entry_id = network_acl_entry_id
        # The name of the inbound rule.
        self.network_acl_entry_name = network_acl_entry_name
        # The action that is performed on network traffic that matches the rule. Valid values:
        # 
        # *   **accept**: allows the network traffic.
        # *   **drop**: blocks the network traffic.
        self.policy = policy
        # The destination port range of the inbound rule.
        # 
        # *   If **Protocol** of the inbound rule is set to **all** or **icmp**, the port range is **-1/-1**, which indicates all ports.
        # *   If **Protocol** of the inbound rule is set to **tcp** or **udp**, the port range is in the following format: **1/200** or **80/80**. 1/200 indicates port 1 to port 200. 80/80 indicates port 80. Valid values for a port: **1 to 65535**.
        self.port_range = port_range
        # The priority of the rule. Valid values: **1 to 100**. Default value: **1**.
        self.priority = priority
        # The protocol type. Valid values:
        # 
        # *   **icmp**: ICMP.
        # *   **tcp**: TCP.
        # *   **udp**: UDP.
        # *   **all**: all protocols.
        self.protocol = protocol
        # The type of the rule. Valid values:
        # 
        # *   **system**: The rule is created by the system.
        # *   **custom**: The rule is created by a user.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.network_acl_entry_id is not None:
            result['NetworkAclEntryId'] = self.network_acl_entry_id

        if self.network_acl_entry_name is not None:
            result['NetworkAclEntryName'] = self.network_acl_entry_name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NetworkAclEntryId') is not None:
            self.network_acl_entry_id = m.get('NetworkAclEntryId')

        if m.get('NetworkAclEntryName') is not None:
            self.network_acl_entry_name = m.get('NetworkAclEntryName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeNetworkAclsResponseBodyNetworkAclsEgressAclEntries(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        network_acl_entry_id: str = None,
        network_acl_entry_name: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        protocol: str = None,
        type: str = None,
    ):
        # The destination CIDR block.
        self.cidr_block = cidr_block
        # The description of the outbound rule.
        self.description = description
        # The ID of the outbound rule.
        self.network_acl_entry_id = network_acl_entry_id
        # The name of the outbound rule.
        self.network_acl_entry_name = network_acl_entry_name
        # The action that is performed on network traffic that matches the rule. Valid values:
        # 
        # *   **accept**: allows the network traffic.
        # *   **drop**: blocks the network traffic.
        self.policy = policy
        # The destination port range of the outbound rule.
        # 
        # *   If **Protocol** of the outbound rule is set to **all** or **icmp** the port range is **-1/-1**, which indicates all ports.
        # *   If **Protocol** of the outbound rule is set to **tcp** or **udp**, the port range is in the following format: **1/200** or **80/80**. 1/200 indicates port 1 to port 200. 80/80 indicates port 80. Valid values for a port: **1 to 65535**.
        self.port_range = port_range
        # The priority of the rule. Valid values: **1 to 100**. Default value: **1**.
        self.priority = priority
        # The protocol type. Valid values:
        # 
        # *   **icmp**: ICMP.
        # *   **tcp**: TCP.
        # *   **udp**: UDP.
        # *   **all**: all protocols.
        self.protocol = protocol
        # The type of the rule. Valid values:
        # 
        # *   **system**: The rule is created by the system.
        # *   **custom**: The rule is created by a user.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.network_acl_entry_id is not None:
            result['NetworkAclEntryId'] = self.network_acl_entry_id

        if self.network_acl_entry_name is not None:
            result['NetworkAclEntryName'] = self.network_acl_entry_name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkAclEntryId') is not None:
            self.network_acl_entry_id = m.get('NetworkAclEntryId')

        if m.get('NetworkAclEntryName') is not None:
            self.network_acl_entry_name = m.get('NetworkAclEntryName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

