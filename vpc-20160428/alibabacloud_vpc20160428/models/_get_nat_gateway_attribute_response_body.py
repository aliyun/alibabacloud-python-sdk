# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetNatGatewayAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_mode: main_models.GetNatGatewayAttributeResponseBodyAccessMode = None,
        billing_config: main_models.GetNatGatewayAttributeResponseBodyBillingConfig = None,
        business_status: str = None,
        creation_time: str = None,
        deletion_protection_info: main_models.GetNatGatewayAttributeResponseBodyDeletionProtectionInfo = None,
        description: str = None,
        ecs_metric_enabled: bool = None,
        enable_session_log: bool = None,
        expired_time: str = None,
        forward_table: main_models.GetNatGatewayAttributeResponseBodyForwardTable = None,
        full_nat_table: main_models.GetNatGatewayAttributeResponseBodyFullNatTable = None,
        ip_list: List[main_models.GetNatGatewayAttributeResponseBodyIpList] = None,
        log_delivery: main_models.GetNatGatewayAttributeResponseBodyLogDelivery = None,
        name: str = None,
        nat_gateway_id: str = None,
        nat_type: str = None,
        network_type: str = None,
        private_info: main_models.GetNatGatewayAttributeResponseBodyPrivateInfo = None,
        private_link_enabled: bool = None,
        private_link_mode: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        snat_table: main_models.GetNatGatewayAttributeResponseBodySnatTable = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.access_mode = access_mode
        # The billing information.
        self.billing_config = billing_config
        # The service status of the NAT gateway. Valid values:
        # 
        # *   **Normal**: normal
        # *   **FinancialLocked**: locked due to overdue payments
        self.business_status = business_status
        # The time when the NAT gateway was created. Format: YYYY-MM-DDThh:mm:ssZ.
        self.creation_time = creation_time
        # The information about the deletion protection feature.
        self.deletion_protection_info = deletion_protection_info
        # The description of the NAT gateway.
        self.description = description
        # Indicates whether the traffic monitoring feature is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ecs_metric_enabled = ecs_metric_enabled
        self.enable_session_log = enable_session_log
        # The time when the NAT gateway expires.
        self.expired_time = expired_time
        # The information about the DNAT table.
        self.forward_table = forward_table
        # The information about the FULLNAT table.
        self.full_nat_table = full_nat_table
        # The elastic IP addresses (EIPs) that are associated with the Internet NAT gateway.
        self.ip_list = ip_list
        self.log_delivery = log_delivery
        # The name of the NAT gateway.
        self.name = name
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The type of the Internet NAT gateway. Only **Enhanced** is returned, which indicates an enhanced Internet NAT gateway.
        self.nat_type = nat_type
        # The type of the NAT gateway. Valid values:
        # 
        # *   **internet**: an Internet NAT gateway
        # *   **intranet**: a VPC NAT gateway
        self.network_type = network_type
        # The private network information about the NAT gateway.
        self.private_info = private_info
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
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The information about the SNAT table.
        self.snat_table = snat_table
        # The status of the NAT gateway. Valid values:
        # 
        # *   **Creating**: being created. The operation to create a NAT gateway is asynchronous. The NAT gateway remains in the **Creating** state until it is created.
        # *   **Available**: available. After a NAT gateway is created, it remains in a stable state.
        # *   **Modifying**: being modified. The operation to upgrade or downgrade a NAT gateway is asynchronous. The NAT gateway remains in the **Modifying** state until it is upgraded or downgraded.
        # *   **Deleting**: being deleted. The operation to delete a NAT gateway is asynchronous. The NAT gateway remains in the **Deleting** state until it is deleted.
        # *   **Converting**: being converted. The operation to convert a standard NAT gateway to an enhanced NAT gateway is asynchronous. The NAT gateway remains in the **Converting** state until it is converted.
        self.status = status
        # The ID of the VPC to which the NAT gateway belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.access_mode:
            self.access_mode.validate()
        if self.billing_config:
            self.billing_config.validate()
        if self.deletion_protection_info:
            self.deletion_protection_info.validate()
        if self.forward_table:
            self.forward_table.validate()
        if self.full_nat_table:
            self.full_nat_table.validate()
        if self.ip_list:
            for v1 in self.ip_list:
                 if v1:
                    v1.validate()
        if self.log_delivery:
            self.log_delivery.validate()
        if self.private_info:
            self.private_info.validate()
        if self.snat_table:
            self.snat_table.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode.to_map()

        if self.billing_config is not None:
            result['BillingConfig'] = self.billing_config.to_map()

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.deletion_protection_info is not None:
            result['DeletionProtectionInfo'] = self.deletion_protection_info.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.ecs_metric_enabled is not None:
            result['EcsMetricEnabled'] = self.ecs_metric_enabled

        if self.enable_session_log is not None:
            result['EnableSessionLog'] = self.enable_session_log

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.forward_table is not None:
            result['ForwardTable'] = self.forward_table.to_map()

        if self.full_nat_table is not None:
            result['FullNatTable'] = self.full_nat_table.to_map()

        result['IpList'] = []
        if self.ip_list is not None:
            for k1 in self.ip_list:
                result['IpList'].append(k1.to_map() if k1 else None)

        if self.log_delivery is not None:
            result['LogDelivery'] = self.log_delivery.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_type is not None:
            result['NatType'] = self.nat_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.private_info is not None:
            result['PrivateInfo'] = self.private_info.to_map()

        if self.private_link_enabled is not None:
            result['PrivateLinkEnabled'] = self.private_link_enabled

        if self.private_link_mode is not None:
            result['PrivateLinkMode'] = self.private_link_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snat_table is not None:
            result['SnatTable'] = self.snat_table.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodyAccessMode()
            self.access_mode = temp_model.from_map(m.get('AccessMode'))

        if m.get('BillingConfig') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodyBillingConfig()
            self.billing_config = temp_model.from_map(m.get('BillingConfig'))

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeletionProtectionInfo') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodyDeletionProtectionInfo()
            self.deletion_protection_info = temp_model.from_map(m.get('DeletionProtectionInfo'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcsMetricEnabled') is not None:
            self.ecs_metric_enabled = m.get('EcsMetricEnabled')

        if m.get('EnableSessionLog') is not None:
            self.enable_session_log = m.get('EnableSessionLog')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ForwardTable') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodyForwardTable()
            self.forward_table = temp_model.from_map(m.get('ForwardTable'))

        if m.get('FullNatTable') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodyFullNatTable()
            self.full_nat_table = temp_model.from_map(m.get('FullNatTable'))

        self.ip_list = []
        if m.get('IpList') is not None:
            for k1 in m.get('IpList'):
                temp_model = main_models.GetNatGatewayAttributeResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k1))

        if m.get('LogDelivery') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodyLogDelivery()
            self.log_delivery = temp_model.from_map(m.get('LogDelivery'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PrivateInfo') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodyPrivateInfo()
            self.private_info = temp_model.from_map(m.get('PrivateInfo'))

        if m.get('PrivateLinkEnabled') is not None:
            self.private_link_enabled = m.get('PrivateLinkEnabled')

        if m.get('PrivateLinkMode') is not None:
            self.private_link_mode = m.get('PrivateLinkMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnatTable') is not None:
            temp_model = main_models.GetNatGatewayAttributeResponseBodySnatTable()
            self.snat_table = temp_model.from_map(m.get('SnatTable'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetNatGatewayAttributeResponseBodySnatTable(DaraModel):
    def __init__(
        self,
        snat_entry_count: int = None,
        snat_table_id: str = None,
    ):
        # The number of SNAT entries.
        self.snat_entry_count = snat_entry_count
        # The ID of the SNAT table.
        self.snat_table_id = snat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snat_entry_count is not None:
            result['SnatEntryCount'] = self.snat_entry_count

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnatEntryCount') is not None:
            self.snat_entry_count = m.get('SnatEntryCount')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        return self

class GetNatGatewayAttributeResponseBodyPrivateInfo(DaraModel):
    def __init__(
        self,
        eni_instance_id: str = None,
        iz_no: str = None,
        max_bandwidth: int = None,
        private_ip_address: str = None,
        vswitch_id: str = None,
    ):
        # The ID of the elastic network interface (ENI).
        self.eni_instance_id = eni_instance_id
        # The zone where the NAT gateway is deployed.
        self.iz_no = iz_no
        # The maximum bandwidth. Unit: Mbit/s.
        self.max_bandwidth = max_bandwidth
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

        if self.iz_no is not None:
            result['IzNo'] = self.iz_no

        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')

        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')

        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class GetNatGatewayAttributeResponseBodyLogDelivery(DaraModel):
    def __init__(
        self,
        deliver_logs_error_message: str = None,
        delivery_status: str = None,
        log_delivery_type: str = None,
        log_destination: str = None,
    ):
        self.deliver_logs_error_message = deliver_logs_error_message
        self.delivery_status = delivery_status
        self.log_delivery_type = log_delivery_type
        self.log_destination = log_destination

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deliver_logs_error_message is not None:
            result['DeliverLogsErrorMessage'] = self.deliver_logs_error_message

        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status

        if self.log_delivery_type is not None:
            result['LogDeliveryType'] = self.log_delivery_type

        if self.log_destination is not None:
            result['LogDestination'] = self.log_destination

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverLogsErrorMessage') is not None:
            self.deliver_logs_error_message = m.get('DeliverLogsErrorMessage')

        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')

        if m.get('LogDeliveryType') is not None:
            self.log_delivery_type = m.get('LogDeliveryType')

        if m.get('LogDestination') is not None:
            self.log_destination = m.get('LogDestination')

        return self

class GetNatGatewayAttributeResponseBodyIpList(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        ip_address: str = None,
        using_status: str = None,
    ):
        # The ID of the EIP.
        self.allocation_id = allocation_id
        # The IP address of the EIP.
        self.ip_address = ip_address
        # The association status of the EIP.
        # 
        # *   **idle**: The EIP is not specified in an SNAT entry or a DNAT entry.
        # *   **UsedBySnatTable**: The EIP is specified in an SNAT entry.
        # *   **UsedByForwardTable**: The EIP is specified in a DNAT entry.
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

        if self.using_status is not None:
            result['UsingStatus'] = self.using_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('UsingStatus') is not None:
            self.using_status = m.get('UsingStatus')

        return self

class GetNatGatewayAttributeResponseBodyFullNatTable(DaraModel):
    def __init__(
        self,
        full_nat_entry_count: int = None,
        full_nat_table_id: str = None,
    ):
        # The number of FULLNAT entries.
        self.full_nat_entry_count = full_nat_entry_count
        # The ID of the FULLNAT table.
        self.full_nat_table_id = full_nat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_nat_entry_count is not None:
            result['FullNatEntryCount'] = self.full_nat_entry_count

        if self.full_nat_table_id is not None:
            result['FullNatTableId'] = self.full_nat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullNatEntryCount') is not None:
            self.full_nat_entry_count = m.get('FullNatEntryCount')

        if m.get('FullNatTableId') is not None:
            self.full_nat_table_id = m.get('FullNatTableId')

        return self

class GetNatGatewayAttributeResponseBodyForwardTable(DaraModel):
    def __init__(
        self,
        forward_entry_count: int = None,
        forward_table_id: str = None,
    ):
        # The number of DNAT entries.
        self.forward_entry_count = forward_entry_count
        # The ID of the DNAT table.
        self.forward_table_id = forward_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_entry_count is not None:
            result['ForwardEntryCount'] = self.forward_entry_count

        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardEntryCount') is not None:
            self.forward_entry_count = m.get('ForwardEntryCount')

        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        return self

class GetNatGatewayAttributeResponseBodyDeletionProtectionInfo(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Indicates whether deletion protection is enabled.
        # 
        # *   **true**: yes
        # *   **false**: no
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class GetNatGatewayAttributeResponseBodyBillingConfig(DaraModel):
    def __init__(
        self,
        auto_pay: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        spec: str = None,
    ):
        # Indicates whether automatic payment is enabled. If the **InstanceChargeType** parameter is set to **PrePaid**, one of the following values is returned:
        # 
        # *   **false**: disabled. After an order is generated, you must go to the Order Center to complete the payment.
        # *   **true**: enabled. Payments are automatically completed.
        # 
        # The return value of this parameter is empty if **InstanceChargeType** is set to **PostPaid**.
        self.auto_pay = auto_pay
        # The billing method of the NAT gateway. The value is set to **PostPaid**, which indicates the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The metering method of the NAT gateway. Valid values:
        # 
        # *   **PayBySpec**: pay-by-specification
        # *   **PayByLcu**: pay-by-CU
        self.internet_charge_type = internet_charge_type
        # The specification of the Internet NAT gateway. If the **InternetChargeType** parameter is set to **PayBySpec**, one of the following values is returned:
        # 
        # *   **Small**: small
        # 
        # *   **Middle**: medium
        # 
        # *   **Large**: large
        # 
        #     The return value of this parameter is empty if **InternetChargeType** is set to **PayByLcu**.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

class GetNatGatewayAttributeResponseBodyAccessMode(DaraModel):
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

