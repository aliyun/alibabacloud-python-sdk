# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewaysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The instances.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListGatewaysResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewaysResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListGatewaysResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The instances.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListGatewaysResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListGatewaysResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        expire_timestamp: int = None,
        gateway_edition: str = None,
        gateway_id: str = None,
        gateway_type: str = None,
        legacy: bool = None,
        load_balancers: List[main_models.ListGatewaysResponseBodyDataItemsLoadBalancers] = None,
        name: str = None,
        replicas: str = None,
        resource_group_id: str = None,
        security_group: main_models.ListGatewaysResponseBodyDataItemsSecurityGroup = None,
        spec: str = None,
        status: str = None,
        sub_domain_infos: List[main_models.SubDomainInfo] = None,
        tags: List[main_models.ListGatewaysResponseBodyDataItemsTags] = None,
        target_version: str = None,
        update_timestamp: int = None,
        v_switch: main_models.ListGatewaysResponseBodyDataItemsVSwitch = None,
        version: str = None,
        vpc: main_models.ListGatewaysResponseBodyDataItemsVpc = None,
        zones: List[main_models.ListGatewaysResponseBodyDataItemsZones] = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type
        # The creation source of the instance. Valid values:
        # 
        # *   Console
        self.create_from = create_from
        # The time when the instance was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The time when the instance expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.expire_timestamp = expire_timestamp
        self.gateway_edition = gateway_edition
        # The instance ID.
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        self.legacy = legacy
        # The ingress addresses of the instance.
        self.load_balancers = load_balancers
        # The instance name.
        self.name = name
        # The node quantity of the instance.
        self.replicas = replicas
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The security group information about the instance.
        self.security_group = security_group
        # The instance specification. Valid values:
        # 
        # *   apigw.small.x1
        self.spec = spec
        # The instance state. Valid values:
        # 
        # *   Running: The instance is running.
        # *   Creating: The instance is being created.
        # *   CreateFailed: The instance fails to be created.
        # *   Upgrading: The instance is being upgraded.
        # *   UpgradeFailed: The instance fails to be upgraded.
        # *   Restarting: The instance is being restarted.
        # *   RestartFailed: The instance fails to be restarted.
        # *   Deleting: The instance is being released.
        # *   DeleteFailed: The instance failed to be released.
        self.status = status
        # The second-level domain names.
        self.sub_domain_infos = sub_domain_infos
        # The tags.
        self.tags = tags
        # The destination version of the instance. If the value is inconsistent with the current version, you can upgrade the instance.
        self.target_version = target_version
        # The time when the instance was last updated. This value is a UNIX timestamp. Unit: milliseconds.
        self.update_timestamp = update_timestamp
        # The vSwitch information.
        self.v_switch = v_switch
        # The instance version.
        self.version = version
        # The virtual private cloud (VPC) information of the instance.
        self.vpc = vpc
        # The availability zones of the instance.
        self.zones = zones

    def validate(self):
        if self.load_balancers:
            for v1 in self.load_balancers:
                 if v1:
                    v1.validate()
        if self.security_group:
            self.security_group.validate()
        if self.sub_domain_infos:
            for v1 in self.sub_domain_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switch:
            self.v_switch.validate()
        if self.vpc:
            self.vpc.validate()
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.create_from is not None:
            result['createFrom'] = self.create_from

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp

        if self.gateway_edition is not None:
            result['gatewayEdition'] = self.gateway_edition

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.legacy is not None:
            result['legacy'] = self.legacy

        result['loadBalancers'] = []
        if self.load_balancers is not None:
            for k1 in self.load_balancers:
                result['loadBalancers'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.replicas is not None:
            result['replicas'] = self.replicas

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.security_group is not None:
            result['securityGroup'] = self.security_group.to_map()

        if self.spec is not None:
            result['spec'] = self.spec

        if self.status is not None:
            result['status'] = self.status

        result['subDomainInfos'] = []
        if self.sub_domain_infos is not None:
            for k1 in self.sub_domain_infos:
                result['subDomainInfos'].append(k1.to_map() if k1 else None)

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        if self.v_switch is not None:
            result['vSwitch'] = self.v_switch.to_map()

        if self.version is not None:
            result['version'] = self.version

        if self.vpc is not None:
            result['vpc'] = self.vpc.to_map()

        result['zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')

        if m.get('gatewayEdition') is not None:
            self.gateway_edition = m.get('gatewayEdition')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('legacy') is not None:
            self.legacy = m.get('legacy')

        self.load_balancers = []
        if m.get('loadBalancers') is not None:
            for k1 in m.get('loadBalancers'):
                temp_model = main_models.ListGatewaysResponseBodyDataItemsLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('securityGroup') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsSecurityGroup()
            self.security_group = temp_model.from_map(m.get('securityGroup'))

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k1 in m.get('subDomainInfos'):
                temp_model = main_models.SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListGatewaysResponseBodyDataItemsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        if m.get('vSwitch') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsVSwitch()
            self.v_switch = temp_model.from_map(m.get('vSwitch'))

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('vpc') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        self.zones = []
        if m.get('zones') is not None:
            for k1 in m.get('zones'):
                temp_model = main_models.ListGatewaysResponseBodyDataItemsZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListGatewaysResponseBodyDataItemsZones(DaraModel):
    def __init__(
        self,
        v_switch: main_models.ListGatewaysResponseBodyDataItemsZonesVSwitch = None,
        zone_id: str = None,
    ):
        # The vSwitch information.
        self.v_switch = v_switch
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.v_switch:
            self.v_switch.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch is not None:
            result['vSwitch'] = self.v_switch.to_map()

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitch') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsZonesVSwitch()
            self.v_switch = temp_model.from_map(m.get('vSwitch'))

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class ListGatewaysResponseBodyDataItemsZonesVSwitch(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        return self

class ListGatewaysResponseBodyDataItemsVpc(DaraModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class ListGatewaysResponseBodyDataItemsVSwitch(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        return self

class ListGatewaysResponseBodyDataItemsTags(DaraModel):
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
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListGatewaysResponseBodyDataItemsSecurityGroup(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
    ):
        # The security group ID.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        return self

class ListGatewaysResponseBodyDataItemsLoadBalancers(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        gateway_default: bool = None,
        ipv_4addresses: List[str] = None,
        ipv_6addresses: List[str] = None,
        load_balancer_id: str = None,
        mode: str = None,
        ports: List[main_models.ListGatewaysResponseBodyDataItemsLoadBalancersPorts] = None,
        status: str = None,
        type: str = None,
    ):
        # The load balancer IP address.
        self.address = address
        # The IP version of the address. Valid values:
        # 
        # *   ipv4: IPv4
        # *   ipv6: IPv6
        self.address_ip_version = address_ip_version
        # The address type. Valid values:
        # 
        # *   Internet
        # *   Intranet
        self.address_type = address_type
        # Indicates whether the address is the default ingress address of the instance.
        self.gateway_default = gateway_default
        self.ipv_4addresses = ipv_4addresses
        self.ipv_6addresses = ipv_6addresses
        # The load balancer ID.
        self.load_balancer_id = load_balancer_id
        # The mode in which the load balancer is provided. Valid values:
        # 
        # *   Managed: Cloud-native API Gateway manages and provides the load balancer.
        self.mode = mode
        # The list of listened ports.
        self.ports = ports
        # The load balancer status. Valid values:
        # 
        # *   Ready: The load balancer is available.
        # *   NotCreate: The load balancer is not associated with the instance.
        self.status = status
        # The load balancer type. Valid values:
        # 
        # *   NLB: Network Load Balancer
        # *   CLB: Classic Load Balancer
        self.type = type

    def validate(self):
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.address_ip_version is not None:
            result['addressIpVersion'] = self.address_ip_version

        if self.address_type is not None:
            result['addressType'] = self.address_type

        if self.gateway_default is not None:
            result['gatewayDefault'] = self.gateway_default

        if self.ipv_4addresses is not None:
            result['ipv4Addresses'] = self.ipv_4addresses

        if self.ipv_6addresses is not None:
            result['ipv6Addresses'] = self.ipv_6addresses

        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id

        if self.mode is not None:
            result['mode'] = self.mode

        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('addressIpVersion') is not None:
            self.address_ip_version = m.get('addressIpVersion')

        if m.get('addressType') is not None:
            self.address_type = m.get('addressType')

        if m.get('gatewayDefault') is not None:
            self.gateway_default = m.get('gatewayDefault')

        if m.get('ipv4Addresses') is not None:
            self.ipv_4addresses = m.get('ipv4Addresses')

        if m.get('ipv6Addresses') is not None:
            self.ipv_6addresses = m.get('ipv6Addresses')

        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.ListGatewaysResponseBodyDataItemsLoadBalancersPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListGatewaysResponseBodyDataItemsLoadBalancersPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   TCP
        # *   UDP
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

