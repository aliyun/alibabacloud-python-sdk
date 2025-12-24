# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkInterfacesResponseBody(DaraModel):
    def __init__(
        self,
        network_interface_sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the ENIs.
        self.network_interface_sets = network_interface_sets
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number of the returned page.
        # 
        # > This parameter will be removed in the future. We recommend that you use the NextToken and MaxResults parameters for a paged query.
        self.page_number = page_number
        # The number of entries returned per page.
        # 
        # > This parameter will be removed in the future. We recommend that you use the NextToken and MaxResults parameters for a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of ENIs.
        # 
        # > If you specify the `MaxResults` and `NextToken` parameters to perform a paged query, the value of the `TotalCount` response parameter is invalid.
        self.total_count = total_count

    def validate(self):
        if self.network_interface_sets:
            self.network_interface_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_sets is not None:
            result['NetworkInterfaceSets'] = self.network_interface_sets.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('NetworkInterfaceSets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets()
            self.network_interface_sets = temp_model.from_map(m.get('NetworkInterfaceSets'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets(DaraModel):
    def __init__(
        self,
        network_interface_set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet] = None,
    ):
        self.network_interface_set = network_interface_set

    def validate(self):
        if self.network_interface_set:
            for v1 in self.network_interface_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInterfaceSet'] = []
        if self.network_interface_set is not None:
            for k1 in self.network_interface_set:
                result['NetworkInterfaceSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface_set = []
        if m.get('NetworkInterfaceSet') is not None:
            for k1 in m.get('NetworkInterfaceSet'):
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet()
                self.network_interface_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet(DaraModel):
    def __init__(
        self,
        associated_public_ip: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetAssociatedPublicIp = None,
        attachment: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetAttachment = None,
        creation_time: str = None,
        delete_on_release: bool = None,
        description: str = None,
        instance_id: str = None,
        ipv_4prefix_sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv4PrefixSets = None,
        ipv_6prefix_sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6PrefixSets = None,
        ipv_6sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6Sets = None,
        mac_address: str = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        network_interface_traffic_mode: str = None,
        owner_id: str = None,
        private_ip_address: str = None,
        private_ip_sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSets = None,
        queue_number: int = None,
        queue_pair_number: int = None,
        resource_group_id: str = None,
        security_group_ids: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetSecurityGroupIds = None,
        service_id: int = None,
        service_managed: bool = None,
        source_dest_check: bool = None,
        status: str = None,
        tags: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetTags = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The EIPs that are associated with the secondary private IP addresses of the ENI.
        self.associated_public_ip = associated_public_ip
        # >  This parameter is in invitational preview and is not publicly available.
        self.attachment = attachment
        # The time when the security group was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # Indicates whether to retain the ENI when the associated instance is released. Valid values:
        # 
        # *   true
        # *   false
        self.delete_on_release = delete_on_release
        # The description of the ENI.
        self.description = description
        # The ID of the Elastic Compute Service (ECS) instance to which the ENI is attached.
        # 
        # >  If the ENI is managed by other Alibaba Cloud services, no instance ID is returned.
        self.instance_id = instance_id
        # The IPv4 prefixes of the ENI.
        self.ipv_4prefix_sets = ipv_4prefix_sets
        # The IPv6 prefixes of the ENI.
        self.ipv_6prefix_sets = ipv_6prefix_sets
        # The IPv6 addresses of the ENI.
        self.ipv_6sets = ipv_6sets
        # The MAC address of the ENI.
        self.mac_address = mac_address
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The name of the ENI.
        self.network_interface_name = network_interface_name
        # The communication mode of the ENI. Valid values:
        # 
        # *   Standard: The TCP communication mode is used.
        # *   HighPerformance: The Elastic RDMA Interface (ERI) is enabled and the remote direct memory access (RDMA) communication mode is used.
        # 
        # >  This parameter can have a value of HighPerformance only when the ENI is attached to a c7re RDMA-enhanced instance that resides in Beijing Zone K.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The ID of the account to which the ENI belongs.
        self.owner_id = owner_id
        # The primary private IP address of the ENI.
        self.private_ip_address = private_ip_address
        # Details about the private IP addresses of the ENI.
        self.private_ip_sets = private_ip_sets
        # The number of queues supported by the ENI.
        # 
        # *   If the ENI is a secondary ENI in the InUse state and the number of queues supported by the ENI has never been modified, the default number of queues per secondary ENI that the instance type supports is returned.
        # *   If the ENI is a secondary ENI and the number of queues supported by the ENI has been modified, the new number of queues is returned.
        # *   If the ENI is a secondary ENI in the Available state and the number of queues supported by the ENI has never been modified, an empty value is returned.
        # *   If the ENI is a primary ENI, the default number of queues per primary ENI that the instance type supports is returned.
        self.queue_number = queue_number
        # >  This parameter is in invitational preview and is not publicly available.
        self.queue_pair_number = queue_pair_number
        # The ID of the resource group to which the ENI belongs.
        self.resource_group_id = resource_group_id
        # The security groups to which the ENI belongs.
        self.security_group_ids = security_group_ids
        # The ID of the distributor to which the ENI belongs.
        self.service_id = service_id
        # Indicates whether the user of the ENI is an Alibaba Cloud service or a distributor.
        self.service_managed = service_managed
        # Indicates whether the source and destination IP address check feature is enabled. To improve network security, enable this feature. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        # 
        # >  Before you use this parameter, read [Source and destination IP address check](https://help.aliyun.com/document_detail/2863210.html).
        self.source_dest_check = source_dest_check
        # The state of the ENI.
        self.status = status
        # The tags of the ENI.
        self.tags = tags
        # The type of the ENI.
        self.type = type
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the ENI belongs.
        self.vpc_id = vpc_id
        # The zone ID of the ENI.
        self.zone_id = zone_id

    def validate(self):
        if self.associated_public_ip:
            self.associated_public_ip.validate()
        if self.attachment:
            self.attachment.validate()
        if self.ipv_4prefix_sets:
            self.ipv_4prefix_sets.validate()
        if self.ipv_6prefix_sets:
            self.ipv_6prefix_sets.validate()
        if self.ipv_6sets:
            self.ipv_6sets.validate()
        if self.private_ip_sets:
            self.private_ip_sets.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_public_ip is not None:
            result['AssociatedPublicIp'] = self.associated_public_ip.to_map()

        if self.attachment is not None:
            result['Attachment'] = self.attachment.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.delete_on_release is not None:
            result['DeleteOnRelease'] = self.delete_on_release

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ipv_4prefix_sets is not None:
            result['Ipv4PrefixSets'] = self.ipv_4prefix_sets.to_map()

        if self.ipv_6prefix_sets is not None:
            result['Ipv6PrefixSets'] = self.ipv_6prefix_sets.to_map()

        if self.ipv_6sets is not None:
            result['Ipv6Sets'] = self.ipv_6sets.to_map()

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.network_interface_traffic_mode is not None:
            result['NetworkInterfaceTrafficMode'] = self.network_interface_traffic_mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.private_ip_sets is not None:
            result['PrivateIpSets'] = self.private_ip_sets.to_map()

        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number

        if self.queue_pair_number is not None:
            result['QueuePairNumber'] = self.queue_pair_number

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.service_id is not None:
            result['ServiceID'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.source_dest_check is not None:
            result['SourceDestCheck'] = self.source_dest_check

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedPublicIp') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetAssociatedPublicIp()
            self.associated_public_ip = temp_model.from_map(m.get('AssociatedPublicIp'))

        if m.get('Attachment') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetAttachment()
            self.attachment = temp_model.from_map(m.get('Attachment'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeleteOnRelease') is not None:
            self.delete_on_release = m.get('DeleteOnRelease')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ipv4PrefixSets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv4PrefixSets()
            self.ipv_4prefix_sets = temp_model.from_map(m.get('Ipv4PrefixSets'))

        if m.get('Ipv6PrefixSets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6PrefixSets()
            self.ipv_6prefix_sets = temp_model.from_map(m.get('Ipv6PrefixSets'))

        if m.get('Ipv6Sets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6Sets()
            self.ipv_6sets = temp_model.from_map(m.get('Ipv6Sets'))

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PrivateIpSets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSets()
            self.private_ip_sets = temp_model.from_map(m.get('PrivateIpSets'))

        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetSecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('ServiceID') is not None:
            self.service_id = m.get('ServiceID')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('SourceDestCheck') is not None:
            self.source_dest_check = m.get('SourceDestCheck')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetTagsTag] = None,
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
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetSecurityGroupIds(DaraModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSets(DaraModel):
    def __init__(
        self,
        private_ip_set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSet] = None,
    ):
        self.private_ip_set = private_ip_set

    def validate(self):
        if self.private_ip_set:
            for v1 in self.private_ip_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateIpSet'] = []
        if self.private_ip_set is not None:
            for k1 in self.private_ip_set:
                result['PrivateIpSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_ip_set = []
        if m.get('PrivateIpSet') is not None:
            for k1 in m.get('PrivateIpSet'):
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSet()
                self.private_ip_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSet(DaraModel):
    def __init__(
        self,
        associated_public_ip: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSetAssociatedPublicIp = None,
        primary: bool = None,
        private_dns_name: str = None,
        private_ip_address: str = None,
    ):
        # The elastic IP address (EIP) that is associated with the private IP address.
        self.associated_public_ip = associated_public_ip
        # Indicates whether the private IP address is the primary private IP address. Valid values:
        # 
        # *   true: The IP address is the primary private IP address.
        # *   false: The IP address is a secondary private IP address.
        self.primary = primary
        # The private domain name of the ECS instance.
        # 
        # >  A private domain name can be returned in a specific format only when `HostnameType` is set to `IP` or `InstanceId`.
        self.private_dns_name = private_dns_name
        # The private IP address of the ENI.
        self.private_ip_address = private_ip_address

    def validate(self):
        if self.associated_public_ip:
            self.associated_public_ip.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_public_ip is not None:
            result['AssociatedPublicIp'] = self.associated_public_ip.to_map()

        if self.primary is not None:
            result['Primary'] = self.primary

        if self.private_dns_name is not None:
            result['PrivateDnsName'] = self.private_dns_name

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedPublicIp') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSetAssociatedPublicIp()
            self.associated_public_ip = temp_model.from_map(m.get('AssociatedPublicIp'))

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrivateDnsName') is not None:
            self.private_dns_name = m.get('PrivateDnsName')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSetAssociatedPublicIp(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        public_ip_address: str = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
        self.allocation_id = allocation_id
        # The EIP.
        self.public_ip_address = public_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6SetsIpv6Set] = None,
    ):
        self.ipv_6set = ipv_6set

    def validate(self):
        if self.ipv_6set:
            for v1 in self.ipv_6set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Set'] = []
        if self.ipv_6set is not None:
            for k1 in self.ipv_6set:
                result['Ipv6Set'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6set = []
        if m.get('Ipv6Set') is not None:
            for k1 in m.get('Ipv6Set'):
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6SetsIpv6Set()
                self.ipv_6set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6SetsIpv6Set(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
    ):
        # The IPv6 address of the ENI.
        self.ipv_6address = ipv_6address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_6prefix_set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6PrefixSetsIpv6PrefixSet] = None,
    ):
        self.ipv_6prefix_set = ipv_6prefix_set

    def validate(self):
        if self.ipv_6prefix_set:
            for v1 in self.ipv_6prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6PrefixSet'] = []
        if self.ipv_6prefix_set is not None:
            for k1 in self.ipv_6prefix_set:
                result['Ipv6PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6prefix_set = []
        if m.get('Ipv6PrefixSet') is not None:
            for k1 in m.get('Ipv6PrefixSet'):
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6PrefixSetsIpv6PrefixSet()
                self.ipv_6prefix_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6PrefixSetsIpv6PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_6prefix: str = None,
    ):
        # The IPv6 prefix of the ENI.
        self.ipv_6prefix = ipv_6prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6prefix is not None:
            result['Ipv6Prefix'] = self.ipv_6prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Prefix') is not None:
            self.ipv_6prefix = m.get('Ipv6Prefix')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv4PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_4prefix_set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv4PrefixSetsIpv4PrefixSet] = None,
    ):
        self.ipv_4prefix_set = ipv_4prefix_set

    def validate(self):
        if self.ipv_4prefix_set:
            for v1 in self.ipv_4prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv4PrefixSet'] = []
        if self.ipv_4prefix_set is not None:
            for k1 in self.ipv_4prefix_set:
                result['Ipv4PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4prefix_set = []
        if m.get('Ipv4PrefixSet') is not None:
            for k1 in m.get('Ipv4PrefixSet'):
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv4PrefixSetsIpv4PrefixSet()
                self.ipv_4prefix_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv4PrefixSetsIpv4PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_4prefix: str = None,
    ):
        # The IPv4 prefix of the ENI.
        self.ipv_4prefix = ipv_4prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetAttachment(DaraModel):
    def __init__(
        self,
        device_index: int = None,
        instance_id: str = None,
        network_card_index: int = None,
        trunk_network_interface_id: str = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
        self.device_index = device_index
        # >  This parameter is in invitational preview and is not publicly available.
        self.instance_id = instance_id
        # The index of the network card.
        # 
        # *   If the ENI is in the Available state or if no network card index was specified when the ENI was attached, this parameter is empty.
        # *   If the ENI is in the InUse state and a network card index was specified when the ENI was attached, the specified network card index is returned as the value of this parameter.
        self.network_card_index = network_card_index
        # >  This parameter is in invitational preview and is not publicly available.
        self.trunk_network_interface_id = trunk_network_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_card_index is not None:
            result['NetworkCardIndex'] = self.network_card_index

        if self.trunk_network_interface_id is not None:
            result['TrunkNetworkInterfaceId'] = self.trunk_network_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkCardIndex') is not None:
            self.network_card_index = m.get('NetworkCardIndex')

        if m.get('TrunkNetworkInterfaceId') is not None:
            self.trunk_network_interface_id = m.get('TrunkNetworkInterfaceId')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetAssociatedPublicIp(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        public_ip_address: str = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
        self.allocation_id = allocation_id
        # The EIP.
        self.public_ip_address = public_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        return self

