# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpn_gateways: main_models.DescribeVpnGatewaysResponseBodyVpnGateways = None,
    ):
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The information about the VPN gateways.
        self.vpn_gateways = vpn_gateways

    def validate(self):
        if self.vpn_gateways:
            self.vpn_gateways.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpn_gateways is not None:
            result['VpnGateways'] = self.vpn_gateways.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VpnGateways') is not None:
            temp_model = main_models.DescribeVpnGatewaysResponseBodyVpnGateways()
            self.vpn_gateways = temp_model.from_map(m.get('VpnGateways'))

        return self

class DescribeVpnGatewaysResponseBodyVpnGateways(DaraModel):
    def __init__(
        self,
        vpn_gateway: List[main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGateway] = None,
    ):
        self.vpn_gateway = vpn_gateway

    def validate(self):
        if self.vpn_gateway:
            for v1 in self.vpn_gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpnGateway'] = []
        if self.vpn_gateway is not None:
            for k1 in self.vpn_gateway:
                result['VpnGateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpn_gateway = []
        if m.get('VpnGateway') is not None:
            for k1 in m.get('VpnGateway'):
                temp_model = main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGateway()
                self.vpn_gateway.append(temp_model.from_map(k1))

        return self

class DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGateway(DaraModel):
    def __init__(
        self,
        auto_propagate: bool = None,
        business_status: str = None,
        charge_type: str = None,
        create_time: int = None,
        description: str = None,
        disaster_recovery_internet_ip: str = None,
        disaster_recovery_vswitch_id: str = None,
        enable_bgp: bool = None,
        end_time: int = None,
        eni_instance_ids: main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayEniInstanceIds = None,
        internet_ip: str = None,
        ipsec_vpn: str = None,
        name: str = None,
        network_type: str = None,
        reservation_data: main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayReservationData = None,
        resource_group_id: str = None,
        spec: str = None,
        ssl_max_connections: int = None,
        ssl_vpn: str = None,
        ssl_vpn_internet_ip: str = None,
        status: str = None,
        tag: str = None,
        tags: main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayTags = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpn_gateway_id: str = None,
        vpn_type: str = None,
    ):
        # Indicates whether BGP routes are automatically advertised to the VPC.
        # 
        # *   **true**
        # *   **false**
        self.auto_propagate = auto_propagate
        # The payment status of the VPN gateway.
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        self.business_status = business_status
        # The billing method of the VPN gateway.
        # 
        # Only **POSTPAY** may be returned, which indicates the pay-as-you-go billing method.
        self.charge_type = charge_type
        # The timestamp generated when the VPN gateway was created. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the VPN gateway.
        self.description = description
        # The second IP address that is assigned to the VPN gateway to create IPsec-VPN connections.
        # 
        # This parameter is returned only if the VPN gateway supports IPsec-VPN connections in dual-tunnel mode.
        self.disaster_recovery_internet_ip = disaster_recovery_internet_ip
        # The ID of the second vSwitch that is associated with the VPN gateway.
        # 
        # This parameter is returned only if the VPN gateway supports IPsec-VPN connections in dual-tunnel mode.
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # The BGP status of the VPN gateway. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_bgp = enable_bgp
        # The timestamp generated when the VPN gateway expires. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The ENIs created by the system for the VPN gateway.
        self.eni_instance_ids = eni_instance_ids
        # *   If the VPN gateway supports IPsec-VPN connections in single-tunnel mode, the value of this parameter is the IP address of the VPN gateway, which can be used to create IPsec-VPN or SSL-VPN connections.
        # 
        # *   If the VPN gateway supports IPsec-VPN connections in dual-tunnel mode, the value of this parameter is the first IP address that is used to create an IPsec-VPN connection. The IP address cannot be used to create SSL-VPN connections.
        # 
        #     If the VPN gateway supports IPsec-VPN connections in dual-tunnel mode, the system assigns two IPsec addresses to the VPN gateway to create IPsec-VPN connections in dual-tunnel mode.
        self.internet_ip = internet_ip
        # Indicates whether IPsec-VPN is enabled for the VPN gateway. Valid values:
        # 
        # *   **enable**
        # *   **disable**
        self.ipsec_vpn = ipsec_vpn
        # The name of the VPN gateway.
        self.name = name
        # The network type of the VPN gateway.
        # 
        # *   **public**
        # *   **private**
        self.network_type = network_type
        # The information about pending orders.
        # 
        # > This parameter is returned only if **IncludeReservationData** is set to **true**.
        self.reservation_data = reservation_data
        # The ID of the resource group to which the VPN gateway belongs.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource groups.
        self.resource_group_id = resource_group_id
        # The maximum bandwidth of the VPN gateway. Unit: **M**, which indicates Mbit/s.
        self.spec = spec
        # The number of SSL-VPN connections supported by the VPN gateway.
        self.ssl_max_connections = ssl_max_connections
        # Indicates whether SSL-VPN is enabled for the VPN gateway. Valid values:
        # 
        # *   **enable**
        # *   **disable**
        self.ssl_vpn = ssl_vpn
        # The IP address of the SSL-VPN connection.
        # 
        # This parameter is returned only if the VPN gateway is a public VPN gateway and supports IPsec-VPN connections in dual-tunnel mode. In addition, SSL-VPN must be enabled for the VPN gateway.
        self.ssl_vpn_internet_ip = ssl_vpn_internet_ip
        # The status of the VPN gateway. Valid values:
        # 
        # *   **init**
        # *   **provisioning**
        # *   **active**
        # *   **updating**
        # *   **deleting**
        self.status = status
        # The tag that is automatically generated for the VPN gateway.
        # 
        # *   **VpnEnableBgp**: indicates whether the VPN gateway supports BGP. Valid values:
        # 
        #     *   **true**
        #     *   **false**
        # 
        # *   **VisuallySsl**: indicates whether the VPN gateway allows you to view the connection information of SSL clients. Valid values:
        # 
        #     *   **true**
        #     *   **false**
        # 
        # *   **PbrPriority**: indicates whether the VPN gateway allows you to configure priorities for policy-based routes. Valid values:
        # 
        #     *   **true**
        #     *   **false**
        # 
        # *   **VpnNewImage**: indicates whether the VPN gateway is upgraded. Valid values:
        # 
        #     *   **true**: queries only SQL templates that need to be optimized.
        #     *   **false**: does not query only SQL statements that need to be optimized.
        # 
        # *   **description**: the description of the VPN gateway. This parameter is only for internal use.
        # 
        # *   **VpnVersion**: the version of the VPN gateway.
        # 
        # *   **IDaaSNewVersion**: indicates whether the VPN gateway can be associated with an EIAM 2.0 instance.
        # 
        #     *   **true**
        #     *   **false**
        self.tag = tag
        # The tags that are added to the VPN gateway.
        self.tags = tags
        # The ID of the vSwitch to which the VPN gateway belongs.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the VPN gateway belongs.
        self.vpc_id = vpc_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id
        # The type of VPN gateway.
        # 
        # Only **Normal** may be returned, which indicates a standard VPN gateway.
        self.vpn_type = vpn_type

    def validate(self):
        if self.eni_instance_ids:
            self.eni_instance_ids.validate()
        if self.reservation_data:
            self.reservation_data.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_propagate is not None:
            result['AutoPropagate'] = self.auto_propagate

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.disaster_recovery_internet_ip is not None:
            result['DisasterRecoveryInternetIp'] = self.disaster_recovery_internet_ip

        if self.disaster_recovery_vswitch_id is not None:
            result['DisasterRecoveryVSwitchId'] = self.disaster_recovery_vswitch_id

        if self.enable_bgp is not None:
            result['EnableBgp'] = self.enable_bgp

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.eni_instance_ids is not None:
            result['EniInstanceIds'] = self.eni_instance_ids.to_map()

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.ipsec_vpn is not None:
            result['IpsecVpn'] = self.ipsec_vpn

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.reservation_data is not None:
            result['ReservationData'] = self.reservation_data.to_map()

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.ssl_max_connections is not None:
            result['SslMaxConnections'] = self.ssl_max_connections

        if self.ssl_vpn is not None:
            result['SslVpn'] = self.ssl_vpn

        if self.ssl_vpn_internet_ip is not None:
            result['SslVpnInternetIp'] = self.ssl_vpn_internet_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        if self.vpn_type is not None:
            result['VpnType'] = self.vpn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPropagate') is not None:
            self.auto_propagate = m.get('AutoPropagate')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisasterRecoveryInternetIp') is not None:
            self.disaster_recovery_internet_ip = m.get('DisasterRecoveryInternetIp')

        if m.get('DisasterRecoveryVSwitchId') is not None:
            self.disaster_recovery_vswitch_id = m.get('DisasterRecoveryVSwitchId')

        if m.get('EnableBgp') is not None:
            self.enable_bgp = m.get('EnableBgp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EniInstanceIds') is not None:
            temp_model = main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayEniInstanceIds()
            self.eni_instance_ids = temp_model.from_map(m.get('EniInstanceIds'))

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IpsecVpn') is not None:
            self.ipsec_vpn = m.get('IpsecVpn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('ReservationData') is not None:
            temp_model = main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayReservationData()
            self.reservation_data = temp_model.from_map(m.get('ReservationData'))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('SslMaxConnections') is not None:
            self.ssl_max_connections = m.get('SslMaxConnections')

        if m.get('SslVpn') is not None:
            self.ssl_vpn = m.get('SslVpn')

        if m.get('SslVpnInternetIp') is not None:
            self.ssl_vpn_internet_ip = m.get('SslVpnInternetIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        if m.get('VpnType') is not None:
            self.vpn_type = m.get('VpnType')

        return self

class DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayTagsTag] = None,
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
                temp_model = main_models.DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayTagsTag(DaraModel):
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

class DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayReservationData(DaraModel):
    def __init__(
        self,
        reservation_end_time: str = None,
        reservation_ipsec: str = None,
        reservation_max_connections: int = None,
        reservation_order_type: str = None,
        reservation_spec: str = None,
        reservation_ssl: str = None,
        status: str = None,
    ):
        # If the value of ReservationOrderType is **TEMP_UPGRADE**, this parameter indicates the time when the temporary upgrade expires.
        # 
        # If the value of ReservationOrderType is **RENEWCHANGE** or **RENEW**, this parameter indicates the time when the renewal or renewal with a specification change takes effect.
        self.reservation_end_time = reservation_end_time
        # The IPsec-VPN status of the pending order. Valid values:
        # 
        # *   **enable**
        # *   **disable**
        self.reservation_ipsec = reservation_ipsec
        # The maximum number of concurrent SSL-VPN connections of the pending order.
        self.reservation_max_connections = reservation_max_connections
        # The type of the order that has not taken effect. Valid values:
        # 
        # *   **RENEWCHANGE**: renewal with upgrade or downgrade
        # *   **TEMP_UPGRADE**: temporary upgrade
        # *   **RENEW**: renewal
        self.reservation_order_type = reservation_order_type
        # The bandwidth of the pending order. Unit: Mbit/s.
        self.reservation_spec = reservation_spec
        # The SSL-VPN status of the pending order. Valid values:
        # 
        # *   **enable**
        # *   **disable**
        self.reservation_ssl = reservation_ssl
        # The status of the pending order.
        # 
        # *   **1**: indicates that the order for renewal or the order for renewal with a specification change has not taken effect.
        # *   **2**: indicates that the order of the temporary upgrade has taken effect. After the temporary upgrade expires, the system restores the VPN gateway to its previous specifications. In this case, the values of **ReservationIpsec**, **ReservationMaxConnections**, **ReservationSpec**, and **ReservationSsl** indicate the previous specifications of the VPN gateway.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reservation_end_time is not None:
            result['ReservationEndTime'] = self.reservation_end_time

        if self.reservation_ipsec is not None:
            result['ReservationIpsec'] = self.reservation_ipsec

        if self.reservation_max_connections is not None:
            result['ReservationMaxConnections'] = self.reservation_max_connections

        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type

        if self.reservation_spec is not None:
            result['ReservationSpec'] = self.reservation_spec

        if self.reservation_ssl is not None:
            result['ReservationSsl'] = self.reservation_ssl

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservationEndTime') is not None:
            self.reservation_end_time = m.get('ReservationEndTime')

        if m.get('ReservationIpsec') is not None:
            self.reservation_ipsec = m.get('ReservationIpsec')

        if m.get('ReservationMaxConnections') is not None:
            self.reservation_max_connections = m.get('ReservationMaxConnections')

        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')

        if m.get('ReservationSpec') is not None:
            self.reservation_spec = m.get('ReservationSpec')

        if m.get('ReservationSsl') is not None:
            self.reservation_ssl = m.get('ReservationSsl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeVpnGatewaysResponseBodyVpnGatewaysVpnGatewayEniInstanceIds(DaraModel):
    def __init__(
        self,
        eni_instance_id: List[str] = None,
    ):
        self.eni_instance_id = eni_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')

        return self

