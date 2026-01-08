# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskEventGroupResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeRiskEventGroupResponseBodyDataList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the details of the intrusion events.
        self.data_list = data_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of risk events.
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeRiskEventGroupResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRiskEventGroupResponseBodyDataList(DaraModel):
    def __init__(
        self,
        attack_app: str = None,
        attack_type: int = None,
        description: str = None,
        direction: str = None,
        dst_ip: str = None,
        event_count: int = None,
        event_id: str = None,
        event_name: str = None,
        first_event_time: int = None,
        iplocation_info: main_models.DescribeRiskEventGroupResponseBodyDataListIPLocationInfo = None,
        last_event_time: int = None,
        resource_private_iplist: List[main_models.DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList] = None,
        resource_type: str = None,
        rule_id: str = None,
        rule_result: int = None,
        rule_source: int = None,
        src_ip: str = None,
        src_iptag: str = None,
        src_iptags: List[str] = None,
        src_private_iplist: List[str] = None,
        tag: str = None,
        vpc_dst_info: main_models.DescribeRiskEventGroupResponseBodyDataListVpcDstInfo = None,
        vpc_src_info: main_models.DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo = None,
        vul_level: int = None,
    ):
        # The name of the attacked application.
        self.attack_app = attack_app
        # The attack type of the intrusion event. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leak
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: trojan backdoor
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        self.attack_type = attack_type
        # The description of the intrusion event.
        self.description = description
        # The direction of the traffic for the intrusion event. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        self.direction = direction
        # The destination IP address that is included in the intrusion event.
        self.dst_ip = dst_ip
        # The number of intrusion events.
        self.event_count = event_count
        # The ID of the intrusion event.
        self.event_id = event_id
        # The name of the intrusion event.
        self.event_name = event_name
        # The time when the intrusion event was first detected. The value is a UNIX timestamp. Unit: seconds.
        self.first_event_time = first_event_time
        # The geographical information about the IP address. The value is a struct that contains the following parameters: **CityId**, **CityName**, **CountryId**, and **CountryName**.\\
        # ****************
        self.iplocation_info = iplocation_info
        # The time when the intrusion event was last detected. The value is a UNIX timestamp. Unit: seconds.
        self.last_event_time = last_event_time
        # The information about the private IP address in the intrusion event. The value is an array that contains the following parameters: **RegionNo**, **ResourceInstanceId**, **ResourceInstanceName**, and **ResourcePrivateIP**.\\
        # ****************
        self.resource_private_iplist = resource_private_iplist
        # The type of the public IP address in the intrusion event. Valid values:
        # 
        # *   **EIP**: the elastic IP address (EIP)
        # *   **EcsPublicIP**: the public IP address of an Elastic Compute Service (ECS) instance
        # *   **EcsEIP**: the EIP of an ECS instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **NatEIP**: the EIP of a NAT gateway
        self.resource_type = resource_type
        # The ID of the rule that is used to detect the intrusion event.
        self.rule_id = rule_id
        # The status of the firewall. Valid values:
        # 
        # *   **1**: alerting
        # *   **2**: blocking
        self.rule_result = rule_result
        # The module of the rule that is used to detect the intrusion event. Valid values:
        # 
        # *   **1**: basic protection
        # *   **2**: virtual patching
        # *   **4**: threat intelligence
        self.rule_source = rule_source
        # The source IP address that is included in the intrusion event.
        self.src_ip = src_ip
        # The tag added to the source IP address. The tag helps identify whether the source IP address is a back-to-origin IP address for a cloud service.
        self.src_iptag = src_iptag
        self.src_iptags = src_iptags
        # An array that consists of the source private IP addresses in the intrusion event.
        self.src_private_iplist = src_private_iplist
        # The tag added to the threat intelligence that is provided for major events.
        self.tag = tag
        # The information about the destination VPC of the intrusion event. The value is a struct that contains the following parameters: **EcsInstanceId**, **EcsInstanceName**, **NetworkInstanceId**, **NetworkInstanceName**, and **RegionNo**.\\
        # ********************
        self.vpc_dst_info = vpc_dst_info
        # The information about the source VPC of the intrusion event. The value is a struct that contains the following parameters: **EcsInstanceId**, **EcsInstanceName**, **NetworkInstanceId**, **NetworkInstanceName**, and **RegionNo**.\\
        # ********************
        self.vpc_src_info = vpc_src_info
        # The risk level of the intrusion event. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.vul_level = vul_level

    def validate(self):
        if self.iplocation_info:
            self.iplocation_info.validate()
        if self.resource_private_iplist:
            for v1 in self.resource_private_iplist:
                 if v1:
                    v1.validate()
        if self.vpc_dst_info:
            self.vpc_dst_info.validate()
        if self.vpc_src_info:
            self.vpc_src_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.description is not None:
            result['Description'] = self.description

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.first_event_time is not None:
            result['FirstEventTime'] = self.first_event_time

        if self.iplocation_info is not None:
            result['IPLocationInfo'] = self.iplocation_info.to_map()

        if self.last_event_time is not None:
            result['LastEventTime'] = self.last_event_time

        result['ResourcePrivateIPList'] = []
        if self.resource_private_iplist is not None:
            for k1 in self.resource_private_iplist:
                result['ResourcePrivateIPList'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_iptag is not None:
            result['SrcIPTag'] = self.src_iptag

        if self.src_iptags is not None:
            result['SrcIPTags'] = self.src_iptags

        if self.src_private_iplist is not None:
            result['SrcPrivateIPList'] = self.src_private_iplist

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.vpc_dst_info is not None:
            result['VpcDstInfo'] = self.vpc_dst_info.to_map()

        if self.vpc_src_info is not None:
            result['VpcSrcInfo'] = self.vpc_src_info.to_map()

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('FirstEventTime') is not None:
            self.first_event_time = m.get('FirstEventTime')

        if m.get('IPLocationInfo') is not None:
            temp_model = main_models.DescribeRiskEventGroupResponseBodyDataListIPLocationInfo()
            self.iplocation_info = temp_model.from_map(m.get('IPLocationInfo'))

        if m.get('LastEventTime') is not None:
            self.last_event_time = m.get('LastEventTime')

        self.resource_private_iplist = []
        if m.get('ResourcePrivateIPList') is not None:
            for k1 in m.get('ResourcePrivateIPList'):
                temp_model = main_models.DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList()
                self.resource_private_iplist.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcIPTag') is not None:
            self.src_iptag = m.get('SrcIPTag')

        if m.get('SrcIPTags') is not None:
            self.src_iptags = m.get('SrcIPTags')

        if m.get('SrcPrivateIPList') is not None:
            self.src_private_iplist = m.get('SrcPrivateIPList')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('VpcDstInfo') is not None:
            temp_model = main_models.DescribeRiskEventGroupResponseBodyDataListVpcDstInfo()
            self.vpc_dst_info = temp_model.from_map(m.get('VpcDstInfo'))

        if m.get('VpcSrcInfo') is not None:
            temp_model = main_models.DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo()
            self.vpc_src_info = temp_model.from_map(m.get('VpcSrcInfo'))

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

class DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo(DaraModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        region_no: str = None,
    ):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The ID of the VPC.
        self.network_instance_id = network_instance_id
        # The name of the VPC.
        self.network_instance_name = network_instance_name
        # The ID of the region in which the source VPC resides.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

class DescribeRiskEventGroupResponseBodyDataListVpcDstInfo(DaraModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        region_no: str = None,
    ):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The ID of the VPC.
        self.network_instance_id = network_instance_id
        # The name of the VPC.
        self.network_instance_name = network_instance_name
        # The ID of the region in which the destination VPC resides.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

class DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList(DaraModel):
    def __init__(
        self,
        region_no: str = None,
        resource_instance_id: str = None,
        resource_instance_name: str = None,
        resource_private_ip: str = None,
    ):
        # The ID of the region to which the private IP address belongs.
        self.region_no = region_no
        # The ID of the instance that uses the private IP address.
        self.resource_instance_id = resource_instance_id
        # The name of the instance that uses the private IP address.
        self.resource_instance_name = resource_instance_name
        # The private IP address.
        self.resource_private_ip = resource_private_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_private_ip is not None:
            result['ResourcePrivateIP'] = self.resource_private_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourcePrivateIP') is not None:
            self.resource_private_ip = m.get('ResourcePrivateIP')

        return self

class DescribeRiskEventGroupResponseBodyDataListIPLocationInfo(DaraModel):
    def __init__(
        self,
        city_id: str = None,
        city_name: str = None,
        country_id: str = None,
        country_name: str = None,
    ):
        # The ID of the city to which the IP address belongs.
        self.city_id = city_id
        # The name of the city to which the IP address belongs.
        self.city_name = city_name
        # The ID of the country to which the IP address belongs.
        self.country_id = country_id
        # The name of the country to which the IP address belongs.
        self.country_name = country_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_id is not None:
            result['CityId'] = self.city_id

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.country_id is not None:
            result['CountryId'] = self.country_id

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        return self

