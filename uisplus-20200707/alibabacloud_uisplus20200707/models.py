# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AssociateEipRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        network_mode: str = None,
        region_id: str = None,
        resource_mode: str = None,
        role: str = None,
        type: str = None,
        uis_id: str = None,
        uis_node_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.network_mode = network_mode
        self.region_id = region_id
        self.resource_mode = resource_mode
        self.role = role
        self.type = type
        self.uis_id = uis_id
        self.uis_node_id = uis_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        return self


class AssociateEipResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateEipResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateEipResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = AssociateEipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGreConnectionRequest(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        client_token: str = None,
        customer_ip: str = None,
        customer_tunnel_ip: str = None,
        description: str = None,
        local_ip: str = None,
        local_tunnel_ip: str = None,
        name: str = None,
        region_id: str = None,
        resource_mode: str = None,
        uis_id: str = None,
    ):
        self.cidrs = cidrs
        self.client_token = client_token
        self.customer_ip = customer_ip
        self.customer_tunnel_ip = customer_tunnel_ip
        self.description = description
        self.local_ip = local_ip
        self.local_tunnel_ip = local_tunnel_ip
        self.name = name
        self.region_id = region_id
        self.resource_mode = resource_mode
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.customer_ip is not None:
            result['CustomerIp'] = self.customer_ip
        if self.customer_tunnel_ip is not None:
            result['CustomerTunnelIp'] = self.customer_tunnel_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.local_ip is not None:
            result['LocalIp'] = self.local_ip
        if self.local_tunnel_ip is not None:
            result['LocalTunnelIp'] = self.local_tunnel_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CustomerIp') is not None:
            self.customer_ip = m.get('CustomerIp')
        if m.get('CustomerTunnelIp') is not None:
            self.customer_tunnel_ip = m.get('CustomerTunnelIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocalIp') is not None:
            self.local_ip = m.get('LocalIp')
        if m.get('LocalTunnelIp') is not None:
            self.local_tunnel_ip = m.get('LocalTunnelIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class CreateGreConnectionResponseBody(TeaModel):
    def __init__(
        self,
        gre_connection_id: str = None,
        request_id: str = None,
    ):
        self.gre_connection_id = gre_connection_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gre_connection_id is not None:
            result['GreConnectionId'] = self.gre_connection_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreConnectionId') is not None:
            self.gre_connection_id = m.get('GreConnectionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGreConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGreConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateGreConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUisRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        network_mode: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_mode: str = None,
        singleton_count: int = None,
        spec: str = None,
        uis_name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.network_mode = network_mode
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_mode = resource_mode
        self.singleton_count = singleton_count
        self.spec = spec
        self.uis_name = uis_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.singleton_count is not None:
            result['SingletonCount'] = self.singleton_count
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.uis_name is not None:
            result['UisName'] = self.uis_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('SingletonCount') is not None:
            self.singleton_count = m.get('SingletonCount')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('UisName') is not None:
            self.uis_name = m.get('UisName')
        return self


class CreateUisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        uis_id: str = None,
        uis_nodes: List[str] = None,
    ):
        self.request_id = request_id
        self.uis_id = uis_id
        self.uis_nodes = uis_nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_nodes is not None:
            result['UisNodes'] = self.uis_nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodes') is not None:
            self.uis_nodes = m.get('UisNodes')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateVnetRequest(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        client_token: str = None,
        flow_quota: int = None,
        kpps_quota: int = None,
        mbps_quota: int = None,
        name: str = None,
        region_id: str = None,
        uis_id: str = None,
    ):
        self.cidrs = cidrs
        self.client_token = client_token
        self.flow_quota = flow_quota
        self.kpps_quota = kpps_quota
        self.mbps_quota = mbps_quota
        self.name = name
        self.region_id = region_id
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.flow_quota is not None:
            result['FlowQuota'] = self.flow_quota
        if self.kpps_quota is not None:
            result['KppsQuota'] = self.kpps_quota
        if self.mbps_quota is not None:
            result['MbpsQuota'] = self.mbps_quota
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FlowQuota') is not None:
            self.flow_quota = m.get('FlowQuota')
        if m.get('KppsQuota') is not None:
            self.kpps_quota = m.get('KppsQuota')
        if m.get('MbpsQuota') is not None:
            self.mbps_quota = m.get('MbpsQuota')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class CreateVnetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vnet_id: str = None,
    ):
        self.request_id = request_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class CreateVnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVnetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateVnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVnetRouteEntryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        destination: str = None,
        nexthop: str = None,
        nexthop_type: str = None,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.client_token = client_token
        self.destination = destination
        self.nexthop = nexthop
        self.nexthop_type = nexthop_type
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.nexthop is not None:
            result['Nexthop'] = self.nexthop
        if self.nexthop_type is not None:
            result['NexthopType'] = self.nexthop_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Nexthop') is not None:
            self.nexthop = m.get('Nexthop')
        if m.get('NexthopType') is not None:
            self.nexthop_type = m.get('NexthopType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class CreateVnetRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVnetRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVnetRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateVnetRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGreConnectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        gre_connection_id: str = None,
        region_id: str = None,
        resource_mode: str = None,
        uis_id: str = None,
    ):
        self.client_token = client_token
        self.gre_connection_id = gre_connection_id
        self.region_id = region_id
        self.resource_mode = resource_mode
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.gre_connection_id is not None:
            result['GreConnectionId'] = self.gre_connection_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GreConnectionId') is not None:
            self.gre_connection_id = m.get('GreConnectionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class DeleteGreConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGreConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGreConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteGreConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUisRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        resource_mode: str = None,
        uis_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.resource_mode = resource_mode
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DeleteVnetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class DeleteVnetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVnetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteVnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVnetRouteEntryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        destination: str = None,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.client_token = client_token
        self.destination = destination
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class DeleteVnetRouteEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVnetRouteEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVnetRouteEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeleteVnetRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGreConnectionRequest(TeaModel):
    def __init__(
        self,
        gre_connection_id: str = None,
        region_id: str = None,
        uis_id: str = None,
    ):
        self.gre_connection_id = gre_connection_id
        self.region_id = region_id
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gre_connection_id is not None:
            result['GreConnectionId'] = self.gre_connection_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GreConnectionId') is not None:
            self.gre_connection_id = m.get('GreConnectionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class DescribeGreConnectionResponseBody(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        create_time: int = None,
        customer_ip: str = None,
        customer_tunnel_ip: str = None,
        description: str = None,
        gre_connection_id: str = None,
        local_ip: str = None,
        local_tunnel_ip: str = None,
        name: str = None,
        request_id: str = None,
        state: str = None,
        uis_id: str = None,
        uis_name: str = None,
    ):
        self.cidrs = cidrs
        self.create_time = create_time
        self.customer_ip = customer_ip
        self.customer_tunnel_ip = customer_tunnel_ip
        self.description = description
        self.gre_connection_id = gre_connection_id
        self.local_ip = local_ip
        self.local_tunnel_ip = local_tunnel_ip
        self.name = name
        self.request_id = request_id
        self.state = state
        self.uis_id = uis_id
        self.uis_name = uis_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.customer_ip is not None:
            result['CustomerIp'] = self.customer_ip
        if self.customer_tunnel_ip is not None:
            result['CustomerTunnelIp'] = self.customer_tunnel_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.gre_connection_id is not None:
            result['GreConnectionId'] = self.gre_connection_id
        if self.local_ip is not None:
            result['LocalIp'] = self.local_ip
        if self.local_tunnel_ip is not None:
            result['LocalTunnelIp'] = self.local_tunnel_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_name is not None:
            result['UisName'] = self.uis_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomerIp') is not None:
            self.customer_ip = m.get('CustomerIp')
        if m.get('CustomerTunnelIp') is not None:
            self.customer_tunnel_ip = m.get('CustomerTunnelIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GreConnectionId') is not None:
            self.gre_connection_id = m.get('GreConnectionId')
        if m.get('LocalIp') is not None:
            self.local_ip = m.get('LocalIp')
        if m.get('LocalTunnelIp') is not None:
            self.local_tunnel_ip = m.get('LocalTunnelIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisName') is not None:
            self.uis_name = m.get('UisName')
        return self


class DescribeGreConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGreConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeGreConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGreConnectionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        uis_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class DescribeGreConnectionsResponseBodyGreConnections(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        create_time: int = None,
        customer_ip: str = None,
        customer_tunnel_ip: str = None,
        description: str = None,
        gre_connection_id: str = None,
        local_ip: str = None,
        local_tunnel_ip: str = None,
        name: str = None,
        state: str = None,
    ):
        self.cidrs = cidrs
        self.create_time = create_time
        self.customer_ip = customer_ip
        self.customer_tunnel_ip = customer_tunnel_ip
        self.description = description
        self.gre_connection_id = gre_connection_id
        self.local_ip = local_ip
        self.local_tunnel_ip = local_tunnel_ip
        self.name = name
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.customer_ip is not None:
            result['CustomerIp'] = self.customer_ip
        if self.customer_tunnel_ip is not None:
            result['CustomerTunnelIp'] = self.customer_tunnel_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.gre_connection_id is not None:
            result['GreConnectionId'] = self.gre_connection_id
        if self.local_ip is not None:
            result['LocalIp'] = self.local_ip
        if self.local_tunnel_ip is not None:
            result['LocalTunnelIp'] = self.local_tunnel_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomerIp') is not None:
            self.customer_ip = m.get('CustomerIp')
        if m.get('CustomerTunnelIp') is not None:
            self.customer_tunnel_ip = m.get('CustomerTunnelIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GreConnectionId') is not None:
            self.gre_connection_id = m.get('GreConnectionId')
        if m.get('LocalIp') is not None:
            self.local_ip = m.get('LocalIp')
        if m.get('LocalTunnelIp') is not None:
            self.local_tunnel_ip = m.get('LocalTunnelIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeGreConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        gre_connections: List[DescribeGreConnectionsResponseBodyGreConnections] = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        state: str = None,
        total_count: int = None,
        uis_id: str = None,
        uis_name: str = None,
    ):
        self.gre_connections = gre_connections
        self.page = page
        self.page_size = page_size
        self.request_id = request_id
        self.state = state
        self.total_count = total_count
        self.uis_id = uis_id
        self.uis_name = uis_name

    def validate(self):
        if self.gre_connections:
            for k in self.gre_connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GreConnections'] = []
        if self.gre_connections is not None:
            for k in self.gre_connections:
                result['GreConnections'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_name is not None:
            result['UisName'] = self.uis_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gre_connections = []
        if m.get('GreConnections') is not None:
            for k in m.get('GreConnections'):
                temp_model = DescribeGreConnectionsResponseBodyGreConnections()
                self.gre_connections.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisName') is not None:
            self.uis_name = m.get('UisName')
        return self


class DescribeGreConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGreConnectionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeGreConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUisRequest(TeaModel):
    def __init__(
        self,
        uis_id: str = None,
    ):
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class DescribeUisResponseBodyInternetIps(TeaModel):
    def __init__(
        self,
        eip_id: str = None,
        ip: str = None,
        role: str = None,
        type: str = None,
        uis_node_id: str = None,
    ):
        self.eip_id = eip_id
        self.ip = ip
        self.role = role
        self.type = type
        self.uis_node_id = uis_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_id is not None:
            result['EipId'] = self.eip_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        return self


class DescribeUisResponseBody(TeaModel):
    def __init__(
        self,
        flow_quota: int = None,
        internet_ips: List[DescribeUisResponseBodyInternetIps] = None,
        kpps_quota: int = None,
        mbps_quota: int = None,
        network_mode: str = None,
        region_id: str = None,
        request_id: str = None,
        spec: str = None,
        state: str = None,
        uis_id: str = None,
        uis_name: str = None,
        uis_nodes: List[str] = None,
        used_flow_quota: int = None,
        used_kpps_quota: int = None,
        used_mbps_quota: int = None,
        wildcard_domain_state: str = None,
    ):
        self.flow_quota = flow_quota
        self.internet_ips = internet_ips
        self.kpps_quota = kpps_quota
        self.mbps_quota = mbps_quota
        self.network_mode = network_mode
        self.region_id = region_id
        self.request_id = request_id
        self.spec = spec
        self.state = state
        self.uis_id = uis_id
        self.uis_name = uis_name
        self.uis_nodes = uis_nodes
        self.used_flow_quota = used_flow_quota
        self.used_kpps_quota = used_kpps_quota
        self.used_mbps_quota = used_mbps_quota
        self.wildcard_domain_state = wildcard_domain_state

    def validate(self):
        if self.internet_ips:
            for k in self.internet_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_quota is not None:
            result['FlowQuota'] = self.flow_quota
        result['InternetIps'] = []
        if self.internet_ips is not None:
            for k in self.internet_ips:
                result['InternetIps'].append(k.to_map() if k else None)
        if self.kpps_quota is not None:
            result['KppsQuota'] = self.kpps_quota
        if self.mbps_quota is not None:
            result['MbpsQuota'] = self.mbps_quota
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_name is not None:
            result['UisName'] = self.uis_name
        if self.uis_nodes is not None:
            result['UisNodes'] = self.uis_nodes
        if self.used_flow_quota is not None:
            result['UsedFlowQuota'] = self.used_flow_quota
        if self.used_kpps_quota is not None:
            result['UsedKPpsQuota'] = self.used_kpps_quota
        if self.used_mbps_quota is not None:
            result['UsedMBpsQuota'] = self.used_mbps_quota
        if self.wildcard_domain_state is not None:
            result['WildcardDomainState'] = self.wildcard_domain_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowQuota') is not None:
            self.flow_quota = m.get('FlowQuota')
        self.internet_ips = []
        if m.get('InternetIps') is not None:
            for k in m.get('InternetIps'):
                temp_model = DescribeUisResponseBodyInternetIps()
                self.internet_ips.append(temp_model.from_map(k))
        if m.get('KppsQuota') is not None:
            self.kpps_quota = m.get('KppsQuota')
        if m.get('MbpsQuota') is not None:
            self.mbps_quota = m.get('MbpsQuota')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisName') is not None:
            self.uis_name = m.get('UisName')
        if m.get('UisNodes') is not None:
            self.uis_nodes = m.get('UisNodes')
        if m.get('UsedFlowQuota') is not None:
            self.used_flow_quota = m.get('UsedFlowQuota')
        if m.get('UsedKPpsQuota') is not None:
            self.used_kpps_quota = m.get('UsedKPpsQuota')
        if m.get('UsedMBpsQuota') is not None:
            self.used_mbps_quota = m.get('UsedMBpsQuota')
        if m.get('WildcardDomainState') is not None:
            self.wildcard_domain_state = m.get('WildcardDomainState')
        return self


class DescribeUisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeUisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUissRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUissResponseBodyUiss(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        flow_quota: int = None,
        kpps_quota: int = None,
        mbps_quota: int = None,
        network_mode: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        state: str = None,
        uis_id: str = None,
        uis_name: str = None,
        used_flow_quota: int = None,
        used_kpps_quota: int = None,
        used_mbps_quota: int = None,
        wildcard_domain_state: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.flow_quota = flow_quota
        self.kpps_quota = kpps_quota
        self.mbps_quota = mbps_quota
        self.network_mode = network_mode
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.spec = spec
        self.state = state
        self.uis_id = uis_id
        self.uis_name = uis_name
        self.used_flow_quota = used_flow_quota
        self.used_kpps_quota = used_kpps_quota
        self.used_mbps_quota = used_mbps_quota
        self.wildcard_domain_state = wildcard_domain_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_quota is not None:
            result['FlowQuota'] = self.flow_quota
        if self.kpps_quota is not None:
            result['KppsQuota'] = self.kpps_quota
        if self.mbps_quota is not None:
            result['MbpsQuota'] = self.mbps_quota
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_name is not None:
            result['UisName'] = self.uis_name
        if self.used_flow_quota is not None:
            result['UsedFlowQuota'] = self.used_flow_quota
        if self.used_kpps_quota is not None:
            result['UsedKPpsQuota'] = self.used_kpps_quota
        if self.used_mbps_quota is not None:
            result['UsedMBpsQuota'] = self.used_mbps_quota
        if self.wildcard_domain_state is not None:
            result['WildcardDomainState'] = self.wildcard_domain_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowQuota') is not None:
            self.flow_quota = m.get('FlowQuota')
        if m.get('KppsQuota') is not None:
            self.kpps_quota = m.get('KppsQuota')
        if m.get('MbpsQuota') is not None:
            self.mbps_quota = m.get('MbpsQuota')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisName') is not None:
            self.uis_name = m.get('UisName')
        if m.get('UsedFlowQuota') is not None:
            self.used_flow_quota = m.get('UsedFlowQuota')
        if m.get('UsedKPpsQuota') is not None:
            self.used_kpps_quota = m.get('UsedKPpsQuota')
        if m.get('UsedMBpsQuota') is not None:
            self.used_mbps_quota = m.get('UsedMBpsQuota')
        if m.get('WildcardDomainState') is not None:
            self.wildcard_domain_state = m.get('WildcardDomainState')
        return self


class DescribeUissResponseBody(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        uiss: List[DescribeUissResponseBodyUiss] = None,
    ):
        self.page = page
        self.page_size = page_size
        self.request_id = request_id
        self.uiss = uiss

    def validate(self):
        if self.uiss:
            for k in self.uiss:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Uiss'] = []
        if self.uiss is not None:
            for k in self.uiss:
                result['Uiss'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.uiss = []
        if m.get('Uiss') is not None:
            for k in m.get('Uiss'):
                temp_model = DescribeUissResponseBodyUiss()
                self.uiss.append(temp_model.from_map(k))
        return self


class DescribeUissResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUissResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeUissResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVnetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class DescribeVnetResponseBody(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        flow_quota: str = None,
        kpps_quota: str = None,
        mbps_quota: str = None,
        name: str = None,
        request_id: str = None,
        state: str = None,
        uis_id: str = None,
        vnet_id: str = None,
        wildcard_domain_state: str = None,
    ):
        self.cidrs = cidrs
        self.flow_quota = flow_quota
        self.kpps_quota = kpps_quota
        self.mbps_quota = mbps_quota
        self.name = name
        self.request_id = request_id
        self.state = state
        self.uis_id = uis_id
        self.vnet_id = vnet_id
        self.wildcard_domain_state = wildcard_domain_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.flow_quota is not None:
            result['FlowQuota'] = self.flow_quota
        if self.kpps_quota is not None:
            result['KppsQuota'] = self.kpps_quota
        if self.mbps_quota is not None:
            result['MbpsQuota'] = self.mbps_quota
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        if self.wildcard_domain_state is not None:
            result['WildcardDomainState'] = self.wildcard_domain_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('FlowQuota') is not None:
            self.flow_quota = m.get('FlowQuota')
        if m.get('KppsQuota') is not None:
            self.kpps_quota = m.get('KppsQuota')
        if m.get('MbpsQuota') is not None:
            self.mbps_quota = m.get('MbpsQuota')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        if m.get('WildcardDomainState') is not None:
            self.wildcard_domain_state = m.get('WildcardDomainState')
        return self


class DescribeVnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVnetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeVnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVnetRouteEntryListRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class DescribeVnetRouteEntryListResponseBodyVnets(TeaModel):
    def __init__(
        self,
        destination: str = None,
        nexthop: str = None,
        nexthop_type: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.destination = destination
        self.nexthop = nexthop
        self.nexthop_type = nexthop_type
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.nexthop is not None:
            result['Nexthop'] = self.nexthop
        if self.nexthop_type is not None:
            result['NexthopType'] = self.nexthop_type
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Nexthop') is not None:
            self.nexthop = m.get('Nexthop')
        if m.get('NexthopType') is not None:
            self.nexthop_type = m.get('NexthopType')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class DescribeVnetRouteEntryListResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vnets: List[DescribeVnetRouteEntryListResponseBodyVnets] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vnets = vnets

    def validate(self):
        if self.vnets:
            for k in self.vnets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vnets'] = []
        if self.vnets is not None:
            for k in self.vnets:
                result['Vnets'].append(k.to_map() if k else None)
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
        self.vnets = []
        if m.get('Vnets') is not None:
            for k in m.get('Vnets'):
                temp_model = DescribeVnetRouteEntryListResponseBodyVnets()
                self.vnets.append(temp_model.from_map(k))
        return self


class DescribeVnetRouteEntryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVnetRouteEntryListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeVnetRouteEntryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVnetsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: List[str] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class DescribeVnetsResponseBodyVnets(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        flow_quota: int = None,
        kpps_quota: int = None,
        mbps_quota: int = None,
        name: str = None,
        state: str = None,
        uis_id: str = None,
        vnet_id: str = None,
        wildcard_domain_state: str = None,
    ):
        self.cidrs = cidrs
        self.flow_quota = flow_quota
        self.kpps_quota = kpps_quota
        self.mbps_quota = mbps_quota
        self.name = name
        self.state = state
        self.uis_id = uis_id
        self.vnet_id = vnet_id
        self.wildcard_domain_state = wildcard_domain_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.flow_quota is not None:
            result['FlowQuota'] = self.flow_quota
        if self.kpps_quota is not None:
            result['KppsQuota'] = self.kpps_quota
        if self.mbps_quota is not None:
            result['MbpsQuota'] = self.mbps_quota
        if self.name is not None:
            result['Name'] = self.name
        if self.state is not None:
            result['State'] = self.state
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        if self.wildcard_domain_state is not None:
            result['WildcardDomainState'] = self.wildcard_domain_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('FlowQuota') is not None:
            self.flow_quota = m.get('FlowQuota')
        if m.get('KppsQuota') is not None:
            self.kpps_quota = m.get('KppsQuota')
        if m.get('MbpsQuota') is not None:
            self.mbps_quota = m.get('MbpsQuota')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        if m.get('WildcardDomainState') is not None:
            self.wildcard_domain_state = m.get('WildcardDomainState')
        return self


class DescribeVnetsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vnets: List[DescribeVnetsResponseBodyVnets] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vnets = vnets

    def validate(self):
        if self.vnets:
            for k in self.vnets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vnets'] = []
        if self.vnets is not None:
            for k in self.vnets:
                result['Vnets'].append(k.to_map() if k else None)
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
        self.vnets = []
        if m.get('Vnets') is not None:
            for k in m.get('Vnets'):
                temp_model = DescribeVnetsResponseBodyVnets()
                self.vnets.append(temp_model.from_map(k))
        return self


class DescribeVnetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVnetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DescribeVnetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableUisWildcardDomainRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        uis_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class DisableUisWildcardDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableUisWildcardDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableUisWildcardDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DisableUisWildcardDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVnetWildcardDomainRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class DisableVnetWildcardDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableVnetWildcardDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableVnetWildcardDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DisableVnetWildcardDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableUisWildcardDomainRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        uis_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class EnableUisWildcardDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableUisWildcardDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableUisWildcardDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = EnableUisWildcardDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGreConnectionRequest(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        client_token: str = None,
        customer_ip: str = None,
        customer_tunnel_ip: str = None,
        description: str = None,
        gre_connection_id: str = None,
        local_ip: str = None,
        local_tunnel_ip: str = None,
        name: str = None,
        region_id: str = None,
        resource_mode: str = None,
        uis_id: str = None,
    ):
        self.cidrs = cidrs
        self.client_token = client_token
        self.customer_ip = customer_ip
        self.customer_tunnel_ip = customer_tunnel_ip
        self.description = description
        self.gre_connection_id = gre_connection_id
        self.local_ip = local_ip
        self.local_tunnel_ip = local_tunnel_ip
        self.name = name
        self.region_id = region_id
        self.resource_mode = resource_mode
        self.uis_id = uis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.customer_ip is not None:
            result['CustomerIp'] = self.customer_ip
        if self.customer_tunnel_ip is not None:
            result['CustomerTunnelIp'] = self.customer_tunnel_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.gre_connection_id is not None:
            result['GreConnectionId'] = self.gre_connection_id
        if self.local_ip is not None:
            result['LocalIp'] = self.local_ip
        if self.local_tunnel_ip is not None:
            result['LocalTunnelIp'] = self.local_tunnel_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CustomerIp') is not None:
            self.customer_ip = m.get('CustomerIp')
        if m.get('CustomerTunnelIp') is not None:
            self.customer_tunnel_ip = m.get('CustomerTunnelIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GreConnectionId') is not None:
            self.gre_connection_id = m.get('GreConnectionId')
        if m.get('LocalIp') is not None:
            self.local_ip = m.get('LocalIp')
        if m.get('LocalTunnelIp') is not None:
            self.local_tunnel_ip = m.get('LocalTunnelIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        return self


class ModifyGreConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyGreConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyGreConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ModifyGreConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVnetRequest(TeaModel):
    def __init__(
        self,
        cidrs: str = None,
        client_token: str = None,
        flow_quota: int = None,
        kpps_quota: int = None,
        mbps_quota: int = None,
        name: str = None,
        region_id: str = None,
        uis_id: str = None,
        vnet_id: str = None,
    ):
        self.cidrs = cidrs
        self.client_token = client_token
        self.flow_quota = flow_quota
        self.kpps_quota = kpps_quota
        self.mbps_quota = mbps_quota
        self.name = name
        self.region_id = region_id
        self.uis_id = uis_id
        self.vnet_id = vnet_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.flow_quota is not None:
            result['FlowQuota'] = self.flow_quota
        if self.kpps_quota is not None:
            result['KppsQuota'] = self.kpps_quota
        if self.mbps_quota is not None:
            result['MbpsQuota'] = self.mbps_quota
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.vnet_id is not None:
            result['VnetId'] = self.vnet_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FlowQuota') is not None:
            self.flow_quota = m.get('FlowQuota')
        if m.get('KppsQuota') is not None:
            self.kpps_quota = m.get('KppsQuota')
        if m.get('MbpsQuota') is not None:
            self.mbps_quota = m.get('MbpsQuota')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('VnetId') is not None:
            self.vnet_id = m.get('VnetId')
        return self


class ModifyVnetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVnetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ModifyVnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAssociateEipRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        network_mode: str = None,
        region_id: str = None,
        resource_mode: str = None,
        type: str = None,
        uis_id: str = None,
        uis_node_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.network_mode = network_mode
        self.region_id = region_id
        self.resource_mode = resource_mode
        self.type = type
        self.uis_id = uis_id
        self.uis_node_id = uis_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode
        if self.type is not None:
            result['Type'] = self.type
        if self.uis_id is not None:
            result['UisId'] = self.uis_id
        if self.uis_node_id is not None:
            result['UisNodeId'] = self.uis_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UisId') is not None:
            self.uis_id = m.get('UisId')
        if m.get('UisNodeId') is not None:
            self.uis_node_id = m.get('UisNodeId')
        return self


class UnAssociateEipResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnAssociateEipResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnAssociateEipResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UnAssociateEipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


