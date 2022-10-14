# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AttachAlbServerGroupsRequestAlbServerGroups(TeaModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
        weight: int = None,
    ):
        self.alb_server_group_id = alb_server_group_id
        self.port = port
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alb_server_group_id is not None:
            result['AlbServerGroupId'] = self.alb_server_group_id
        if self.port is not None:
            result['Port'] = self.port
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbServerGroupId') is not None:
            self.alb_server_group_id = m.get('AlbServerGroupId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class AttachAlbServerGroupsRequest(TeaModel):
    def __init__(
        self,
        alb_server_groups: List[AttachAlbServerGroupsRequestAlbServerGroups] = None,
        client_token: str = None,
        force_attach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.alb_server_groups = alb_server_groups
        self.client_token = client_token
        self.force_attach = force_attach
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        if self.alb_server_groups:
            for k in self.alb_server_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlbServerGroups'] = []
        if self.alb_server_groups is not None:
            for k in self.alb_server_groups:
                result['AlbServerGroups'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_server_groups = []
        if m.get('AlbServerGroups') is not None:
            for k in m.get('AlbServerGroups'):
                temp_model = AttachAlbServerGroupsRequestAlbServerGroups()
                self.alb_server_groups.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class AttachAlbServerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class AttachAlbServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachAlbServerGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachAlbServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDBInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstances: List[str] = None,
        force_attach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.client_token = client_token
        self.dbinstances = dbinstances
        self.force_attach = force_attach
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances
        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')
        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class AttachDBInstancesResponseBody(TeaModel):
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


class AttachDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachDBInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachInstancesRequest(TeaModel):
    def __init__(
        self,
        entrusted: bool = None,
        instance_ids: List[str] = None,
        lifecycle_hook: bool = None,
        load_balancer_weights: List[int] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.entrusted = entrusted
        self.instance_ids = instance_ids
        self.lifecycle_hook = lifecycle_hook
        self.load_balancer_weights = load_balancer_weights
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entrusted is not None:
            result['Entrusted'] = self.entrusted
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.lifecycle_hook is not None:
            result['LifecycleHook'] = self.lifecycle_hook
        if self.load_balancer_weights is not None:
            result['LoadBalancerWeights'] = self.load_balancer_weights
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entrusted') is not None:
            self.entrusted = m.get('Entrusted')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('LifecycleHook') is not None:
            self.lifecycle_hook = m.get('LifecycleHook')
        if m.get('LoadBalancerWeights') is not None:
            self.load_balancer_weights = m.get('LoadBalancerWeights')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class AttachInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class AttachInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachLoadBalancersRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        client_token: str = None,
        force_attach: bool = None,
        load_balancers: List[str] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.async_ = async_
        self.client_token = client_token
        self.force_attach = force_attach
        self.load_balancers = load_balancers
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach
        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')
        if m.get('LoadBalancers') is not None:
            self.load_balancers = m.get('LoadBalancers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class AttachLoadBalancersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class AttachLoadBalancersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachLoadBalancersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachVServerGroupsRequestVServerGroupsVServerGroupAttributes(TeaModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
        weight: int = None,
    ):
        self.port = port
        self.vserver_group_id = vserver_group_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class AttachVServerGroupsRequestVServerGroups(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[AttachVServerGroupsRequestVServerGroupsVServerGroupAttributes] = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.vserver_group_attributes = vserver_group_attributes

    def validate(self):
        if self.vserver_group_attributes:
            for k in self.vserver_group_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        result['VServerGroupAttributes'] = []
        if self.vserver_group_attributes is not None:
            for k in self.vserver_group_attributes:
                result['VServerGroupAttributes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        self.vserver_group_attributes = []
        if m.get('VServerGroupAttributes') is not None:
            for k in m.get('VServerGroupAttributes'):
                temp_model = AttachVServerGroupsRequestVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k))
        return self


class AttachVServerGroupsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        force_attach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        vserver_groups: List[AttachVServerGroupsRequestVServerGroups] = None,
    ):
        self.client_token = client_token
        self.force_attach = force_attach
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id
        self.vserver_groups = vserver_groups

    def validate(self):
        if self.vserver_groups:
            for k in self.vserver_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_attach is not None:
            result['ForceAttach'] = self.force_attach
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        result['VServerGroups'] = []
        if self.vserver_groups is not None:
            for k in self.vserver_groups:
                result['VServerGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceAttach') is not None:
            self.force_attach = m.get('ForceAttach')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k in m.get('VServerGroups'):
                temp_model = AttachVServerGroupsRequestVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k))
        return self


class AttachVServerGroupsResponseBody(TeaModel):
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


class AttachVServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachVServerGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachVServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteLifecycleActionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        lifecycle_action_result: str = None,
        lifecycle_action_token: str = None,
        lifecycle_hook_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.client_token = client_token
        self.lifecycle_action_result = lifecycle_action_result
        self.lifecycle_action_token = lifecycle_action_token
        self.lifecycle_hook_id = lifecycle_hook_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lifecycle_action_result is not None:
            result['LifecycleActionResult'] = self.lifecycle_action_result
        if self.lifecycle_action_token is not None:
            result['LifecycleActionToken'] = self.lifecycle_action_token
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LifecycleActionResult') is not None:
            self.lifecycle_action_result = m.get('LifecycleActionResult')
        if m.get('LifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('LifecycleActionToken')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class CompleteLifecycleActionResponseBody(TeaModel):
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


class CompleteLifecycleActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompleteLifecycleActionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CompleteLifecycleActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmRequestDimensions(TeaModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        self.dimension_key = dimension_key
        self.dimension_value = dimension_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class CreateAlarmRequestExpressions(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.comparison_operator = comparison_operator
        self.metric_name = metric_name
        self.period = period
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.period is not None:
            result['Period'] = self.period
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class CreateAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_actions: List[str] = None,
        comparison_operator: str = None,
        description: str = None,
        dimensions: List[CreateAlarmRequestDimensions] = None,
        effective: str = None,
        evaluation_count: int = None,
        expressions: List[CreateAlarmRequestExpressions] = None,
        expressions_logic_operator: str = None,
        group_id: int = None,
        metric_name: str = None,
        metric_type: str = None,
        name: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.alarm_actions = alarm_actions
        self.comparison_operator = comparison_operator
        self.description = description
        self.dimensions = dimensions
        self.effective = effective
        self.evaluation_count = evaluation_count
        self.expressions = expressions
        self.expressions_logic_operator = expressions_logic_operator
        self.group_id = group_id
        self.metric_name = metric_name
        self.metric_type = metric_type
        self.name = name
        self.owner_id = owner_id
        self.period = period
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.expressions:
            for k in self.expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_actions is not None:
            result['AlarmActions'] = self.alarm_actions
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.description is not None:
            result['Description'] = self.description
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        result['Expressions'] = []
        if self.expressions is not None:
            for k in self.expressions:
                result['Expressions'].append(k.to_map() if k else None)
        if self.expressions_logic_operator is not None:
            result['ExpressionsLogicOperator'] = self.expressions_logic_operator
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmActions') is not None:
            self.alarm_actions = m.get('AlarmActions')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = CreateAlarmRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        self.expressions = []
        if m.get('Expressions') is not None:
            for k in m.get('Expressions'):
                temp_model = CreateAlarmRequestExpressions()
                self.expressions.append(temp_model.from_map(k))
        if m.get('ExpressionsLogicOperator') is not None:
            self.expressions_logic_operator = m.get('ExpressionsLogicOperator')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class CreateAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        request_id: str = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEciScalingConfigurationRequestAcrRegistryInfos(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.domains = domains
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEciScalingConfigurationRequestContainersLivenessProbeExec(TeaModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class CreateEciScalingConfigurationRequestContainersLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class CreateEciScalingConfigurationRequestContainersLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateEciScalingConfigurationRequestContainersLivenessProbe(TeaModel):
    def __init__(
        self,
        exec: CreateEciScalingConfigurationRequestContainersLivenessProbeExec = None,
        failure_threshold: int = None,
        http_get: CreateEciScalingConfigurationRequestContainersLivenessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: CreateEciScalingConfigurationRequestContainersLivenessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersLivenessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class CreateEciScalingConfigurationRequestContainersReadinessProbeExec(TeaModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class CreateEciScalingConfigurationRequestContainersReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class CreateEciScalingConfigurationRequestContainersReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class CreateEciScalingConfigurationRequestContainersReadinessProbe(TeaModel):
    def __init__(
        self,
        exec: CreateEciScalingConfigurationRequestContainersReadinessProbeExec = None,
        failure_threshold: int = None,
        http_get: CreateEciScalingConfigurationRequestContainersReadinessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: CreateEciScalingConfigurationRequestContainersReadinessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersReadinessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class CreateEciScalingConfigurationRequestContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
    ):
        self.add = add

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        return self


class CreateEciScalingConfigurationRequestContainersSecurityContext(TeaModel):
    def __init__(
        self,
        capability: CreateEciScalingConfigurationRequestContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateEciScalingConfigurationRequestContainersEnvironmentVars(TeaModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref_field_path = field_ref_field_path
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEciScalingConfigurationRequestContainersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class CreateEciScalingConfigurationRequestContainersVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        self.mount_path = mount_path
        self.mount_propagation = mount_propagation
        self.name = name
        self.read_only = read_only
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class CreateEciScalingConfigurationRequestContainers(TeaModel):
    def __init__(
        self,
        liveness_probe: CreateEciScalingConfigurationRequestContainersLivenessProbe = None,
        readiness_probe: CreateEciScalingConfigurationRequestContainersReadinessProbe = None,
        security_context: CreateEciScalingConfigurationRequestContainersSecurityContext = None,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        environment_vars: List[CreateEciScalingConfigurationRequestContainersEnvironmentVars] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        memory: float = None,
        name: str = None,
        ports: List[CreateEciScalingConfigurationRequestContainersPorts] = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mounts: List[CreateEciScalingConfigurationRequestContainersVolumeMounts] = None,
        working_dir: str = None,
    ):
        self.liveness_probe = liveness_probe
        self.readiness_probe = readiness_probe
        self.security_context = security_context
        self.args = args
        self.commands = commands
        self.cpu = cpu
        self.environment_vars = environment_vars
        self.gpu = gpu
        self.image = image
        self.image_pull_policy = image_pull_policy
        self.memory = memory
        self.name = name
        self.ports = ports
        self.stdin = stdin
        self.stdin_once = stdin_once
        self.tty = tty
        self.volume_mounts = volume_mounts
        self.working_dir = working_dir

    def validate(self):
        self.validate_required(self.liveness_probe, 'liveness_probe')
        if self.liveness_probe:
            self.liveness_probe.validate()
        self.validate_required(self.readiness_probe, 'readiness_probe')
        if self.readiness_probe:
            self.readiness_probe.validate()
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.args is not None:
            result['Args'] = self.args
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivenessProbe') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('ReadinessProbe') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = CreateEciScalingConfigurationRequestContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = CreateEciScalingConfigurationRequestContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = CreateEciScalingConfigurationRequestContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = CreateEciScalingConfigurationRequestContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateEciScalingConfigurationRequestDnsConfigOptions(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEciScalingConfigurationRequestHostAliases(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        self.hostnames = hostnames
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class CreateEciScalingConfigurationRequestImageRegistryCredentials(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateEciScalingConfigurationRequestInitContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class CreateEciScalingConfigurationRequestInitContainersSecurityContext(TeaModel):
    def __init__(
        self,
        capability: CreateEciScalingConfigurationRequestInitContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = CreateEciScalingConfigurationRequestInitContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class CreateEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars(TeaModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref_field_path = field_ref_field_path
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEciScalingConfigurationRequestInitContainersInitContainerPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class CreateEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        self.mount_path = mount_path
        self.mount_propagation = mount_propagation
        self.name = name
        self.read_only = read_only
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class CreateEciScalingConfigurationRequestInitContainers(TeaModel):
    def __init__(
        self,
        security_context: CreateEciScalingConfigurationRequestInitContainersSecurityContext = None,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        init_container_environment_vars: List[CreateEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars] = None,
        init_container_ports: List[CreateEciScalingConfigurationRequestInitContainersInitContainerPorts] = None,
        init_container_volume_mounts: List[CreateEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts] = None,
        memory: float = None,
        name: str = None,
        working_dir: str = None,
    ):
        self.security_context = security_context
        self.args = args
        self.commands = commands
        self.cpu = cpu
        self.gpu = gpu
        self.image = image
        self.image_pull_policy = image_pull_policy
        self.init_container_environment_vars = init_container_environment_vars
        self.init_container_ports = init_container_ports
        self.init_container_volume_mounts = init_container_volume_mounts
        self.memory = memory
        self.name = name
        self.working_dir = working_dir

    def validate(self):
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        if self.init_container_environment_vars:
            for k in self.init_container_environment_vars:
                if k:
                    k.validate()
        if self.init_container_ports:
            for k in self.init_container_ports:
                if k:
                    k.validate()
        if self.init_container_volume_mounts:
            for k in self.init_container_volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.args is not None:
            result['Args'] = self.args
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        result['InitContainerEnvironmentVars'] = []
        if self.init_container_environment_vars is not None:
            for k in self.init_container_environment_vars:
                result['InitContainerEnvironmentVars'].append(k.to_map() if k else None)
        result['InitContainerPorts'] = []
        if self.init_container_ports is not None:
            for k in self.init_container_ports:
                result['InitContainerPorts'].append(k.to_map() if k else None)
        result['InitContainerVolumeMounts'] = []
        if self.init_container_volume_mounts is not None:
            for k in self.init_container_volume_mounts:
                result['InitContainerVolumeMounts'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = CreateEciScalingConfigurationRequestInitContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        self.init_container_environment_vars = []
        if m.get('InitContainerEnvironmentVars') is not None:
            for k in m.get('InitContainerEnvironmentVars'):
                temp_model = CreateEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars()
                self.init_container_environment_vars.append(temp_model.from_map(k))
        self.init_container_ports = []
        if m.get('InitContainerPorts') is not None:
            for k in m.get('InitContainerPorts'):
                temp_model = CreateEciScalingConfigurationRequestInitContainersInitContainerPorts()
                self.init_container_ports.append(temp_model.from_map(k))
        self.init_container_volume_mounts = []
        if m.get('InitContainerVolumeMounts') is not None:
            for k in m.get('InitContainerVolumeMounts'):
                temp_model = CreateEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts()
                self.init_container_volume_mounts.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateEciScalingConfigurationRequestSecurityContextSysctls(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEciScalingConfigurationRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateEciScalingConfigurationRequestVolumesDiskVolume(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        fs_type: str = None,
    ):
        self.disk_id = disk_id
        self.disk_size = disk_size
        self.fs_type = fs_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        return self


class CreateEciScalingConfigurationRequestVolumesEmptyDirVolume(TeaModel):
    def __init__(
        self,
        medium: str = None,
    ):
        self.medium = medium

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        return self


class CreateEciScalingConfigurationRequestVolumesFlexVolume(TeaModel):
    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: str = None,
    ):
        self.driver = driver
        self.fs_type = fs_type
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class CreateEciScalingConfigurationRequestVolumesHostPathVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateEciScalingConfigurationRequestVolumesNFSVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        self.path = path
        self.read_only = read_only
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class CreateEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPaths(TeaModel):
    def __init__(
        self,
        content: str = None,
        mode: int = None,
        path: str = None,
    ):
        self.content = content
        self.mode = mode
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateEciScalingConfigurationRequestVolumes(TeaModel):
    def __init__(
        self,
        disk_volume: CreateEciScalingConfigurationRequestVolumesDiskVolume = None,
        empty_dir_volume: CreateEciScalingConfigurationRequestVolumesEmptyDirVolume = None,
        flex_volume: CreateEciScalingConfigurationRequestVolumesFlexVolume = None,
        host_path_volume: CreateEciScalingConfigurationRequestVolumesHostPathVolume = None,
        nfsvolume: CreateEciScalingConfigurationRequestVolumesNFSVolume = None,
        config_file_volume_config_file_to_paths: List[CreateEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPaths] = None,
        config_file_volume_default_mode: int = None,
        name: str = None,
        type: str = None,
    ):
        self.disk_volume = disk_volume
        self.empty_dir_volume = empty_dir_volume
        self.flex_volume = flex_volume
        self.host_path_volume = host_path_volume
        self.nfsvolume = nfsvolume
        self.config_file_volume_config_file_to_paths = config_file_volume_config_file_to_paths
        self.config_file_volume_default_mode = config_file_volume_default_mode
        self.name = name
        self.type = type

    def validate(self):
        self.validate_required(self.disk_volume, 'disk_volume')
        if self.disk_volume:
            self.disk_volume.validate()
        self.validate_required(self.empty_dir_volume, 'empty_dir_volume')
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()
        self.validate_required(self.flex_volume, 'flex_volume')
        if self.flex_volume:
            self.flex_volume.validate()
        self.validate_required(self.host_path_volume, 'host_path_volume')
        if self.host_path_volume:
            self.host_path_volume.validate()
        self.validate_required(self.nfsvolume, 'nfsvolume')
        if self.nfsvolume:
            self.nfsvolume.validate()
        if self.config_file_volume_config_file_to_paths:
            for k in self.config_file_volume_config_file_to_paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_volume is not None:
            result['DiskVolume'] = self.disk_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()
        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        result['ConfigFileVolumeConfigFileToPaths'] = []
        if self.config_file_volume_config_file_to_paths is not None:
            for k in self.config_file_volume_config_file_to_paths:
                result['ConfigFileVolumeConfigFileToPaths'].append(k.to_map() if k else None)
        if self.config_file_volume_default_mode is not None:
            result['ConfigFileVolumeDefaultMode'] = self.config_file_volume_default_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskVolume') is not None:
            temp_model = CreateEciScalingConfigurationRequestVolumesDiskVolume()
            self.disk_volume = temp_model.from_map(m['DiskVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = CreateEciScalingConfigurationRequestVolumesEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('FlexVolume') is not None:
            temp_model = CreateEciScalingConfigurationRequestVolumesFlexVolume()
            self.flex_volume = temp_model.from_map(m['FlexVolume'])
        if m.get('HostPathVolume') is not None:
            temp_model = CreateEciScalingConfigurationRequestVolumesHostPathVolume()
            self.host_path_volume = temp_model.from_map(m['HostPathVolume'])
        if m.get('NFSVolume') is not None:
            temp_model = CreateEciScalingConfigurationRequestVolumesNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        self.config_file_volume_config_file_to_paths = []
        if m.get('ConfigFileVolumeConfigFileToPaths') is not None:
            for k in m.get('ConfigFileVolumeConfigFileToPaths'):
                temp_model = CreateEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPaths()
                self.config_file_volume_config_file_to_paths.append(temp_model.from_map(k))
        if m.get('ConfigFileVolumeDefaultMode') is not None:
            self.config_file_volume_default_mode = m.get('ConfigFileVolumeDefaultMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateEciScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        acr_registry_infos: List[CreateEciScalingConfigurationRequestAcrRegistryInfos] = None,
        active_deadline_seconds: int = None,
        auto_create_eip: bool = None,
        auto_match_image_cache: bool = None,
        container_group_name: str = None,
        containers: List[CreateEciScalingConfigurationRequestContainers] = None,
        cost_optimization: bool = None,
        cpu: float = None,
        cpu_options_core: int = None,
        cpu_options_threads_per_core: int = None,
        description: str = None,
        dns_config_name_servers: List[str] = None,
        dns_config_options: List[CreateEciScalingConfigurationRequestDnsConfigOptions] = None,
        dns_config_searchs: List[str] = None,
        dns_policy: str = None,
        egress_bandwidth: int = None,
        eip_bandwidth: int = None,
        enable_sls: bool = None,
        ephemeral_storage: int = None,
        host_aliases: List[CreateEciScalingConfigurationRequestHostAliases] = None,
        host_name: str = None,
        image_registry_credentials: List[CreateEciScalingConfigurationRequestImageRegistryCredentials] = None,
        image_snapshot_id: str = None,
        ingress_bandwidth: int = None,
        init_containers: List[CreateEciScalingConfigurationRequestInitContainers] = None,
        instance_family_level: str = None,
        ipv_6address_count: int = None,
        load_balancer_weight: int = None,
        memory: float = None,
        ntp_servers: List[str] = None,
        owner_id: int = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        restart_policy: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        security_context_sysctls: List[CreateEciScalingConfigurationRequestSecurityContextSysctls] = None,
        security_group_id: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        tags: List[CreateEciScalingConfigurationRequestTags] = None,
        termination_grace_period_seconds: int = None,
        volumes: List[CreateEciScalingConfigurationRequestVolumes] = None,
    ):
        self.acr_registry_infos = acr_registry_infos
        self.active_deadline_seconds = active_deadline_seconds
        self.auto_create_eip = auto_create_eip
        self.auto_match_image_cache = auto_match_image_cache
        self.container_group_name = container_group_name
        self.containers = containers
        self.cost_optimization = cost_optimization
        self.cpu = cpu
        self.cpu_options_core = cpu_options_core
        self.cpu_options_threads_per_core = cpu_options_threads_per_core
        self.description = description
        self.dns_config_name_servers = dns_config_name_servers
        self.dns_config_options = dns_config_options
        self.dns_config_searchs = dns_config_searchs
        self.dns_policy = dns_policy
        self.egress_bandwidth = egress_bandwidth
        self.eip_bandwidth = eip_bandwidth
        self.enable_sls = enable_sls
        self.ephemeral_storage = ephemeral_storage
        self.host_aliases = host_aliases
        self.host_name = host_name
        self.image_registry_credentials = image_registry_credentials
        self.image_snapshot_id = image_snapshot_id
        self.ingress_bandwidth = ingress_bandwidth
        self.init_containers = init_containers
        self.instance_family_level = instance_family_level
        self.ipv_6address_count = ipv_6address_count
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.ntp_servers = ntp_servers
        self.owner_id = owner_id
        self.ram_role_name = ram_role_name
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.restart_policy = restart_policy
        self.scaling_configuration_name = scaling_configuration_name
        self.scaling_group_id = scaling_group_id
        self.security_context_sysctls = security_context_sysctls
        self.security_group_id = security_group_id
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.tags = tags
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.volumes = volumes

    def validate(self):
        if self.acr_registry_infos:
            for k in self.acr_registry_infos:
                if k:
                    k.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.dns_config_options:
            for k in self.dns_config_options:
                if k:
                    k.validate()
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.image_registry_credentials:
            for k in self.image_registry_credentials:
                if k:
                    k.validate()
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.security_context_sysctls:
            for k in self.security_context_sysctls:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfos'] = []
        if self.acr_registry_infos is not None:
            for k in self.acr_registry_infos:
                result['AcrRegistryInfos'].append(k.to_map() if k else None)
        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds
        if self.auto_create_eip is not None:
            result['AutoCreateEip'] = self.auto_create_eip
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.cost_optimization is not None:
            result['CostOptimization'] = self.cost_optimization
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_options_core is not None:
            result['CpuOptionsCore'] = self.cpu_options_core
        if self.cpu_options_threads_per_core is not None:
            result['CpuOptionsThreadsPerCore'] = self.cpu_options_threads_per_core
        if self.description is not None:
            result['Description'] = self.description
        if self.dns_config_name_servers is not None:
            result['DnsConfigNameServers'] = self.dns_config_name_servers
        result['DnsConfigOptions'] = []
        if self.dns_config_options is not None:
            for k in self.dns_config_options:
                result['DnsConfigOptions'].append(k.to_map() if k else None)
        if self.dns_config_searchs is not None:
            result['DnsConfigSearchs'] = self.dns_config_searchs
        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy
        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.enable_sls is not None:
            result['EnableSls'] = self.enable_sls
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k in self.host_aliases:
                result['HostAliases'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['HostName'] = self.host_name
        result['ImageRegistryCredentials'] = []
        if self.image_registry_credentials is not None:
            for k in self.image_registry_credentials:
                result['ImageRegistryCredentials'].append(k.to_map() if k else None)
        if self.image_snapshot_id is not None:
            result['ImageSnapshotId'] = self.image_snapshot_id
        if self.ingress_bandwidth is not None:
            result['IngressBandwidth'] = self.ingress_bandwidth
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.ntp_servers is not None:
            result['NtpServers'] = self.ntp_servers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        result['SecurityContextSysctls'] = []
        if self.security_context_sysctls is not None:
            for k in self.security_context_sysctls:
                result['SecurityContextSysctls'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_infos = []
        if m.get('AcrRegistryInfos') is not None:
            for k in m.get('AcrRegistryInfos'):
                temp_model = CreateEciScalingConfigurationRequestAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k))
        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')
        if m.get('AutoCreateEip') is not None:
            self.auto_create_eip = m.get('AutoCreateEip')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = CreateEciScalingConfigurationRequestContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('CostOptimization') is not None:
            self.cost_optimization = m.get('CostOptimization')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuOptionsCore') is not None:
            self.cpu_options_core = m.get('CpuOptionsCore')
        if m.get('CpuOptionsThreadsPerCore') is not None:
            self.cpu_options_threads_per_core = m.get('CpuOptionsThreadsPerCore')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnsConfigNameServers') is not None:
            self.dns_config_name_servers = m.get('DnsConfigNameServers')
        self.dns_config_options = []
        if m.get('DnsConfigOptions') is not None:
            for k in m.get('DnsConfigOptions'):
                temp_model = CreateEciScalingConfigurationRequestDnsConfigOptions()
                self.dns_config_options.append(temp_model.from_map(k))
        if m.get('DnsConfigSearchs') is not None:
            self.dns_config_searchs = m.get('DnsConfigSearchs')
        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')
        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EnableSls') is not None:
            self.enable_sls = m.get('EnableSls')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k in m.get('HostAliases'):
                temp_model = CreateEciScalingConfigurationRequestHostAliases()
                self.host_aliases.append(temp_model.from_map(k))
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k in m.get('ImageRegistryCredentials'):
                temp_model = CreateEciScalingConfigurationRequestImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k))
        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')
        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = CreateEciScalingConfigurationRequestInitContainers()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NtpServers') is not None:
            self.ntp_servers = m.get('NtpServers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        self.security_context_sysctls = []
        if m.get('SecurityContextSysctls') is not None:
            for k in m.get('SecurityContextSysctls'):
                temp_model = CreateEciScalingConfigurationRequestSecurityContextSysctls()
                self.security_context_sysctls.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateEciScalingConfigurationRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = CreateEciScalingConfigurationRequestVolumes()
                self.volumes.append(temp_model.from_map(k))
        return self


class CreateEciScalingConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_configuration_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        return self


class CreateEciScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEciScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEciScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecycleHookRequest(TeaModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_hook_name: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.default_result = default_result
        self.heartbeat_timeout = heartbeat_timeout
        self.lifecycle_hook_name = lifecycle_hook_name
        self.lifecycle_transition = lifecycle_transition
        self.notification_arn = notification_arn
        self.notification_metadata = notification_metadata
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class CreateLifecycleHookResponseBody(TeaModel):
    def __init__(
        self,
        lifecycle_hook_id: str = None,
        request_id: str = None,
    ):
        self.lifecycle_hook_id = lifecycle_hook_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLifecycleHookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLifecycleHookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLifecycleHookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNotificationConfigurationRequest(TeaModel):
    def __init__(
        self,
        notification_arn: str = None,
        notification_types: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.notification_arn = notification_arn
        self.notification_types = notification_types
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationTypes') is not None:
            self.notification_types = m.get('NotificationTypes')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class CreateNotificationConfigurationResponseBody(TeaModel):
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


class CreateNotificationConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNotificationConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNotificationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingConfigurationRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        self.id = id
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        return self


class CreateScalingConfigurationRequestSystemDisk(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        description: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.description = description
        self.disk_name = disk_name
        self.encrypt_algorithm = encrypt_algorithm
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateScalingConfigurationRequestDataDisks(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        categories: List[str] = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.categories = categories
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.description = description
        self.device = device
        self.disk_name = disk_name
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.description is not None:
            result['Description'] = self.description
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateScalingConfigurationRequestInstancePatternInfos(TeaModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burstable_performance: str = None,
        cores: int = None,
        excluded_instance_types: List[str] = None,
        instance_family_level: str = None,
        max_price: float = None,
        memory: float = None,
    ):
        self.architectures = architectures
        self.burstable_performance = burstable_performance
        self.cores = cores
        self.excluded_instance_types = excluded_instance_types
        self.instance_family_level = instance_family_level
        self.max_price = max_price
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architectures is not None:
            result['Architectures'] = self.architectures
        if self.burstable_performance is not None:
            result['BurstablePerformance'] = self.burstable_performance
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.excluded_instance_types is not None:
            result['ExcludedInstanceTypes'] = self.excluded_instance_types
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architectures') is not None:
            self.architectures = m.get('Architectures')
        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('ExcludedInstanceTypes') is not None:
            self.excluded_instance_types = m.get('ExcludedInstanceTypes')
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class CreateScalingConfigurationRequestInstanceTypeOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class CreateScalingConfigurationRequestSpotPriceLimits(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        return self


class CreateScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: CreateScalingConfigurationRequestPrivatePoolOptions = None,
        system_disk: CreateScalingConfigurationRequestSystemDisk = None,
        affinity: str = None,
        client_token: str = None,
        cpu: int = None,
        credit_specification: str = None,
        data_disks: List[CreateScalingConfigurationRequestDataDisks] = None,
        dedicated_host_id: str = None,
        deployment_set_id: str = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_description: str = None,
        instance_name: str = None,
        instance_pattern_infos: List[CreateScalingConfigurationRequestInstancePatternInfos] = None,
        instance_type: str = None,
        instance_type_overrides: List[CreateScalingConfigurationRequestInstanceTypeOverrides] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        scheduler_options: Dict[str, Any] = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[CreateScalingConfigurationRequestSpotPriceLimits] = None,
        spot_strategy: str = None,
        system_disk_categories: List[str] = None,
        tags: str = None,
        tenancy: str = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.system_disk = system_disk
        self.affinity = affinity
        self.client_token = client_token
        self.cpu = cpu
        self.credit_specification = credit_specification
        self.data_disks = data_disks
        self.dedicated_host_id = dedicated_host_id
        self.deployment_set_id = deployment_set_id
        self.host_name = host_name
        self.hpc_cluster_id = hpc_cluster_id
        self.image_family = image_family
        self.image_id = image_id
        self.image_name = image_name
        self.instance_description = instance_description
        self.instance_name = instance_name
        self.instance_pattern_infos = instance_pattern_infos
        self.instance_type = instance_type
        self.instance_type_overrides = instance_type_overrides
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.io_optimized = io_optimized
        self.ipv_6address_count = ipv_6address_count
        self.key_pair_name = key_pair_name
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.password = password
        self.password_inherit = password_inherit
        self.ram_role_name = ram_role_name
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.scaling_configuration_name = scaling_configuration_name
        self.scaling_group_id = scaling_group_id
        self.scheduler_options = scheduler_options
        self.security_enhancement_strategy = security_enhancement_strategy
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_duration = spot_duration
        self.spot_interruption_behavior = spot_interruption_behavior
        self.spot_price_limits = spot_price_limits
        self.spot_strategy = spot_strategy
        self.system_disk_categories = system_disk_categories
        self.tags = tags
        self.tenancy = tenancy
        self.user_data = user_data
        self.zone_id = zone_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.instance_pattern_infos:
            for k in self.instance_pattern_infos:
                if k:
                    k.validate()
        if self.instance_type_overrides:
            for k in self.instance_type_overrides:
                if k:
                    k.validate()
        if self.spot_price_limits:
            for k in self.spot_price_limits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['InstancePatternInfos'] = []
        if self.instance_pattern_infos is not None:
            for k in self.instance_pattern_infos:
                result['InstancePatternInfos'].append(k.to_map() if k else None)
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        result['InstanceTypeOverrides'] = []
        if self.instance_type_overrides is not None:
            for k in self.instance_type_overrides:
                result['InstanceTypeOverrides'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        result['SpotPriceLimits'] = []
        if self.spot_price_limits is not None:
            for k in self.spot_price_limits:
                result['SpotPriceLimits'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = CreateScalingConfigurationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('SystemDisk') is not None:
            temp_model = CreateScalingConfigurationRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = CreateScalingConfigurationRequestDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.instance_pattern_infos = []
        if m.get('InstancePatternInfos') is not None:
            for k in m.get('InstancePatternInfos'):
                temp_model = CreateScalingConfigurationRequestInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k))
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        self.instance_type_overrides = []
        if m.get('InstanceTypeOverrides') is not None:
            for k in m.get('InstanceTypeOverrides'):
                temp_model = CreateScalingConfigurationRequestInstanceTypeOverrides()
                self.instance_type_overrides.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options = m.get('SchedulerOptions')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k in m.get('SpotPriceLimits'):
                temp_model = CreateScalingConfigurationRequestSpotPriceLimits()
                self.spot_price_limits.append(temp_model.from_map(k))
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateScalingConfigurationShrinkRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        self.id = id
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        return self


class CreateScalingConfigurationShrinkRequestSystemDisk(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        description: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.description = description
        self.disk_name = disk_name
        self.encrypt_algorithm = encrypt_algorithm
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateScalingConfigurationShrinkRequestDataDisks(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        categories: List[str] = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.categories = categories
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.description = description
        self.device = device
        self.disk_name = disk_name
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.description is not None:
            result['Description'] = self.description
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateScalingConfigurationShrinkRequestInstancePatternInfos(TeaModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burstable_performance: str = None,
        cores: int = None,
        excluded_instance_types: List[str] = None,
        instance_family_level: str = None,
        max_price: float = None,
        memory: float = None,
    ):
        self.architectures = architectures
        self.burstable_performance = burstable_performance
        self.cores = cores
        self.excluded_instance_types = excluded_instance_types
        self.instance_family_level = instance_family_level
        self.max_price = max_price
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architectures is not None:
            result['Architectures'] = self.architectures
        if self.burstable_performance is not None:
            result['BurstablePerformance'] = self.burstable_performance
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.excluded_instance_types is not None:
            result['ExcludedInstanceTypes'] = self.excluded_instance_types
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architectures') is not None:
            self.architectures = m.get('Architectures')
        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('ExcludedInstanceTypes') is not None:
            self.excluded_instance_types = m.get('ExcludedInstanceTypes')
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class CreateScalingConfigurationShrinkRequestInstanceTypeOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class CreateScalingConfigurationShrinkRequestSpotPriceLimits(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        return self


class CreateScalingConfigurationShrinkRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: CreateScalingConfigurationShrinkRequestPrivatePoolOptions = None,
        system_disk: CreateScalingConfigurationShrinkRequestSystemDisk = None,
        affinity: str = None,
        client_token: str = None,
        cpu: int = None,
        credit_specification: str = None,
        data_disks: List[CreateScalingConfigurationShrinkRequestDataDisks] = None,
        dedicated_host_id: str = None,
        deployment_set_id: str = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_description: str = None,
        instance_name: str = None,
        instance_pattern_infos: List[CreateScalingConfigurationShrinkRequestInstancePatternInfos] = None,
        instance_type: str = None,
        instance_type_overrides: List[CreateScalingConfigurationShrinkRequestInstanceTypeOverrides] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        scheduler_options_shrink: str = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[CreateScalingConfigurationShrinkRequestSpotPriceLimits] = None,
        spot_strategy: str = None,
        system_disk_categories: List[str] = None,
        tags: str = None,
        tenancy: str = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.system_disk = system_disk
        self.affinity = affinity
        self.client_token = client_token
        self.cpu = cpu
        self.credit_specification = credit_specification
        self.data_disks = data_disks
        self.dedicated_host_id = dedicated_host_id
        self.deployment_set_id = deployment_set_id
        self.host_name = host_name
        self.hpc_cluster_id = hpc_cluster_id
        self.image_family = image_family
        self.image_id = image_id
        self.image_name = image_name
        self.instance_description = instance_description
        self.instance_name = instance_name
        self.instance_pattern_infos = instance_pattern_infos
        self.instance_type = instance_type
        self.instance_type_overrides = instance_type_overrides
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.io_optimized = io_optimized
        self.ipv_6address_count = ipv_6address_count
        self.key_pair_name = key_pair_name
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.password = password
        self.password_inherit = password_inherit
        self.ram_role_name = ram_role_name
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.scaling_configuration_name = scaling_configuration_name
        self.scaling_group_id = scaling_group_id
        self.scheduler_options_shrink = scheduler_options_shrink
        self.security_enhancement_strategy = security_enhancement_strategy
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_duration = spot_duration
        self.spot_interruption_behavior = spot_interruption_behavior
        self.spot_price_limits = spot_price_limits
        self.spot_strategy = spot_strategy
        self.system_disk_categories = system_disk_categories
        self.tags = tags
        self.tenancy = tenancy
        self.user_data = user_data
        self.zone_id = zone_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.instance_pattern_infos:
            for k in self.instance_pattern_infos:
                if k:
                    k.validate()
        if self.instance_type_overrides:
            for k in self.instance_type_overrides:
                if k:
                    k.validate()
        if self.spot_price_limits:
            for k in self.spot_price_limits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['InstancePatternInfos'] = []
        if self.instance_pattern_infos is not None:
            for k in self.instance_pattern_infos:
                result['InstancePatternInfos'].append(k.to_map() if k else None)
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        result['InstanceTypeOverrides'] = []
        if self.instance_type_overrides is not None:
            for k in self.instance_type_overrides:
                result['InstanceTypeOverrides'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scheduler_options_shrink is not None:
            result['SchedulerOptions'] = self.scheduler_options_shrink
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        result['SpotPriceLimits'] = []
        if self.spot_price_limits is not None:
            for k in self.spot_price_limits:
                result['SpotPriceLimits'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = CreateScalingConfigurationShrinkRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('SystemDisk') is not None:
            temp_model = CreateScalingConfigurationShrinkRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = CreateScalingConfigurationShrinkRequestDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.instance_pattern_infos = []
        if m.get('InstancePatternInfos') is not None:
            for k in m.get('InstancePatternInfos'):
                temp_model = CreateScalingConfigurationShrinkRequestInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k))
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        self.instance_type_overrides = []
        if m.get('InstanceTypeOverrides') is not None:
            for k in m.get('InstanceTypeOverrides'):
                temp_model = CreateScalingConfigurationShrinkRequestInstanceTypeOverrides()
                self.instance_type_overrides.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options_shrink = m.get('SchedulerOptions')
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k in m.get('SpotPriceLimits'):
                temp_model = CreateScalingConfigurationShrinkRequestSpotPriceLimits()
                self.spot_price_limits.append(temp_model.from_map(k))
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateScalingConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_configuration_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        return self


class CreateScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingGroupRequestAlbServerGroups(TeaModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
        weight: int = None,
    ):
        self.alb_server_group_id = alb_server_group_id
        self.port = port
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alb_server_group_id is not None:
            result['AlbServerGroupId'] = self.alb_server_group_id
        if self.port is not None:
            result['Port'] = self.port
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbServerGroupId') is not None:
            self.alb_server_group_id = m.get('AlbServerGroupId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateScalingGroupRequestLaunchTemplateOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class CreateScalingGroupRequestLifecycleHooks(TeaModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_hook_name: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
    ):
        self.default_result = default_result
        self.heartbeat_timeout = heartbeat_timeout
        self.lifecycle_hook_name = lifecycle_hook_name
        self.lifecycle_transition = lifecycle_transition
        self.notification_arn = notification_arn
        self.notification_metadata = notification_metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        return self


class CreateScalingGroupRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateScalingGroupRequestVServerGroupsVServerGroupAttributes(TeaModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
        weight: int = None,
    ):
        self.port = port
        self.vserver_group_id = vserver_group_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateScalingGroupRequestVServerGroups(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[CreateScalingGroupRequestVServerGroupsVServerGroupAttributes] = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.vserver_group_attributes = vserver_group_attributes

    def validate(self):
        if self.vserver_group_attributes:
            for k in self.vserver_group_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        result['VServerGroupAttributes'] = []
        if self.vserver_group_attributes is not None:
            for k in self.vserver_group_attributes:
                result['VServerGroupAttributes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        self.vserver_group_attributes = []
        if m.get('VServerGroupAttributes') is not None:
            for k in m.get('VServerGroupAttributes'):
                temp_model = CreateScalingGroupRequestVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k))
        return self


class CreateScalingGroupRequest(TeaModel):
    def __init__(
        self,
        alb_server_groups: List[CreateScalingGroupRequestAlbServerGroups] = None,
        allocation_strategy: str = None,
        az_balance: bool = None,
        client_token: str = None,
        compensate_with_on_demand: bool = None,
        container_group_id: str = None,
        dbinstance_ids: str = None,
        default_cooldown: int = None,
        desired_capacity: int = None,
        group_deletion_protection: bool = None,
        group_type: str = None,
        health_check_type: str = None,
        instance_id: str = None,
        launch_template_id: str = None,
        launch_template_overrides: List[CreateScalingGroupRequestLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        lifecycle_hooks: List[CreateScalingGroupRequestLifecycleHooks] = None,
        load_balancer_ids: str = None,
        max_instance_lifetime: int = None,
        max_size: int = None,
        min_size: int = None,
        multi_azpolicy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        removal_policies: List[str] = None,
        resource_owner_account: str = None,
        scaling_group_name: str = None,
        scaling_policy: str = None,
        spot_allocation_strategy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        sync_alarm_rule_to_cms: bool = None,
        tags: List[CreateScalingGroupRequestTags] = None,
        vserver_groups: List[CreateScalingGroupRequestVServerGroups] = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.alb_server_groups = alb_server_groups
        self.allocation_strategy = allocation_strategy
        self.az_balance = az_balance
        self.client_token = client_token
        self.compensate_with_on_demand = compensate_with_on_demand
        self.container_group_id = container_group_id
        self.dbinstance_ids = dbinstance_ids
        self.default_cooldown = default_cooldown
        self.desired_capacity = desired_capacity
        self.group_deletion_protection = group_deletion_protection
        self.group_type = group_type
        self.health_check_type = health_check_type
        self.instance_id = instance_id
        self.launch_template_id = launch_template_id
        self.launch_template_overrides = launch_template_overrides
        self.launch_template_version = launch_template_version
        self.lifecycle_hooks = lifecycle_hooks
        self.load_balancer_ids = load_balancer_ids
        self.max_instance_lifetime = max_instance_lifetime
        self.max_size = max_size
        self.min_size = min_size
        self.multi_azpolicy = multi_azpolicy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.removal_policies = removal_policies
        self.resource_owner_account = resource_owner_account
        self.scaling_group_name = scaling_group_name
        self.scaling_policy = scaling_policy
        self.spot_allocation_strategy = spot_allocation_strategy
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.sync_alarm_rule_to_cms = sync_alarm_rule_to_cms
        self.tags = tags
        self.vserver_groups = vserver_groups
        self.v_switch_id = v_switch_id
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.alb_server_groups:
            for k in self.alb_server_groups:
                if k:
                    k.validate()
        if self.launch_template_overrides:
            for k in self.launch_template_overrides:
                if k:
                    k.validate()
        if self.lifecycle_hooks:
            for k in self.lifecycle_hooks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vserver_groups:
            for k in self.vserver_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlbServerGroups'] = []
        if self.alb_server_groups is not None:
            for k in self.alb_server_groups:
                result['AlbServerGroups'].append(k.to_map() if k else None)
        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy
        if self.az_balance is not None:
            result['AzBalance'] = self.az_balance
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand
        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k.to_map() if k else None)
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        result['LifecycleHooks'] = []
        if self.lifecycle_hooks is not None:
            for k in self.lifecycle_hooks:
                result['LifecycleHooks'].append(k.to_map() if k else None)
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.max_instance_lifetime is not None:
            result['MaxInstanceLifetime'] = self.max_instance_lifetime
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.multi_azpolicy is not None:
            result['MultiAZPolicy'] = self.multi_azpolicy
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.removal_policies is not None:
            result['RemovalPolicies'] = self.removal_policies
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy
        if self.spot_allocation_strategy is not None:
            result['SpotAllocationStrategy'] = self.spot_allocation_strategy
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.sync_alarm_rule_to_cms is not None:
            result['SyncAlarmRuleToCms'] = self.sync_alarm_rule_to_cms
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['VServerGroups'] = []
        if self.vserver_groups is not None:
            for k in self.vserver_groups:
                result['VServerGroups'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_server_groups = []
        if m.get('AlbServerGroups') is not None:
            for k in m.get('AlbServerGroups'):
                temp_model = CreateScalingGroupRequestAlbServerGroups()
                self.alb_server_groups.append(temp_model.from_map(k))
        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')
        if m.get('AzBalance') is not None:
            self.az_balance = m.get('AzBalance')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')
        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k in m.get('LaunchTemplateOverrides'):
                temp_model = CreateScalingGroupRequestLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k))
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        self.lifecycle_hooks = []
        if m.get('LifecycleHooks') is not None:
            for k in m.get('LifecycleHooks'):
                temp_model = CreateScalingGroupRequestLifecycleHooks()
                self.lifecycle_hooks.append(temp_model.from_map(k))
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('MaxInstanceLifetime') is not None:
            self.max_instance_lifetime = m.get('MaxInstanceLifetime')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('MultiAZPolicy') is not None:
            self.multi_azpolicy = m.get('MultiAZPolicy')
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemovalPolicies') is not None:
            self.removal_policies = m.get('RemovalPolicies')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')
        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('SyncAlarmRuleToCms') is not None:
            self.sync_alarm_rule_to_cms = m.get('SyncAlarmRuleToCms')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateScalingGroupRequestTags()
                self.tags.append(temp_model.from_map(k))
        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k in m.get('VServerGroups'):
                temp_model = CreateScalingGroupRequestVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class CreateScalingGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_group_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class CreateScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScalingRuleRequestStepAdjustments(TeaModel):
    def __init__(
        self,
        metric_interval_lower_bound: float = None,
        metric_interval_upper_bound: float = None,
        scaling_adjustment: int = None,
    ):
        self.metric_interval_lower_bound = metric_interval_lower_bound
        self.metric_interval_upper_bound = metric_interval_upper_bound
        self.scaling_adjustment = scaling_adjustment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_interval_lower_bound is not None:
            result['MetricIntervalLowerBound'] = self.metric_interval_lower_bound
        if self.metric_interval_upper_bound is not None:
            result['MetricIntervalUpperBound'] = self.metric_interval_upper_bound
        if self.scaling_adjustment is not None:
            result['ScalingAdjustment'] = self.scaling_adjustment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricIntervalLowerBound') is not None:
            self.metric_interval_lower_bound = m.get('MetricIntervalLowerBound')
        if m.get('MetricIntervalUpperBound') is not None:
            self.metric_interval_upper_bound = m.get('MetricIntervalUpperBound')
        if m.get('ScalingAdjustment') is not None:
            self.scaling_adjustment = m.get('ScalingAdjustment')
        return self


class CreateScalingRuleRequest(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        cooldown: int = None,
        disable_scale_in: bool = None,
        estimated_instance_warmup: int = None,
        initial_max_size: int = None,
        metric_name: str = None,
        min_adjustment_magnitude: int = None,
        owner_account: str = None,
        owner_id: int = None,
        predictive_scaling_mode: str = None,
        predictive_task_buffer_time: int = None,
        predictive_value_behavior: str = None,
        predictive_value_buffer: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scale_in_evaluation_count: int = None,
        scale_out_evaluation_count: int = None,
        scaling_group_id: str = None,
        scaling_rule_name: str = None,
        scaling_rule_type: str = None,
        step_adjustments: List[CreateScalingRuleRequestStepAdjustments] = None,
        target_value: float = None,
    ):
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.cooldown = cooldown
        self.disable_scale_in = disable_scale_in
        self.estimated_instance_warmup = estimated_instance_warmup
        self.initial_max_size = initial_max_size
        self.metric_name = metric_name
        self.min_adjustment_magnitude = min_adjustment_magnitude
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.predictive_scaling_mode = predictive_scaling_mode
        self.predictive_task_buffer_time = predictive_task_buffer_time
        self.predictive_value_behavior = predictive_value_behavior
        self.predictive_value_buffer = predictive_value_buffer
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scale_in_evaluation_count = scale_in_evaluation_count
        self.scale_out_evaluation_count = scale_out_evaluation_count
        self.scaling_group_id = scaling_group_id
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_type = scaling_rule_type
        self.step_adjustments = step_adjustments
        self.target_value = target_value

    def validate(self):
        if self.step_adjustments:
            for k in self.step_adjustments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.disable_scale_in is not None:
            result['DisableScaleIn'] = self.disable_scale_in
        if self.estimated_instance_warmup is not None:
            result['EstimatedInstanceWarmup'] = self.estimated_instance_warmup
        if self.initial_max_size is not None:
            result['InitialMaxSize'] = self.initial_max_size
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode
        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time
        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior
        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count
        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        result['StepAdjustments'] = []
        if self.step_adjustments is not None:
            for k in self.step_adjustments:
                result['StepAdjustments'].append(k.to_map() if k else None)
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')
        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')
        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')
        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')
        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')
        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')
        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        self.step_adjustments = []
        if m.get('StepAdjustments') is not None:
            for k in m.get('StepAdjustments'):
                temp_model = CreateScalingRuleRequestStepAdjustments()
                self.step_adjustments.append(temp_model.from_map(k))
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        return self


class CreateScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_rule_ari: str = None,
        scaling_rule_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_rule_ari = scaling_rule_ari
        self.scaling_rule_id = scaling_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        return self


class CreateScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        desired_capacity: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        max_value: int = None,
        min_value: int = None,
        owner_account: str = None,
        owner_id: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        scheduled_action: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        self.description = description
        self.desired_capacity = desired_capacity
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.max_value = max_value
        self.min_value = min_value
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.recurrence_end_time = recurrence_end_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id
        self.scheduled_action = scheduled_action
        self.scheduled_task_name = scheduled_task_name
        self.task_enabled = task_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        return self


class CreateScheduledTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scheduled_task_id: str = None,
    ):
        self.request_id = request_id
        self.scheduled_task_id = scheduled_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        return self


class CreateScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactivateScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_configuration_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        return self


class DeactivateScalingConfigurationResponseBody(TeaModel):
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


class DeactivateScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeactivateScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeactivateScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DeleteAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        request_id: str = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLifecycleHookRequest(TeaModel):
    def __init__(
        self,
        lifecycle_hook_id: str = None,
        lifecycle_hook_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.lifecycle_hook_id = lifecycle_hook_id
        self.lifecycle_hook_name = lifecycle_hook_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DeleteLifecycleHookResponseBody(TeaModel):
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


class DeleteLifecycleHookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLifecycleHookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLifecycleHookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNotificationConfigurationRequest(TeaModel):
    def __init__(
        self,
        notification_arn: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.notification_arn = notification_arn
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DeleteNotificationConfigurationResponseBody(TeaModel):
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


class DeleteNotificationConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNotificationConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNotificationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_configuration_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.scaling_configuration_id = scaling_configuration_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        return self


class DeleteScalingConfigurationResponseBody(TeaModel):
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


class DeleteScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingGroupRequest(TeaModel):
    def __init__(
        self,
        force_delete: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.force_delete = force_delete
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DeleteScalingGroupResponseBody(TeaModel):
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


class DeleteScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScalingRuleRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_rule_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_rule_id = scaling_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        return self


class DeleteScalingRuleResponseBody(TeaModel):
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


class DeleteScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scheduled_task_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scheduled_task_id = scheduled_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        return self


class DeleteScheduledTaskResponseBody(TeaModel):
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


class DeleteScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmsRequest(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        is_enable: bool = None,
        metric_name: str = None,
        metric_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        state: str = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.is_enable = is_enable
        self.metric_name = metric_name
        self.metric_type = metric_type
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeAlarmsResponseBodyAlarmListDimensions(TeaModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        self.dimension_key = dimension_key
        self.dimension_value = dimension_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class DescribeAlarmsResponseBodyAlarmListExpressions(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.comparison_operator = comparison_operator
        self.metric_name = metric_name
        self.period = period
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.period is not None:
            result['Period'] = self.period
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DescribeAlarmsResponseBodyAlarmList(TeaModel):
    def __init__(
        self,
        alarm_actions: List[str] = None,
        alarm_task_id: str = None,
        comparison_operator: str = None,
        description: str = None,
        dimensions: List[DescribeAlarmsResponseBodyAlarmListDimensions] = None,
        effective: str = None,
        enable: bool = None,
        evaluation_count: int = None,
        expressions: List[DescribeAlarmsResponseBodyAlarmListExpressions] = None,
        expressions_logic_operator: str = None,
        metric_name: str = None,
        metric_type: str = None,
        name: str = None,
        period: int = None,
        scaling_group_id: str = None,
        state: str = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.alarm_actions = alarm_actions
        self.alarm_task_id = alarm_task_id
        self.comparison_operator = comparison_operator
        self.description = description
        self.dimensions = dimensions
        self.effective = effective
        self.enable = enable
        self.evaluation_count = evaluation_count
        self.expressions = expressions
        self.expressions_logic_operator = expressions_logic_operator
        self.metric_name = metric_name
        self.metric_type = metric_type
        self.name = name
        self.period = period
        self.scaling_group_id = scaling_group_id
        self.state = state
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.expressions:
            for k in self.expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_actions is not None:
            result['AlarmActions'] = self.alarm_actions
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.description is not None:
            result['Description'] = self.description
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        result['Expressions'] = []
        if self.expressions is not None:
            for k in self.expressions:
                result['Expressions'].append(k.to_map() if k else None)
        if self.expressions_logic_operator is not None:
            result['ExpressionsLogicOperator'] = self.expressions_logic_operator
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.period is not None:
            result['Period'] = self.period
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.state is not None:
            result['State'] = self.state
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmActions') is not None:
            self.alarm_actions = m.get('AlarmActions')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = DescribeAlarmsResponseBodyAlarmListDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        self.expressions = []
        if m.get('Expressions') is not None:
            for k in m.get('Expressions'):
                temp_model = DescribeAlarmsResponseBodyAlarmListExpressions()
                self.expressions.append(temp_model.from_map(k))
        if m.get('ExpressionsLogicOperator') is not None:
            self.expressions_logic_operator = m.get('ExpressionsLogicOperator')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DescribeAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        alarm_list: List[DescribeAlarmsResponseBodyAlarmList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.alarm_list = alarm_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.alarm_list:
            for k in self.alarm_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmList'] = []
        if self.alarm_list is not None:
            for k in self.alarm_list:
                result['AlarmList'].append(k.to_map() if k else None)
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
        self.alarm_list = []
        if m.get('AlarmList') is not None:
            for k in m.get('AlarmList'):
                temp_model = DescribeAlarmsResponseBodyAlarmList()
                self.alarm_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlarmsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEciScalingConfigurationsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_configuration_ids: List[str] = None,
        scaling_configuration_names: List[str] = None,
        scaling_group_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_configuration_ids = scaling_configuration_ids
        self.scaling_configuration_names = scaling_configuration_names
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_configuration_ids is not None:
            result['ScalingConfigurationIds'] = self.scaling_configuration_ids
        if self.scaling_configuration_names is not None:
            result['ScalingConfigurationNames'] = self.scaling_configuration_names
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingConfigurationIds') is not None:
            self.scaling_configuration_ids = m.get('ScalingConfigurationIds')
        if m.get('ScalingConfigurationNames') is not None:
            self.scaling_configuration_names = m.get('ScalingConfigurationNames')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsAcrRegistryInfos(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.domains = domains
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersEnvironmentVars(TeaModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref_field_path = field_ref_field_path
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        self.mount_path = mount_path
        self.mount_propagation = mount_propagation
        self.name = name
        self.read_only = read_only
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainers(TeaModel):
    def __init__(
        self,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        environment_vars: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersEnvironmentVars] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        liveness_probe_exec_commands: List[str] = None,
        liveness_probe_failure_threshold: int = None,
        liveness_probe_http_get_path: str = None,
        liveness_probe_http_get_port: int = None,
        liveness_probe_http_get_scheme: str = None,
        liveness_probe_initial_delay_seconds: int = None,
        liveness_probe_period_seconds: int = None,
        liveness_probe_success_threshold: int = None,
        liveness_probe_tcp_socket_port: int = None,
        liveness_probe_timeout_seconds: int = None,
        memory: float = None,
        name: str = None,
        ports: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersPorts] = None,
        readiness_probe_exec_commands: List[str] = None,
        readiness_probe_failure_threshold: int = None,
        readiness_probe_http_get_path: str = None,
        readiness_probe_http_get_port: int = None,
        readiness_probe_http_get_scheme: str = None,
        readiness_probe_initial_delay_seconds: int = None,
        readiness_probe_period_seconds: int = None,
        readiness_probe_success_threshold: int = None,
        readiness_probe_tcp_socket_port: int = None,
        readiness_probe_timeout_seconds: int = None,
        security_context_capability_adds: List[str] = None,
        security_context_read_only_root_filesystem: bool = None,
        security_context_run_as_user: int = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mounts: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersVolumeMounts] = None,
        working_dir: str = None,
    ):
        self.args = args
        self.commands = commands
        self.cpu = cpu
        self.environment_vars = environment_vars
        self.gpu = gpu
        self.image = image
        self.image_pull_policy = image_pull_policy
        self.liveness_probe_exec_commands = liveness_probe_exec_commands
        self.liveness_probe_failure_threshold = liveness_probe_failure_threshold
        self.liveness_probe_http_get_path = liveness_probe_http_get_path
        self.liveness_probe_http_get_port = liveness_probe_http_get_port
        self.liveness_probe_http_get_scheme = liveness_probe_http_get_scheme
        self.liveness_probe_initial_delay_seconds = liveness_probe_initial_delay_seconds
        self.liveness_probe_period_seconds = liveness_probe_period_seconds
        self.liveness_probe_success_threshold = liveness_probe_success_threshold
        self.liveness_probe_tcp_socket_port = liveness_probe_tcp_socket_port
        self.liveness_probe_timeout_seconds = liveness_probe_timeout_seconds
        self.memory = memory
        self.name = name
        self.ports = ports
        self.readiness_probe_exec_commands = readiness_probe_exec_commands
        self.readiness_probe_failure_threshold = readiness_probe_failure_threshold
        self.readiness_probe_http_get_path = readiness_probe_http_get_path
        self.readiness_probe_http_get_port = readiness_probe_http_get_port
        self.readiness_probe_http_get_scheme = readiness_probe_http_get_scheme
        self.readiness_probe_initial_delay_seconds = readiness_probe_initial_delay_seconds
        self.readiness_probe_period_seconds = readiness_probe_period_seconds
        self.readiness_probe_success_threshold = readiness_probe_success_threshold
        self.readiness_probe_tcp_socket_port = readiness_probe_tcp_socket_port
        self.readiness_probe_timeout_seconds = readiness_probe_timeout_seconds
        self.security_context_capability_adds = security_context_capability_adds
        self.security_context_read_only_root_filesystem = security_context_read_only_root_filesystem
        self.security_context_run_as_user = security_context_run_as_user
        self.stdin = stdin
        self.stdin_once = stdin_once
        self.tty = tty
        self.volume_mounts = volume_mounts
        self.working_dir = working_dir

    def validate(self):
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.liveness_probe_exec_commands is not None:
            result['LivenessProbeExecCommands'] = self.liveness_probe_exec_commands
        if self.liveness_probe_failure_threshold is not None:
            result['LivenessProbeFailureThreshold'] = self.liveness_probe_failure_threshold
        if self.liveness_probe_http_get_path is not None:
            result['LivenessProbeHttpGetPath'] = self.liveness_probe_http_get_path
        if self.liveness_probe_http_get_port is not None:
            result['LivenessProbeHttpGetPort'] = self.liveness_probe_http_get_port
        if self.liveness_probe_http_get_scheme is not None:
            result['LivenessProbeHttpGetScheme'] = self.liveness_probe_http_get_scheme
        if self.liveness_probe_initial_delay_seconds is not None:
            result['LivenessProbeInitialDelaySeconds'] = self.liveness_probe_initial_delay_seconds
        if self.liveness_probe_period_seconds is not None:
            result['LivenessProbePeriodSeconds'] = self.liveness_probe_period_seconds
        if self.liveness_probe_success_threshold is not None:
            result['LivenessProbeSuccessThreshold'] = self.liveness_probe_success_threshold
        if self.liveness_probe_tcp_socket_port is not None:
            result['LivenessProbeTcpSocketPort'] = self.liveness_probe_tcp_socket_port
        if self.liveness_probe_timeout_seconds is not None:
            result['LivenessProbeTimeoutSeconds'] = self.liveness_probe_timeout_seconds
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.readiness_probe_exec_commands is not None:
            result['ReadinessProbeExecCommands'] = self.readiness_probe_exec_commands
        if self.readiness_probe_failure_threshold is not None:
            result['ReadinessProbeFailureThreshold'] = self.readiness_probe_failure_threshold
        if self.readiness_probe_http_get_path is not None:
            result['ReadinessProbeHttpGetPath'] = self.readiness_probe_http_get_path
        if self.readiness_probe_http_get_port is not None:
            result['ReadinessProbeHttpGetPort'] = self.readiness_probe_http_get_port
        if self.readiness_probe_http_get_scheme is not None:
            result['ReadinessProbeHttpGetScheme'] = self.readiness_probe_http_get_scheme
        if self.readiness_probe_initial_delay_seconds is not None:
            result['ReadinessProbeInitialDelaySeconds'] = self.readiness_probe_initial_delay_seconds
        if self.readiness_probe_period_seconds is not None:
            result['ReadinessProbePeriodSeconds'] = self.readiness_probe_period_seconds
        if self.readiness_probe_success_threshold is not None:
            result['ReadinessProbeSuccessThreshold'] = self.readiness_probe_success_threshold
        if self.readiness_probe_tcp_socket_port is not None:
            result['ReadinessProbeTcpSocketPort'] = self.readiness_probe_tcp_socket_port
        if self.readiness_probe_timeout_seconds is not None:
            result['ReadinessProbeTimeoutSeconds'] = self.readiness_probe_timeout_seconds
        if self.security_context_capability_adds is not None:
            result['SecurityContextCapabilityAdds'] = self.security_context_capability_adds
        if self.security_context_read_only_root_filesystem is not None:
            result['SecurityContextReadOnlyRootFilesystem'] = self.security_context_read_only_root_filesystem
        if self.security_context_run_as_user is not None:
            result['SecurityContextRunAsUser'] = self.security_context_run_as_user
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('LivenessProbeExecCommands') is not None:
            self.liveness_probe_exec_commands = m.get('LivenessProbeExecCommands')
        if m.get('LivenessProbeFailureThreshold') is not None:
            self.liveness_probe_failure_threshold = m.get('LivenessProbeFailureThreshold')
        if m.get('LivenessProbeHttpGetPath') is not None:
            self.liveness_probe_http_get_path = m.get('LivenessProbeHttpGetPath')
        if m.get('LivenessProbeHttpGetPort') is not None:
            self.liveness_probe_http_get_port = m.get('LivenessProbeHttpGetPort')
        if m.get('LivenessProbeHttpGetScheme') is not None:
            self.liveness_probe_http_get_scheme = m.get('LivenessProbeHttpGetScheme')
        if m.get('LivenessProbeInitialDelaySeconds') is not None:
            self.liveness_probe_initial_delay_seconds = m.get('LivenessProbeInitialDelaySeconds')
        if m.get('LivenessProbePeriodSeconds') is not None:
            self.liveness_probe_period_seconds = m.get('LivenessProbePeriodSeconds')
        if m.get('LivenessProbeSuccessThreshold') is not None:
            self.liveness_probe_success_threshold = m.get('LivenessProbeSuccessThreshold')
        if m.get('LivenessProbeTcpSocketPort') is not None:
            self.liveness_probe_tcp_socket_port = m.get('LivenessProbeTcpSocketPort')
        if m.get('LivenessProbeTimeoutSeconds') is not None:
            self.liveness_probe_timeout_seconds = m.get('LivenessProbeTimeoutSeconds')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('ReadinessProbeExecCommands') is not None:
            self.readiness_probe_exec_commands = m.get('ReadinessProbeExecCommands')
        if m.get('ReadinessProbeFailureThreshold') is not None:
            self.readiness_probe_failure_threshold = m.get('ReadinessProbeFailureThreshold')
        if m.get('ReadinessProbeHttpGetPath') is not None:
            self.readiness_probe_http_get_path = m.get('ReadinessProbeHttpGetPath')
        if m.get('ReadinessProbeHttpGetPort') is not None:
            self.readiness_probe_http_get_port = m.get('ReadinessProbeHttpGetPort')
        if m.get('ReadinessProbeHttpGetScheme') is not None:
            self.readiness_probe_http_get_scheme = m.get('ReadinessProbeHttpGetScheme')
        if m.get('ReadinessProbeInitialDelaySeconds') is not None:
            self.readiness_probe_initial_delay_seconds = m.get('ReadinessProbeInitialDelaySeconds')
        if m.get('ReadinessProbePeriodSeconds') is not None:
            self.readiness_probe_period_seconds = m.get('ReadinessProbePeriodSeconds')
        if m.get('ReadinessProbeSuccessThreshold') is not None:
            self.readiness_probe_success_threshold = m.get('ReadinessProbeSuccessThreshold')
        if m.get('ReadinessProbeTcpSocketPort') is not None:
            self.readiness_probe_tcp_socket_port = m.get('ReadinessProbeTcpSocketPort')
        if m.get('ReadinessProbeTimeoutSeconds') is not None:
            self.readiness_probe_timeout_seconds = m.get('ReadinessProbeTimeoutSeconds')
        if m.get('SecurityContextCapabilityAdds') is not None:
            self.security_context_capability_adds = m.get('SecurityContextCapabilityAdds')
        if m.get('SecurityContextReadOnlyRootFilesystem') is not None:
            self.security_context_read_only_root_filesystem = m.get('SecurityContextReadOnlyRootFilesystem')
        if m.get('SecurityContextRunAsUser') is not None:
            self.security_context_run_as_user = m.get('SecurityContextRunAsUser')
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsDnsConfigOptions(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsHostAliases(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        self.hostnames = hostnames
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsImageRegistryCredentials(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerEnvironmentVars(TeaModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref_field_path = field_ref_field_path
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        self.mount_path = mount_path
        self.mount_propagation = mount_propagation
        self.name = name
        self.read_only = read_only
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainers(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        init_container_args: List[str] = None,
        init_container_commands: List[str] = None,
        init_container_environment_vars: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerEnvironmentVars] = None,
        init_container_ports: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerPorts] = None,
        init_container_volume_mounts: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerVolumeMounts] = None,
        memory: float = None,
        name: str = None,
        security_context_capability_adds: List[str] = None,
        security_context_read_only_root_filesystem: bool = None,
        security_context_run_as_user: str = None,
        working_dir: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.image = image
        self.image_pull_policy = image_pull_policy
        self.init_container_args = init_container_args
        self.init_container_commands = init_container_commands
        self.init_container_environment_vars = init_container_environment_vars
        self.init_container_ports = init_container_ports
        self.init_container_volume_mounts = init_container_volume_mounts
        self.memory = memory
        self.name = name
        self.security_context_capability_adds = security_context_capability_adds
        self.security_context_read_only_root_filesystem = security_context_read_only_root_filesystem
        self.security_context_run_as_user = security_context_run_as_user
        self.working_dir = working_dir

    def validate(self):
        if self.init_container_environment_vars:
            for k in self.init_container_environment_vars:
                if k:
                    k.validate()
        if self.init_container_ports:
            for k in self.init_container_ports:
                if k:
                    k.validate()
        if self.init_container_volume_mounts:
            for k in self.init_container_volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.init_container_args is not None:
            result['InitContainerArgs'] = self.init_container_args
        if self.init_container_commands is not None:
            result['InitContainerCommands'] = self.init_container_commands
        result['InitContainerEnvironmentVars'] = []
        if self.init_container_environment_vars is not None:
            for k in self.init_container_environment_vars:
                result['InitContainerEnvironmentVars'].append(k.to_map() if k else None)
        result['InitContainerPorts'] = []
        if self.init_container_ports is not None:
            for k in self.init_container_ports:
                result['InitContainerPorts'].append(k.to_map() if k else None)
        result['InitContainerVolumeMounts'] = []
        if self.init_container_volume_mounts is not None:
            for k in self.init_container_volume_mounts:
                result['InitContainerVolumeMounts'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.security_context_capability_adds is not None:
            result['SecurityContextCapabilityAdds'] = self.security_context_capability_adds
        if self.security_context_read_only_root_filesystem is not None:
            result['SecurityContextReadOnlyRootFilesystem'] = self.security_context_read_only_root_filesystem
        if self.security_context_run_as_user is not None:
            result['SecurityContextRunAsUser'] = self.security_context_run_as_user
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('InitContainerArgs') is not None:
            self.init_container_args = m.get('InitContainerArgs')
        if m.get('InitContainerCommands') is not None:
            self.init_container_commands = m.get('InitContainerCommands')
        self.init_container_environment_vars = []
        if m.get('InitContainerEnvironmentVars') is not None:
            for k in m.get('InitContainerEnvironmentVars'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerEnvironmentVars()
                self.init_container_environment_vars.append(temp_model.from_map(k))
        self.init_container_ports = []
        if m.get('InitContainerPorts') is not None:
            for k in m.get('InitContainerPorts'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerPorts()
                self.init_container_ports.append(temp_model.from_map(k))
        self.init_container_volume_mounts = []
        if m.get('InitContainerVolumeMounts') is not None:
            for k in m.get('InitContainerVolumeMounts'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerVolumeMounts()
                self.init_container_volume_mounts.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityContextCapabilityAdds') is not None:
            self.security_context_capability_adds = m.get('SecurityContextCapabilityAdds')
        if m.get('SecurityContextReadOnlyRootFilesystem') is not None:
            self.security_context_read_only_root_filesystem = m.get('SecurityContextReadOnlyRootFilesystem')
        if m.get('SecurityContextRunAsUser') is not None:
            self.security_context_run_as_user = m.get('SecurityContextRunAsUser')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsSecurityContextSysCtls(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumesConfigFileVolumeConfigFileToPaths(TeaModel):
    def __init__(
        self,
        content: str = None,
        mode: int = None,
        path: str = None,
    ):
        self.content = content
        self.mode = mode
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumes(TeaModel):
    def __init__(
        self,
        config_file_volume_config_file_to_paths: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumesConfigFileVolumeConfigFileToPaths] = None,
        config_file_volume_default_mode: int = None,
        disk_volume_disk_id: str = None,
        disk_volume_disk_size: int = None,
        disk_volume_fs_type: str = None,
        empty_dir_volume_medium: str = None,
        flex_volume_driver: str = None,
        flex_volume_fs_type: str = None,
        flex_volume_options: str = None,
        nfsvolume_path: str = None,
        nfsvolume_read_only: bool = None,
        nfsvolume_server: str = None,
        name: str = None,
        type: str = None,
    ):
        self.config_file_volume_config_file_to_paths = config_file_volume_config_file_to_paths
        self.config_file_volume_default_mode = config_file_volume_default_mode
        self.disk_volume_disk_id = disk_volume_disk_id
        self.disk_volume_disk_size = disk_volume_disk_size
        self.disk_volume_fs_type = disk_volume_fs_type
        self.empty_dir_volume_medium = empty_dir_volume_medium
        self.flex_volume_driver = flex_volume_driver
        self.flex_volume_fs_type = flex_volume_fs_type
        self.flex_volume_options = flex_volume_options
        self.nfsvolume_path = nfsvolume_path
        self.nfsvolume_read_only = nfsvolume_read_only
        self.nfsvolume_server = nfsvolume_server
        self.name = name
        self.type = type

    def validate(self):
        if self.config_file_volume_config_file_to_paths:
            for k in self.config_file_volume_config_file_to_paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigFileVolumeConfigFileToPaths'] = []
        if self.config_file_volume_config_file_to_paths is not None:
            for k in self.config_file_volume_config_file_to_paths:
                result['ConfigFileVolumeConfigFileToPaths'].append(k.to_map() if k else None)
        if self.config_file_volume_default_mode is not None:
            result['ConfigFileVolumeDefaultMode'] = self.config_file_volume_default_mode
        if self.disk_volume_disk_id is not None:
            result['DiskVolumeDiskId'] = self.disk_volume_disk_id
        if self.disk_volume_disk_size is not None:
            result['DiskVolumeDiskSize'] = self.disk_volume_disk_size
        if self.disk_volume_fs_type is not None:
            result['DiskVolumeFsType'] = self.disk_volume_fs_type
        if self.empty_dir_volume_medium is not None:
            result['EmptyDirVolumeMedium'] = self.empty_dir_volume_medium
        if self.flex_volume_driver is not None:
            result['FlexVolumeDriver'] = self.flex_volume_driver
        if self.flex_volume_fs_type is not None:
            result['FlexVolumeFsType'] = self.flex_volume_fs_type
        if self.flex_volume_options is not None:
            result['FlexVolumeOptions'] = self.flex_volume_options
        if self.nfsvolume_path is not None:
            result['NFSVolumePath'] = self.nfsvolume_path
        if self.nfsvolume_read_only is not None:
            result['NFSVolumeReadOnly'] = self.nfsvolume_read_only
        if self.nfsvolume_server is not None:
            result['NFSVolumeServer'] = self.nfsvolume_server
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_file_volume_config_file_to_paths = []
        if m.get('ConfigFileVolumeConfigFileToPaths') is not None:
            for k in m.get('ConfigFileVolumeConfigFileToPaths'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumesConfigFileVolumeConfigFileToPaths()
                self.config_file_volume_config_file_to_paths.append(temp_model.from_map(k))
        if m.get('ConfigFileVolumeDefaultMode') is not None:
            self.config_file_volume_default_mode = m.get('ConfigFileVolumeDefaultMode')
        if m.get('DiskVolumeDiskId') is not None:
            self.disk_volume_disk_id = m.get('DiskVolumeDiskId')
        if m.get('DiskVolumeDiskSize') is not None:
            self.disk_volume_disk_size = m.get('DiskVolumeDiskSize')
        if m.get('DiskVolumeFsType') is not None:
            self.disk_volume_fs_type = m.get('DiskVolumeFsType')
        if m.get('EmptyDirVolumeMedium') is not None:
            self.empty_dir_volume_medium = m.get('EmptyDirVolumeMedium')
        if m.get('FlexVolumeDriver') is not None:
            self.flex_volume_driver = m.get('FlexVolumeDriver')
        if m.get('FlexVolumeFsType') is not None:
            self.flex_volume_fs_type = m.get('FlexVolumeFsType')
        if m.get('FlexVolumeOptions') is not None:
            self.flex_volume_options = m.get('FlexVolumeOptions')
        if m.get('NFSVolumePath') is not None:
            self.nfsvolume_path = m.get('NFSVolumePath')
        if m.get('NFSVolumeReadOnly') is not None:
            self.nfsvolume_read_only = m.get('NFSVolumeReadOnly')
        if m.get('NFSVolumeServer') is not None:
            self.nfsvolume_server = m.get('NFSVolumeServer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeEciScalingConfigurationsResponseBodyScalingConfigurations(TeaModel):
    def __init__(
        self,
        acr_registry_infos: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsAcrRegistryInfos] = None,
        active_deadline_seconds: int = None,
        auto_create_eip: bool = None,
        auto_match_image_cache: bool = None,
        container_group_name: str = None,
        containers: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainers] = None,
        cost_optimization: bool = None,
        cpu: float = None,
        cpu_options_core: int = None,
        cpu_options_threads_per_core: int = None,
        creation_time: str = None,
        description: str = None,
        dns_config_name_servers: List[str] = None,
        dns_config_options: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsDnsConfigOptions] = None,
        dns_config_searches: List[str] = None,
        dns_policy: str = None,
        egress_bandwidth: int = None,
        eip_bandwidth: int = None,
        ephemeral_storage: int = None,
        host_aliases: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsHostAliases] = None,
        host_name: str = None,
        image_registry_credentials: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsImageRegistryCredentials] = None,
        image_snapshot_id: str = None,
        ingress_bandwidth: int = None,
        init_containers: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainers] = None,
        instance_family_level: str = None,
        ipv_6address_count: int = None,
        lifecycle_state: str = None,
        load_balancer_weight: int = None,
        memory: float = None,
        ntp_servers: List[str] = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        restart_policy: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        security_context_sys_ctls: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsSecurityContextSysCtls] = None,
        security_group_id: str = None,
        sls_enable: bool = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        tags: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsTags] = None,
        termination_grace_period_seconds: int = None,
        volumes: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumes] = None,
    ):
        self.acr_registry_infos = acr_registry_infos
        self.active_deadline_seconds = active_deadline_seconds
        self.auto_create_eip = auto_create_eip
        self.auto_match_image_cache = auto_match_image_cache
        self.container_group_name = container_group_name
        self.containers = containers
        self.cost_optimization = cost_optimization
        self.cpu = cpu
        self.cpu_options_core = cpu_options_core
        self.cpu_options_threads_per_core = cpu_options_threads_per_core
        self.creation_time = creation_time
        self.description = description
        self.dns_config_name_servers = dns_config_name_servers
        self.dns_config_options = dns_config_options
        self.dns_config_searches = dns_config_searches
        self.dns_policy = dns_policy
        self.egress_bandwidth = egress_bandwidth
        self.eip_bandwidth = eip_bandwidth
        self.ephemeral_storage = ephemeral_storage
        self.host_aliases = host_aliases
        self.host_name = host_name
        self.image_registry_credentials = image_registry_credentials
        self.image_snapshot_id = image_snapshot_id
        self.ingress_bandwidth = ingress_bandwidth
        self.init_containers = init_containers
        self.instance_family_level = instance_family_level
        self.ipv_6address_count = ipv_6address_count
        self.lifecycle_state = lifecycle_state
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.ntp_servers = ntp_servers
        self.ram_role_name = ram_role_name
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.restart_policy = restart_policy
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_configuration_name = scaling_configuration_name
        self.scaling_group_id = scaling_group_id
        self.security_context_sys_ctls = security_context_sys_ctls
        self.security_group_id = security_group_id
        self.sls_enable = sls_enable
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.tags = tags
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.volumes = volumes

    def validate(self):
        if self.acr_registry_infos:
            for k in self.acr_registry_infos:
                if k:
                    k.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.dns_config_options:
            for k in self.dns_config_options:
                if k:
                    k.validate()
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.image_registry_credentials:
            for k in self.image_registry_credentials:
                if k:
                    k.validate()
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.security_context_sys_ctls:
            for k in self.security_context_sys_ctls:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfos'] = []
        if self.acr_registry_infos is not None:
            for k in self.acr_registry_infos:
                result['AcrRegistryInfos'].append(k.to_map() if k else None)
        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds
        if self.auto_create_eip is not None:
            result['AutoCreateEip'] = self.auto_create_eip
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.cost_optimization is not None:
            result['CostOptimization'] = self.cost_optimization
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_options_core is not None:
            result['CpuOptionsCore'] = self.cpu_options_core
        if self.cpu_options_threads_per_core is not None:
            result['CpuOptionsThreadsPerCore'] = self.cpu_options_threads_per_core
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dns_config_name_servers is not None:
            result['DnsConfigNameServers'] = self.dns_config_name_servers
        result['DnsConfigOptions'] = []
        if self.dns_config_options is not None:
            for k in self.dns_config_options:
                result['DnsConfigOptions'].append(k.to_map() if k else None)
        if self.dns_config_searches is not None:
            result['DnsConfigSearches'] = self.dns_config_searches
        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy
        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k in self.host_aliases:
                result['HostAliases'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['HostName'] = self.host_name
        result['ImageRegistryCredentials'] = []
        if self.image_registry_credentials is not None:
            for k in self.image_registry_credentials:
                result['ImageRegistryCredentials'].append(k.to_map() if k else None)
        if self.image_snapshot_id is not None:
            result['ImageSnapshotId'] = self.image_snapshot_id
        if self.ingress_bandwidth is not None:
            result['IngressBandwidth'] = self.ingress_bandwidth
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.ntp_servers is not None:
            result['NtpServers'] = self.ntp_servers
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        result['SecurityContextSysCtls'] = []
        if self.security_context_sys_ctls is not None:
            for k in self.security_context_sys_ctls:
                result['SecurityContextSysCtls'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sls_enable is not None:
            result['SlsEnable'] = self.sls_enable
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_infos = []
        if m.get('AcrRegistryInfos') is not None:
            for k in m.get('AcrRegistryInfos'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k))
        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')
        if m.get('AutoCreateEip') is not None:
            self.auto_create_eip = m.get('AutoCreateEip')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('CostOptimization') is not None:
            self.cost_optimization = m.get('CostOptimization')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuOptionsCore') is not None:
            self.cpu_options_core = m.get('CpuOptionsCore')
        if m.get('CpuOptionsThreadsPerCore') is not None:
            self.cpu_options_threads_per_core = m.get('CpuOptionsThreadsPerCore')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnsConfigNameServers') is not None:
            self.dns_config_name_servers = m.get('DnsConfigNameServers')
        self.dns_config_options = []
        if m.get('DnsConfigOptions') is not None:
            for k in m.get('DnsConfigOptions'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsDnsConfigOptions()
                self.dns_config_options.append(temp_model.from_map(k))
        if m.get('DnsConfigSearches') is not None:
            self.dns_config_searches = m.get('DnsConfigSearches')
        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')
        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k in m.get('HostAliases'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsHostAliases()
                self.host_aliases.append(temp_model.from_map(k))
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k in m.get('ImageRegistryCredentials'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k))
        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')
        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainers()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NtpServers') is not None:
            self.ntp_servers = m.get('NtpServers')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        self.security_context_sys_ctls = []
        if m.get('SecurityContextSysCtls') is not None:
            for k in m.get('SecurityContextSysCtls'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsSecurityContextSysCtls()
                self.security_context_sys_ctls.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SlsEnable') is not None:
            self.sls_enable = m.get('SlsEnable')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumes()
                self.volumes.append(temp_model.from_map(k))
        return self


class DescribeEciScalingConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_configurations: List[DescribeEciScalingConfigurationsResponseBodyScalingConfigurations] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_configurations = scaling_configurations
        self.total_count = total_count

    def validate(self):
        if self.scaling_configurations:
            for k in self.scaling_configurations:
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
        result['ScalingConfigurations'] = []
        if self.scaling_configurations is not None:
            for k in self.scaling_configurations:
                result['ScalingConfigurations'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scaling_configurations = []
        if m.get('ScalingConfigurations') is not None:
            for k in m.get('ScalingConfigurations'):
                temp_model = DescribeEciScalingConfigurationsResponseBodyScalingConfigurations()
                self.scaling_configurations.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEciScalingConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEciScalingConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEciScalingConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLifecycleActionsRequest(TeaModel):
    def __init__(
        self,
        lifecycle_action_status: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_activity_id: str = None,
    ):
        self.lifecycle_action_status = lifecycle_action_status
        self.max_results = max_results
        self.next_token = next_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle_action_status is not None:
            result['LifecycleActionStatus'] = self.lifecycle_action_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LifecycleActionStatus') is not None:
            self.lifecycle_action_status = m.get('LifecycleActionStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DescribeLifecycleActionsResponseBodyLifecycleActions(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        lifecycle_action_result: str = None,
        lifecycle_action_status: str = None,
        lifecycle_action_token: str = None,
        lifecycle_hook_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.lifecycle_action_result = lifecycle_action_result
        self.lifecycle_action_status = lifecycle_action_status
        self.lifecycle_action_token = lifecycle_action_token
        self.lifecycle_hook_id = lifecycle_hook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.lifecycle_action_result is not None:
            result['LifecycleActionResult'] = self.lifecycle_action_result
        if self.lifecycle_action_status is not None:
            result['LifecycleActionStatus'] = self.lifecycle_action_status
        if self.lifecycle_action_token is not None:
            result['LifecycleActionToken'] = self.lifecycle_action_token
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('LifecycleActionResult') is not None:
            self.lifecycle_action_result = m.get('LifecycleActionResult')
        if m.get('LifecycleActionStatus') is not None:
            self.lifecycle_action_status = m.get('LifecycleActionStatus')
        if m.get('LifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('LifecycleActionToken')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        return self


class DescribeLifecycleActionsResponseBody(TeaModel):
    def __init__(
        self,
        lifecycle_actions: List[DescribeLifecycleActionsResponseBodyLifecycleActions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.lifecycle_actions = lifecycle_actions
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_actions:
            for k in self.lifecycle_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LifecycleActions'] = []
        if self.lifecycle_actions is not None:
            for k in self.lifecycle_actions:
                result['LifecycleActions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_actions = []
        if m.get('LifecycleActions') is not None:
            for k in m.get('LifecycleActions'):
                temp_model = DescribeLifecycleActionsResponseBodyLifecycleActions()
                self.lifecycle_actions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLifecycleActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLifecycleActionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLifecycleActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLifecycleHooksRequest(TeaModel):
    def __init__(
        self,
        lifecycle_hook_ids: List[str] = None,
        lifecycle_hook_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.lifecycle_hook_ids = lifecycle_hook_ids
        self.lifecycle_hook_name = lifecycle_hook_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle_hook_ids is not None:
            result['LifecycleHookIds'] = self.lifecycle_hook_ids
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LifecycleHookIds') is not None:
            self.lifecycle_hook_ids = m.get('LifecycleHookIds')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeLifecycleHooksResponseBodyLifecycleHooks(TeaModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_hook_id: str = None,
        lifecycle_hook_name: str = None,
        lifecycle_hook_status: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
        scaling_group_id: str = None,
    ):
        self.default_result = default_result
        self.heartbeat_timeout = heartbeat_timeout
        self.lifecycle_hook_id = lifecycle_hook_id
        self.lifecycle_hook_name = lifecycle_hook_name
        self.lifecycle_hook_status = lifecycle_hook_status
        self.lifecycle_transition = lifecycle_transition
        self.notification_arn = notification_arn
        self.notification_metadata = notification_metadata
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.lifecycle_hook_status is not None:
            result['LifecycleHookStatus'] = self.lifecycle_hook_status
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('LifecycleHookStatus') is not None:
            self.lifecycle_hook_status = m.get('LifecycleHookStatus')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeLifecycleHooksResponseBody(TeaModel):
    def __init__(
        self,
        lifecycle_hooks: List[DescribeLifecycleHooksResponseBodyLifecycleHooks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.lifecycle_hooks = lifecycle_hooks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_hooks:
            for k in self.lifecycle_hooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LifecycleHooks'] = []
        if self.lifecycle_hooks is not None:
            for k in self.lifecycle_hooks:
                result['LifecycleHooks'].append(k.to_map() if k else None)
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
        self.lifecycle_hooks = []
        if m.get('LifecycleHooks') is not None:
            for k in m.get('LifecycleHooks'):
                temp_model = DescribeLifecycleHooksResponseBodyLifecycleHooks()
                self.lifecycle_hooks.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLifecycleHooksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLifecycleHooksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLifecycleHooksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLimitationRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DescribeLimitationResponseBody(TeaModel):
    def __init__(
        self,
        max_number_of_alb_server_group: int = None,
        max_number_of_dbinstances: int = None,
        max_number_of_lifecycle_hooks: int = None,
        max_number_of_load_balancers: int = None,
        max_number_of_max_size: int = None,
        max_number_of_min_size: int = None,
        max_number_of_notification_configurations: int = None,
        max_number_of_scaling_configurations: int = None,
        max_number_of_scaling_groups: int = None,
        max_number_of_scaling_instances: int = None,
        max_number_of_scaling_rules: int = None,
        max_number_of_scheduled_tasks: int = None,
        max_number_of_vserver_groups: int = None,
        request_id: str = None,
    ):
        self.max_number_of_alb_server_group = max_number_of_alb_server_group
        self.max_number_of_dbinstances = max_number_of_dbinstances
        self.max_number_of_lifecycle_hooks = max_number_of_lifecycle_hooks
        self.max_number_of_load_balancers = max_number_of_load_balancers
        self.max_number_of_max_size = max_number_of_max_size
        self.max_number_of_min_size = max_number_of_min_size
        self.max_number_of_notification_configurations = max_number_of_notification_configurations
        self.max_number_of_scaling_configurations = max_number_of_scaling_configurations
        self.max_number_of_scaling_groups = max_number_of_scaling_groups
        self.max_number_of_scaling_instances = max_number_of_scaling_instances
        self.max_number_of_scaling_rules = max_number_of_scaling_rules
        self.max_number_of_scheduled_tasks = max_number_of_scheduled_tasks
        self.max_number_of_vserver_groups = max_number_of_vserver_groups
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_number_of_alb_server_group is not None:
            result['MaxNumberOfAlbServerGroup'] = self.max_number_of_alb_server_group
        if self.max_number_of_dbinstances is not None:
            result['MaxNumberOfDBInstances'] = self.max_number_of_dbinstances
        if self.max_number_of_lifecycle_hooks is not None:
            result['MaxNumberOfLifecycleHooks'] = self.max_number_of_lifecycle_hooks
        if self.max_number_of_load_balancers is not None:
            result['MaxNumberOfLoadBalancers'] = self.max_number_of_load_balancers
        if self.max_number_of_max_size is not None:
            result['MaxNumberOfMaxSize'] = self.max_number_of_max_size
        if self.max_number_of_min_size is not None:
            result['MaxNumberOfMinSize'] = self.max_number_of_min_size
        if self.max_number_of_notification_configurations is not None:
            result['MaxNumberOfNotificationConfigurations'] = self.max_number_of_notification_configurations
        if self.max_number_of_scaling_configurations is not None:
            result['MaxNumberOfScalingConfigurations'] = self.max_number_of_scaling_configurations
        if self.max_number_of_scaling_groups is not None:
            result['MaxNumberOfScalingGroups'] = self.max_number_of_scaling_groups
        if self.max_number_of_scaling_instances is not None:
            result['MaxNumberOfScalingInstances'] = self.max_number_of_scaling_instances
        if self.max_number_of_scaling_rules is not None:
            result['MaxNumberOfScalingRules'] = self.max_number_of_scaling_rules
        if self.max_number_of_scheduled_tasks is not None:
            result['MaxNumberOfScheduledTasks'] = self.max_number_of_scheduled_tasks
        if self.max_number_of_vserver_groups is not None:
            result['MaxNumberOfVServerGroups'] = self.max_number_of_vserver_groups
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxNumberOfAlbServerGroup') is not None:
            self.max_number_of_alb_server_group = m.get('MaxNumberOfAlbServerGroup')
        if m.get('MaxNumberOfDBInstances') is not None:
            self.max_number_of_dbinstances = m.get('MaxNumberOfDBInstances')
        if m.get('MaxNumberOfLifecycleHooks') is not None:
            self.max_number_of_lifecycle_hooks = m.get('MaxNumberOfLifecycleHooks')
        if m.get('MaxNumberOfLoadBalancers') is not None:
            self.max_number_of_load_balancers = m.get('MaxNumberOfLoadBalancers')
        if m.get('MaxNumberOfMaxSize') is not None:
            self.max_number_of_max_size = m.get('MaxNumberOfMaxSize')
        if m.get('MaxNumberOfMinSize') is not None:
            self.max_number_of_min_size = m.get('MaxNumberOfMinSize')
        if m.get('MaxNumberOfNotificationConfigurations') is not None:
            self.max_number_of_notification_configurations = m.get('MaxNumberOfNotificationConfigurations')
        if m.get('MaxNumberOfScalingConfigurations') is not None:
            self.max_number_of_scaling_configurations = m.get('MaxNumberOfScalingConfigurations')
        if m.get('MaxNumberOfScalingGroups') is not None:
            self.max_number_of_scaling_groups = m.get('MaxNumberOfScalingGroups')
        if m.get('MaxNumberOfScalingInstances') is not None:
            self.max_number_of_scaling_instances = m.get('MaxNumberOfScalingInstances')
        if m.get('MaxNumberOfScalingRules') is not None:
            self.max_number_of_scaling_rules = m.get('MaxNumberOfScalingRules')
        if m.get('MaxNumberOfScheduledTasks') is not None:
            self.max_number_of_scheduled_tasks = m.get('MaxNumberOfScheduledTasks')
        if m.get('MaxNumberOfVServerGroups') is not None:
            self.max_number_of_vserver_groups = m.get('MaxNumberOfVServerGroups')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLimitationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLimitationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLimitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNotificationConfigurationsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels(TeaModel):
    def __init__(
        self,
        notification_arn: str = None,
        notification_types: List[str] = None,
        scaling_group_id: str = None,
    ):
        self.notification_arn = notification_arn
        self.notification_types = notification_types
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationTypes') is not None:
            self.notification_types = m.get('NotificationTypes')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeNotificationConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        notification_configuration_models: List[DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels] = None,
        request_id: str = None,
    ):
        self.notification_configuration_models = notification_configuration_models
        self.request_id = request_id

    def validate(self):
        if self.notification_configuration_models:
            for k in self.notification_configuration_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotificationConfigurationModels'] = []
        if self.notification_configuration_models is not None:
            for k in self.notification_configuration_models:
                result['NotificationConfigurationModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notification_configuration_models = []
        if m.get('NotificationConfigurationModels') is not None:
            for k in m.get('NotificationConfigurationModels'):
                temp_model = DescribeNotificationConfigurationsResponseBodyNotificationConfigurationModels()
                self.notification_configuration_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNotificationConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNotificationConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNotificationConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNotificationTypesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DescribeNotificationTypesResponseBody(TeaModel):
    def __init__(
        self,
        notification_types: List[str] = None,
        request_id: str = None,
    ):
        self.notification_types = notification_types
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationTypes') is not None:
            self.notification_types = m.get('NotificationTypes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNotificationTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNotificationTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNotificationTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.accept_language = accept_language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        classic_unavailable: bool = None,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        vpc_unavailable: bool = None,
    ):
        self.classic_unavailable = classic_unavailable
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id
        self.vpc_unavailable = vpc_unavailable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classic_unavailable is not None:
            result['ClassicUnavailable'] = self.classic_unavailable
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_unavailable is not None:
            result['VpcUnavailable'] = self.vpc_unavailable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassicUnavailable') is not None:
            self.classic_unavailable = m.get('ClassicUnavailable')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcUnavailable') is not None:
            self.vpc_unavailable = m.get('VpcUnavailable')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingActivitiesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_activity_ids: List[str] = None,
        scaling_group_id: str = None,
        status_code: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_activity_ids = scaling_activity_ids
        self.scaling_group_id = scaling_group_id
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_activity_ids is not None:
            result['ScalingActivityIds'] = self.scaling_activity_ids
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingActivityIds') is not None:
            self.scaling_activity_ids = m.get('ScalingActivityIds')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class DescribeScalingActivitiesResponseBodyScalingActivities(TeaModel):
    def __init__(
        self,
        attached_capacity: str = None,
        auto_created_capacity: str = None,
        cause: str = None,
        description: str = None,
        end_time: str = None,
        progress: int = None,
        scaling_activity_id: str = None,
        scaling_group_id: str = None,
        scaling_instance_number: int = None,
        start_time: str = None,
        status_code: str = None,
        status_message: str = None,
        total_capacity: str = None,
    ):
        self.attached_capacity = attached_capacity
        self.auto_created_capacity = auto_created_capacity
        self.cause = cause
        self.description = description
        self.end_time = end_time
        self.progress = progress
        self.scaling_activity_id = scaling_activity_id
        self.scaling_group_id = scaling_group_id
        self.scaling_instance_number = scaling_instance_number
        self.start_time = start_time
        self.status_code = status_code
        self.status_message = status_message
        self.total_capacity = total_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_capacity is not None:
            result['AttachedCapacity'] = self.attached_capacity
        if self.auto_created_capacity is not None:
            result['AutoCreatedCapacity'] = self.auto_created_capacity
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_instance_number is not None:
            result['ScalingInstanceNumber'] = self.scaling_instance_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedCapacity') is not None:
            self.attached_capacity = m.get('AttachedCapacity')
        if m.get('AutoCreatedCapacity') is not None:
            self.auto_created_capacity = m.get('AutoCreatedCapacity')
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingInstanceNumber') is not None:
            self.scaling_instance_number = m.get('ScalingInstanceNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        return self


class DescribeScalingActivitiesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_activities: List[DescribeScalingActivitiesResponseBodyScalingActivities] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_activities = scaling_activities
        self.total_count = total_count

    def validate(self):
        if self.scaling_activities:
            for k in self.scaling_activities:
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
        result['ScalingActivities'] = []
        if self.scaling_activities is not None:
            for k in self.scaling_activities:
                result['ScalingActivities'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scaling_activities = []
        if m.get('ScalingActivities') is not None:
            for k in m.get('ScalingActivities'):
                temp_model = DescribeScalingActivitiesResponseBodyScalingActivities()
                self.scaling_activities.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingActivitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingActivitiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingActivitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingActivityDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_activity_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DescribeScalingActivityDetailResponseBody(TeaModel):
    def __init__(
        self,
        detail: str = None,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.detail = detail
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DescribeScalingActivityDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingActivityDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingActivityDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingConfigurationsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_configuration_ids: List[str] = None,
        scaling_configuration_names: List[str] = None,
        scaling_group_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_configuration_ids = scaling_configuration_ids
        self.scaling_configuration_names = scaling_configuration_names
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_configuration_ids is not None:
            result['ScalingConfigurationIds'] = self.scaling_configuration_ids
        if self.scaling_configuration_names is not None:
            result['ScalingConfigurationNames'] = self.scaling_configuration_names
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingConfigurationIds') is not None:
            self.scaling_configuration_ids = m.get('ScalingConfigurationIds')
        if m.get('ScalingConfigurationNames') is not None:
            self.scaling_configuration_names = m.get('ScalingConfigurationNames')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        self.id = id
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsDataDisks(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        categories: List[str] = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.categories = categories
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.description = description
        self.device = device
        self.disk_name = disk_name
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.description is not None:
            result['Description'] = self.description
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstancePatternInfos(TeaModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burstable_performance: str = None,
        cores: int = None,
        excluded_instance_types: List[str] = None,
        instance_family_level: str = None,
        max_price: float = None,
        memory: float = None,
    ):
        self.architectures = architectures
        self.burstable_performance = burstable_performance
        self.cores = cores
        self.excluded_instance_types = excluded_instance_types
        self.instance_family_level = instance_family_level
        self.max_price = max_price
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architectures is not None:
            result['Architectures'] = self.architectures
        if self.burstable_performance is not None:
            result['BurstablePerformance'] = self.burstable_performance
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.excluded_instance_types is not None:
            result['ExcludedInstanceTypes'] = self.excluded_instance_types
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architectures') is not None:
            self.architectures = m.get('Architectures')
        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('ExcludedInstanceTypes') is not None:
            self.excluded_instance_types = m.get('ExcludedInstanceTypes')
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsSchedulerOptions(TeaModel):
    def __init__(
        self,
        managed_private_space_id: str = None,
    ):
        self.managed_private_space_id = managed_private_space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_private_space_id is not None:
            result['ManagedPrivateSpaceId'] = self.managed_private_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedPrivateSpaceId') is not None:
            self.managed_private_space_id = m.get('ManagedPrivateSpaceId')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsSpotPriceLimits(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        return self


class DescribeScalingConfigurationsResponseBodyScalingConfigurationsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeScalingConfigurationsResponseBodyScalingConfigurations(TeaModel):
    def __init__(
        self,
        private_pool_options: DescribeScalingConfigurationsResponseBodyScalingConfigurationsPrivatePoolOptions = None,
        affinity: str = None,
        cpu: int = None,
        creation_time: str = None,
        credit_specification: str = None,
        data_disks: List[DescribeScalingConfigurationsResponseBodyScalingConfigurationsDataDisks] = None,
        dedicated_host_id: str = None,
        deployment_set_id: str = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_description: str = None,
        instance_generation: str = None,
        instance_name: str = None,
        instance_pattern_infos: List[DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstancePatternInfos] = None,
        instance_type: str = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        lifecycle_state: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        scheduler_options: DescribeScalingConfigurationsResponseBodyScalingConfigurationsSchedulerOptions = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[DescribeScalingConfigurationsResponseBodyScalingConfigurationsSpotPriceLimits] = None,
        spot_strategy: str = None,
        system_disk_auto_snapshot_policy_id: str = None,
        system_disk_bursting_enabled: bool = None,
        system_disk_categories: List[str] = None,
        system_disk_category: str = None,
        system_disk_description: str = None,
        system_disk_encrypt_algorithm: str = None,
        system_disk_encrypted: bool = None,
        system_disk_kmskey_id: str = None,
        system_disk_name: str = None,
        system_disk_performance_level: str = None,
        system_disk_provisioned_iops: int = None,
        system_disk_size: int = None,
        tags: List[DescribeScalingConfigurationsResponseBodyScalingConfigurationsTags] = None,
        tenancy: str = None,
        user_data: str = None,
        weighted_capacities: List[int] = None,
        zone_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.affinity = affinity
        self.cpu = cpu
        self.creation_time = creation_time
        self.credit_specification = credit_specification
        self.data_disks = data_disks
        self.dedicated_host_id = dedicated_host_id
        self.deployment_set_id = deployment_set_id
        self.host_name = host_name
        self.hpc_cluster_id = hpc_cluster_id
        self.image_family = image_family
        self.image_id = image_id
        self.image_name = image_name
        self.instance_description = instance_description
        self.instance_generation = instance_generation
        self.instance_name = instance_name
        self.instance_pattern_infos = instance_pattern_infos
        self.instance_type = instance_type
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.io_optimized = io_optimized
        self.ipv_6address_count = ipv_6address_count
        self.key_pair_name = key_pair_name
        self.lifecycle_state = lifecycle_state
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.password_inherit = password_inherit
        self.ram_role_name = ram_role_name
        self.resource_group_id = resource_group_id
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_configuration_name = scaling_configuration_name
        self.scaling_group_id = scaling_group_id
        self.scheduler_options = scheduler_options
        self.security_enhancement_strategy = security_enhancement_strategy
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_duration = spot_duration
        self.spot_interruption_behavior = spot_interruption_behavior
        self.spot_price_limits = spot_price_limits
        self.spot_strategy = spot_strategy
        self.system_disk_auto_snapshot_policy_id = system_disk_auto_snapshot_policy_id
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        self.system_disk_categories = system_disk_categories
        self.system_disk_category = system_disk_category
        self.system_disk_description = system_disk_description
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        self.system_disk_encrypted = system_disk_encrypted
        self.system_disk_kmskey_id = system_disk_kmskey_id
        self.system_disk_name = system_disk_name
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        self.system_disk_size = system_disk_size
        self.tags = tags
        self.tenancy = tenancy
        self.user_data = user_data
        self.weighted_capacities = weighted_capacities
        self.zone_id = zone_id

    def validate(self):
        self.validate_required(self.private_pool_options, 'private_pool_options')
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.instance_pattern_infos:
            for k in self.instance_pattern_infos:
                if k:
                    k.validate()
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.spot_price_limits:
            for k in self.spot_price_limits:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['InstancePatternInfos'] = []
        if self.instance_pattern_infos is not None:
            for k in self.instance_pattern_infos:
                result['InstancePatternInfos'].append(k.to_map() if k else None)
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()
        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        result['SpotPriceLimits'] = []
        if self.spot_price_limits is not None:
            for k in self.spot_price_limits:
                result['SpotPriceLimits'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_auto_snapshot_policy_id is not None:
            result['SystemDiskAutoSnapshotPolicyId'] = self.system_disk_auto_snapshot_policy_id
        if self.system_disk_bursting_enabled is not None:
            result['SystemDiskBurstingEnabled'] = self.system_disk_bursting_enabled
        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_description is not None:
            result['SystemDiskDescription'] = self.system_disk_description
        if self.system_disk_encrypt_algorithm is not None:
            result['SystemDiskEncryptAlgorithm'] = self.system_disk_encrypt_algorithm
        if self.system_disk_encrypted is not None:
            result['SystemDiskEncrypted'] = self.system_disk_encrypted
        if self.system_disk_kmskey_id is not None:
            result['SystemDiskKMSKeyId'] = self.system_disk_kmskey_id
        if self.system_disk_name is not None:
            result['SystemDiskName'] = self.system_disk_name
        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level
        if self.system_disk_provisioned_iops is not None:
            result['SystemDiskProvisionedIops'] = self.system_disk_provisioned_iops
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.weighted_capacities is not None:
            result['WeightedCapacities'] = self.weighted_capacities
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.instance_pattern_infos = []
        if m.get('InstancePatternInfos') is not None:
            for k in m.get('InstancePatternInfos'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k))
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('SchedulerOptions') is not None:
            temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m['SchedulerOptions'])
        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k in m.get('SpotPriceLimits'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsSpotPriceLimits()
                self.spot_price_limits.append(temp_model.from_map(k))
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskAutoSnapshotPolicyId') is not None:
            self.system_disk_auto_snapshot_policy_id = m.get('SystemDiskAutoSnapshotPolicyId')
        if m.get('SystemDiskBurstingEnabled') is not None:
            self.system_disk_bursting_enabled = m.get('SystemDiskBurstingEnabled')
        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskDescription') is not None:
            self.system_disk_description = m.get('SystemDiskDescription')
        if m.get('SystemDiskEncryptAlgorithm') is not None:
            self.system_disk_encrypt_algorithm = m.get('SystemDiskEncryptAlgorithm')
        if m.get('SystemDiskEncrypted') is not None:
            self.system_disk_encrypted = m.get('SystemDiskEncrypted')
        if m.get('SystemDiskKMSKeyId') is not None:
            self.system_disk_kmskey_id = m.get('SystemDiskKMSKeyId')
        if m.get('SystemDiskName') is not None:
            self.system_disk_name = m.get('SystemDiskName')
        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')
        if m.get('SystemDiskProvisionedIops') is not None:
            self.system_disk_provisioned_iops = m.get('SystemDiskProvisionedIops')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurationsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('WeightedCapacities') is not None:
            self.weighted_capacities = m.get('WeightedCapacities')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeScalingConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_configurations: List[DescribeScalingConfigurationsResponseBodyScalingConfigurations] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_configurations = scaling_configurations
        self.total_count = total_count

    def validate(self):
        if self.scaling_configurations:
            for k in self.scaling_configurations:
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
        result['ScalingConfigurations'] = []
        if self.scaling_configurations is not None:
            for k in self.scaling_configurations:
                result['ScalingConfigurations'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scaling_configurations = []
        if m.get('ScalingConfigurations') is not None:
            for k in m.get('ScalingConfigurations'):
                temp_model = DescribeScalingConfigurationsResponseBodyScalingConfigurations()
                self.scaling_configurations.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingConfigurationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingGroupsRequest(TeaModel):
    def __init__(
        self,
        group_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_ids: List[str] = None,
        scaling_group_name: str = None,
        scaling_group_names: List[str] = None,
    ):
        self.group_type = group_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_ids = scaling_group_ids
        self.scaling_group_name = scaling_group_name
        self.scaling_group_names = scaling_group_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_ids is not None:
            result['ScalingGroupIds'] = self.scaling_group_ids
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.scaling_group_names is not None:
            result['ScalingGroupNames'] = self.scaling_group_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupIds') is not None:
            self.scaling_group_ids = m.get('ScalingGroupIds')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('ScalingGroupNames') is not None:
            self.scaling_group_names = m.get('ScalingGroupNames')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsAlbServerGroups(TeaModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
        weight: int = None,
    ):
        self.alb_server_group_id = alb_server_group_id
        self.port = port
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alb_server_group_id is not None:
            result['AlbServerGroupId'] = self.alb_server_group_id
        if self.port is not None:
            result['Port'] = self.port
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbServerGroupId') is not None:
            self.alb_server_group_id = m.get('AlbServerGroupId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsLaunchTemplateOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsVServerGroupsVServerGroupAttributes(TeaModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
        weight: int = None,
    ):
        self.port = port
        self.vserver_group_id = vserver_group_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeScalingGroupsResponseBodyScalingGroupsVServerGroups(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[DescribeScalingGroupsResponseBodyScalingGroupsVServerGroupsVServerGroupAttributes] = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.vserver_group_attributes = vserver_group_attributes

    def validate(self):
        if self.vserver_group_attributes:
            for k in self.vserver_group_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        result['VServerGroupAttributes'] = []
        if self.vserver_group_attributes is not None:
            for k in self.vserver_group_attributes:
                result['VServerGroupAttributes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        self.vserver_group_attributes = []
        if m.get('VServerGroupAttributes') is not None:
            for k in m.get('VServerGroupAttributes'):
                temp_model = DescribeScalingGroupsResponseBodyScalingGroupsVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k))
        return self


class DescribeScalingGroupsResponseBodyScalingGroups(TeaModel):
    def __init__(
        self,
        active_capacity: int = None,
        active_scaling_configuration_id: str = None,
        alb_server_groups: List[DescribeScalingGroupsResponseBodyScalingGroupsAlbServerGroups] = None,
        allocation_strategy: str = None,
        az_balance: bool = None,
        compensate_with_on_demand: bool = None,
        creation_time: str = None,
        current_host_name: str = None,
        dbinstance_ids: List[str] = None,
        default_cooldown: int = None,
        desired_capacity: int = None,
        group_deletion_protection: bool = None,
        group_type: str = None,
        health_check_type: str = None,
        is_elastic_strength_in_alarm: bool = None,
        launch_template_id: str = None,
        launch_template_overrides: List[DescribeScalingGroupsResponseBodyScalingGroupsLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        lifecycle_state: str = None,
        load_balancer_ids: List[str] = None,
        max_instance_lifetime: int = None,
        max_size: int = None,
        min_size: int = None,
        modification_time: str = None,
        monitor_group_id: str = None,
        multi_azpolicy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        pending_capacity: int = None,
        pending_wait_capacity: int = None,
        protected_capacity: int = None,
        region_id: str = None,
        removal_policies: List[str] = None,
        removing_capacity: int = None,
        removing_wait_capacity: int = None,
        scaling_group_id: str = None,
        scaling_group_name: str = None,
        scaling_policy: str = None,
        spot_allocation_strategy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        standby_capacity: int = None,
        stopped_capacity: int = None,
        suspended_processes: List[str] = None,
        system_suspended: bool = None,
        total_capacity: int = None,
        total_instance_count: int = None,
        vserver_groups: List[DescribeScalingGroupsResponseBodyScalingGroupsVServerGroups] = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.active_capacity = active_capacity
        self.active_scaling_configuration_id = active_scaling_configuration_id
        self.alb_server_groups = alb_server_groups
        self.allocation_strategy = allocation_strategy
        self.az_balance = az_balance
        self.compensate_with_on_demand = compensate_with_on_demand
        self.creation_time = creation_time
        self.current_host_name = current_host_name
        self.dbinstance_ids = dbinstance_ids
        self.default_cooldown = default_cooldown
        self.desired_capacity = desired_capacity
        self.group_deletion_protection = group_deletion_protection
        self.group_type = group_type
        self.health_check_type = health_check_type
        self.is_elastic_strength_in_alarm = is_elastic_strength_in_alarm
        self.launch_template_id = launch_template_id
        self.launch_template_overrides = launch_template_overrides
        self.launch_template_version = launch_template_version
        self.lifecycle_state = lifecycle_state
        self.load_balancer_ids = load_balancer_ids
        self.max_instance_lifetime = max_instance_lifetime
        self.max_size = max_size
        self.min_size = min_size
        self.modification_time = modification_time
        self.monitor_group_id = monitor_group_id
        self.multi_azpolicy = multi_azpolicy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.pending_capacity = pending_capacity
        self.pending_wait_capacity = pending_wait_capacity
        self.protected_capacity = protected_capacity
        self.region_id = region_id
        self.removal_policies = removal_policies
        self.removing_capacity = removing_capacity
        self.removing_wait_capacity = removing_wait_capacity
        self.scaling_group_id = scaling_group_id
        self.scaling_group_name = scaling_group_name
        self.scaling_policy = scaling_policy
        self.spot_allocation_strategy = spot_allocation_strategy
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.standby_capacity = standby_capacity
        self.stopped_capacity = stopped_capacity
        self.suspended_processes = suspended_processes
        self.system_suspended = system_suspended
        self.total_capacity = total_capacity
        self.total_instance_count = total_instance_count
        self.vserver_groups = vserver_groups
        self.v_switch_id = v_switch_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        if self.alb_server_groups:
            for k in self.alb_server_groups:
                if k:
                    k.validate()
        if self.launch_template_overrides:
            for k in self.launch_template_overrides:
                if k:
                    k.validate()
        if self.vserver_groups:
            for k in self.vserver_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_capacity is not None:
            result['ActiveCapacity'] = self.active_capacity
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        result['AlbServerGroups'] = []
        if self.alb_server_groups is not None:
            for k in self.alb_server_groups:
                result['AlbServerGroups'].append(k.to_map() if k else None)
        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy
        if self.az_balance is not None:
            result['AzBalance'] = self.az_balance
        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.current_host_name is not None:
            result['CurrentHostName'] = self.current_host_name
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.is_elastic_strength_in_alarm is not None:
            result['IsElasticStrengthInAlarm'] = self.is_elastic_strength_in_alarm
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k.to_map() if k else None)
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.max_instance_lifetime is not None:
            result['MaxInstanceLifetime'] = self.max_instance_lifetime
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.monitor_group_id is not None:
            result['MonitorGroupId'] = self.monitor_group_id
        if self.multi_azpolicy is not None:
            result['MultiAZPolicy'] = self.multi_azpolicy
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.pending_capacity is not None:
            result['PendingCapacity'] = self.pending_capacity
        if self.pending_wait_capacity is not None:
            result['PendingWaitCapacity'] = self.pending_wait_capacity
        if self.protected_capacity is not None:
            result['ProtectedCapacity'] = self.protected_capacity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.removal_policies is not None:
            result['RemovalPolicies'] = self.removal_policies
        if self.removing_capacity is not None:
            result['RemovingCapacity'] = self.removing_capacity
        if self.removing_wait_capacity is not None:
            result['RemovingWaitCapacity'] = self.removing_wait_capacity
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy
        if self.spot_allocation_strategy is not None:
            result['SpotAllocationStrategy'] = self.spot_allocation_strategy
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.standby_capacity is not None:
            result['StandbyCapacity'] = self.standby_capacity
        if self.stopped_capacity is not None:
            result['StoppedCapacity'] = self.stopped_capacity
        if self.suspended_processes is not None:
            result['SuspendedProcesses'] = self.suspended_processes
        if self.system_suspended is not None:
            result['SystemSuspended'] = self.system_suspended
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.total_instance_count is not None:
            result['TotalInstanceCount'] = self.total_instance_count
        result['VServerGroups'] = []
        if self.vserver_groups is not None:
            for k in self.vserver_groups:
                result['VServerGroups'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCapacity') is not None:
            self.active_capacity = m.get('ActiveCapacity')
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        self.alb_server_groups = []
        if m.get('AlbServerGroups') is not None:
            for k in m.get('AlbServerGroups'):
                temp_model = DescribeScalingGroupsResponseBodyScalingGroupsAlbServerGroups()
                self.alb_server_groups.append(temp_model.from_map(k))
        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')
        if m.get('AzBalance') is not None:
            self.az_balance = m.get('AzBalance')
        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CurrentHostName') is not None:
            self.current_host_name = m.get('CurrentHostName')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('IsElasticStrengthInAlarm') is not None:
            self.is_elastic_strength_in_alarm = m.get('IsElasticStrengthInAlarm')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k in m.get('LaunchTemplateOverrides'):
                temp_model = DescribeScalingGroupsResponseBodyScalingGroupsLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k))
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('MaxInstanceLifetime') is not None:
            self.max_instance_lifetime = m.get('MaxInstanceLifetime')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('MonitorGroupId') is not None:
            self.monitor_group_id = m.get('MonitorGroupId')
        if m.get('MultiAZPolicy') is not None:
            self.multi_azpolicy = m.get('MultiAZPolicy')
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('PendingCapacity') is not None:
            self.pending_capacity = m.get('PendingCapacity')
        if m.get('PendingWaitCapacity') is not None:
            self.pending_wait_capacity = m.get('PendingWaitCapacity')
        if m.get('ProtectedCapacity') is not None:
            self.protected_capacity = m.get('ProtectedCapacity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemovalPolicies') is not None:
            self.removal_policies = m.get('RemovalPolicies')
        if m.get('RemovingCapacity') is not None:
            self.removing_capacity = m.get('RemovingCapacity')
        if m.get('RemovingWaitCapacity') is not None:
            self.removing_wait_capacity = m.get('RemovingWaitCapacity')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')
        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('StandbyCapacity') is not None:
            self.standby_capacity = m.get('StandbyCapacity')
        if m.get('StoppedCapacity') is not None:
            self.stopped_capacity = m.get('StoppedCapacity')
        if m.get('SuspendedProcesses') is not None:
            self.suspended_processes = m.get('SuspendedProcesses')
        if m.get('SystemSuspended') is not None:
            self.system_suspended = m.get('SystemSuspended')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')
        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k in m.get('VServerGroups'):
                temp_model = DescribeScalingGroupsResponseBodyScalingGroupsVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeScalingGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_groups: List[DescribeScalingGroupsResponseBodyScalingGroups] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_groups = scaling_groups
        self.total_count = total_count

    def validate(self):
        if self.scaling_groups:
            for k in self.scaling_groups:
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
        result['ScalingGroups'] = []
        if self.scaling_groups is not None:
            for k in self.scaling_groups:
                result['ScalingGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scaling_groups = []
        if m.get('ScalingGroups') is not None:
            for k in m.get('ScalingGroups'):
                temp_model = DescribeScalingGroupsResponseBodyScalingGroups()
                self.scaling_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingInstancesRequest(TeaModel):
    def __init__(
        self,
        creation_type: str = None,
        health_status: str = None,
        instance_ids: List[str] = None,
        lifecycle_state: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_activity_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
    ):
        self.creation_type = creation_type
        self.health_status = health_status
        self.instance_ids = instance_ids
        self.lifecycle_state = lifecycle_state
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_activity_id = scaling_activity_id
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_type is not None:
            result['CreationType'] = self.creation_type
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DescribeScalingInstancesResponseBodyScalingInstances(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        creation_time: str = None,
        creation_type: str = None,
        entrusted: bool = None,
        health_status: str = None,
        instance_id: str = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        lifecycle_state: str = None,
        load_balancer_weight: int = None,
        scaling_activity_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
        spot_strategy: str = None,
        warmup_state: str = None,
        weighted_capacity: int = None,
        zone_id: str = None,
    ):
        self.created_time = created_time
        self.creation_time = creation_time
        self.creation_type = creation_type
        self.entrusted = entrusted
        self.health_status = health_status
        self.instance_id = instance_id
        self.launch_template_id = launch_template_id
        self.launch_template_version = launch_template_version
        self.lifecycle_state = lifecycle_state
        self.load_balancer_weight = load_balancer_weight
        self.scaling_activity_id = scaling_activity_id
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_group_id = scaling_group_id
        self.spot_strategy = spot_strategy
        self.warmup_state = warmup_state
        self.weighted_capacity = weighted_capacity
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.creation_type is not None:
            result['CreationType'] = self.creation_type
        if self.entrusted is not None:
            result['Entrusted'] = self.entrusted
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.warmup_state is not None:
            result['WarmupState'] = self.warmup_state
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')
        if m.get('Entrusted') is not None:
            self.entrusted = m.get('Entrusted')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('WarmupState') is not None:
            self.warmup_state = m.get('WarmupState')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeScalingInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_instances: List[DescribeScalingInstancesResponseBodyScalingInstances] = None,
        total_count: int = None,
        total_spot_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_instances = scaling_instances
        self.total_count = total_count
        self.total_spot_count = total_spot_count

    def validate(self):
        if self.scaling_instances:
            for k in self.scaling_instances:
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
        result['ScalingInstances'] = []
        if self.scaling_instances is not None:
            for k in self.scaling_instances:
                result['ScalingInstances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_spot_count is not None:
            result['TotalSpotCount'] = self.total_spot_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scaling_instances = []
        if m.get('ScalingInstances') is not None:
            for k in m.get('ScalingInstances'):
                temp_model = DescribeScalingInstancesResponseBodyScalingInstances()
                self.scaling_instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalSpotCount') is not None:
            self.total_spot_count = m.get('TotalSpotCount')
        return self


class DescribeScalingInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScalingRulesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scaling_rule_aris: List[str] = None,
        scaling_rule_ids: List[str] = None,
        scaling_rule_names: List[str] = None,
        scaling_rule_type: str = None,
        show_alarm_rules: bool = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id
        self.scaling_rule_aris = scaling_rule_aris
        self.scaling_rule_ids = scaling_rule_ids
        self.scaling_rule_names = scaling_rule_names
        self.scaling_rule_type = scaling_rule_type
        self.show_alarm_rules = show_alarm_rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_aris is not None:
            result['ScalingRuleAris'] = self.scaling_rule_aris
        if self.scaling_rule_ids is not None:
            result['ScalingRuleIds'] = self.scaling_rule_ids
        if self.scaling_rule_names is not None:
            result['ScalingRuleNames'] = self.scaling_rule_names
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        if self.show_alarm_rules is not None:
            result['ShowAlarmRules'] = self.show_alarm_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleAris') is not None:
            self.scaling_rule_aris = m.get('ScalingRuleAris')
        if m.get('ScalingRuleIds') is not None:
            self.scaling_rule_ids = m.get('ScalingRuleIds')
        if m.get('ScalingRuleNames') is not None:
            self.scaling_rule_names = m.get('ScalingRuleNames')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        if m.get('ShowAlarmRules') is not None:
            self.show_alarm_rules = m.get('ShowAlarmRules')
        return self


class DescribeScalingRulesResponseBodyScalingRulesAlarmsDimensions(TeaModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        self.dimension_key = dimension_key
        self.dimension_value = dimension_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class DescribeScalingRulesResponseBodyScalingRulesAlarms(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        alarm_task_name: str = None,
        comparison_operator: str = None,
        dimensions: List[DescribeScalingRulesResponseBodyScalingRulesAlarmsDimensions] = None,
        evaluation_count: int = None,
        metric_name: str = None,
        metric_type: str = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.alarm_task_name = alarm_task_name
        self.comparison_operator = comparison_operator
        self.dimensions = dimensions
        self.evaluation_count = evaluation_count
        self.metric_name = metric_name
        self.metric_type = metric_type
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.alarm_task_name is not None:
            result['AlarmTaskName'] = self.alarm_task_name
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('AlarmTaskName') is not None:
            self.alarm_task_name = m.get('AlarmTaskName')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesAlarmsDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DescribeScalingRulesResponseBodyScalingRulesStepAdjustments(TeaModel):
    def __init__(
        self,
        metric_interval_lower_bound: float = None,
        metric_interval_upper_bound: float = None,
        scaling_adjustment: int = None,
    ):
        self.metric_interval_lower_bound = metric_interval_lower_bound
        self.metric_interval_upper_bound = metric_interval_upper_bound
        self.scaling_adjustment = scaling_adjustment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_interval_lower_bound is not None:
            result['MetricIntervalLowerBound'] = self.metric_interval_lower_bound
        if self.metric_interval_upper_bound is not None:
            result['MetricIntervalUpperBound'] = self.metric_interval_upper_bound
        if self.scaling_adjustment is not None:
            result['ScalingAdjustment'] = self.scaling_adjustment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricIntervalLowerBound') is not None:
            self.metric_interval_lower_bound = m.get('MetricIntervalLowerBound')
        if m.get('MetricIntervalUpperBound') is not None:
            self.metric_interval_upper_bound = m.get('MetricIntervalUpperBound')
        if m.get('ScalingAdjustment') is not None:
            self.scaling_adjustment = m.get('ScalingAdjustment')
        return self


class DescribeScalingRulesResponseBodyScalingRules(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        alarms: List[DescribeScalingRulesResponseBodyScalingRulesAlarms] = None,
        cooldown: int = None,
        disable_scale_in: bool = None,
        estimated_instance_warmup: int = None,
        initial_max_size: int = None,
        max_size: int = None,
        metric_name: str = None,
        min_adjustment_magnitude: int = None,
        min_size: int = None,
        predictive_scaling_mode: str = None,
        predictive_task_buffer_time: int = None,
        predictive_value_behavior: str = None,
        predictive_value_buffer: int = None,
        scale_in_evaluation_count: int = None,
        scale_out_evaluation_count: int = None,
        scaling_group_id: str = None,
        scaling_rule_ari: str = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
        scaling_rule_type: str = None,
        step_adjustments: List[DescribeScalingRulesResponseBodyScalingRulesStepAdjustments] = None,
        target_value: float = None,
    ):
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.alarms = alarms
        self.cooldown = cooldown
        self.disable_scale_in = disable_scale_in
        self.estimated_instance_warmup = estimated_instance_warmup
        self.initial_max_size = initial_max_size
        self.max_size = max_size
        self.metric_name = metric_name
        self.min_adjustment_magnitude = min_adjustment_magnitude
        self.min_size = min_size
        self.predictive_scaling_mode = predictive_scaling_mode
        self.predictive_task_buffer_time = predictive_task_buffer_time
        self.predictive_value_behavior = predictive_value_behavior
        self.predictive_value_buffer = predictive_value_buffer
        self.scale_in_evaluation_count = scale_in_evaluation_count
        self.scale_out_evaluation_count = scale_out_evaluation_count
        self.scaling_group_id = scaling_group_id
        self.scaling_rule_ari = scaling_rule_ari
        self.scaling_rule_id = scaling_rule_id
        self.scaling_rule_name = scaling_rule_name
        self.scaling_rule_type = scaling_rule_type
        self.step_adjustments = step_adjustments
        self.target_value = target_value

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()
        if self.step_adjustments:
            for k in self.step_adjustments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.disable_scale_in is not None:
            result['DisableScaleIn'] = self.disable_scale_in
        if self.estimated_instance_warmup is not None:
            result['EstimatedInstanceWarmup'] = self.estimated_instance_warmup
        if self.initial_max_size is not None:
            result['InitialMaxSize'] = self.initial_max_size
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode
        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time
        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior
        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer
        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count
        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        result['StepAdjustments'] = []
        if self.step_adjustments is not None:
            for k in self.step_adjustments:
                result['StepAdjustments'].append(k.to_map() if k else None)
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesAlarms()
                self.alarms.append(temp_model.from_map(k))
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')
        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')
        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')
        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')
        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')
        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')
        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')
        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        self.step_adjustments = []
        if m.get('StepAdjustments') is not None:
            for k in m.get('StepAdjustments'):
                temp_model = DescribeScalingRulesResponseBodyScalingRulesStepAdjustments()
                self.step_adjustments.append(temp_model.from_map(k))
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        return self


class DescribeScalingRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_rules: List[DescribeScalingRulesResponseBodyScalingRules] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scaling_rules = scaling_rules
        self.total_count = total_count

    def validate(self):
        if self.scaling_rules:
            for k in self.scaling_rules:
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
        result['ScalingRules'] = []
        if self.scaling_rules is not None:
            for k in self.scaling_rules:
                result['ScalingRules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scaling_rules = []
        if m.get('ScalingRules') is not None:
            for k in m.get('ScalingRules'):
                temp_model = DescribeScalingRulesResponseBodyScalingRules()
                self.scaling_rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScalingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScalingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduledTasksRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scheduled_actions: List[str] = None,
        scheduled_task_ids: List[str] = None,
        scheduled_task_names: List[str] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id
        self.scheduled_actions = scheduled_actions
        self.scheduled_task_ids = scheduled_task_ids
        self.scheduled_task_names = scheduled_task_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scheduled_actions is not None:
            result['ScheduledActions'] = self.scheduled_actions
        if self.scheduled_task_ids is not None:
            result['ScheduledTaskIds'] = self.scheduled_task_ids
        if self.scheduled_task_names is not None:
            result['ScheduledTaskNames'] = self.scheduled_task_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScheduledActions') is not None:
            self.scheduled_actions = m.get('ScheduledActions')
        if m.get('ScheduledTaskIds') is not None:
            self.scheduled_task_ids = m.get('ScheduledTaskIds')
        if m.get('ScheduledTaskNames') is not None:
            self.scheduled_task_names = m.get('ScheduledTaskNames')
        return self


class DescribeScheduledTasksResponseBodyScheduledTasks(TeaModel):
    def __init__(
        self,
        description: str = None,
        desired_capacity: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        max_value: int = None,
        min_value: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        scaling_group_id: str = None,
        scheduled_action: str = None,
        scheduled_task_id: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        self.description = description
        self.desired_capacity = desired_capacity
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.max_value = max_value
        self.min_value = min_value
        self.recurrence_end_time = recurrence_end_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value
        self.scaling_group_id = scaling_group_id
        self.scheduled_action = scheduled_action
        self.scheduled_task_id = scheduled_task_id
        self.scheduled_task_name = scheduled_task_name
        self.task_enabled = task_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        return self


class DescribeScheduledTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scheduled_tasks: List[DescribeScheduledTasksResponseBodyScheduledTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scheduled_tasks = scheduled_tasks
        self.total_count = total_count

    def validate(self):
        if self.scheduled_tasks:
            for k in self.scheduled_tasks:
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
        result['ScheduledTasks'] = []
        if self.scheduled_tasks is not None:
            for k in self.scheduled_tasks:
                result['ScheduledTasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scheduled_tasks = []
        if m.get('ScheduledTasks') is not None:
            for k in m.get('ScheduledTasks'):
                temp_model = DescribeScheduledTasksResponseBodyScheduledTasks()
                self.scheduled_tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeScheduledTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScheduledTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeScheduledTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachAlbServerGroupsRequestAlbServerGroups(TeaModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
    ):
        self.alb_server_group_id = alb_server_group_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alb_server_group_id is not None:
            result['AlbServerGroupId'] = self.alb_server_group_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbServerGroupId') is not None:
            self.alb_server_group_id = m.get('AlbServerGroupId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DetachAlbServerGroupsRequest(TeaModel):
    def __init__(
        self,
        alb_server_groups: List[DetachAlbServerGroupsRequestAlbServerGroups] = None,
        client_token: str = None,
        force_detach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.alb_server_groups = alb_server_groups
        self.client_token = client_token
        self.force_detach = force_detach
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        if self.alb_server_groups:
            for k in self.alb_server_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlbServerGroups'] = []
        if self.alb_server_groups is not None:
            for k in self.alb_server_groups:
                result['AlbServerGroups'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_server_groups = []
        if m.get('AlbServerGroups') is not None:
            for k in m.get('AlbServerGroups'):
                temp_model = DetachAlbServerGroupsRequestAlbServerGroups()
                self.alb_server_groups.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DetachAlbServerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DetachAlbServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachAlbServerGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachAlbServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDBInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstances: List[str] = None,
        force_detach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.client_token = client_token
        self.dbinstances = dbinstances
        self.force_detach = force_detach
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances
        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstances') is not None:
            self.dbinstances = m.get('DBInstances')
        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DetachDBInstancesResponseBody(TeaModel):
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


class DetachDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachDBInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachInstancesRequest(TeaModel):
    def __init__(
        self,
        decrease_desired_capacity: bool = None,
        detach_option: str = None,
        instance_ids: List[str] = None,
        lifecycle_hook: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.decrease_desired_capacity = decrease_desired_capacity
        self.detach_option = detach_option
        self.instance_ids = instance_ids
        self.lifecycle_hook = lifecycle_hook
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decrease_desired_capacity is not None:
            result['DecreaseDesiredCapacity'] = self.decrease_desired_capacity
        if self.detach_option is not None:
            result['DetachOption'] = self.detach_option
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.lifecycle_hook is not None:
            result['LifecycleHook'] = self.lifecycle_hook
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DecreaseDesiredCapacity') is not None:
            self.decrease_desired_capacity = m.get('DecreaseDesiredCapacity')
        if m.get('DetachOption') is not None:
            self.detach_option = m.get('DetachOption')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('LifecycleHook') is not None:
            self.lifecycle_hook = m.get('LifecycleHook')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DetachInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DetachInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachLoadBalancersRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        client_token: str = None,
        force_detach: bool = None,
        load_balancers: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.async_ = async_
        self.client_token = client_token
        self.force_detach = force_detach
        self.load_balancers = load_balancers
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach
        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')
        if m.get('LoadBalancers') is not None:
            self.load_balancers = m.get('LoadBalancers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DetachLoadBalancersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class DetachLoadBalancersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachLoadBalancersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachVServerGroupsRequestVServerGroupsVServerGroupAttributes(TeaModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
    ):
        self.port = port
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        return self


class DetachVServerGroupsRequestVServerGroups(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[DetachVServerGroupsRequestVServerGroupsVServerGroupAttributes] = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.vserver_group_attributes = vserver_group_attributes

    def validate(self):
        if self.vserver_group_attributes:
            for k in self.vserver_group_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        result['VServerGroupAttributes'] = []
        if self.vserver_group_attributes is not None:
            for k in self.vserver_group_attributes:
                result['VServerGroupAttributes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        self.vserver_group_attributes = []
        if m.get('VServerGroupAttributes') is not None:
            for k in m.get('VServerGroupAttributes'):
                temp_model = DetachVServerGroupsRequestVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k))
        return self


class DetachVServerGroupsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        force_detach: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        vserver_groups: List[DetachVServerGroupsRequestVServerGroups] = None,
    ):
        self.client_token = client_token
        self.force_detach = force_detach
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id
        self.vserver_groups = vserver_groups

    def validate(self):
        if self.vserver_groups:
            for k in self.vserver_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        result['VServerGroups'] = []
        if self.vserver_groups is not None:
            for k in self.vserver_groups:
                result['VServerGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k in m.get('VServerGroups'):
                temp_model = DetachVServerGroupsRequestVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k))
        return self


class DetachVServerGroupsResponseBody(TeaModel):
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


class DetachVServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachVServerGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachVServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DisableAlarmResponseBody(TeaModel):
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


class DisableAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableScalingGroupRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
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
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class DisableScalingGroupResponseBody(TeaModel):
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


class DisableScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class EnableAlarmResponseBody(TeaModel):
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


class EnableAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableScalingGroupRequestLaunchTemplateOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class EnableScalingGroupRequest(TeaModel):
    def __init__(
        self,
        active_scaling_configuration_id: str = None,
        instance_ids: List[str] = None,
        launch_template_id: str = None,
        launch_template_overrides: List[EnableScalingGroupRequestLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        load_balancer_weights: List[int] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.active_scaling_configuration_id = active_scaling_configuration_id
        self.instance_ids = instance_ids
        self.launch_template_id = launch_template_id
        self.launch_template_overrides = launch_template_overrides
        self.launch_template_version = launch_template_version
        self.load_balancer_weights = load_balancer_weights
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        if self.launch_template_overrides:
            for k in self.launch_template_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k.to_map() if k else None)
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.load_balancer_weights is not None:
            result['LoadBalancerWeights'] = self.load_balancer_weights
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k in m.get('LaunchTemplateOverrides'):
                temp_model = EnableScalingGroupRequestLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k))
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('LoadBalancerWeights') is not None:
            self.load_balancer_weights = m.get('LoadBalancerWeights')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class EnableScalingGroupResponseBody(TeaModel):
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


class EnableScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnterStandbyRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        client_token: str = None,
        instance_ids: List[str] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.async_ = async_
        self.client_token = client_token
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class EnterStandbyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class EnterStandbyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnterStandbyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnterStandbyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteScalingRuleRequest(TeaModel):
    def __init__(
        self,
        breach_threshold: float = None,
        client_token: str = None,
        metric_value: float = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_rule_ari: str = None,
    ):
        self.breach_threshold = breach_threshold
        self.client_token = client_token
        self.metric_value = metric_value
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_rule_ari = scaling_rule_ari

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.breach_threshold is not None:
            result['BreachThreshold'] = self.breach_threshold
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreachThreshold') is not None:
            self.breach_threshold = m.get('BreachThreshold')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')
        return self


class ExecuteScalingRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class ExecuteScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExitStandbyRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        client_token: str = None,
        instance_ids: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.async_ = async_
        self.client_token = client_token
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class ExitStandbyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class ExitStandbyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExitStandbyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExitStandbyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_id: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        self.next_token = next_token
        self.owner_id = owner_id
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        keys: List[str] = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.keys = keys
        self.next_token = next_token
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tags: List[ListTagResourcesRequestTags] = None,
    ):
        self.next_token = next_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        propagate: bool = None,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.propagate = propagate
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.propagate is not None:
            result['Propagate'] = self.propagate
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Propagate') is not None:
            self.propagate = m.get('Propagate')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        next_token: str = None,
        owner_id: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        self.key = key
        self.next_token = next_token
        self.owner_id = owner_id
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        values: List[str] = None,
    ):
        self.next_token = next_token
        self.page_size = page_size
        self.request_id = request_id
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAlarmRequestDimensions(TeaModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        self.dimension_key = dimension_key
        self.dimension_value = dimension_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        return self


class ModifyAlarmRequestExpressions(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.comparison_operator = comparison_operator
        self.metric_name = metric_name
        self.period = period
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.period is not None:
            result['Period'] = self.period
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ModifyAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_actions: List[str] = None,
        alarm_task_id: str = None,
        comparison_operator: str = None,
        description: str = None,
        dimensions: List[ModifyAlarmRequestDimensions] = None,
        effective: str = None,
        evaluation_count: int = None,
        expressions: List[ModifyAlarmRequestExpressions] = None,
        expressions_logic_operator: str = None,
        group_id: int = None,
        metric_name: str = None,
        metric_type: str = None,
        name: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.alarm_actions = alarm_actions
        self.alarm_task_id = alarm_task_id
        self.comparison_operator = comparison_operator
        self.description = description
        self.dimensions = dimensions
        self.effective = effective
        self.evaluation_count = evaluation_count
        self.expressions = expressions
        self.expressions_logic_operator = expressions_logic_operator
        self.group_id = group_id
        self.metric_name = metric_name
        self.metric_type = metric_type
        self.name = name
        self.owner_id = owner_id
        self.period = period
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.expressions:
            for k in self.expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_actions is not None:
            result['AlarmActions'] = self.alarm_actions
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.description is not None:
            result['Description'] = self.description
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count
        result['Expressions'] = []
        if self.expressions is not None:
            for k in self.expressions:
                result['Expressions'].append(k.to_map() if k else None)
        if self.expressions_logic_operator is not None:
            result['ExpressionsLogicOperator'] = self.expressions_logic_operator
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmActions') is not None:
            self.alarm_actions = m.get('AlarmActions')
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ModifyAlarmRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')
        self.expressions = []
        if m.get('Expressions') is not None:
            for k in m.get('Expressions'):
                temp_model = ModifyAlarmRequestExpressions()
                self.expressions.append(temp_model.from_map(k))
        if m.get('ExpressionsLogicOperator') is not None:
            self.expressions_logic_operator = m.get('ExpressionsLogicOperator')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ModifyAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        request_id: str = None,
    ):
        self.alarm_task_id = alarm_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEciScalingConfigurationRequestAcrRegistryInfos(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.domains = domains
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyEciScalingConfigurationRequestContainersLivenessProbeExec(TeaModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class ModifyEciScalingConfigurationRequestContainersLivenessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class ModifyEciScalingConfigurationRequestContainersLivenessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyEciScalingConfigurationRequestContainersLivenessProbe(TeaModel):
    def __init__(
        self,
        exec: ModifyEciScalingConfigurationRequestContainersLivenessProbeExec = None,
        failure_threshold: int = None,
        http_get: ModifyEciScalingConfigurationRequestContainersLivenessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: ModifyEciScalingConfigurationRequestContainersLivenessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersLivenessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class ModifyEciScalingConfigurationRequestContainersReadinessProbeExec(TeaModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commands is not None:
            result['Commands'] = self.commands
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        return self


class ModifyEciScalingConfigurationRequestContainersReadinessProbeHttpGet(TeaModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        self.path = path
        self.port = port
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class ModifyEciScalingConfigurationRequestContainersReadinessProbeTcpSocket(TeaModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyEciScalingConfigurationRequestContainersReadinessProbe(TeaModel):
    def __init__(
        self,
        exec: ModifyEciScalingConfigurationRequestContainersReadinessProbeExec = None,
        failure_threshold: int = None,
        http_get: ModifyEciScalingConfigurationRequestContainersReadinessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: ModifyEciScalingConfigurationRequestContainersReadinessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        self.timeout_seconds = timeout_seconds

    def validate(self):
        self.validate_required(self.exec, 'exec')
        if self.exec:
            self.exec.validate()
        self.validate_required(self.http_get, 'http_get')
        if self.http_get:
            self.http_get.validate()
        self.validate_required(self.tcp_socket, 'tcp_socket')
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold
        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()
        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold
        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()
        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersReadinessProbeExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')
        if m.get('HttpGet') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m['HttpGet'])
        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')
        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')
        if m.get('TcpSocket') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m['TcpSocket'])
        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')
        return self


class ModifyEciScalingConfigurationRequestContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class ModifyEciScalingConfigurationRequestContainersSecurityContext(TeaModel):
    def __init__(
        self,
        capability: ModifyEciScalingConfigurationRequestContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class ModifyEciScalingConfigurationRequestContainersEnvironmentVarsFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class ModifyEciScalingConfigurationRequestContainersEnvironmentVars(TeaModel):
    def __init__(
        self,
        field_ref: ModifyEciScalingConfigurationRequestContainersEnvironmentVarsFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.field_ref, 'field_ref')
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersEnvironmentVarsFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyEciScalingConfigurationRequestContainersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class ModifyEciScalingConfigurationRequestContainersVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        self.mount_path = mount_path
        self.mount_propagation = mount_propagation
        self.name = name
        self.read_only = read_only
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class ModifyEciScalingConfigurationRequestContainers(TeaModel):
    def __init__(
        self,
        liveness_probe: ModifyEciScalingConfigurationRequestContainersLivenessProbe = None,
        readiness_probe: ModifyEciScalingConfigurationRequestContainersReadinessProbe = None,
        security_context: ModifyEciScalingConfigurationRequestContainersSecurityContext = None,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        environment_vars: List[ModifyEciScalingConfigurationRequestContainersEnvironmentVars] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        memory: float = None,
        name: str = None,
        ports: List[ModifyEciScalingConfigurationRequestContainersPorts] = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mounts: List[ModifyEciScalingConfigurationRequestContainersVolumeMounts] = None,
        working_dir: str = None,
    ):
        self.liveness_probe = liveness_probe
        self.readiness_probe = readiness_probe
        self.security_context = security_context
        self.args = args
        self.commands = commands
        self.cpu = cpu
        self.environment_vars = environment_vars
        self.gpu = gpu
        self.image = image
        self.image_pull_policy = image_pull_policy
        self.memory = memory
        self.name = name
        self.ports = ports
        self.stdin = stdin
        self.stdin_once = stdin_once
        self.tty = tty
        self.volume_mounts = volume_mounts
        self.working_dir = working_dir

    def validate(self):
        self.validate_required(self.liveness_probe, 'liveness_probe')
        if self.liveness_probe:
            self.liveness_probe.validate()
        self.validate_required(self.readiness_probe, 'readiness_probe')
        if self.readiness_probe:
            self.readiness_probe.validate()
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        if self.environment_vars:
            for k in self.environment_vars:
                if k:
                    k.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()
        if self.volume_mounts:
            for k in self.volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()
        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.args is not None:
            result['Args'] = self.args
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k in self.environment_vars:
                result['EnvironmentVars'].append(k.to_map() if k else None)
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.stdin is not None:
            result['Stdin'] = self.stdin
        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once
        if self.tty is not None:
            result['Tty'] = self.tty
        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k in self.volume_mounts:
                result['VolumeMounts'].append(k.to_map() if k else None)
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivenessProbe') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersLivenessProbe()
            self.liveness_probe = temp_model.from_map(m['LivenessProbe'])
        if m.get('ReadinessProbe') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersReadinessProbe()
            self.readiness_probe = temp_model.from_map(m['ReadinessProbe'])
        if m.get('SecurityContext') is not None:
            temp_model = ModifyEciScalingConfigurationRequestContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k in m.get('EnvironmentVars'):
                temp_model = ModifyEciScalingConfigurationRequestContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k))
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = ModifyEciScalingConfigurationRequestContainersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')
        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')
        if m.get('Tty') is not None:
            self.tty = m.get('Tty')
        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k in m.get('VolumeMounts'):
                temp_model = ModifyEciScalingConfigurationRequestContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k))
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class ModifyEciScalingConfigurationRequestDnsConfigOptions(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyEciScalingConfigurationRequestHostAliases(TeaModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        self.hostnames = hostnames
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class ModifyEciScalingConfigurationRequestImageRegistryCredentials(TeaModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.server = server
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.server is not None:
            result['Server'] = self.server
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyEciScalingConfigurationRequestInitContainersSecurityContextCapability(TeaModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adds is not None:
            result['Adds'] = self.adds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')
        return self


class ModifyEciScalingConfigurationRequestInitContainersSecurityContext(TeaModel):
    def __init__(
        self,
        capability: ModifyEciScalingConfigurationRequestInitContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user

    def validate(self):
        self.validate_required(self.capability, 'capability')
        if self.capability:
            self.capability.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()
        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem
        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = ModifyEciScalingConfigurationRequestInitContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m['Capability'])
        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')
        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')
        return self


class ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVarsFieldRef(TeaModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_path is not None:
            result['FieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')
        return self


class ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars(TeaModel):
    def __init__(
        self,
        field_ref: ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVarsFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.field_ref, 'field_ref')
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVarsFieldRef()
            self.field_ref = temp_model.from_map(m['FieldRef'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyEciScalingConfigurationRequestInitContainersInitContainerPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class ModifyEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts(TeaModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        self.mount_path = mount_path
        self.mount_propagation = mount_propagation
        self.name = name
        self.read_only = read_only
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation
        if self.name is not None:
            result['Name'] = self.name
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        return self


class ModifyEciScalingConfigurationRequestInitContainers(TeaModel):
    def __init__(
        self,
        security_context: ModifyEciScalingConfigurationRequestInitContainersSecurityContext = None,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        init_container_environment_vars: List[ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars] = None,
        init_container_ports: List[ModifyEciScalingConfigurationRequestInitContainersInitContainerPorts] = None,
        init_container_volume_mounts: List[ModifyEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts] = None,
        memory: float = None,
        name: str = None,
        working_dir: str = None,
    ):
        self.security_context = security_context
        self.args = args
        self.commands = commands
        self.cpu = cpu
        self.gpu = gpu
        self.image = image
        self.image_pull_policy = image_pull_policy
        self.init_container_environment_vars = init_container_environment_vars
        self.init_container_ports = init_container_ports
        self.init_container_volume_mounts = init_container_volume_mounts
        self.memory = memory
        self.name = name
        self.working_dir = working_dir

    def validate(self):
        self.validate_required(self.security_context, 'security_context')
        if self.security_context:
            self.security_context.validate()
        if self.init_container_environment_vars:
            for k in self.init_container_environment_vars:
                if k:
                    k.validate()
        if self.init_container_ports:
            for k in self.init_container_ports:
                if k:
                    k.validate()
        if self.init_container_volume_mounts:
            for k in self.init_container_volume_mounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()
        if self.args is not None:
            result['Args'] = self.args
        if self.commands is not None:
            result['Commands'] = self.commands
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy
        result['InitContainerEnvironmentVars'] = []
        if self.init_container_environment_vars is not None:
            for k in self.init_container_environment_vars:
                result['InitContainerEnvironmentVars'].append(k.to_map() if k else None)
        result['InitContainerPorts'] = []
        if self.init_container_ports is not None:
            for k in self.init_container_ports:
                result['InitContainerPorts'].append(k.to_map() if k else None)
        result['InitContainerVolumeMounts'] = []
        if self.init_container_volume_mounts is not None:
            for k in self.init_container_volume_mounts:
                result['InitContainerVolumeMounts'].append(k.to_map() if k else None)
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.name is not None:
            result['Name'] = self.name
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = ModifyEciScalingConfigurationRequestInitContainersSecurityContext()
            self.security_context = temp_model.from_map(m['SecurityContext'])
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')
        self.init_container_environment_vars = []
        if m.get('InitContainerEnvironmentVars') is not None:
            for k in m.get('InitContainerEnvironmentVars'):
                temp_model = ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars()
                self.init_container_environment_vars.append(temp_model.from_map(k))
        self.init_container_ports = []
        if m.get('InitContainerPorts') is not None:
            for k in m.get('InitContainerPorts'):
                temp_model = ModifyEciScalingConfigurationRequestInitContainersInitContainerPorts()
                self.init_container_ports.append(temp_model.from_map(k))
        self.init_container_volume_mounts = []
        if m.get('InitContainerVolumeMounts') is not None:
            for k in m.get('InitContainerVolumeMounts'):
                temp_model = ModifyEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts()
                self.init_container_volume_mounts.append(temp_model.from_map(k))
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class ModifyEciScalingConfigurationRequestSecurityContextSysCtls(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyEciScalingConfigurationRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyEciScalingConfigurationRequestVolumesDiskVolume(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        fs_type: str = None,
    ):
        self.disk_id = disk_id
        self.disk_size = disk_size
        self.fs_type = fs_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        return self


class ModifyEciScalingConfigurationRequestVolumesEmptyDirVolume(TeaModel):
    def __init__(
        self,
        medium: str = None,
    ):
        self.medium = medium

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.medium is not None:
            result['Medium'] = self.medium
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        return self


class ModifyEciScalingConfigurationRequestVolumesFlexVolume(TeaModel):
    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: str = None,
    ):
        self.driver = driver
        self.fs_type = fs_type
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver is not None:
            result['Driver'] = self.driver
        if self.fs_type is not None:
            result['FsType'] = self.fs_type
        if self.options is not None:
            result['Options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')
        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        return self


class ModifyEciScalingConfigurationRequestVolumesHostPathVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ModifyEciScalingConfigurationRequestVolumesNFSVolume(TeaModel):
    def __init__(
        self,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        self.path = path
        self.read_only = read_only
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class ModifyEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPath(TeaModel):
    def __init__(
        self,
        content: str = None,
        mode: int = None,
        path: str = None,
    ):
        self.content = content
        self.mode = mode
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ModifyEciScalingConfigurationRequestVolumes(TeaModel):
    def __init__(
        self,
        disk_volume: ModifyEciScalingConfigurationRequestVolumesDiskVolume = None,
        empty_dir_volume: ModifyEciScalingConfigurationRequestVolumesEmptyDirVolume = None,
        flex_volume: ModifyEciScalingConfigurationRequestVolumesFlexVolume = None,
        host_path_volume: ModifyEciScalingConfigurationRequestVolumesHostPathVolume = None,
        nfsvolume: ModifyEciScalingConfigurationRequestVolumesNFSVolume = None,
        config_file_volume_config_file_to_path: List[ModifyEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPath] = None,
        config_file_volume_default_mode: int = None,
        name: str = None,
        type: str = None,
    ):
        self.disk_volume = disk_volume
        self.empty_dir_volume = empty_dir_volume
        self.flex_volume = flex_volume
        self.host_path_volume = host_path_volume
        self.nfsvolume = nfsvolume
        self.config_file_volume_config_file_to_path = config_file_volume_config_file_to_path
        self.config_file_volume_default_mode = config_file_volume_default_mode
        self.name = name
        self.type = type

    def validate(self):
        self.validate_required(self.disk_volume, 'disk_volume')
        if self.disk_volume:
            self.disk_volume.validate()
        self.validate_required(self.empty_dir_volume, 'empty_dir_volume')
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()
        self.validate_required(self.flex_volume, 'flex_volume')
        if self.flex_volume:
            self.flex_volume.validate()
        self.validate_required(self.host_path_volume, 'host_path_volume')
        if self.host_path_volume:
            self.host_path_volume.validate()
        self.validate_required(self.nfsvolume, 'nfsvolume')
        if self.nfsvolume:
            self.nfsvolume.validate()
        if self.config_file_volume_config_file_to_path:
            for k in self.config_file_volume_config_file_to_path:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_volume is not None:
            result['DiskVolume'] = self.disk_volume.to_map()
        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()
        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()
        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()
        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()
        result['ConfigFileVolumeConfigFileToPath'] = []
        if self.config_file_volume_config_file_to_path is not None:
            for k in self.config_file_volume_config_file_to_path:
                result['ConfigFileVolumeConfigFileToPath'].append(k.to_map() if k else None)
        if self.config_file_volume_default_mode is not None:
            result['ConfigFileVolumeDefaultMode'] = self.config_file_volume_default_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskVolume') is not None:
            temp_model = ModifyEciScalingConfigurationRequestVolumesDiskVolume()
            self.disk_volume = temp_model.from_map(m['DiskVolume'])
        if m.get('EmptyDirVolume') is not None:
            temp_model = ModifyEciScalingConfigurationRequestVolumesEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m['EmptyDirVolume'])
        if m.get('FlexVolume') is not None:
            temp_model = ModifyEciScalingConfigurationRequestVolumesFlexVolume()
            self.flex_volume = temp_model.from_map(m['FlexVolume'])
        if m.get('HostPathVolume') is not None:
            temp_model = ModifyEciScalingConfigurationRequestVolumesHostPathVolume()
            self.host_path_volume = temp_model.from_map(m['HostPathVolume'])
        if m.get('NFSVolume') is not None:
            temp_model = ModifyEciScalingConfigurationRequestVolumesNFSVolume()
            self.nfsvolume = temp_model.from_map(m['NFSVolume'])
        self.config_file_volume_config_file_to_path = []
        if m.get('ConfigFileVolumeConfigFileToPath') is not None:
            for k in m.get('ConfigFileVolumeConfigFileToPath'):
                temp_model = ModifyEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPath()
                self.config_file_volume_config_file_to_path.append(temp_model.from_map(k))
        if m.get('ConfigFileVolumeDefaultMode') is not None:
            self.config_file_volume_default_mode = m.get('ConfigFileVolumeDefaultMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ModifyEciScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        acr_registry_infos: List[ModifyEciScalingConfigurationRequestAcrRegistryInfos] = None,
        active_deadline_seconds: int = None,
        auto_create_eip: bool = None,
        auto_match_image_cache: bool = None,
        container_group_name: str = None,
        containers: List[ModifyEciScalingConfigurationRequestContainers] = None,
        cost_optimization: bool = None,
        cpu: float = None,
        cpu_options_core: int = None,
        cpu_options_threads_per_core: int = None,
        description: str = None,
        dns_config_name_servers: List[str] = None,
        dns_config_options: List[ModifyEciScalingConfigurationRequestDnsConfigOptions] = None,
        dns_config_searchs: List[str] = None,
        dns_policy: str = None,
        egress_bandwidth: int = None,
        eip_bandwidth: int = None,
        enable_sls: bool = None,
        ephemeral_storage: int = None,
        host_aliases: List[ModifyEciScalingConfigurationRequestHostAliases] = None,
        host_name: str = None,
        image_registry_credentials: List[ModifyEciScalingConfigurationRequestImageRegistryCredentials] = None,
        image_snapshot_id: str = None,
        ingress_bandwidth: int = None,
        init_containers: List[ModifyEciScalingConfigurationRequestInitContainers] = None,
        instance_family_level: str = None,
        ipv_6address_count: int = None,
        load_balancer_weight: int = None,
        memory: float = None,
        ntp_servers: List[str] = None,
        owner_id: int = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        restart_policy: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        security_context_sys_ctls: List[ModifyEciScalingConfigurationRequestSecurityContextSysCtls] = None,
        security_group_id: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        tags: List[ModifyEciScalingConfigurationRequestTags] = None,
        termination_grace_period_seconds: int = None,
        volumes: List[ModifyEciScalingConfigurationRequestVolumes] = None,
    ):
        self.acr_registry_infos = acr_registry_infos
        self.active_deadline_seconds = active_deadline_seconds
        self.auto_create_eip = auto_create_eip
        self.auto_match_image_cache = auto_match_image_cache
        self.container_group_name = container_group_name
        self.containers = containers
        self.cost_optimization = cost_optimization
        self.cpu = cpu
        self.cpu_options_core = cpu_options_core
        self.cpu_options_threads_per_core = cpu_options_threads_per_core
        self.description = description
        self.dns_config_name_servers = dns_config_name_servers
        self.dns_config_options = dns_config_options
        self.dns_config_searchs = dns_config_searchs
        self.dns_policy = dns_policy
        self.egress_bandwidth = egress_bandwidth
        self.eip_bandwidth = eip_bandwidth
        self.enable_sls = enable_sls
        self.ephemeral_storage = ephemeral_storage
        self.host_aliases = host_aliases
        self.host_name = host_name
        self.image_registry_credentials = image_registry_credentials
        self.image_snapshot_id = image_snapshot_id
        self.ingress_bandwidth = ingress_bandwidth
        self.init_containers = init_containers
        self.instance_family_level = instance_family_level
        self.ipv_6address_count = ipv_6address_count
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.ntp_servers = ntp_servers
        self.owner_id = owner_id
        self.ram_role_name = ram_role_name
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.restart_policy = restart_policy
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_configuration_name = scaling_configuration_name
        self.security_context_sys_ctls = security_context_sys_ctls
        self.security_group_id = security_group_id
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.tags = tags
        self.termination_grace_period_seconds = termination_grace_period_seconds
        self.volumes = volumes

    def validate(self):
        if self.acr_registry_infos:
            for k in self.acr_registry_infos:
                if k:
                    k.validate()
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()
        if self.dns_config_options:
            for k in self.dns_config_options:
                if k:
                    k.validate()
        if self.host_aliases:
            for k in self.host_aliases:
                if k:
                    k.validate()
        if self.image_registry_credentials:
            for k in self.image_registry_credentials:
                if k:
                    k.validate()
        if self.init_containers:
            for k in self.init_containers:
                if k:
                    k.validate()
        if self.security_context_sys_ctls:
            for k in self.security_context_sys_ctls:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.volumes:
            for k in self.volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcrRegistryInfos'] = []
        if self.acr_registry_infos is not None:
            for k in self.acr_registry_infos:
                result['AcrRegistryInfos'].append(k.to_map() if k else None)
        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds
        if self.auto_create_eip is not None:
            result['AutoCreateEip'] = self.auto_create_eip
        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache
        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.cost_optimization is not None:
            result['CostOptimization'] = self.cost_optimization
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_options_core is not None:
            result['CpuOptionsCore'] = self.cpu_options_core
        if self.cpu_options_threads_per_core is not None:
            result['CpuOptionsThreadsPerCore'] = self.cpu_options_threads_per_core
        if self.description is not None:
            result['Description'] = self.description
        if self.dns_config_name_servers is not None:
            result['DnsConfigNameServers'] = self.dns_config_name_servers
        result['DnsConfigOptions'] = []
        if self.dns_config_options is not None:
            for k in self.dns_config_options:
                result['DnsConfigOptions'].append(k.to_map() if k else None)
        if self.dns_config_searchs is not None:
            result['DnsConfigSearchs'] = self.dns_config_searchs
        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy
        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.enable_sls is not None:
            result['EnableSls'] = self.enable_sls
        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage
        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k in self.host_aliases:
                result['HostAliases'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['HostName'] = self.host_name
        result['ImageRegistryCredentials'] = []
        if self.image_registry_credentials is not None:
            for k in self.image_registry_credentials:
                result['ImageRegistryCredentials'].append(k.to_map() if k else None)
        if self.image_snapshot_id is not None:
            result['ImageSnapshotId'] = self.image_snapshot_id
        if self.ingress_bandwidth is not None:
            result['IngressBandwidth'] = self.ingress_bandwidth
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k in self.init_containers:
                result['InitContainers'].append(k.to_map() if k else None)
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.ntp_servers is not None:
            result['NtpServers'] = self.ntp_servers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        result['SecurityContextSysCtls'] = []
        if self.security_context_sys_ctls is not None:
            for k in self.security_context_sys_ctls:
                result['SecurityContextSysCtls'].append(k.to_map() if k else None)
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        result['Volumes'] = []
        if self.volumes is not None:
            for k in self.volumes:
                result['Volumes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_infos = []
        if m.get('AcrRegistryInfos') is not None:
            for k in m.get('AcrRegistryInfos'):
                temp_model = ModifyEciScalingConfigurationRequestAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k))
        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')
        if m.get('AutoCreateEip') is not None:
            self.auto_create_eip = m.get('AutoCreateEip')
        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')
        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = ModifyEciScalingConfigurationRequestContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('CostOptimization') is not None:
            self.cost_optimization = m.get('CostOptimization')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuOptionsCore') is not None:
            self.cpu_options_core = m.get('CpuOptionsCore')
        if m.get('CpuOptionsThreadsPerCore') is not None:
            self.cpu_options_threads_per_core = m.get('CpuOptionsThreadsPerCore')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnsConfigNameServers') is not None:
            self.dns_config_name_servers = m.get('DnsConfigNameServers')
        self.dns_config_options = []
        if m.get('DnsConfigOptions') is not None:
            for k in m.get('DnsConfigOptions'):
                temp_model = ModifyEciScalingConfigurationRequestDnsConfigOptions()
                self.dns_config_options.append(temp_model.from_map(k))
        if m.get('DnsConfigSearchs') is not None:
            self.dns_config_searchs = m.get('DnsConfigSearchs')
        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')
        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EnableSls') is not None:
            self.enable_sls = m.get('EnableSls')
        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')
        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k in m.get('HostAliases'):
                temp_model = ModifyEciScalingConfigurationRequestHostAliases()
                self.host_aliases.append(temp_model.from_map(k))
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k in m.get('ImageRegistryCredentials'):
                temp_model = ModifyEciScalingConfigurationRequestImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k))
        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')
        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k in m.get('InitContainers'):
                temp_model = ModifyEciScalingConfigurationRequestInitContainers()
                self.init_containers.append(temp_model.from_map(k))
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NtpServers') is not None:
            self.ntp_servers = m.get('NtpServers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        self.security_context_sys_ctls = []
        if m.get('SecurityContextSysCtls') is not None:
            for k in m.get('SecurityContextSysCtls'):
                temp_model = ModifyEciScalingConfigurationRequestSecurityContextSysCtls()
                self.security_context_sys_ctls.append(temp_model.from_map(k))
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ModifyEciScalingConfigurationRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        self.volumes = []
        if m.get('Volumes') is not None:
            for k in m.get('Volumes'):
                temp_model = ModifyEciScalingConfigurationRequestVolumes()
                self.volumes.append(temp_model.from_map(k))
        return self


class ModifyEciScalingConfigurationResponseBody(TeaModel):
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


class ModifyEciScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyEciScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyEciScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLifecycleHookRequest(TeaModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_hook_id: str = None,
        lifecycle_hook_name: str = None,
        lifecycle_hook_status: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.default_result = default_result
        self.heartbeat_timeout = heartbeat_timeout
        self.lifecycle_hook_id = lifecycle_hook_id
        self.lifecycle_hook_name = lifecycle_hook_name
        self.lifecycle_hook_status = lifecycle_hook_status
        self.lifecycle_transition = lifecycle_transition
        self.notification_arn = notification_arn
        self.notification_metadata = notification_metadata
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout
        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id
        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name
        if self.lifecycle_hook_status is not None:
            result['LifecycleHookStatus'] = self.lifecycle_hook_status
        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')
        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')
        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')
        if m.get('LifecycleHookStatus') is not None:
            self.lifecycle_hook_status = m.get('LifecycleHookStatus')
        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class ModifyLifecycleHookResponseBody(TeaModel):
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


class ModifyLifecycleHookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLifecycleHookResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyLifecycleHookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNotificationConfigurationRequest(TeaModel):
    def __init__(
        self,
        notification_arn: str = None,
        notification_types: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.notification_arn = notification_arn
        self.notification_types = notification_types
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn
        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')
        if m.get('NotificationTypes') is not None:
            self.notification_types = m.get('NotificationTypes')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class ModifyNotificationConfigurationResponseBody(TeaModel):
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


class ModifyNotificationConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNotificationConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyNotificationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingConfigurationRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        self.id = id
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        return self


class ModifyScalingConfigurationRequestSystemDisk(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        description: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.description = description
        self.disk_name = disk_name
        self.encrypt_algorithm = encrypt_algorithm
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ModifyScalingConfigurationRequestDataDisks(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        categories: List[str] = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.categories = categories
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.description = description
        self.device = device
        self.disk_name = disk_name
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.description is not None:
            result['Description'] = self.description
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ModifyScalingConfigurationRequestInstancePatternInfos(TeaModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burstable_performance: str = None,
        cores: int = None,
        excluded_instance_types: List[str] = None,
        instance_family_level: str = None,
        max_price: float = None,
        memory: float = None,
    ):
        self.architectures = architectures
        self.burstable_performance = burstable_performance
        self.cores = cores
        self.excluded_instance_types = excluded_instance_types
        self.instance_family_level = instance_family_level
        self.max_price = max_price
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architectures is not None:
            result['Architectures'] = self.architectures
        if self.burstable_performance is not None:
            result['BurstablePerformance'] = self.burstable_performance
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.excluded_instance_types is not None:
            result['ExcludedInstanceTypes'] = self.excluded_instance_types
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architectures') is not None:
            self.architectures = m.get('Architectures')
        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('ExcludedInstanceTypes') is not None:
            self.excluded_instance_types = m.get('ExcludedInstanceTypes')
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ModifyScalingConfigurationRequestInstanceTypeOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class ModifyScalingConfigurationRequestSpotPriceLimits(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        return self


class ModifyScalingConfigurationRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: ModifyScalingConfigurationRequestPrivatePoolOptions = None,
        system_disk: ModifyScalingConfigurationRequestSystemDisk = None,
        affinity: str = None,
        cpu: int = None,
        credit_specification: str = None,
        data_disks: List[ModifyScalingConfigurationRequestDataDisks] = None,
        dedicated_host_id: str = None,
        deployment_set_id: str = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_description: str = None,
        instance_name: str = None,
        instance_pattern_infos: List[ModifyScalingConfigurationRequestInstancePatternInfos] = None,
        instance_type_overrides: List[ModifyScalingConfigurationRequestInstanceTypeOverrides] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        override: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scheduler_options: Dict[str, Any] = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[ModifyScalingConfigurationRequestSpotPriceLimits] = None,
        spot_strategy: str = None,
        system_disk_categories: List[str] = None,
        tags: str = None,
        tenancy: str = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.system_disk = system_disk
        self.affinity = affinity
        self.cpu = cpu
        self.credit_specification = credit_specification
        self.data_disks = data_disks
        self.dedicated_host_id = dedicated_host_id
        self.deployment_set_id = deployment_set_id
        self.host_name = host_name
        self.hpc_cluster_id = hpc_cluster_id
        self.image_family = image_family
        self.image_id = image_id
        self.image_name = image_name
        self.instance_description = instance_description
        self.instance_name = instance_name
        self.instance_pattern_infos = instance_pattern_infos
        self.instance_type_overrides = instance_type_overrides
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.io_optimized = io_optimized
        self.ipv_6address_count = ipv_6address_count
        self.key_pair_name = key_pair_name
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.override = override
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.password_inherit = password_inherit
        self.ram_role_name = ram_role_name
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_configuration_name = scaling_configuration_name
        self.scheduler_options = scheduler_options
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_duration = spot_duration
        self.spot_interruption_behavior = spot_interruption_behavior
        self.spot_price_limits = spot_price_limits
        self.spot_strategy = spot_strategy
        self.system_disk_categories = system_disk_categories
        self.tags = tags
        self.tenancy = tenancy
        self.user_data = user_data
        self.zone_id = zone_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.instance_pattern_infos:
            for k in self.instance_pattern_infos:
                if k:
                    k.validate()
        if self.instance_type_overrides:
            for k in self.instance_type_overrides:
                if k:
                    k.validate()
        if self.spot_price_limits:
            for k in self.spot_price_limits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['InstancePatternInfos'] = []
        if self.instance_pattern_infos is not None:
            for k in self.instance_pattern_infos:
                result['InstancePatternInfos'].append(k.to_map() if k else None)
        result['InstanceTypeOverrides'] = []
        if self.instance_type_overrides is not None:
            for k in self.instance_type_overrides:
                result['InstanceTypeOverrides'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.override is not None:
            result['Override'] = self.override
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        result['SpotPriceLimits'] = []
        if self.spot_price_limits is not None:
            for k in self.spot_price_limits:
                result['SpotPriceLimits'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ModifyScalingConfigurationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('SystemDisk') is not None:
            temp_model = ModifyScalingConfigurationRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = ModifyScalingConfigurationRequestDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.instance_pattern_infos = []
        if m.get('InstancePatternInfos') is not None:
            for k in m.get('InstancePatternInfos'):
                temp_model = ModifyScalingConfigurationRequestInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k))
        self.instance_type_overrides = []
        if m.get('InstanceTypeOverrides') is not None:
            for k in m.get('InstanceTypeOverrides'):
                temp_model = ModifyScalingConfigurationRequestInstanceTypeOverrides()
                self.instance_type_overrides.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options = m.get('SchedulerOptions')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k in m.get('SpotPriceLimits'):
                temp_model = ModifyScalingConfigurationRequestSpotPriceLimits()
                self.spot_price_limits.append(temp_model.from_map(k))
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ModifyScalingConfigurationShrinkRequestPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        self.id = id
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')
        return self


class ModifyScalingConfigurationShrinkRequestSystemDisk(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        description: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.description = description
        self.disk_name = disk_name
        self.encrypt_algorithm = encrypt_algorithm
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ModifyScalingConfigurationShrinkRequestDataDisks(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        categories: List[str] = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.categories = categories
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.description = description
        self.device = device
        self.disk_name = disk_name
        self.encrypted = encrypted
        self.kmskey_id = kmskey_id
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.description is not None:
            result['Description'] = self.description
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ModifyScalingConfigurationShrinkRequestInstancePatternInfos(TeaModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burstable_performance: str = None,
        cores: int = None,
        excluded_instance_types: List[str] = None,
        instance_family_level: str = None,
        max_price: float = None,
        memory: float = None,
    ):
        self.architectures = architectures
        self.burstable_performance = burstable_performance
        self.cores = cores
        self.excluded_instance_types = excluded_instance_types
        self.instance_family_level = instance_family_level
        self.max_price = max_price
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architectures is not None:
            result['Architectures'] = self.architectures
        if self.burstable_performance is not None:
            result['BurstablePerformance'] = self.burstable_performance
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.excluded_instance_types is not None:
            result['ExcludedInstanceTypes'] = self.excluded_instance_types
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architectures') is not None:
            self.architectures = m.get('Architectures')
        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('ExcludedInstanceTypes') is not None:
            self.excluded_instance_types = m.get('ExcludedInstanceTypes')
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ModifyScalingConfigurationShrinkRequestInstanceTypeOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class ModifyScalingConfigurationShrinkRequestSpotPriceLimits(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        return self


class ModifyScalingConfigurationShrinkRequest(TeaModel):
    def __init__(
        self,
        private_pool_options: ModifyScalingConfigurationShrinkRequestPrivatePoolOptions = None,
        system_disk: ModifyScalingConfigurationShrinkRequestSystemDisk = None,
        affinity: str = None,
        cpu: int = None,
        credit_specification: str = None,
        data_disks: List[ModifyScalingConfigurationShrinkRequestDataDisks] = None,
        dedicated_host_id: str = None,
        deployment_set_id: str = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_description: str = None,
        instance_name: str = None,
        instance_pattern_infos: List[ModifyScalingConfigurationShrinkRequestInstancePatternInfos] = None,
        instance_type_overrides: List[ModifyScalingConfigurationShrinkRequestInstanceTypeOverrides] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        override: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scheduler_options_shrink: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[ModifyScalingConfigurationShrinkRequestSpotPriceLimits] = None,
        spot_strategy: str = None,
        system_disk_categories: List[str] = None,
        tags: str = None,
        tenancy: str = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        self.system_disk = system_disk
        self.affinity = affinity
        self.cpu = cpu
        self.credit_specification = credit_specification
        self.data_disks = data_disks
        self.dedicated_host_id = dedicated_host_id
        self.deployment_set_id = deployment_set_id
        self.host_name = host_name
        self.hpc_cluster_id = hpc_cluster_id
        self.image_family = image_family
        self.image_id = image_id
        self.image_name = image_name
        self.instance_description = instance_description
        self.instance_name = instance_name
        self.instance_pattern_infos = instance_pattern_infos
        self.instance_type_overrides = instance_type_overrides
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.io_optimized = io_optimized
        self.ipv_6address_count = ipv_6address_count
        self.key_pair_name = key_pair_name
        self.load_balancer_weight = load_balancer_weight
        self.memory = memory
        self.override = override
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.password_inherit = password_inherit
        self.ram_role_name = ram_role_name
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.scaling_configuration_id = scaling_configuration_id
        self.scaling_configuration_name = scaling_configuration_name
        self.scheduler_options_shrink = scheduler_options_shrink
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_duration = spot_duration
        self.spot_interruption_behavior = spot_interruption_behavior
        self.spot_price_limits = spot_price_limits
        self.spot_strategy = spot_strategy
        self.system_disk_categories = system_disk_categories
        self.tags = tags
        self.tenancy = tenancy
        self.user_data = user_data
        self.zone_id = zone_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.instance_pattern_infos:
            for k in self.instance_pattern_infos:
                if k:
                    k.validate()
        if self.instance_type_overrides:
            for k in self.instance_type_overrides:
                if k:
                    k.validate()
        if self.spot_price_limits:
            for k in self.spot_price_limits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.affinity is not None:
            result['Affinity'] = self.affinity
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['DataDisks'].append(k.to_map() if k else None)
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id
        if self.image_family is not None:
            result['ImageFamily'] = self.image_family
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['InstancePatternInfos'] = []
        if self.instance_pattern_infos is not None:
            for k in self.instance_pattern_infos:
                result['InstancePatternInfos'].append(k.to_map() if k else None)
        result['InstanceTypeOverrides'] = []
        if self.instance_type_overrides is not None:
            for k in self.instance_type_overrides:
                result['InstanceTypeOverrides'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.override is not None:
            result['Override'] = self.override
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id
        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name
        if self.scheduler_options_shrink is not None:
            result['SchedulerOptions'] = self.scheduler_options_shrink
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration
        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior
        result['SpotPriceLimits'] = []
        if self.spot_price_limits is not None:
            for k in self.spot_price_limits:
                result['SpotPriceLimits'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = ModifyScalingConfigurationShrinkRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['PrivatePoolOptions'])
        if m.get('SystemDisk') is not None:
            temp_model = ModifyScalingConfigurationShrinkRequestSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k in m.get('DataDisks'):
                temp_model = ModifyScalingConfigurationShrinkRequestDataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')
        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.instance_pattern_infos = []
        if m.get('InstancePatternInfos') is not None:
            for k in m.get('InstancePatternInfos'):
                temp_model = ModifyScalingConfigurationShrinkRequestInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k))
        self.instance_type_overrides = []
        if m.get('InstanceTypeOverrides') is not None:
            for k in m.get('InstanceTypeOverrides'):
                temp_model = ModifyScalingConfigurationShrinkRequestInstanceTypeOverrides()
                self.instance_type_overrides.append(temp_model.from_map(k))
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')
        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')
        if m.get('SchedulerOptions') is not None:
            self.scheduler_options_shrink = m.get('SchedulerOptions')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')
        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')
        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k in m.get('SpotPriceLimits'):
                temp_model = ModifyScalingConfigurationShrinkRequestSpotPriceLimits()
                self.spot_price_limits.append(temp_model.from_map(k))
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ModifyScalingConfigurationResponseBody(TeaModel):
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


class ModifyScalingConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScalingConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScalingConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingGroupRequestLaunchTemplateOverrides(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')
        return self


class ModifyScalingGroupRequest(TeaModel):
    def __init__(
        self,
        active_scaling_configuration_id: str = None,
        allocation_strategy: str = None,
        az_balance: bool = None,
        compensate_with_on_demand: bool = None,
        default_cooldown: int = None,
        desired_capacity: int = None,
        group_deletion_protection: bool = None,
        health_check_type: str = None,
        launch_template_id: str = None,
        launch_template_overrides: List[ModifyScalingGroupRequestLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        max_instance_lifetime: int = None,
        max_size: int = None,
        min_size: int = None,
        multi_azpolicy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        owner_account: str = None,
        owner_id: int = None,
        removal_policies: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scaling_group_name: str = None,
        spot_allocation_strategy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        v_switch_ids: List[str] = None,
    ):
        self.active_scaling_configuration_id = active_scaling_configuration_id
        self.allocation_strategy = allocation_strategy
        self.az_balance = az_balance
        self.compensate_with_on_demand = compensate_with_on_demand
        self.default_cooldown = default_cooldown
        self.desired_capacity = desired_capacity
        self.group_deletion_protection = group_deletion_protection
        self.health_check_type = health_check_type
        self.launch_template_id = launch_template_id
        self.launch_template_overrides = launch_template_overrides
        self.launch_template_version = launch_template_version
        self.max_instance_lifetime = max_instance_lifetime
        self.max_size = max_size
        self.min_size = min_size
        self.multi_azpolicy = multi_azpolicy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.removal_policies = removal_policies
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id
        self.scaling_group_name = scaling_group_name
        self.spot_allocation_strategy = spot_allocation_strategy
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.launch_template_overrides:
            for k in self.launch_template_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id
        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy
        if self.az_balance is not None:
            result['AzBalance'] = self.az_balance
        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand
        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k.to_map() if k else None)
        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version
        if self.max_instance_lifetime is not None:
            result['MaxInstanceLifetime'] = self.max_instance_lifetime
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.multi_azpolicy is not None:
            result['MultiAZPolicy'] = self.multi_azpolicy
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity
        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.removal_policies is not None:
            result['RemovalPolicies'] = self.removal_policies
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name
        if self.spot_allocation_strategy is not None:
            result['SpotAllocationStrategy'] = self.spot_allocation_strategy
        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')
        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')
        if m.get('AzBalance') is not None:
            self.az_balance = m.get('AzBalance')
        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')
        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k in m.get('LaunchTemplateOverrides'):
                temp_model = ModifyScalingGroupRequestLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k))
        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')
        if m.get('MaxInstanceLifetime') is not None:
            self.max_instance_lifetime = m.get('MaxInstanceLifetime')
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('MultiAZPolicy') is not None:
            self.multi_azpolicy = m.get('MultiAZPolicy')
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')
        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RemovalPolicies') is not None:
            self.removal_policies = m.get('RemovalPolicies')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')
        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')
        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')
        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class ModifyScalingGroupResponseBody(TeaModel):
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


class ModifyScalingGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScalingGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScalingGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScalingRuleRequestStepAdjustments(TeaModel):
    def __init__(
        self,
        metric_interval_lower_bound: float = None,
        metric_interval_upper_bound: float = None,
        scaling_adjustment: int = None,
    ):
        self.metric_interval_lower_bound = metric_interval_lower_bound
        self.metric_interval_upper_bound = metric_interval_upper_bound
        self.scaling_adjustment = scaling_adjustment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_interval_lower_bound is not None:
            result['MetricIntervalLowerBound'] = self.metric_interval_lower_bound
        if self.metric_interval_upper_bound is not None:
            result['MetricIntervalUpperBound'] = self.metric_interval_upper_bound
        if self.scaling_adjustment is not None:
            result['ScalingAdjustment'] = self.scaling_adjustment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricIntervalLowerBound') is not None:
            self.metric_interval_lower_bound = m.get('MetricIntervalLowerBound')
        if m.get('MetricIntervalUpperBound') is not None:
            self.metric_interval_upper_bound = m.get('MetricIntervalUpperBound')
        if m.get('ScalingAdjustment') is not None:
            self.scaling_adjustment = m.get('ScalingAdjustment')
        return self


class ModifyScalingRuleRequest(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        cooldown: int = None,
        disable_scale_in: bool = None,
        estimated_instance_warmup: int = None,
        initial_max_size: int = None,
        metric_name: str = None,
        min_adjustment_magnitude: int = None,
        owner_account: str = None,
        owner_id: int = None,
        predictive_scaling_mode: str = None,
        predictive_task_buffer_time: int = None,
        predictive_value_behavior: str = None,
        predictive_value_buffer: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_in_evaluation_count: int = None,
        scale_out_evaluation_count: int = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
        step_adjustments: List[ModifyScalingRuleRequestStepAdjustments] = None,
        target_value: float = None,
    ):
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.cooldown = cooldown
        self.disable_scale_in = disable_scale_in
        self.estimated_instance_warmup = estimated_instance_warmup
        self.initial_max_size = initial_max_size
        self.metric_name = metric_name
        self.min_adjustment_magnitude = min_adjustment_magnitude
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.predictive_scaling_mode = predictive_scaling_mode
        self.predictive_task_buffer_time = predictive_task_buffer_time
        self.predictive_value_behavior = predictive_value_behavior
        self.predictive_value_buffer = predictive_value_buffer
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scale_in_evaluation_count = scale_in_evaluation_count
        self.scale_out_evaluation_count = scale_out_evaluation_count
        self.scaling_rule_id = scaling_rule_id
        self.scaling_rule_name = scaling_rule_name
        self.step_adjustments = step_adjustments
        self.target_value = target_value

    def validate(self):
        if self.step_adjustments:
            for k in self.step_adjustments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown
        if self.disable_scale_in is not None:
            result['DisableScaleIn'] = self.disable_scale_in
        if self.estimated_instance_warmup is not None:
            result['EstimatedInstanceWarmup'] = self.estimated_instance_warmup
        if self.initial_max_size is not None:
            result['InitialMaxSize'] = self.initial_max_size
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode
        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time
        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior
        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count
        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count
        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        result['StepAdjustments'] = []
        if self.step_adjustments is not None:
            for k in self.step_adjustments:
                result['StepAdjustments'].append(k.to_map() if k else None)
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')
        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')
        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')
        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')
        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')
        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')
        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')
        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')
        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        self.step_adjustments = []
        if m.get('StepAdjustments') is not None:
            for k in m.get('StepAdjustments'):
                temp_model = ModifyScalingRuleRequestStepAdjustments()
                self.step_adjustments.append(temp_model.from_map(k))
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        return self


class ModifyScalingRuleResponseBody(TeaModel):
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


class ModifyScalingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScalingRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledTaskRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        desired_capacity: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        max_value: int = None,
        min_value: int = None,
        owner_account: str = None,
        owner_id: int = None,
        recurrence_end_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scheduled_action: str = None,
        scheduled_task_id: str = None,
        scheduled_task_name: str = None,
        task_enabled: bool = None,
    ):
        self.description = description
        self.desired_capacity = desired_capacity
        self.launch_expiration_time = launch_expiration_time
        self.launch_time = launch_time
        self.max_value = max_value
        self.min_value = min_value
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.recurrence_end_time = recurrence_end_time
        self.recurrence_type = recurrence_type
        self.recurrence_value = recurrence_value
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id
        self.scheduled_action = scheduled_action
        self.scheduled_task_id = scheduled_task_id
        self.scheduled_task_name = scheduled_task_name
        self.task_enabled = task_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity
        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time
        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.recurrence_end_time is not None:
            result['RecurrenceEndTime'] = self.recurrence_end_time
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.scheduled_action is not None:
            result['ScheduledAction'] = self.scheduled_action
        if self.scheduled_task_id is not None:
            result['ScheduledTaskId'] = self.scheduled_task_id
        if self.scheduled_task_name is not None:
            result['ScheduledTaskName'] = self.scheduled_task_name
        if self.task_enabled is not None:
            result['TaskEnabled'] = self.task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')
        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')
        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RecurrenceEndTime') is not None:
            self.recurrence_end_time = m.get('RecurrenceEndTime')
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('ScheduledAction') is not None:
            self.scheduled_action = m.get('ScheduledAction')
        if m.get('ScheduledTaskId') is not None:
            self.scheduled_task_id = m.get('ScheduledTaskId')
        if m.get('ScheduledTaskName') is not None:
            self.scheduled_task_name = m.get('ScheduledTaskName')
        if m.get('TaskEnabled') is not None:
            self.task_enabled = m.get('TaskEnabled')
        return self


class ModifyScheduledTaskResponseBody(TeaModel):
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


class ModifyScheduledTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyScheduledTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebalanceInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class RebalanceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class RebalanceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebalanceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RebalanceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordLifecycleActionHeartbeatRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        heartbeat_timeout: int = None,
        lifecycle_action_token: str = None,
        lifecycle_hook_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.heartbeat_timeout = heartbeat_timeout
        self.lifecycle_action_token = lifecycle_action_token
        self.lifecycle_hook_id = lifecycle_hook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.heartbeat_timeout is not None:
            result['heartbeatTimeout'] = self.heartbeat_timeout
        if self.lifecycle_action_token is not None:
            result['lifecycleActionToken'] = self.lifecycle_action_token
        if self.lifecycle_hook_id is not None:
            result['lifecycleHookId'] = self.lifecycle_hook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('heartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('heartbeatTimeout')
        if m.get('lifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('lifecycleActionToken')
        if m.get('lifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('lifecycleHookId')
        return self


class RecordLifecycleActionHeartbeatResponseBody(TeaModel):
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


class RecordLifecycleActionHeartbeatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecordLifecycleActionHeartbeatResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecordLifecycleActionHeartbeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveInstancesRequest(TeaModel):
    def __init__(
        self,
        decrease_desired_capacity: bool = None,
        instance_ids: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_policy: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        self.decrease_desired_capacity = decrease_desired_capacity
        self.instance_ids = instance_ids
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.remove_policy = remove_policy
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decrease_desired_capacity is not None:
            result['DecreaseDesiredCapacity'] = self.decrease_desired_capacity
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remove_policy is not None:
            result['RemovePolicy'] = self.remove_policy
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DecreaseDesiredCapacity') is not None:
            self.decrease_desired_capacity = m.get('DecreaseDesiredCapacity')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemovePolicy') is not None:
            self.remove_policy = m.get('RemovePolicy')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class RemoveInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class RemoveInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeProcessesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: int = None,
        processes: List[str] = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.processes = processes
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.processes is not None:
            result['Processes'] = self.processes
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Processes') is not None:
            self.processes = m.get('Processes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class ResumeProcessesResponseBody(TeaModel):
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


class ResumeProcessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeProcessesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeProcessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleWithAdjustmentRequest(TeaModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        client_token: str = None,
        min_adjustment_magnitude: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        sync_activity: bool = None,
    ):
        self.adjustment_type = adjustment_type
        self.adjustment_value = adjustment_value
        self.client_token = client_token
        self.min_adjustment_magnitude = min_adjustment_magnitude
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id
        self.sync_activity = sync_activity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type
        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        if self.sync_activity is not None:
            result['SyncActivity'] = self.sync_activity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')
        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        if m.get('SyncActivity') is not None:
            self.sync_activity = m.get('SyncActivity')
        return self


class ScaleWithAdjustmentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scaling_activity_id: str = None,
    ):
        self.request_id = request_id
        self.scaling_activity_id = scaling_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')
        return self


class ScaleWithAdjustmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScaleWithAdjustmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScaleWithAdjustmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        group_deletion_protection: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.group_deletion_protection = group_deletion_protection
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class SetGroupDeletionProtectionResponseBody(TeaModel):
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


class SetGroupDeletionProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGroupDeletionProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetGroupDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceHealthRequest(TeaModel):
    def __init__(
        self,
        health_status: str = None,
        instance_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        self.health_status = health_status
        self.instance_id = instance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class SetInstanceHealthResponseBody(TeaModel):
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


class SetInstanceHealthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetInstanceHealthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetInstanceHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstancesProtectionRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        owner_id: int = None,
        protected_from_scale_in: bool = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.protected_from_scale_in = protected_from_scale_in
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.protected_from_scale_in is not None:
            result['ProtectedFromScaleIn'] = self.protected_from_scale_in
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProtectedFromScaleIn') is not None:
            self.protected_from_scale_in = m.get('ProtectedFromScaleIn')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class SetInstancesProtectionResponseBody(TeaModel):
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


class SetInstancesProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetInstancesProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetInstancesProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendProcessesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: int = None,
        processes: List[str] = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.processes = processes
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.processes is not None:
            result['Processes'] = self.processes
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Processes') is not None:
            self.processes = m.get('Processes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')
        return self


class SuspendProcessesResponseBody(TeaModel):
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


class SuspendProcessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendProcessesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SuspendProcessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        propagate: bool = None,
        value: str = None,
    ):
        self.key = key
        self.propagate = propagate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.propagate is not None:
            result['Propagate'] = self.propagate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Propagate') is not None:
            self.propagate = m.get('Propagate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tags: List[TagResourcesRequestTags] = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = TagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tag_keys: List[str] = None,
    ):
        self.all = all
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyAuthenticationRequest(TeaModel):
    def __init__(
        self,
        only_check: bool = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uid: int = None,
    ):
        self.only_check = only_check
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.only_check is not None:
            result['OnlyCheck'] = self.only_check
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlyCheck') is not None:
            self.only_check = m.get('OnlyCheck')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class VerifyAuthenticationResponseBody(TeaModel):
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


class VerifyAuthenticationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyAuthenticationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyAuthenticationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyUserRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class VerifyUserResponseBody(TeaModel):
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


class VerifyUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


