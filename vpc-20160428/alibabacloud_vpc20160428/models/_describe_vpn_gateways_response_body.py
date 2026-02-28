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
        gateway_type: str = None,
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
        # 是否已开启VPN网关的路由自动传播功能。
        # 
        # - **true**：已开启。
        # 
        # - **false**：未开启。
        self.auto_propagate = auto_propagate
        # VPN网关的付费状态。
        # 
        # - **Normal**：正常。
        # 
        # - **FinancialLocked**：欠费锁定。
        self.business_status = business_status
        # VPN网关的付费类型。
        # 
        # <props="china">仅取值：**Prepay**，包年包月。
        # 
        # <props="intl">仅取值：**POSTPAY**，按量计费。
        # 
        # <props="partner">仅取值： **POSTPAY**，按量计费。
        self.charge_type = charge_type
        # 创建VPN网关的时间戳。单位：毫秒。
        # 
        # 时间戳的格式采用Unix时间戳，表示从格林威治时间1970年01月01日00时00分00秒至创建VPN网关实例时的总时长。
        self.create_time = create_time
        # VPN网关的描述信息。
        self.description = description
        # 系统为VPN网关实例分配的用于创建IPsec-VPN连接的第二个IP地址。
        # 
        # 仅支持创建双隧道模式IPsec-VPN连接的VPN网关实例会返回当前参数。
        self.disaster_recovery_internet_ip = disaster_recovery_internet_ip
        # VPN网关实例关联的第二个交换机ID。
        # 
        # 仅支持创建双隧道模式IPsec-VPN连接的VPN网关实例会返回当前参数。
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # VPN网关BGP功能的开启状态。
        # 
        # - **true**：已开启。
        # 
        # - **false**：未开启。
        self.enable_bgp = enable_bgp
        # VPN网关到期时间戳。单位：毫秒。
        # 
        # 时间戳的格式采用Unix时间戳，表示从格林威治时间1970年01月01日00时00分00秒至VPN网关实例到期时的总时长。
        self.end_time = end_time
        # 系统为VPN网关实例创建的弹性网卡ENI（Elastic Network Interfaces）列表。
        self.eni_instance_ids = eni_instance_ids
        # VPN 网关类型，取值：
        # Traditional：传统型VPN网关，覆盖IPsec功能和SSL功能
        # Enhance.SiteToSite：增强型站点入云VPN，只覆盖IPsec功能
        self.gateway_type = gateway_type
        # - 在VPN网关实例支持创建单隧道模式IPsec-VPN连接的场景下，该地址为VPN网关实例的IP地址，可用于创建IPsec-VPN连接或SSL-VPN连接。
        # 
        # - 在VPN网关实例支持创建双隧道模式IPsec-VPN连接的场景下，该地址为用于创建IPsec-VPN连接的第一个IP地址，不能用于创建SSL-VPN连接。
        # 
        #     在VPN网关实例支持创建双隧道模式IPsec-VPN连接的场景下，系统会为VPN网关实例分配两个IPsec地址，用于创建双隧道模式的IPsec-VPN连接。
        self.internet_ip = internet_ip
        # VPN网关是否开启了IPsec-VPN功能。
        # 
        # - **enable**：已开启。
        # 
        # - **disable**：未开启。
        self.ipsec_vpn = ipsec_vpn
        # VPN网关的名称。
        self.name = name
        # VPN网关的网络类型。
        # 
        # - **public**：公网VPN网关。
        # - **private**：私网VPN网关。
        self.network_type = network_type
        # 未生效的订购数据。
        # 
        # >仅**IncludeReservationData**传入**true**才会返回该组参数。
        self.reservation_data = reservation_data
        # VPN网关所属的资源组ID。
        # 
        # 您可以调用[ListResourceGroups](https://help.aliyun.com/document_detail/158855.html)接口查询资源组信息。
        self.resource_group_id = resource_group_id
        # VPN网关的带宽峰值。**M**表示单位Mbps。
        self.spec = spec
        # VPN网关SSL连接数的规格。
        self.ssl_max_connections = ssl_max_connections
        # VPN网关是否开启了SSL-VPN功能。
        # 
        # - **enable**：已开启。
        # 
        # - **disable**：未开启。
        self.ssl_vpn = ssl_vpn
        # SSL-VPN连接的IP地址。
        # 
        # 仅支持创建双隧道模式IPsec-VPN连接的公网网络类型的VPN网关实例开启SSL-VPN功能后，才会返回当前参数。
        self.ssl_vpn_internet_ip = ssl_vpn_internet_ip
        # VPN网关的状态。
        # 
        # - **init** ：初始化。
        # 
        # - **provisioning** ：准备中。
        # 
        # - **active** ：正常。
        # 
        # - **updating** ：更新中。
        # 
        # - **deleting** ：删除中。
        self.status = status
        # 系统自动生成的VPN网关标签。
        # 
        # - **VpnEnableBgp**：表示VPN网关是否支持BGP功能。
        #     - **true**：支持。
        #     - **false**：不支持。
        # - **VisuallySsl**：表示VPN网关是否支持查看SSL客户端的连接信息。
        #     - **true**：支持。
        #     - **false**：不支持。
        # - **PbrPriority**：表示VPN网关是否支持为策略路由配置策略优先级。
        #     - **true**：支持。
        #     - **false**：不支持。
        # - **VpnNewImage**：表示VPN网关是否为新型VPN网关。
        #     - **true**：是。
        #     - **false**：否。
        # - **description**：表示VPN网关的描述信息，仅供系统内部使用。
        # - **VpnVersion**：表示VPN网关的版本号。
        # - **IDaaSNewVersion**：表示VPN网关是否支持绑定EIAM 2.0实例。
        #     - **true**：支持。
        #     - **false**：不支持。
        self.tag = tag
        # VPN网关绑定的标签列表。
        self.tags = tags
        # VPN网关所属交换机的ID。
        self.v_switch_id = v_switch_id
        # VPN网关所属VPC的ID。
        self.vpc_id = vpc_id
        # VPN网关的ID。
        self.vpn_gateway_id = vpn_gateway_id
        # VPN网关类型。
        # 	
        # <props="china">
        # 
        # - **Normal**：普通型。
        # - **NationalStandard**：国密型。
        # 
        # 
        # 
        # <props="intl">取值：**Normal**，表示普通型。
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

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

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

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

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
        # 标签键。
        self.key = key
        # 标签值。
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
        # 如果未生效订单类型为**TEMP_UPGRADE**（临时升配）时，该参数表示为临时升配的还原时间。
        # 
        # 如果未生效订单类型为**RENEWCHANGE**（续费变配）或**RENEW**（续费）时，该参数表示为续费或续费变配开始生效时间。
        self.reservation_end_time = reservation_end_time
        # 未生效订单IPsec-VPN功能开启状态。
        # 
        # - **enable**：已开启。
        # 
        # - **disable**：未开启。
        self.reservation_ipsec = reservation_ipsec
        # 未生效订单SSL-VPN并发连接用户数的规格。
        self.reservation_max_connections = reservation_max_connections
        # 未生效订单类型。
        # 
        # - **RENEWCHANGE**：续费变配。
        # 
        # - **TEMP_UPGRADE**：临时升配。
        # 
        # - **RENEW**：续费。
        self.reservation_order_type = reservation_order_type
        # 未生效订单的带宽规格。单位：Mbps。
        self.reservation_spec = reservation_spec
        # 未生效订单SSL-VPN功能开启状态。
        # - **enable**：已开启。
        # 
        # - **disable**：未开启。
        self.reservation_ssl = reservation_ssl
        # 未生效订单状态。
        # 
        # - **1**：表示续费或续费变配的订单未生效。
        # 
        # - **2**：表示临时升配的订单已生效。在到达还原时间后，系统会将VPN网关规格恢复到临时升配前的规格。此时**ReservationIpsec**、**ReservationMaxConnections**、**ReservationSpec**、**ReservationSsl**表示为VPN网关临时升配前的规格。
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

