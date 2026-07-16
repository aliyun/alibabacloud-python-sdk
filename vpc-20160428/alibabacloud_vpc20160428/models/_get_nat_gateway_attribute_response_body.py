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
        availability_mode: str = None,
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
        # The access mode of the VPC NAT Gateway.
        self.access_mode = access_mode
        self.availability_mode = availability_mode
        # The billing configuration.
        self.billing_config = billing_config
        # The business status of the NAT Gateway instance. Valid values:
        # 
        # - **Normal**: The instance is running normally.
        # 
        # - **FinancialLocked**: The instance is suspended due to an overdue payment.
        self.business_status = business_status
        # The creation time of the NAT Gateway instance. The time is in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.creation_time = creation_time
        # Information about the deletion protection feature.
        self.deletion_protection_info = deletion_protection_info
        # The description of the NAT Gateway instance.
        self.description = description
        # Indicates whether the gateway traffic monitoring feature is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.ecs_metric_enabled = ecs_metric_enabled
        # Indicates whether session logging is enabled. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.enable_session_log = enable_session_log
        # The expiration time of the NAT Gateway instance.
        self.expired_time = expired_time
        # Information about the DNAT table.
        self.forward_table = forward_table
        # Information about the FULLNAT table.
        self.full_nat_table = full_nat_table
        # The Elastic IP Addresses (EIPs) that are associated with the public NAT gateway.
        self.ip_list = ip_list
        # The session log delivery settings.
        self.log_delivery = log_delivery
        # The name of the NAT Gateway instance.
        self.name = name
        # The ID of the NAT Gateway instance.
        self.nat_gateway_id = nat_gateway_id
        # The type of the public NAT gateway. The value **Enhanced** indicates an Enhanced NAT Gateway.
        self.nat_type = nat_type
        # The type of the NAT Gateway. Valid values:
        # 
        # - **internet**: A public NAT gateway.
        # 
        # - **intranet**: A VPC NAT Gateway.
        self.network_type = network_type
        # The private network information about the NAT Gateway instance.
        self.private_info = private_info
        # Indicates whether PrivateLink is supported. Valid values:
        # 
        # - **true**: PrivateLink is supported.
        # 
        # - **false**: PrivateLink is not supported.
        self.private_link_enabled = private_link_enabled
        # The mode of the PrivateLink service. Valid values:
        # 
        # - **FullNat**: FULLNAT mode.
        # 
        # - **Geneve**: Geneve mode.
        self.private_link_mode = private_link_mode
        # The region ID of the NAT Gateway instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Information about the SNAT table.
        self.snat_table = snat_table
        # The status of the NAT Gateway instance. Valid values:
        # 
        # - **Creating**: Being created. This is an asynchronous operation.
        # 
        # - **Available**: Available. This is the steady state of the NAT Gateway after creation.
        # 
        # - **Modifying**: Being modified. This is an asynchronous operation.
        # 
        # - **Deleting**: Being deleted. This is an asynchronous operation.
        # 
        # - **Converting**: Being converted to an Enhanced NAT Gateway. This is an asynchronous operation.
        self.status = status
        # The ID of the VPC to which the NAT Gateway instance belongs.
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

        if self.availability_mode is not None:
            result['AvailabilityMode'] = self.availability_mode

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

        if m.get('AvailabilityMode') is not None:
            self.availability_mode = m.get('AvailabilityMode')

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
        # The ID of the elastic network interface instance.
        self.eni_instance_id = eni_instance_id
        # The ID of the availability zone to which the NAT Gateway instance belongs.
        self.iz_no = iz_no
        # The maximum bandwidth, in Mbps.
        self.max_bandwidth = max_bandwidth
        # The private IP address.
        self.private_ip_address = private_ip_address
        # The ID of the vSwitch to which the NAT Gateway instance belongs.
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
        # The error message that is returned when log delivery fails.
        self.deliver_logs_error_message = deliver_logs_error_message
        # The status of log delivery. Valid values:
        # 
        # - **Success**: The logs are delivered successfully.
        # 
        # - **Failure**: The logs failed to be delivered.
        self.delivery_status = delivery_status
        # The destination to which session logs are delivered. The value is always
        # **sls**, which indicates Log Service.
        self.log_delivery_type = log_delivery_type
        # The Log Service Logstore to which session logs are delivered.
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
        # The ID of the EIP instance.
        self.allocation_id = allocation_id
        # The EIP address.
        self.ip_address = ip_address
        # The usage status of the EIP.
        # 
        # - **Idle**: Not associated with an SNAT entry or a DNAT entry.
        # 
        # - **UsedBySnat**: Associated with an SNAT entry.
        # 
        # - **UsedByForward**: Associated with a DNAT entry.
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
        # - **true**
        # 
        # - **false**
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
        # Indicates whether auto-payment is enabled. This parameter is returned only if **InstanceChargeType** is set to **PrePaid**. Valid values:
        # 
        # - **false**: Auto-payment is disabled. After an order is generated, the payment must be completed in the Orders console.
        # 
        # - **true**: Auto-payment is enabled. Payments are automatically completed.
        # 
        # If **InstanceChargeType** is set to **PostPaid**, an empty string is returned.
        self.auto_pay = auto_pay
        # <props="china">
        # 
        # The billing method of the NAT Gateway instance. Valid values:
        # 
        # 
        # 
        # <props="china">
        # 
        # - **PostPaid**: pay-as-you-go.
        # 
        # 
        # 
        # <props="china">
        # 
        # - **PrePaid**: subscription.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # The billing method of the NAT Gateway instance. The value is **PostPaid** (pay-as-you-go).
        self.instance_charge_type = instance_charge_type
        # The billing method of the NAT Gateway instance. Valid values:
        # 
        # - **PayBySpec**: billed by specification.
        # 
        # - **PayByLcu**: billed by usage.
        self.internet_charge_type = internet_charge_type
        # The specification of the public NAT gateway instance. This parameter is returned only if **InternetChargeType** is set to **PayBySpec**. Valid values:
        # 
        # - **Small**
        # 
        # - **Middle**
        # 
        # - **Large**
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
        # The access mode. Valid values:
        # 
        # - **route**: route mode.
        # 
        # - **tunnel**: tunnel mode.
        self.mode_value = mode_value
        # The tunnel type. This parameter is returned only when `ModeValue` is set to `tunnel`. Valid value:
        # 
        # - **geneve**: Geneve.
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

