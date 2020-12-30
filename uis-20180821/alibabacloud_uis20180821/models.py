# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddHighPriorityIpRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        uis_id: str = None,
        high_priority_ip: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.uis_id = uis_id
        self.high_priority_ip = high_priority_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.high_priority_ip is not None:
            result['HighPriorityIp'] = self.high_priority_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('HighPriorityIp') is not None:
            self.high_priority_ip = m.get('HighPriorityIp')
        return self


class AddHighPriorityIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddHighPriorityIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddHighPriorityIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddHighPriorityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUisNodeIpRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        uis_node_id: str = None,
        ip_addrs_num: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.ip_addrs_num = ip_addrs_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.ip_addrs_num is not None:
            result['IpAddrsNum'] = self.ip_addrs_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('IpAddrsNum') is not None:
            self.ip_addrs_num = m.get('IpAddrsNum')
        return self


class AddUisNodeIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUisNodeIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUisNodeIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUisNodeIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDnatEntryRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_node_id: str = None,
        destination_ip: str = None,
        destination_port: int = None,
        original_ip: str = None,
        original_port: int = None,
        ip_protocol: str = None,
        name: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_node_id = uis_node_id
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.original_ip = original_ip
        self.original_port = original_port
        self.ip_protocol = ip_protocol
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
        if self.original_ip is not None:
            result['OriginalIp'] = self.original_ip
        if self.original_port is not None:
            result['OriginalPort'] = self.original_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
        if m.get('OriginalIp') is not None:
            self.original_ip = m.get('OriginalIp')
        if m.get('OriginalPort') is not None:
            self.original_port = m.get('OriginalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateDnatEntryResponseBody(TeaModel):
    def __init__(
        self,
        uis_dnat_id: str = None,
        request_id: str = None,
    ):
        self.uis_dnat_id = uis_dnat_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uis_dnat_id is not None:
            result['UisDnatId'] = self.uis_dnat_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UisDnatId') is not None:
            self.uis_dnat_id = m.get('UisDnatId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDnatEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDnatEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDnatEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_node_id: str = None,
        ip: str = None,
        description: str = None,
        name: str = None,
        gre_config: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_node_id = uis_node_id
        self.ip = ip
        self.description = description
        self.name = name
        self.gre_config = gre_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.gre_config is not None:
            result['GreConfig'] = self.gre_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GreConfig') is not None:
            self.gre_config = m.get('GreConfig')
        return self


class CreateSubConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        uis_sub_connection_id: str = None,
    ):
        self.request_id = request_id
        self.uis_sub_connection_id = uis_sub_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uis_sub_connection_id is not None:
            result['UisSubConnectionId'] = self.uis_sub_connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UisSubConnectionId') is not None:
            self.uis_sub_connection_id = m.get('UisSubConnectionId')
        return self


class CreateSubConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSubConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSubConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUisRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        client_token: str = None,
        name: str = None,
        description: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        auto_pay: bool = None,
        duration: int = None,
        pricing_cycle: str = None,
        bandwidth: int = None,
        bandwidth_type: str = None,
        uis_protocol: str = None,
        connection_bandwidth: int = None,
        connection_count: int = None,
        service_region: str = None,
        access_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.auto_pay = auto_pay
        self.duration = duration
        self.pricing_cycle = pricing_cycle
        self.bandwidth = bandwidth
        self.bandwidth_type = bandwidth_type
        self.uis_protocol = uis_protocol
        self.connection_bandwidth = connection_bandwidth
        self.connection_count = connection_count
        self.service_region = service_region
        self.access_type = access_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.uis_protocol is not None:
            result['UisProtocol'] = self.uis_protocol
        if self.connection_bandwidth is not None:
            result['ConnectionBandwidth'] = self.connection_bandwidth
        if self.connection_count is not None:
            result['ConnectionCount'] = self.connection_count
        if self.service_region is not None:
            result['ServiceRegion'] = self.service_region
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('UisProtocol') is not None:
            self.uis_protocol = m.get('UisProtocol')
        if m.get('ConnectionBandwidth') is not None:
            self.connection_bandwidth = m.get('ConnectionBandwidth')
        if m.get('ConnectionCount') is not None:
            self.connection_count = m.get('ConnectionCount')
        if m.get('ServiceRegion') is not None:
            self.service_region = m.get('ServiceRegion')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        return self


class CreateUisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        uis_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.uis_id = uis_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateUisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUisConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_node_id: str = None,
        uis_protocol: str = None,
        description: str = None,
        name: str = None,
        gre_config: str = None,
        ssl_config: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.uis_protocol = uis_protocol
        self.description = description
        self.name = name
        self.gre_config = gre_config
        self.ssl_config = ssl_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_protocol is not None:
            result['UisProtocol'] = self.uis_protocol
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.gre_config is not None:
            result['GreConfig'] = self.gre_config
        if self.ssl_config is not None:
            result['SslConfig'] = self.ssl_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisProtocol') is not None:
            self.uis_protocol = m.get('UisProtocol')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GreConfig') is not None:
            self.gre_config = m.get('GreConfig')
        if m.get('SslConfig') is not None:
            self.ssl_config = m.get('SslConfig')
        return self


class CreateUisConnectionResponseBody(TeaModel):
    def __init__(
        self,
        uis_connection_id: str = None,
        request_id: str = None,
    ):
        self.uis_connection_id = uis_connection_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uis_connection_id is not None:
            result['UisConnectionId'] = self.uis_connection_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UisConnectionId') is not None:
            self.uis_connection_id = m.get('UisConnectionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUisConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUisConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUisConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUisNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_node_id: str = None,
        vswitch_id: str = None,
        security_group_id: str = None,
        ip_address: str = None,
        name: str = None,
        description: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_node_id = uis_node_id
        self.vswitch_id = vswitch_id
        self.security_group_id = security_group_id
        self.ip_address = ip_address
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateUisNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        uis_eni_id: str = None,
        request_id: str = None,
    ):
        self.uis_eni_id = uis_eni_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uis_eni_id is not None:
            result['UisEniId'] = self.uis_eni_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UisEniId') is not None:
            self.uis_eni_id = m.get('UisEniId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUisNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUisNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUisNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUisNodeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_id: str = None,
        name: str = None,
        description: str = None,
        uis_node_bandwidth: int = None,
        ip_addrs_num: int = None,
        uis_node_area_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_id = uis_id
        self.name = name
        self.description = description
        self.uis_node_bandwidth = uis_node_bandwidth
        self.ip_addrs_num = ip_addrs_num
        self.uis_node_area_id = uis_node_area_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.uis_node_bandwidth is not None:
            result['UisNodeBandwidth'] = self.uis_node_bandwidth
        if self.ip_addrs_num is not None:
            result['IpAddrsNum'] = self.ip_addrs_num
        if self.uis_node_area_id is not None:
            result['UisNodeAreaId'] = self.uis_node_area_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UisNodeBandwidth') is not None:
            self.uis_node_bandwidth = m.get('UisNodeBandwidth')
        if m.get('IpAddrsNum') is not None:
            self.ip_addrs_num = m.get('IpAddrsNum')
        if m.get('UisNodeAreaId') is not None:
            self.uis_node_area_id = m.get('UisNodeAreaId')
        return self


class CreateUisNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        uis_node_id: str = None,
    ):
        self.request_id = request_id
        self.uis_node_id = uis_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        return self


class CreateUisNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUisNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUisNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDnatEntryRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_node_id: str = None,
        uis_dnat_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_node_id = uis_node_id
        self.uis_dnat_id = uis_dnat_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_dnat_id is not None:
            result['UisDnatId'] = self.uis_dnat_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisDnatId') is not None:
            self.uis_dnat_id = m.get('UisDnatId')
        return self


class DeleteDnatEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDnatEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDnatEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDnatEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHighPriorityIpRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        uis_id: str = None,
        high_priority_ip: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.uis_id = uis_id
        self.high_priority_ip = high_priority_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.high_priority_ip is not None:
            result['HighPriorityIp'] = self.high_priority_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('HighPriorityIp') is not None:
            self.high_priority_ip = m.get('HighPriorityIp')
        return self


class DeleteHighPriorityIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHighPriorityIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHighPriorityIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHighPriorityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_sub_connection_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_sub_connection_id = uis_sub_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_sub_connection_id is not None:
            result['UisSubConnectionId'] = self.uis_sub_connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisSubConnectionId') is not None:
            self.uis_sub_connection_id = m.get('UisSubConnectionId')
        return self


class DeleteSubConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSubConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSubConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSubConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUisRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        uis_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class DeleteUisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUisConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        uis_connection_id: str = None,
        uis_node_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.uis_connection_id = uis_connection_id
        self.uis_node_id = uis_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.uis_connection_id is not None:
            result['UisConnectionId'] = self.uis_connection_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('UisConnectionId') is not None:
            self.uis_connection_id = m.get('UisConnectionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        return self


class DeleteUisConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUisConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUisConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUisConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUisNetworkInterfaceRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_node_id: str = None,
        uis_eni_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_node_id = uis_node_id
        self.uis_eni_id = uis_eni_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_eni_id is not None:
            result['UisEniId'] = self.uis_eni_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisEniId') is not None:
            self.uis_eni_id = m.get('UisEniId')
        return self


class DeleteUisNetworkInterfaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUisNetworkInterfaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUisNetworkInterfaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUisNetworkInterfaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUisNodeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        uis_id: str = None,
        uis_node_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.uis_id = uis_id
        self.uis_node_id = uis_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        return self


class DeleteUisNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUisNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUisNodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUisNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUisNodeIpRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        uis_node_id: str = None,
        uis_node_ip_address: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.uis_node_ip_address = uis_node_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_node_ip_address is not None:
            result['UisNodeIpAddress'] = self.uis_node_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisNodeIpAddress') is not None:
            self.uis_node_ip_address = m.get('UisNodeIpAddress')
        return self


class DeleteUisNodeIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUisNodeIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUisNodeIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUisNodeIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAreasRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAreasResponseBodyAreasArea(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        area_id: str = None,
    ):
        self.local_name = local_name
        self.area_id = area_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        return self


class DescribeAreasResponseBodyAreas(TeaModel):
    def __init__(
        self,
        area: List[DescribeAreasResponseBodyAreasArea] = None,
    ):
        self.area = area

    def validate(self):
        if self.area:
            for k in self.area:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Area'] = []
        if self.area is not None:
            for k in self.area:
                result['Area'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.area = []
        if m.get('Area') is not None:
            for k in m.get('Area'):
                temp_model = DescribeAreasResponseBodyAreasArea()
                self.area.append(temp_model.from_map(k))
        return self


class DescribeAreasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        areas: DescribeAreasResponseBodyAreas = None,
    ):
        self.request_id = request_id
        self.areas = areas

    def validate(self):
        if self.areas:
            self.areas.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.areas is not None:
            result['Areas'] = self.areas.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Areas') is not None:
            temp_model = DescribeAreasResponseBodyAreas()
            self.areas = temp_model.from_map(m['Areas'])
        return self


class DescribeAreasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAreasResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDnatEntriesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_node_id: str = None,
        uis_dnat_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.uis_dnat_id = uis_dnat_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_dnat_id is not None:
            result['UisDnatId'] = self.uis_dnat_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisDnatId') is not None:
            self.uis_dnat_id = m.get('UisDnatId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDnatEntriesResponseBodyUisDnatEntriesUisDnatEntry(TeaModel):
    def __init__(
        self,
        original_port: int = None,
        destination_port: int = None,
        original_ip: str = None,
        ip_protocol: str = None,
        uis_dnat_id: str = None,
        destination_ip: str = None,
    ):
        self.original_port = original_port
        self.destination_port = destination_port
        self.original_ip = original_ip
        self.ip_protocol = ip_protocol
        self.uis_dnat_id = uis_dnat_id
        self.destination_ip = destination_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.original_port is not None:
            result['OriginalPort'] = self.original_port
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
        if self.original_ip is not None:
            result['OriginalIp'] = self.original_ip
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.uis_dnat_id is not None:
            result['UisDnatId'] = self.uis_dnat_id
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalPort') is not None:
            self.original_port = m.get('OriginalPort')
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
        if m.get('OriginalIp') is not None:
            self.original_ip = m.get('OriginalIp')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('UisDnatId') is not None:
            self.uis_dnat_id = m.get('UisDnatId')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        return self


class DescribeDnatEntriesResponseBodyUisDnatEntries(TeaModel):
    def __init__(
        self,
        uis_dnat_entry: List[DescribeDnatEntriesResponseBodyUisDnatEntriesUisDnatEntry] = None,
    ):
        self.uis_dnat_entry = uis_dnat_entry

    def validate(self):
        if self.uis_dnat_entry:
            for k in self.uis_dnat_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UisDnatEntry'] = []
        if self.uis_dnat_entry is not None:
            for k in self.uis_dnat_entry:
                result['UisDnatEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.uis_dnat_entry = []
        if m.get('UisDnatEntry') is not None:
            for k in m.get('UisDnatEntry'):
                temp_model = DescribeDnatEntriesResponseBodyUisDnatEntriesUisDnatEntry()
                self.uis_dnat_entry.append(temp_model.from_map(k))
        return self


class DescribeDnatEntriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        uis_dnat_entries: DescribeDnatEntriesResponseBodyUisDnatEntries = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.uis_dnat_entries = uis_dnat_entries

    def validate(self):
        if self.uis_dnat_entries:
            self.uis_dnat_entries.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.uis_dnat_entries is not None:
            result['UisDnatEntries'] = self.uis_dnat_entries.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UisDnatEntries') is not None:
            temp_model = DescribeDnatEntriesResponseBodyUisDnatEntries()
            self.uis_dnat_entries = temp_model.from_map(m['UisDnatEntries'])
        return self


class DescribeDnatEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDnatEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDnatEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHighPriorityIpRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_id: str = None,
        high_priority_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        client_token: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_id = uis_id
        self.high_priority_ip = high_priority_ip
        self.page_number = page_number
        self.page_size = page_size
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.high_priority_ip is not None:
            result['HighPriorityIp'] = self.high_priority_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('HighPriorityIp') is not None:
            self.high_priority_ip = m.get('HighPriorityIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeHighPriorityIpResponseBodyHighPriorityIpsHighPriorityIp(TeaModel):
    def __init__(
        self,
        static_off_area_id: str = None,
        domain: str = None,
        dynamic_off_area_id: str = None,
        state: str = None,
        ip: str = None,
        board_area_id: str = None,
    ):
        self.static_off_area_id = static_off_area_id
        self.domain = domain
        self.dynamic_off_area_id = dynamic_off_area_id
        self.state = state
        self.ip = ip
        self.board_area_id = board_area_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.static_off_area_id is not None:
            result['StaticOffAreaId'] = self.static_off_area_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.dynamic_off_area_id is not None:
            result['DynamicOffAreaId'] = self.dynamic_off_area_id
        if self.state is not None:
            result['State'] = self.state
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.board_area_id is not None:
            result['BoardAreaId'] = self.board_area_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StaticOffAreaId') is not None:
            self.static_off_area_id = m.get('StaticOffAreaId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DynamicOffAreaId') is not None:
            self.dynamic_off_area_id = m.get('DynamicOffAreaId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('BoardAreaId') is not None:
            self.board_area_id = m.get('BoardAreaId')
        return self


class DescribeHighPriorityIpResponseBodyHighPriorityIps(TeaModel):
    def __init__(
        self,
        high_priority_ip: List[DescribeHighPriorityIpResponseBodyHighPriorityIpsHighPriorityIp] = None,
    ):
        self.high_priority_ip = high_priority_ip

    def validate(self):
        if self.high_priority_ip:
            for k in self.high_priority_ip:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HighPriorityIp'] = []
        if self.high_priority_ip is not None:
            for k in self.high_priority_ip:
                result['HighPriorityIp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.high_priority_ip = []
        if m.get('HighPriorityIp') is not None:
            for k in m.get('HighPriorityIp'):
                temp_model = DescribeHighPriorityIpResponseBodyHighPriorityIpsHighPriorityIp()
                self.high_priority_ip.append(temp_model.from_map(k))
        return self


class DescribeHighPriorityIpResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        high_priority_ips: DescribeHighPriorityIpResponseBodyHighPriorityIps = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.high_priority_ips = high_priority_ips

    def validate(self):
        if self.high_priority_ips:
            self.high_priority_ips.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.high_priority_ips is not None:
            result['HighPriorityIps'] = self.high_priority_ips.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('HighPriorityIps') is not None:
            temp_model = DescribeHighPriorityIpResponseBodyHighPriorityIps()
            self.high_priority_ips = temp_model.from_map(m['HighPriorityIps'])
        return self


class DescribeHighPriorityIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHighPriorityIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHighPriorityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHighPriorityIpsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_id = uis_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeHighPriorityIpsResponseBodyHighPriorityIpsHighPriorityIp(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        destination: str = None,
    ):
        self.area_id = area_id
        self.destination = destination

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.destination is not None:
            result['Destination'] = self.destination
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        return self


class DescribeHighPriorityIpsResponseBodyHighPriorityIps(TeaModel):
    def __init__(
        self,
        high_priority_ip: List[DescribeHighPriorityIpsResponseBodyHighPriorityIpsHighPriorityIp] = None,
    ):
        self.high_priority_ip = high_priority_ip

    def validate(self):
        if self.high_priority_ip:
            for k in self.high_priority_ip:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HighPriorityIp'] = []
        if self.high_priority_ip is not None:
            for k in self.high_priority_ip:
                result['HighPriorityIp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.high_priority_ip = []
        if m.get('HighPriorityIp') is not None:
            for k in m.get('HighPriorityIp'):
                temp_model = DescribeHighPriorityIpsResponseBodyHighPriorityIpsHighPriorityIp()
                self.high_priority_ip.append(temp_model.from_map(k))
        return self


class DescribeHighPriorityIpsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        high_priority_ips: DescribeHighPriorityIpsResponseBodyHighPriorityIps = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.high_priority_ips = high_priority_ips

    def validate(self):
        if self.high_priority_ips:
            self.high_priority_ips.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.high_priority_ips is not None:
            result['HighPriorityIps'] = self.high_priority_ips.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('HighPriorityIps') is not None:
            temp_model = DescribeHighPriorityIpsResponseBodyHighPriorityIps()
            self.high_priority_ips = temp_model.from_map(m['HighPriorityIps'])
        return self


class DescribeHighPriorityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHighPriorityIpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHighPriorityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_sub_connection_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_sub_connection_id = uis_sub_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_sub_connection_id is not None:
            result['UisSubConnectionId'] = self.uis_sub_connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisSubConnectionId') is not None:
            self.uis_sub_connection_id = m.get('UisSubConnectionId')
        return self


class DescribeSubConnectionResponseBody(TeaModel):
    def __init__(
        self,
        customer_tunnel_ip: str = None,
        description: str = None,
        local_tunnel_ip: str = None,
        request_id: str = None,
        uis_id: str = None,
        customer_ip: str = None,
        ip: str = None,
        uis_node_id: str = None,
        uis_sub_connection_id: str = None,
        customer_subnet: str = None,
        name: str = None,
    ):
        self.customer_tunnel_ip = customer_tunnel_ip
        self.description = description
        self.local_tunnel_ip = local_tunnel_ip
        self.request_id = request_id
        self.uis_id = uis_id
        self.customer_ip = customer_ip
        self.ip = ip
        self.uis_node_id = uis_node_id
        self.uis_sub_connection_id = uis_sub_connection_id
        self.customer_subnet = customer_subnet
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.customer_tunnel_ip is not None:
            result['CustomerTunnelIp'] = self.customer_tunnel_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.local_tunnel_ip is not None:
            result['LocalTunnelIp'] = self.local_tunnel_ip
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.customer_ip is not None:
            result['CustomerIp'] = self.customer_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_sub_connection_id is not None:
            result['UisSubConnectionId'] = self.uis_sub_connection_id
        if self.customer_subnet is not None:
            result['CustomerSubnet'] = self.customer_subnet
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerTunnelIp') is not None:
            self.customer_tunnel_ip = m.get('CustomerTunnelIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocalTunnelIp') is not None:
            self.local_tunnel_ip = m.get('LocalTunnelIp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('CustomerIp') is not None:
            self.customer_ip = m.get('CustomerIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisSubConnectionId') is not None:
            self.uis_sub_connection_id = m.get('UisSubConnectionId')
        if m.get('CustomerSubnet') is not None:
            self.customer_subnet = m.get('CustomerSubnet')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeSubConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSubConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubConnectionsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_node_id: str = None,
        ip: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_node_id = uis_node_id
        self.ip = ip
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSubConnectionsResponseBodyUisSubConnectionsUisSubConnection(TeaModel):
    def __init__(
        self,
        uis_sub_connection_id: str = None,
        description: str = None,
        create_time: int = None,
        ip: str = None,
        name: str = None,
    ):
        self.uis_sub_connection_id = uis_sub_connection_id
        self.description = description
        self.create_time = create_time
        self.ip = ip
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uis_sub_connection_id is not None:
            result['UisSubConnectionId'] = self.uis_sub_connection_id
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UisSubConnectionId') is not None:
            self.uis_sub_connection_id = m.get('UisSubConnectionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeSubConnectionsResponseBodyUisSubConnections(TeaModel):
    def __init__(
        self,
        uis_sub_connection: List[DescribeSubConnectionsResponseBodyUisSubConnectionsUisSubConnection] = None,
    ):
        self.uis_sub_connection = uis_sub_connection

    def validate(self):
        if self.uis_sub_connection:
            for k in self.uis_sub_connection:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UisSubConnection'] = []
        if self.uis_sub_connection is not None:
            for k in self.uis_sub_connection:
                result['UisSubConnection'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.uis_sub_connection = []
        if m.get('UisSubConnection') is not None:
            for k in m.get('UisSubConnection'):
                temp_model = DescribeSubConnectionsResponseBodyUisSubConnectionsUisSubConnection()
                self.uis_sub_connection.append(temp_model.from_map(k))
        return self


class DescribeSubConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        uis_sub_connections: DescribeSubConnectionsResponseBodyUisSubConnections = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.uis_sub_connections = uis_sub_connections

    def validate(self):
        if self.uis_sub_connections:
            self.uis_sub_connections.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.uis_sub_connections is not None:
            result['UisSubConnections'] = self.uis_sub_connections.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UisSubConnections') is not None:
            temp_model = DescribeSubConnectionsResponseBodyUisSubConnections()
            self.uis_sub_connections = temp_model.from_map(m['UisSubConnections'])
        return self


class DescribeSubConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubConnectionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSubConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUisConnectionsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_node_id: str = None,
        uis_connection_id: str = None,
        page_number: int = None,
        page_size: int = None,
        client_token: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.uis_connection_id = uis_connection_id
        self.page_number = page_number
        self.page_size = page_size
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_connection_id is not None:
            result['UisConnectionId'] = self.uis_connection_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisConnectionId') is not None:
            self.uis_connection_id = m.get('UisConnectionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeUisConnectionsResponseBodyUisConnectionsUisConnection(TeaModel):
    def __init__(
        self,
        gre_config: str = None,
        uis_id: str = None,
        uis_node_id: str = None,
        description: str = None,
        state: str = None,
        uis_protocol: str = None,
        name: str = None,
        ssl_config: str = None,
        uis_connection_id: str = None,
    ):
        self.gre_config = gre_config
        self.uis_id = uis_id
        self.uis_node_id = uis_node_id
        self.description = description
        self.state = state
        self.uis_protocol = uis_protocol
        self.name = name
        self.ssl_config = ssl_config
        self.uis_connection_id = uis_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gre_config is not None:
            result['GreConfig'] = self.gre_config
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.description is not None:
            result['Description'] = self.description
        if self.state is not None:
            result['State'] = self.state
        if self.uis_protocol is not None:
            result['UisProtocol'] = self.uis_protocol
        if self.name is not None:
            result['Name'] = self.name
        if self.ssl_config is not None:
            result['SslConfig'] = self.ssl_config
        if self.uis_connection_id is not None:
            result['UisConnectionId'] = self.uis_connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreConfig') is not None:
            self.gre_config = m.get('GreConfig')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UisProtocol') is not None:
            self.uis_protocol = m.get('UisProtocol')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SslConfig') is not None:
            self.ssl_config = m.get('SslConfig')
        if m.get('UisConnectionId') is not None:
            self.uis_connection_id = m.get('UisConnectionId')
        return self


class DescribeUisConnectionsResponseBodyUisConnections(TeaModel):
    def __init__(
        self,
        uis_connection: List[DescribeUisConnectionsResponseBodyUisConnectionsUisConnection] = None,
    ):
        self.uis_connection = uis_connection

    def validate(self):
        if self.uis_connection:
            for k in self.uis_connection:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UisConnection'] = []
        if self.uis_connection is not None:
            for k in self.uis_connection:
                result['UisConnection'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.uis_connection = []
        if m.get('UisConnection') is not None:
            for k in m.get('UisConnection'):
                temp_model = DescribeUisConnectionsResponseBodyUisConnectionsUisConnection()
                self.uis_connection.append(temp_model.from_map(k))
        return self


class DescribeUisConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        uis_connections: DescribeUisConnectionsResponseBodyUisConnections = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.uis_connections = uis_connections

    def validate(self):
        if self.uis_connections:
            self.uis_connections.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.uis_connections is not None:
            result['UisConnections'] = self.uis_connections.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UisConnections') is not None:
            temp_model = DescribeUisConnectionsResponseBodyUisConnections()
            self.uis_connections = temp_model.from_map(m['UisConnections'])
        return self


class DescribeUisConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUisConnectionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUisConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUiseNodeStatusRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_node_id: str = None,
        ip: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_node_id = uis_node_id
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeUiseNodeStatusResponseBodyIpStatusListIpStatus(TeaModel):
    def __init__(
        self,
        current_connections: int = None,
        ip: str = None,
        max_connections: int = None,
    ):
        self.current_connections = current_connections
        self.ip = ip
        self.max_connections = max_connections

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_connections is not None:
            result['CurrentConnections'] = self.current_connections
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentConnections') is not None:
            self.current_connections = m.get('CurrentConnections')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        return self


class DescribeUiseNodeStatusResponseBodyIpStatusList(TeaModel):
    def __init__(
        self,
        ip_status: List[DescribeUiseNodeStatusResponseBodyIpStatusListIpStatus] = None,
    ):
        self.ip_status = ip_status

    def validate(self):
        if self.ip_status:
            for k in self.ip_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IpStatus'] = []
        if self.ip_status is not None:
            for k in self.ip_status:
                result['IpStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_status = []
        if m.get('IpStatus') is not None:
            for k in m.get('IpStatus'):
                temp_model = DescribeUiseNodeStatusResponseBodyIpStatusListIpStatus()
                self.ip_status.append(temp_model.from_map(k))
        return self


class DescribeUiseNodeStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_status_list: DescribeUiseNodeStatusResponseBodyIpStatusList = None,
    ):
        self.request_id = request_id
        self.ip_status_list = ip_status_list

    def validate(self):
        if self.ip_status_list:
            self.ip_status_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_status_list is not None:
            result['IpStatusList'] = self.ip_status_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpStatusList') is not None:
            temp_model = DescribeUiseNodeStatusResponseBodyIpStatusList()
            self.ip_status_list = temp_model.from_map(m['IpStatusList'])
        return self


class DescribeUiseNodeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUiseNodeStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUiseNodeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUisesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_id = uis_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeUisesResponseBodyUisesUisUserInfo(TeaModel):
    def __init__(
        self,
        client_info_dbaccount: str = None,
        client_info_db: str = None,
        client_info_dbpassword: str = None,
    ):
        self.client_info_dbaccount = client_info_dbaccount
        self.client_info_db = client_info_db
        self.client_info_dbpassword = client_info_dbpassword

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_info_dbaccount is not None:
            result['ClientInfoDBAccount'] = self.client_info_dbaccount
        if self.client_info_db is not None:
            result['ClientInfoDB'] = self.client_info_db
        if self.client_info_dbpassword is not None:
            result['ClientInfoDBPassword'] = self.client_info_dbpassword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfoDBAccount') is not None:
            self.client_info_dbaccount = m.get('ClientInfoDBAccount')
        if m.get('ClientInfoDB') is not None:
            self.client_info_db = m.get('ClientInfoDB')
        if m.get('ClientInfoDBPassword') is not None:
            self.client_info_dbpassword = m.get('ClientInfoDBPassword')
        return self


class DescribeUisesResponseBodyUisesUisUisNodeIds(TeaModel):
    def __init__(
        self,
        uis_node_ids: List[str] = None,
    ):
        self.uis_node_ids = uis_node_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uis_node_ids is not None:
            result['UisNodeIds'] = self.uis_node_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UisNodeIds') is not None:
            self.uis_node_ids = m.get('UisNodeIds')
        return self


class DescribeUisesResponseBodyUisesUis(TeaModel):
    def __init__(
        self,
        status: str = None,
        uis_id: str = None,
        connection_type: str = None,
        bandwidth_type: str = None,
        create_time: int = None,
        charge_type: str = None,
        pay_type: str = None,
        user_info: DescribeUisesResponseBodyUisesUisUserInfo = None,
        ssl_client_cert_url: str = None,
        connection_count: int = None,
        uis_node_ids: DescribeUisesResponseBodyUisesUisUisNodeIds = None,
        end_time: int = None,
        bandwidth: int = None,
        description: str = None,
        service_region: str = None,
        connection_bandwidth: int = None,
        business_status: str = None,
        name: str = None,
    ):
        self.status = status
        self.uis_id = uis_id
        self.connection_type = connection_type
        self.bandwidth_type = bandwidth_type
        self.create_time = create_time
        self.charge_type = charge_type
        self.pay_type = pay_type
        self.user_info = user_info
        self.ssl_client_cert_url = ssl_client_cert_url
        self.connection_count = connection_count
        self.uis_node_ids = uis_node_ids
        self.end_time = end_time
        self.bandwidth = bandwidth
        self.description = description
        self.service_region = service_region
        self.connection_bandwidth = connection_bandwidth
        self.business_status = business_status
        self.name = name

    def validate(self):
        if self.user_info:
            self.user_info.validate()
        if self.uis_node_ids:
            self.uis_node_ids.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.ssl_client_cert_url is not None:
            result['SslClientCertUrl'] = self.ssl_client_cert_url
        if self.connection_count is not None:
            result['ConnectionCount'] = self.connection_count
        if self.uis_node_ids is not None:
            result['UisNodeIds'] = self.uis_node_ids.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.service_region is not None:
            result['ServiceRegion'] = self.service_region
        if self.connection_bandwidth is not None:
            result['ConnectionBandwidth'] = self.connection_bandwidth
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('UserInfo') is not None:
            temp_model = DescribeUisesResponseBodyUisesUisUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('SslClientCertUrl') is not None:
            self.ssl_client_cert_url = m.get('SslClientCertUrl')
        if m.get('ConnectionCount') is not None:
            self.connection_count = m.get('ConnectionCount')
        if m.get('UisNodeIds') is not None:
            temp_model = DescribeUisesResponseBodyUisesUisUisNodeIds()
            self.uis_node_ids = temp_model.from_map(m['UisNodeIds'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceRegion') is not None:
            self.service_region = m.get('ServiceRegion')
        if m.get('ConnectionBandwidth') is not None:
            self.connection_bandwidth = m.get('ConnectionBandwidth')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeUisesResponseBodyUises(TeaModel):
    def __init__(
        self,
        uis: List[DescribeUisesResponseBodyUisesUis] = None,
    ):
        self.uis = uis

    def validate(self):
        if self.uis:
            for k in self.uis:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Uis'] = []
        if self.uis is not None:
            for k in self.uis:
                result['Uis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.uis = []
        if m.get('Uis') is not None:
            for k in m.get('Uis'):
                temp_model = DescribeUisesResponseBodyUisesUis()
                self.uis.append(temp_model.from_map(k))
        return self


class DescribeUisesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        uises: DescribeUisesResponseBodyUises = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.uises = uises
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.uises:
            self.uises.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.uises is not None:
            result['Uises'] = self.uises.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Uises') is not None:
            temp_model = DescribeUisesResponseBodyUises()
            self.uises = temp_model.from_map(m['Uises'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeUisesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUisesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUisesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUisNetworkInterfacesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_node_id: str = None,
        uis_eni_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.uis_eni_id = uis_eni_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_eni_id is not None:
            result['UisEniId'] = self.uis_eni_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisEniId') is not None:
            self.uis_eni_id = m.get('UisEniId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeUisNetworkInterfacesResponseBodyNetworkInterfacesNetworkInterface(TeaModel):
    def __init__(
        self,
        uis_eni_id: str = None,
        uis_node_id: str = None,
        ip_address: str = None,
        description: str = None,
        vswitch_id: str = None,
        state: str = None,
        security_group_id: str = None,
        network_interface_id: str = None,
        name: str = None,
        log: str = None,
    ):
        self.uis_eni_id = uis_eni_id
        self.uis_node_id = uis_node_id
        self.ip_address = ip_address
        self.description = description
        self.vswitch_id = vswitch_id
        self.state = state
        self.security_group_id = security_group_id
        self.network_interface_id = network_interface_id
        self.name = name
        self.log = log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uis_eni_id is not None:
            result['UisEniId'] = self.uis_eni_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.description is not None:
            result['Description'] = self.description
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.state is not None:
            result['State'] = self.state
        if self.security_group_id is not None:
            result['SecurityGroupID'] = self.security_group_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.name is not None:
            result['Name'] = self.name
        if self.log is not None:
            result['Log'] = self.log
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UisEniId') is not None:
            self.uis_eni_id = m.get('UisEniId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SecurityGroupID') is not None:
            self.security_group_id = m.get('SecurityGroupID')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Log') is not None:
            self.log = m.get('Log')
        return self


class DescribeUisNetworkInterfacesResponseBodyNetworkInterfaces(TeaModel):
    def __init__(
        self,
        network_interface: List[DescribeUisNetworkInterfacesResponseBodyNetworkInterfacesNetworkInterface] = None,
    ):
        self.network_interface = network_interface

    def validate(self):
        if self.network_interface:
            for k in self.network_interface:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NetworkInterface'] = []
        if self.network_interface is not None:
            for k in self.network_interface:
                result['NetworkInterface'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface = []
        if m.get('NetworkInterface') is not None:
            for k in m.get('NetworkInterface'):
                temp_model = DescribeUisNetworkInterfacesResponseBodyNetworkInterfacesNetworkInterface()
                self.network_interface.append(temp_model.from_map(k))
        return self


class DescribeUisNetworkInterfacesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        network_interfaces: DescribeUisNetworkInterfacesResponseBodyNetworkInterfaces = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.network_interfaces = network_interfaces

    def validate(self):
        if self.network_interfaces:
            self.network_interfaces.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.network_interfaces is not None:
            result['NetworkInterfaces'] = self.network_interfaces.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('NetworkInterfaces') is not None:
            temp_model = DescribeUisNetworkInterfacesResponseBodyNetworkInterfaces()
            self.network_interfaces = temp_model.from_map(m['NetworkInterfaces'])
        return self


class DescribeUisNetworkInterfacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUisNetworkInterfacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUisNetworkInterfacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUisNodesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_id: str = None,
        uis_node_id: str = None,
        name: str = None,
        status: str = None,
        page_number: int = None,
        page_size: int = None,
        client_token: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_id = uis_id
        self.uis_node_id = uis_node_id
        self.name = name
        self.status = status
        self.page_number = page_number
        self.page_size = page_size
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeUisNodesResponseBodyUisNodeListUisNode(TeaModel):
    def __init__(
        self,
        status: str = None,
        uis_id: str = None,
        uis_node_active_ip: str = None,
        create_time: int = None,
        uis_eni_ips: str = None,
        uis_node_area_id: str = None,
        uis_node_id: str = None,
        uis_node_ips: str = None,
        description: str = None,
        uis_node_bandwidth: int = None,
        ip_addrs_num: int = None,
        name: str = None,
    ):
        self.status = status
        self.uis_id = uis_id
        self.uis_node_active_ip = uis_node_active_ip
        self.create_time = create_time
        self.uis_eni_ips = uis_eni_ips
        self.uis_node_area_id = uis_node_area_id
        self.uis_node_id = uis_node_id
        self.uis_node_ips = uis_node_ips
        self.description = description
        self.uis_node_bandwidth = uis_node_bandwidth
        self.ip_addrs_num = ip_addrs_num
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_node_active_ip is not None:
            result['UisNodeActiveIp'] = self.uis_node_active_ip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.uis_eni_ips is not None:
            result['UisEniIps'] = self.uis_eni_ips
        if self.uis_node_area_id is not None:
            result['UisNodeAreaId'] = self.uis_node_area_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_node_ips is not None:
            result['UisNodeIps'] = self.uis_node_ips
        if self.description is not None:
            result['Description'] = self.description
        if self.uis_node_bandwidth is not None:
            result['UisNodeBandwidth'] = self.uis_node_bandwidth
        if self.ip_addrs_num is not None:
            result['IpAddrsNum'] = self.ip_addrs_num
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodeActiveIp') is not None:
            self.uis_node_active_ip = m.get('UisNodeActiveIp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UisEniIps') is not None:
            self.uis_eni_ips = m.get('UisEniIps')
        if m.get('UisNodeAreaId') is not None:
            self.uis_node_area_id = m.get('UisNodeAreaId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisNodeIps') is not None:
            self.uis_node_ips = m.get('UisNodeIps')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UisNodeBandwidth') is not None:
            self.uis_node_bandwidth = m.get('UisNodeBandwidth')
        if m.get('IpAddrsNum') is not None:
            self.ip_addrs_num = m.get('IpAddrsNum')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeUisNodesResponseBodyUisNodeList(TeaModel):
    def __init__(
        self,
        uis_node: List[DescribeUisNodesResponseBodyUisNodeListUisNode] = None,
    ):
        self.uis_node = uis_node

    def validate(self):
        if self.uis_node:
            for k in self.uis_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UisNode'] = []
        if self.uis_node is not None:
            for k in self.uis_node:
                result['UisNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.uis_node = []
        if m.get('UisNode') is not None:
            for k in m.get('UisNode'):
                temp_model = DescribeUisNodesResponseBodyUisNodeListUisNode()
                self.uis_node.append(temp_model.from_map(k))
        return self


class DescribeUisNodesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        uis_node_list: DescribeUisNodesResponseBodyUisNodeList = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.uis_node_list = uis_node_list

    def validate(self):
        if self.uis_node_list:
            self.uis_node_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.uis_node_list is not None:
            result['UisNodeList'] = self.uis_node_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UisNodeList') is not None:
            temp_model = DescribeUisNodesResponseBodyUisNodeList()
            self.uis_node_list = temp_model.from_map(m['UisNodeList'])
        return self


class DescribeUisNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUisNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUisNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhiteListRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_id: str = None,
        client_token: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_id = uis_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        whitelist: str = None,
    ):
        self.request_id = request_id
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class DescribeWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDroppedIpListRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_id: str = None,
        chart_date: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_id = uis_id
        self.chart_date = chart_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.chart_date is not None:
            result['ChartDate'] = self.chart_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('ChartDate') is not None:
            self.chart_date = m.get('ChartDate')
        return self


class GetDroppedIpListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dropped_ip_list_url: str = None,
    ):
        self.request_id = request_id
        self.dropped_ip_list_url = dropped_ip_list_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dropped_ip_list_url is not None:
            result['DroppedIpListUrl'] = self.dropped_ip_list_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DroppedIpListUrl') is not None:
            self.dropped_ip_list_url = m.get('DroppedIpListUrl')
        return self


class GetDroppedIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDroppedIpListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDroppedIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDnatEntryRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_node_id: str = None,
        uis_dnat_id: str = None,
        destination_ip: str = None,
        destination_port: int = None,
        original_ip: str = None,
        original_port: int = None,
        ip_protocol: str = None,
        name: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.uis_dnat_id = uis_dnat_id
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.original_ip = original_ip
        self.original_port = original_port
        self.ip_protocol = ip_protocol
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_dnat_id is not None:
            result['UisDnatId'] = self.uis_dnat_id
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
        if self.original_ip is not None:
            result['OriginalIp'] = self.original_ip
        if self.original_port is not None:
            result['OriginalPort'] = self.original_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisDnatId') is not None:
            self.uis_dnat_id = m.get('UisDnatId')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
        if m.get('OriginalIp') is not None:
            self.original_ip = m.get('OriginalIp')
        if m.get('OriginalPort') is not None:
            self.original_port = m.get('OriginalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyDnatEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDnatEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDnatEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDnatEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHighPriorityIpRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        client_token: str = None,
        uis_id: str = None,
        high_priority_ip: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.client_token = client_token
        self.uis_id = uis_id
        self.high_priority_ip = high_priority_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.high_priority_ip is not None:
            result['HighPriorityIp'] = self.high_priority_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('HighPriorityIp') is not None:
            self.high_priority_ip = m.get('HighPriorityIp')
        return self


class ModifyHighPriorityIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHighPriorityIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHighPriorityIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHighPriorityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubConnectionRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uis_sub_connection_id: str = None,
        description: str = None,
        name: str = None,
        gre_config: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uis_sub_connection_id = uis_sub_connection_id
        self.description = description
        self.name = name
        self.gre_config = gre_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uis_sub_connection_id is not None:
            result['UisSubConnectionId'] = self.uis_sub_connection_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.gre_config is not None:
            result['GreConfig'] = self.gre_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UisSubConnectionId') is not None:
            self.uis_sub_connection_id = m.get('UisSubConnectionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GreConfig') is not None:
            self.gre_config = m.get('GreConfig')
        return self


class ModifySubConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifySubConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySubConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySubConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUisAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        uis_id: str = None,
        name: str = None,
        description: str = None,
        region_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.uis_id = uis_id
        self.name = name
        self.description = description
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyUisAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUisAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUisAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUisAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUisConnectionAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_node_id: str = None,
        uis_connection_id: str = None,
        uis_protocol: str = None,
        description: str = None,
        name: str = None,
        gre_config: str = None,
        ssl_config: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_node_id = uis_node_id
        self.uis_connection_id = uis_connection_id
        self.uis_protocol = uis_protocol
        self.description = description
        self.name = name
        self.gre_config = gre_config
        self.ssl_config = ssl_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.uis_connection_id is not None:
            result['UisConnectionId'] = self.uis_connection_id
        if self.uis_protocol is not None:
            result['UisProtocol'] = self.uis_protocol
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.gre_config is not None:
            result['GreConfig'] = self.gre_config
        if self.ssl_config is not None:
            result['SslConfig'] = self.ssl_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('UisConnectionId') is not None:
            self.uis_connection_id = m.get('UisConnectionId')
        if m.get('UisProtocol') is not None:
            self.uis_protocol = m.get('UisProtocol')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GreConfig') is not None:
            self.gre_config = m.get('GreConfig')
        if m.get('SslConfig') is not None:
            self.ssl_config = m.get('SslConfig')
        return self


class ModifyUisConnectionAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUisConnectionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUisConnectionAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUisConnectionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUisNodeAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        uis_id: str = None,
        uis_node_id: str = None,
        name: str = None,
        description: str = None,
        uis_node_bandwidth: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.uis_id = uis_id
        self.uis_node_id = uis_node_id
        self.name = name
        self.description = description
        self.uis_node_bandwidth = uis_node_bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.uis_node_bandwidth is not None:
            result['UisNodeBandwidth'] = self.uis_node_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UisNodeBandwidth') is not None:
            self.uis_node_bandwidth = m.get('UisNodeBandwidth')
        return self


class ModifyUisNodeAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUisNodeAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUisNodeAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUisNodeAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWhiteListRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        client_token: str = None,
        uis_id: str = None,
        whitelist: str = None,
        modify_mode: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.client_token = client_token
        self.uis_id = uis_id
        self.whitelist = whitelist
        self.modify_mode = modify_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        return self


class ModifyWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


