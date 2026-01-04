# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeNatGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        nat_gateways: main_models.DescribeNatGatewaysResponseBodyNatGateways = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the NAT gateway.
        self.nat_gateways = nat_gateways
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of NAT gateway entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.nat_gateways:
            self.nat_gateways.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateways is not None:
            result['NatGateways'] = self.nat_gateways.to_map()

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
        if m.get('NatGateways') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGateways()
            self.nat_gateways = temp_model.from_map(m.get('NatGateways'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNatGatewaysResponseBodyNatGateways(DaraModel):
    def __init__(
        self,
        nat_gateway: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGateway] = None,
    ):
        self.nat_gateway = nat_gateway

    def validate(self):
        if self.nat_gateway:
            for v1 in self.nat_gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NatGateway'] = []
        if self.nat_gateway is not None:
            for k1 in self.nat_gateway:
                result['NatGateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_gateway = []
        if m.get('NatGateway') is not None:
            for k1 in m.get('NatGateway'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGateway()
                self.nat_gateway.append(temp_model.from_map(k1))

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGateway(DaraModel):
    def __init__(
        self,
        access_mode: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayAccessMode = None,
        auto_pay: bool = None,
        business_status: str = None,
        creation_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        ecs_metric_enabled: bool = None,
        eip_bind_mode: str = None,
        enable_session_log: str = None,
        expired_time: str = None,
        forward_table_ids: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayForwardTableIds = None,
        full_nat_table_ids: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayFullNatTableIds = None,
        icmp_reply_enabled: bool = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ip_lists: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpLists = None,
        ip_prefix_list: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpPrefixList = None,
        name: str = None,
        nat_gateway_id: str = None,
        nat_gateway_private_info: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayNatGatewayPrivateInfo = None,
        nat_type: str = None,
        network_type: str = None,
        private_link_enabled: bool = None,
        private_link_mode: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_protection_enabled: bool = None,
        snat_table_ids: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewaySnatTableIds = None,
        spec: str = None,
        status: str = None,
        tags: main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayTags = None,
        vpc_id: str = None,
    ):
        self.access_mode = access_mode
        # Indicates whether automatic payment is enabled. Valid values:
        # 
        # *   **false**: no
        # *   **true**: yes
        self.auto_pay = auto_pay
        # The status of the NAT gateway. Valid values:
        # 
        # *   **Normal**: normal
        # *   **FinancialLocked**: locked due to overdue payments
        self.business_status = business_status
        # The time when the NAT gateway was created.
        self.creation_time = creation_time
        # Indicates whether the deletion protection feature is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.deletion_protection = deletion_protection
        # The description of the NAT gateway.
        self.description = description
        # Indicates whether the traffic monitoring feature is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ecs_metric_enabled = ecs_metric_enabled
        # The mode in which the NAT gateway is associated with an elastic IP address (EIP). Valid values:
        # 
        # *   **MULTI_BINDED**: multi-EIP-to-ENI mode
        # *   **NAT**: NAT mode, which is compatible with IPv4 addresses.
        # 
        # >  Note: If you use the NAT mode, the EIP occupies one private IP address on the vSwitch of the NAT gateway. Make sure that the vSwitch has sufficient private IP addresses. Otherwise, the NAT gateway fails to be associated with the EIP. In NAT mode, you can associate a NAT gateway with up to 50 EIPs.
        self.eip_bind_mode = eip_bind_mode
        self.enable_session_log = enable_session_log
        # The time when the NAT gateway expires.
        self.expired_time = expired_time
        # The ID of the DNAT table.
        self.forward_table_ids = forward_table_ids
        # The ID of the FULLNAT table.
        self.full_nat_table_ids = full_nat_table_ids
        # Indicates whether the ICMP non-retrieval feature is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.icmp_reply_enabled = icmp_reply_enabled
        # The billing method of the NAT gateway. The value is set to **PostPaid**, which indicates the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The metering method of the NAT gateway. Valid values:
        # 
        # *   **PayBySpec**: pay-by-specification
        # *   **PayByLcu**: pay-by-CU
        self.internet_charge_type = internet_charge_type
        # The list of elastic IP addresses (EIPs) that are associated with the Internet NAT gateway.
        self.ip_lists = ip_lists
        self.ip_prefix_list = ip_prefix_list
        # The name of the NAT gateway.
        self.name = name
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The private network information about the enhanced Internet NAT gateway.
        # 
        # >  If **NatType** is set to **Normal**, all parameters returned in this list are empty.
        self.nat_gateway_private_info = nat_gateway_private_info
        # The type of the NAT gateway. The value is set to **Enhanced** (enhanced NAT gateway).
        self.nat_type = nat_type
        # The type of NAT gateway. Valid values:
        # 
        # *   **internet**: an Internet NAT gateway
        # *   **intranet**: a VPC NAT gateway
        self.network_type = network_type
        # Indicates whether the NAT gateway supports PrivateLink. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.private_link_enabled = private_link_enabled
        # The mode that is used by PrivateLink. Valid values:
        # 
        # *   **FullNat**: the FULLNAT mode
        # *   **Geneve**: the GENEVE mode
        self.private_link_mode = private_link_mode
        # The ID of the region where the NAT gateway is deployed.
        self.region_id = region_id
        # The ID of the resource group to which the contiguous EIP group belongs.
        self.resource_group_id = resource_group_id
        # Indicates whether the firewall feature is enabled. Valid values:
        # 
        # *   **false**: no
        # *   **true**: yes
        self.security_protection_enabled = security_protection_enabled
        # The ID of the SNAT table of the NAT gateway.
        self.snat_table_ids = snat_table_ids
        # The size of the NAT gateway. An empty value is returned for the parameter.
        # 
        # If **InternetChargeType** is set to **PayByLcu**, an empty value is returned.
        self.spec = spec
        # The status of the NAT gateway. Valid values:
        # 
        # *   **Creating**: After you send a request to create a NAT gateway, the system creates the NAT gateway in the background. The NAT gateway remains in the Creating state until the operation is completed.
        # *   **Available**: The NAT gateway remains in a stable state after the NAT gateway is created.
        # *   **Modifying**: After you send a request to modify a NAT gateway, the system modifies the NAT gateway in the background. The NAT gateway remains in the Modifying state until the operation is completed.
        # *   **Deleting**: After you send a request to delete a NAT gateway, the system deletes the NAT gateway in the background. The NAT gateway remains in the Deleting state until the operation is completed.
        # *   **Converting**: After you send a request to upgrade a standard NAT gateway to an enhanced NAT gateway, the system upgrades the NAT gateway in the background. The NAT gateway remains in the Converting state until the operation is completed.
        self.status = status
        # The tags that are added to the resource group.
        self.tags = tags
        # The ID of the VPC where the NAT gateway is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        if self.access_mode:
            self.access_mode.validate()
        if self.forward_table_ids:
            self.forward_table_ids.validate()
        if self.full_nat_table_ids:
            self.full_nat_table_ids.validate()
        if self.ip_lists:
            self.ip_lists.validate()
        if self.ip_prefix_list:
            self.ip_prefix_list.validate()
        if self.nat_gateway_private_info:
            self.nat_gateway_private_info.validate()
        if self.snat_table_ids:
            self.snat_table_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode.to_map()

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['Description'] = self.description

        if self.ecs_metric_enabled is not None:
            result['EcsMetricEnabled'] = self.ecs_metric_enabled

        if self.eip_bind_mode is not None:
            result['EipBindMode'] = self.eip_bind_mode

        if self.enable_session_log is not None:
            result['EnableSessionLog'] = self.enable_session_log

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids.to_map()

        if self.full_nat_table_ids is not None:
            result['FullNatTableIds'] = self.full_nat_table_ids.to_map()

        if self.icmp_reply_enabled is not None:
            result['IcmpReplyEnabled'] = self.icmp_reply_enabled

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_lists is not None:
            result['IpLists'] = self.ip_lists.to_map()

        if self.ip_prefix_list is not None:
            result['IpPrefixList'] = self.ip_prefix_list.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_private_info is not None:
            result['NatGatewayPrivateInfo'] = self.nat_gateway_private_info.to_map()

        if self.nat_type is not None:
            result['NatType'] = self.nat_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.private_link_enabled is not None:
            result['PrivateLinkEnabled'] = self.private_link_enabled

        if self.private_link_mode is not None:
            result['PrivateLinkMode'] = self.private_link_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_protection_enabled is not None:
            result['SecurityProtectionEnabled'] = self.security_protection_enabled

        if self.snat_table_ids is not None:
            result['SnatTableIds'] = self.snat_table_ids.to_map()

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayAccessMode()
            self.access_mode = temp_model.from_map(m.get('AccessMode'))

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcsMetricEnabled') is not None:
            self.ecs_metric_enabled = m.get('EcsMetricEnabled')

        if m.get('EipBindMode') is not None:
            self.eip_bind_mode = m.get('EipBindMode')

        if m.get('EnableSessionLog') is not None:
            self.enable_session_log = m.get('EnableSessionLog')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ForwardTableIds') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayForwardTableIds()
            self.forward_table_ids = temp_model.from_map(m.get('ForwardTableIds'))

        if m.get('FullNatTableIds') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayFullNatTableIds()
            self.full_nat_table_ids = temp_model.from_map(m.get('FullNatTableIds'))

        if m.get('IcmpReplyEnabled') is not None:
            self.icmp_reply_enabled = m.get('IcmpReplyEnabled')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpLists') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpLists()
            self.ip_lists = temp_model.from_map(m.get('IpLists'))

        if m.get('IpPrefixList') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpPrefixList()
            self.ip_prefix_list = temp_model.from_map(m.get('IpPrefixList'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayPrivateInfo') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayNatGatewayPrivateInfo()
            self.nat_gateway_private_info = temp_model.from_map(m.get('NatGatewayPrivateInfo'))

        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PrivateLinkEnabled') is not None:
            self.private_link_enabled = m.get('PrivateLinkEnabled')

        if m.get('PrivateLinkMode') is not None:
            self.private_link_mode = m.get('PrivateLinkMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityProtectionEnabled') is not None:
            self.security_protection_enabled = m.get('SecurityProtectionEnabled')

        if m.get('SnatTableIds') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewaySnatTableIds()
            self.snat_table_ids = temp_model.from_map(m.get('SnatTableIds'))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayTagsTag] = None,
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
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the instance.
        self.tag_key = tag_key
        # The tag value of the instance.
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

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewaySnatTableIds(DaraModel):
    def __init__(
        self,
        snat_table_id: List[str] = None,
    ):
        self.snat_table_id = snat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayNatGatewayPrivateInfo(DaraModel):
    def __init__(
        self,
        eni_instance_id: str = None,
        eni_type: str = None,
        iz_no: str = None,
        max_bandwidth: int = None,
        max_session_establish_rate: int = None,
        max_session_quota: int = None,
        private_ip_address: str = None,
        vswitch_id: str = None,
    ):
        # The ID of the elastic network interface (ENI).
        self.eni_instance_id = eni_instance_id
        # The mode in which the ENI is associated with the NAT gateway.
        # 
        # *   **indirect**: non-cut-through mode
        # *   If an empty value is returned, it indicates that the cut-through mode is used.
        self.eni_type = eni_type
        # The zone to which the NAT gateway belongs.
        self.iz_no = iz_no
        # The maximum bandwidth. Unit: Mbit/s.
        self.max_bandwidth = max_bandwidth
        # The number of new connections to the NAT gateway. Unit: connections per second.
        self.max_session_establish_rate = max_session_establish_rate
        # The number of concurrent connections to the NAT gateway. Unit: connections.
        self.max_session_quota = max_session_quota
        # The private IP address.
        self.private_ip_address = private_ip_address
        # The ID of the vSwitch to which the NAT gateway belongs.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id

        if self.eni_type is not None:
            result['EniType'] = self.eni_type

        if self.iz_no is not None:
            result['IzNo'] = self.iz_no

        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth

        if self.max_session_establish_rate is not None:
            result['MaxSessionEstablishRate'] = self.max_session_establish_rate

        if self.max_session_quota is not None:
            result['MaxSessionQuota'] = self.max_session_quota

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')

        if m.get('EniType') is not None:
            self.eni_type = m.get('EniType')

        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')

        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')

        if m.get('MaxSessionEstablishRate') is not None:
            self.max_session_establish_rate = m.get('MaxSessionEstablishRate')

        if m.get('MaxSessionQuota') is not None:
            self.max_session_quota = m.get('MaxSessionQuota')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpPrefixList(DaraModel):
    def __init__(
        self,
        ip_prefix_list: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpPrefixListIpPrefixList] = None,
    ):
        self.ip_prefix_list = ip_prefix_list

    def validate(self):
        if self.ip_prefix_list:
            for v1 in self.ip_prefix_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpPrefixList'] = []
        if self.ip_prefix_list is not None:
            for k1 in self.ip_prefix_list:
                result['IpPrefixList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_prefix_list = []
        if m.get('IpPrefixList') is not None:
            for k1 in m.get('IpPrefixList'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpPrefixListIpPrefixList()
                self.ip_prefix_list.append(temp_model.from_map(k1))

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpPrefixListIpPrefixList(DaraModel):
    def __init__(
        self,
        ip_prefix: str = None,
    ):
        self.ip_prefix = ip_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_prefix is not None:
            result['IpPrefix'] = self.ip_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPrefix') is not None:
            self.ip_prefix = m.get('IpPrefix')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpLists(DaraModel):
    def __init__(
        self,
        ip_list: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpListsIpList] = None,
    ):
        self.ip_list = ip_list

    def validate(self):
        if self.ip_list:
            for v1 in self.ip_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpList'] = []
        if self.ip_list is not None:
            for k1 in self.ip_list:
                result['IpList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_list = []
        if m.get('IpList') is not None:
            for k1 in m.get('IpList'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpListsIpList()
                self.ip_list.append(temp_model.from_map(k1))

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayIpListsIpList(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        ip_address: str = None,
        private_ip_address: str = None,
        snat_entry_enabled: bool = None,
        using_status: str = None,
    ):
        # The ID of the EIP associated with the NAT gateway.
        self.allocation_id = allocation_id
        # The IP address of the EIP associated with the NAT gateway.
        self.ip_address = ip_address
        # The private IP address of the NAT gateway.
        self.private_ip_address = private_ip_address
        # Indicates whether IP addresses that are used in DNAT entries can be specified in SNAT entries. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.snat_entry_enabled = snat_entry_enabled
        # The association between the EIP and the Internet NAT gateway. Valid values:
        # 
        # *   **UsedByForwardTable**: The EIP is specified in a DNAT entry.
        # *   **UsedBySnatTable**: The EIP is specified in an SNAT entry.
        # *   **UsedByForwardSnatTable**: The EIP is specified in both an SNAT entry and a DNAT entry.
        # *   **Idle**: The EIP is not specified in a DNAT or SNAT entry.
        self.using_status = using_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.snat_entry_enabled is not None:
            result['SnatEntryEnabled'] = self.snat_entry_enabled

        if self.using_status is not None:
            result['UsingStatus'] = self.using_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('SnatEntryEnabled') is not None:
            self.snat_entry_enabled = m.get('SnatEntryEnabled')

        if m.get('UsingStatus') is not None:
            self.using_status = m.get('UsingStatus')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayFullNatTableIds(DaraModel):
    def __init__(
        self,
        full_nat_table_id: List[str] = None,
    ):
        self.full_nat_table_id = full_nat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_nat_table_id is not None:
            result['FullNatTableId'] = self.full_nat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullNatTableId') is not None:
            self.full_nat_table_id = m.get('FullNatTableId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayForwardTableIds(DaraModel):
    def __init__(
        self,
        forward_table_id: List[str] = None,
    ):
        self.forward_table_id = forward_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysNatGatewayAccessMode(DaraModel):
    def __init__(
        self,
        mode_value: str = None,
        tunnel_type: str = None,
    ):
        self.mode_value = mode_value
        self.tunnel_type = tunnel_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode_value is not None:
            result['ModeValue'] = self.mode_value

        if self.tunnel_type is not None:
            result['TunnelType'] = self.tunnel_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModeValue') is not None:
            self.mode_value = m.get('ModeValue')

        if m.get('TunnelType') is not None:
            self.tunnel_type = m.get('TunnelType')

        return self

