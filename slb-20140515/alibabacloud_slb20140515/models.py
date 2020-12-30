# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddAccessControlListEntryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
        acl_id: str = None,
        acl_entrys: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id
        self.acl_id = acl_id
        self.acl_entrys = acl_entrys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_entrys is not None:
            result['AclEntrys'] = self.acl_entrys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclEntrys') is not None:
            self.acl_entrys = m.get('AclEntrys')
        return self


class AddAccessControlListEntryResponseBody(TeaModel):
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


class AddAccessControlListEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAccessControlListEntryResponseBody = None,
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
            temp_model = AddAccessControlListEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBackendServersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        backend_servers: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: str = None,
        description: str = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class AddBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[AddBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = AddBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class AddBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        load_balancer_id: str = None,
        backend_servers: AddBackendServersResponseBodyBackendServers = None,
    ):
        self.request_id = request_id
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            temp_model = AddBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class AddBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddBackendServersResponseBody = None,
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
            temp_model = AddBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddListenerWhiteListItemRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        source_items: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        listener_protocol: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.source_items = source_items
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.listener_protocol = listener_protocol
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.source_items is not None:
            result['SourceItems'] = self.source_items
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('SourceItems') is not None:
            self.source_items = m.get('SourceItems')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddListenerWhiteListItemResponseBody(TeaModel):
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


class AddListenerWhiteListItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddListenerWhiteListItemResponseBody = None,
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
            temp_model = AddListenerWhiteListItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        load_balancer_id: str = None,
        tags: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.load_balancer_id = load_balancer_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddTagsResponseBody(TeaModel):
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


class AddTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddTagsResponseBody = None,
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
            temp_model = AddTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVServerGroupBackendServersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group_id: str = None,
        backend_servers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group_id = vserver_group_id
        self.backend_servers = backend_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')
        return self


class AddVServerGroupBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class AddVServerGroupBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[AddVServerGroupBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = AddVServerGroupBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class AddVServerGroupBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        request_id: str = None,
        backend_servers: AddVServerGroupBackendServersResponseBodyBackendServers = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.request_id = request_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackendServers') is not None:
            temp_model = AddVServerGroupBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class AddVServerGroupBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVServerGroupBackendServersResponseBody = None,
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
            temp_model = AddVServerGroupBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessControlListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
        acl_name: str = None,
        address_ipversion: str = None,
        resource_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id
        self.acl_name = acl_name
        self.address_ipversion = address_ipversion
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateAccessControlListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        acl_id: str = None,
    ):
        self.request_id = request_id
        self.acl_id = acl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class CreateAccessControlListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAccessControlListResponseBody = None,
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
            temp_model = CreateAccessControlListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainExtensionRequestServerCertificate(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateDomainExtensionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        domain: str = None,
        server_certificate_id: str = None,
        certificate_id: List[str] = None,
        server_certificate: List[CreateDomainExtensionRequestServerCertificate] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.domain = domain
        self.server_certificate_id = server_certificate_id
        self.certificate_id = certificate_id
        self.server_certificate = server_certificate

    def validate(self):
        if self.server_certificate:
            for k in self.server_certificate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        result['ServerCertificate'] = []
        if self.server_certificate is not None:
            for k in self.server_certificate:
                result['ServerCertificate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        self.server_certificate = []
        if m.get('ServerCertificate') is not None:
            for k in m.get('ServerCertificate'):
                temp_model = CreateDomainExtensionRequestServerCertificate()
                self.server_certificate.append(temp_model.from_map(k))
        return self


class CreateDomainExtensionResponseBody(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        domain_extension_id: str = None,
        request_id: str = None,
    ):
        self.listener_port = listener_port
        self.domain_extension_id = domain_extension_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDomainExtensionResponseBody = None,
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
            temp_model = CreateDomainExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        address_type: str = None,
        internet_charge_type: str = None,
        bandwidth: int = None,
        client_token: str = None,
        load_balancer_name: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        owner_account: str = None,
        master_zone_id: str = None,
        slave_zone_id: str = None,
        access_key_id: str = None,
        tags: str = None,
        enable_vpc_vip_flow: str = None,
        load_balancer_spec: str = None,
        resource_group_id: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        duration: int = None,
        auto_pay: bool = None,
        address_ipversion: str = None,
        address: str = None,
        ratio: int = None,
        delete_protection: str = None,
        cloud_type: str = None,
        support_private_link: bool = None,
        modification_protection_status: str = None,
        modification_protection_reason: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.address_type = address_type
        self.internet_charge_type = internet_charge_type
        self.bandwidth = bandwidth
        self.client_token = client_token
        self.load_balancer_name = load_balancer_name
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.owner_account = owner_account
        self.master_zone_id = master_zone_id
        self.slave_zone_id = slave_zone_id
        self.access_key_id = access_key_id
        self.tags = tags
        self.enable_vpc_vip_flow = enable_vpc_vip_flow
        self.load_balancer_spec = load_balancer_spec
        self.resource_group_id = resource_group_id
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.auto_pay = auto_pay
        self.address_ipversion = address_ipversion
        self.address = address
        self.ratio = ratio
        self.delete_protection = delete_protection
        self.cloud_type = cloud_type
        self.support_private_link = support_private_link
        self.modification_protection_status = modification_protection_status
        self.modification_protection_reason = modification_protection_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.enable_vpc_vip_flow is not None:
            result['EnableVpcVipFlow'] = self.enable_vpc_vip_flow
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.address is not None:
            result['Address'] = self.address
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection
        if self.cloud_type is not None:
            result['CloudType'] = self.cloud_type
        if self.support_private_link is not None:
            result['SupportPrivateLink'] = self.support_private_link
        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status
        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('EnableVpcVipFlow') is not None:
            self.enable_vpc_vip_flow = m.get('EnableVpcVipFlow')
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')
        if m.get('CloudType') is not None:
            self.cloud_type = m.get('CloudType')
        if m.get('SupportPrivateLink') is not None:
            self.support_private_link = m.get('SupportPrivateLink')
        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')
        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')
        return self


class CreateLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        load_balancer_name: str = None,
        vpc_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        address: str = None,
        network_type: str = None,
        address_ipversion: str = None,
        v_switch_id: str = None,
        load_balancer_id: str = None,
        order_id: int = None,
    ):
        self.load_balancer_name = load_balancer_name
        self.vpc_id = vpc_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.address = address
        self.network_type = network_type
        self.address_ipversion = address_ipversion
        self.v_switch_id = v_switch_id
        self.load_balancer_id = load_balancer_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.address is not None:
            result['Address'] = self.address
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerResponseBody = None,
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
            temp_model = CreateLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerHTTPListenerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        bandwidth: int = None,
        listener_port: int = None,
        backend_server_port: int = None,
        xforwarded_for: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        cookie_timeout: int = None,
        cookie: str = None,
        health_check: str = None,
        health_check_type: str = None,
        health_check_method: str = None,
        health_check_http_version: str = None,
        health_check_domain: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_interval: int = None,
        health_check_http_code: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        vserver_group_id: str = None,
        tags: str = None,
        xforwarded_for__slbip: str = None,
        xforwarded_for__slbid: str = None,
        xforwarded_for_proto: str = None,
        gzip: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        description: str = None,
        listener_forward: str = None,
        forward_port: int = None,
        idle_timeout: int = None,
        request_timeout: int = None,
        xforwarded_for__slbport: str = None,
        xforwarded_for__client_src_port: str = None,
        forward_code: int = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.bandwidth = bandwidth
        self.listener_port = listener_port
        self.backend_server_port = backend_server_port
        self.xforwarded_for = xforwarded_for
        self.scheduler = scheduler
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        self.cookie_timeout = cookie_timeout
        self.cookie = cookie
        self.health_check = health_check
        self.health_check_type = health_check_type
        self.health_check_method = health_check_method
        self.health_check_http_version = health_check_http_version
        self.health_check_domain = health_check_domain
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_timeout = health_check_timeout
        self.health_check_connect_port = health_check_connect_port
        self.health_check_interval = health_check_interval
        self.health_check_http_code = health_check_http_code
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.vserver_group_id = vserver_group_id
        self.tags = tags
        self.xforwarded_for__slbip = xforwarded_for__slbip
        self.xforwarded_for__slbid = xforwarded_for__slbid
        self.xforwarded_for_proto = xforwarded_for_proto
        self.gzip = gzip
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.description = description
        self.listener_forward = listener_forward
        self.forward_port = forward_port
        self.idle_timeout = idle_timeout
        self.request_timeout = request_timeout
        self.xforwarded_for__slbport = xforwarded_for__slbport
        self.xforwarded_for__client_src_port = xforwarded_for__client_src_port
        self.forward_code = forward_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.xforwarded_for__slbip is not None:
            result['XForwardedFor_SLBIP'] = self.xforwarded_for__slbip
        if self.xforwarded_for__slbid is not None:
            result['XForwardedFor_SLBID'] = self.xforwarded_for__slbid
        if self.xforwarded_for_proto is not None:
            result['XForwardedFor_proto'] = self.xforwarded_for_proto
        if self.gzip is not None:
            result['Gzip'] = self.gzip
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.xforwarded_for__slbport is not None:
            result['XForwardedFor_SLBPORT'] = self.xforwarded_for__slbport
        if self.xforwarded_for__client_src_port is not None:
            result['XForwardedFor_ClientSrcPort'] = self.xforwarded_for__client_src_port
        if self.forward_code is not None:
            result['ForwardCode'] = self.forward_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('XForwardedFor_SLBIP') is not None:
            self.xforwarded_for__slbip = m.get('XForwardedFor_SLBIP')
        if m.get('XForwardedFor_SLBID') is not None:
            self.xforwarded_for__slbid = m.get('XForwardedFor_SLBID')
        if m.get('XForwardedFor_proto') is not None:
            self.xforwarded_for_proto = m.get('XForwardedFor_proto')
        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('XForwardedFor_SLBPORT') is not None:
            self.xforwarded_for__slbport = m.get('XForwardedFor_SLBPORT')
        if m.get('XForwardedFor_ClientSrcPort') is not None:
            self.xforwarded_for__client_src_port = m.get('XForwardedFor_ClientSrcPort')
        if m.get('ForwardCode') is not None:
            self.forward_code = m.get('ForwardCode')
        return self


class CreateLoadBalancerHTTPListenerResponseBody(TeaModel):
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


class CreateLoadBalancerHTTPListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerHTTPListenerResponseBody = None,
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
            temp_model = CreateLoadBalancerHTTPListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerHTTPSListenerRequestServerCertificate(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateLoadBalancerHTTPSListenerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        bandwidth: int = None,
        listener_port: int = None,
        backend_server_port: int = None,
        backend_protocol: str = None,
        xforwarded_for: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        cookie_timeout: int = None,
        cookie: str = None,
        health_check: str = None,
        health_check_type: str = None,
        health_check_method: str = None,
        health_check_http_version: str = None,
        health_check_domain: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_interval: int = None,
        health_check_http_code: str = None,
        server_certificate_id: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        vserver_group_id: str = None,
        cacertificate_id: str = None,
        tags: str = None,
        xforwarded_for__slbip: str = None,
        xforwarded_for__slbid: str = None,
        xforwarded_for_proto: str = None,
        gzip: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        description: str = None,
        idle_timeout: int = None,
        request_timeout: int = None,
        enable_http_2: str = None,
        tlscipher_policy: str = None,
        xforwarded_for__slbport: str = None,
        xforwarded_for__client_src_port: str = None,
        xforwarded_for__client_cert_subject_dn: str = None,
        xforwarded_for__client_cert_issuer_dn: str = None,
        xforwarded_for__client_cert_fingerprint: str = None,
        xforwarded_for__client_cert_client_verify: str = None,
        xforwarded_for__client_cert_issuer_dnalias: str = None,
        xforwarded_for__client_cert_subject_dnalias: str = None,
        xforwarded_for__client_cert_fingerprint_alias: str = None,
        xforwarded_for__client_cert_client_verify_alias: str = None,
        server_certificate: List[CreateLoadBalancerHTTPSListenerRequestServerCertificate] = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.bandwidth = bandwidth
        self.listener_port = listener_port
        self.backend_server_port = backend_server_port
        self.backend_protocol = backend_protocol
        self.xforwarded_for = xforwarded_for
        self.scheduler = scheduler
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        self.cookie_timeout = cookie_timeout
        self.cookie = cookie
        self.health_check = health_check
        self.health_check_type = health_check_type
        self.health_check_method = health_check_method
        self.health_check_http_version = health_check_http_version
        self.health_check_domain = health_check_domain
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_timeout = health_check_timeout
        self.health_check_connect_port = health_check_connect_port
        self.health_check_interval = health_check_interval
        self.health_check_http_code = health_check_http_code
        self.server_certificate_id = server_certificate_id
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.vserver_group_id = vserver_group_id
        self.cacertificate_id = cacertificate_id
        self.tags = tags
        self.xforwarded_for__slbip = xforwarded_for__slbip
        self.xforwarded_for__slbid = xforwarded_for__slbid
        self.xforwarded_for_proto = xforwarded_for_proto
        self.gzip = gzip
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.description = description
        self.idle_timeout = idle_timeout
        self.request_timeout = request_timeout
        self.enable_http_2 = enable_http_2
        self.tlscipher_policy = tlscipher_policy
        self.xforwarded_for__slbport = xforwarded_for__slbport
        self.xforwarded_for__client_src_port = xforwarded_for__client_src_port
        self.xforwarded_for__client_cert_subject_dn = xforwarded_for__client_cert_subject_dn
        self.xforwarded_for__client_cert_issuer_dn = xforwarded_for__client_cert_issuer_dn
        self.xforwarded_for__client_cert_fingerprint = xforwarded_for__client_cert_fingerprint
        self.xforwarded_for__client_cert_client_verify = xforwarded_for__client_cert_client_verify
        self.xforwarded_for__client_cert_issuer_dnalias = xforwarded_for__client_cert_issuer_dnalias
        self.xforwarded_for__client_cert_subject_dnalias = xforwarded_for__client_cert_subject_dnalias
        self.xforwarded_for__client_cert_fingerprint_alias = xforwarded_for__client_cert_fingerprint_alias
        self.xforwarded_for__client_cert_client_verify_alias = xforwarded_for__client_cert_client_verify_alias
        self.server_certificate = server_certificate

    def validate(self):
        if self.server_certificate:
            for k in self.server_certificate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.xforwarded_for__slbip is not None:
            result['XForwardedFor_SLBIP'] = self.xforwarded_for__slbip
        if self.xforwarded_for__slbid is not None:
            result['XForwardedFor_SLBID'] = self.xforwarded_for__slbid
        if self.xforwarded_for_proto is not None:
            result['XForwardedFor_proto'] = self.xforwarded_for_proto
        if self.gzip is not None:
            result['Gzip'] = self.gzip
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.enable_http_2 is not None:
            result['EnableHttp2'] = self.enable_http_2
        if self.tlscipher_policy is not None:
            result['TLSCipherPolicy'] = self.tlscipher_policy
        if self.xforwarded_for__slbport is not None:
            result['XForwardedFor_SLBPORT'] = self.xforwarded_for__slbport
        if self.xforwarded_for__client_src_port is not None:
            result['XForwardedFor_ClientSrcPort'] = self.xforwarded_for__client_src_port
        if self.xforwarded_for__client_cert_subject_dn is not None:
            result['XForwardedFor_ClientCertSubjectDN'] = self.xforwarded_for__client_cert_subject_dn
        if self.xforwarded_for__client_cert_issuer_dn is not None:
            result['XForwardedFor_ClientCertIssuerDN'] = self.xforwarded_for__client_cert_issuer_dn
        if self.xforwarded_for__client_cert_fingerprint is not None:
            result['XForwardedFor_ClientCertFingerprint'] = self.xforwarded_for__client_cert_fingerprint
        if self.xforwarded_for__client_cert_client_verify is not None:
            result['XForwardedFor_ClientCertClientVerify'] = self.xforwarded_for__client_cert_client_verify
        if self.xforwarded_for__client_cert_issuer_dnalias is not None:
            result['XForwardedFor_ClientCertIssuerDNAlias'] = self.xforwarded_for__client_cert_issuer_dnalias
        if self.xforwarded_for__client_cert_subject_dnalias is not None:
            result['XForwardedFor_ClientCertSubjectDNAlias'] = self.xforwarded_for__client_cert_subject_dnalias
        if self.xforwarded_for__client_cert_fingerprint_alias is not None:
            result['XForwardedFor_ClientCertFingerprintAlias'] = self.xforwarded_for__client_cert_fingerprint_alias
        if self.xforwarded_for__client_cert_client_verify_alias is not None:
            result['XForwardedFor_ClientCertClientVerifyAlias'] = self.xforwarded_for__client_cert_client_verify_alias
        result['ServerCertificate'] = []
        if self.server_certificate is not None:
            for k in self.server_certificate:
                result['ServerCertificate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('XForwardedFor_SLBIP') is not None:
            self.xforwarded_for__slbip = m.get('XForwardedFor_SLBIP')
        if m.get('XForwardedFor_SLBID') is not None:
            self.xforwarded_for__slbid = m.get('XForwardedFor_SLBID')
        if m.get('XForwardedFor_proto') is not None:
            self.xforwarded_for_proto = m.get('XForwardedFor_proto')
        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('EnableHttp2') is not None:
            self.enable_http_2 = m.get('EnableHttp2')
        if m.get('TLSCipherPolicy') is not None:
            self.tlscipher_policy = m.get('TLSCipherPolicy')
        if m.get('XForwardedFor_SLBPORT') is not None:
            self.xforwarded_for__slbport = m.get('XForwardedFor_SLBPORT')
        if m.get('XForwardedFor_ClientSrcPort') is not None:
            self.xforwarded_for__client_src_port = m.get('XForwardedFor_ClientSrcPort')
        if m.get('XForwardedFor_ClientCertSubjectDN') is not None:
            self.xforwarded_for__client_cert_subject_dn = m.get('XForwardedFor_ClientCertSubjectDN')
        if m.get('XForwardedFor_ClientCertIssuerDN') is not None:
            self.xforwarded_for__client_cert_issuer_dn = m.get('XForwardedFor_ClientCertIssuerDN')
        if m.get('XForwardedFor_ClientCertFingerprint') is not None:
            self.xforwarded_for__client_cert_fingerprint = m.get('XForwardedFor_ClientCertFingerprint')
        if m.get('XForwardedFor_ClientCertClientVerify') is not None:
            self.xforwarded_for__client_cert_client_verify = m.get('XForwardedFor_ClientCertClientVerify')
        if m.get('XForwardedFor_ClientCertIssuerDNAlias') is not None:
            self.xforwarded_for__client_cert_issuer_dnalias = m.get('XForwardedFor_ClientCertIssuerDNAlias')
        if m.get('XForwardedFor_ClientCertSubjectDNAlias') is not None:
            self.xforwarded_for__client_cert_subject_dnalias = m.get('XForwardedFor_ClientCertSubjectDNAlias')
        if m.get('XForwardedFor_ClientCertFingerprintAlias') is not None:
            self.xforwarded_for__client_cert_fingerprint_alias = m.get('XForwardedFor_ClientCertFingerprintAlias')
        if m.get('XForwardedFor_ClientCertClientVerifyAlias') is not None:
            self.xforwarded_for__client_cert_client_verify_alias = m.get('XForwardedFor_ClientCertClientVerifyAlias')
        self.server_certificate = []
        if m.get('ServerCertificate') is not None:
            for k in m.get('ServerCertificate'):
                temp_model = CreateLoadBalancerHTTPSListenerRequestServerCertificate()
                self.server_certificate.append(temp_model.from_map(k))
        return self


class CreateLoadBalancerHTTPSListenerResponseBody(TeaModel):
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


class CreateLoadBalancerHTTPSListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerHTTPSListenerResponseBody = None,
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
            temp_model = CreateLoadBalancerHTTPSListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerTCPListenerRequestPortRange(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateLoadBalancerTCPListenerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        backend_server_port: int = None,
        bandwidth: int = None,
        scheduler: str = None,
        persistence_timeout: int = None,
        established_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_connect_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_interval: int = None,
        health_check_domain: str = None,
        health_check_uri: str = None,
        health_check_http_code: str = None,
        health_check_method: str = None,
        health_check_type: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        vserver_group_id: str = None,
        master_slave_server_group_id: str = None,
        tags: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        description: str = None,
        connection_drain: str = None,
        connection_drain_timeout: int = None,
        port_range: List[CreateLoadBalancerTCPListenerRequestPortRange] = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.backend_server_port = backend_server_port
        self.bandwidth = bandwidth
        self.scheduler = scheduler
        self.persistence_timeout = persistence_timeout
        self.established_timeout = established_timeout
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_connect_timeout = health_check_connect_timeout
        self.health_check_connect_port = health_check_connect_port
        self.health_check_interval = health_check_interval
        self.health_check_domain = health_check_domain
        self.health_check_uri = health_check_uri
        self.health_check_http_code = health_check_http_code
        self.health_check_method = health_check_method
        self.health_check_type = health_check_type
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.vserver_group_id = vserver_group_id
        self.master_slave_server_group_id = master_slave_server_group_id
        self.tags = tags
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.description = description
        self.connection_drain = connection_drain
        self.connection_drain_timeout = connection_drain_timeout
        self.port_range = port_range

    def validate(self):
        if self.port_range:
            for k in self.port_range:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.connection_drain is not None:
            result['ConnectionDrain'] = self.connection_drain
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        result['PortRange'] = []
        if self.port_range is not None:
            for k in self.port_range:
                result['PortRange'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConnectionDrain') is not None:
            self.connection_drain = m.get('ConnectionDrain')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        self.port_range = []
        if m.get('PortRange') is not None:
            for k in m.get('PortRange'):
                temp_model = CreateLoadBalancerTCPListenerRequestPortRange()
                self.port_range.append(temp_model.from_map(k))
        return self


class CreateLoadBalancerTCPListenerResponseBody(TeaModel):
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


class CreateLoadBalancerTCPListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerTCPListenerResponseBody = None,
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
            temp_model = CreateLoadBalancerTCPListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerUDPListenerRequestPortRange(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateLoadBalancerUDPListenerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        backend_server_port: int = None,
        bandwidth: int = None,
        scheduler: str = None,
        persistence_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_connect_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        health_check_exp: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        vserver_group_id: str = None,
        master_slave_server_group_id: str = None,
        tags: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        description: str = None,
        connection_drain: str = None,
        connection_drain_timeout: int = None,
        port_range: List[CreateLoadBalancerUDPListenerRequestPortRange] = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.backend_server_port = backend_server_port
        self.bandwidth = bandwidth
        self.scheduler = scheduler
        self.persistence_timeout = persistence_timeout
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_connect_timeout = health_check_connect_timeout
        self.health_check_connect_port = health_check_connect_port
        self.health_check_interval = health_check_interval
        self.health_check_req = health_check_req
        self.health_check_exp = health_check_exp
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.vserver_group_id = vserver_group_id
        self.master_slave_server_group_id = master_slave_server_group_id
        self.tags = tags
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.description = description
        self.connection_drain = connection_drain
        self.connection_drain_timeout = connection_drain_timeout
        self.port_range = port_range

    def validate(self):
        if self.port_range:
            for k in self.port_range:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval
        if self.health_check_req is not None:
            result['healthCheckReq'] = self.health_check_req
        if self.health_check_exp is not None:
            result['healthCheckExp'] = self.health_check_exp
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.connection_drain is not None:
            result['ConnectionDrain'] = self.connection_drain
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        result['PortRange'] = []
        if self.port_range is not None:
            for k in self.port_range:
                result['PortRange'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')
        if m.get('healthCheckReq') is not None:
            self.health_check_req = m.get('healthCheckReq')
        if m.get('healthCheckExp') is not None:
            self.health_check_exp = m.get('healthCheckExp')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConnectionDrain') is not None:
            self.connection_drain = m.get('ConnectionDrain')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        self.port_range = []
        if m.get('PortRange') is not None:
            for k in m.get('PortRange'):
                temp_model = CreateLoadBalancerUDPListenerRequestPortRange()
                self.port_range.append(temp_model.from_map(k))
        return self


class CreateLoadBalancerUDPListenerResponseBody(TeaModel):
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


class CreateLoadBalancerUDPListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLoadBalancerUDPListenerResponseBody = None,
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
            temp_model = CreateLoadBalancerUDPListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMasterSlaveServerGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        master_slave_server_group_name: str = None,
        master_slave_backend_servers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.master_slave_server_group_name = master_slave_server_group_name
        self.master_slave_backend_servers = master_slave_backend_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.master_slave_server_group_name is not None:
            result['MasterSlaveServerGroupName'] = self.master_slave_server_group_name
        if self.master_slave_backend_servers is not None:
            result['MasterSlaveBackendServers'] = self.master_slave_backend_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('MasterSlaveServerGroupName') is not None:
            self.master_slave_server_group_name = m.get('MasterSlaveServerGroupName')
        if m.get('MasterSlaveBackendServers') is not None:
            self.master_slave_backend_servers = m.get('MasterSlaveBackendServers')
        return self


class CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_type: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id
        self.server_type = server_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        return self


class CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServers(TeaModel):
    def __init__(
        self,
        master_slave_backend_server: List[CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer] = None,
    ):
        self.master_slave_backend_server = master_slave_backend_server

    def validate(self):
        if self.master_slave_backend_server:
            for k in self.master_slave_backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MasterSlaveBackendServer'] = []
        if self.master_slave_backend_server is not None:
            for k in self.master_slave_backend_server:
                result['MasterSlaveBackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_slave_backend_server = []
        if m.get('MasterSlaveBackendServer') is not None:
            for k in m.get('MasterSlaveBackendServer'):
                temp_model = CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer()
                self.master_slave_backend_server.append(temp_model.from_map(k))
        return self


class CreateMasterSlaveServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        master_slave_server_group_id: str = None,
        master_slave_backend_servers: CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServers = None,
    ):
        self.request_id = request_id
        self.master_slave_server_group_id = master_slave_server_group_id
        self.master_slave_backend_servers = master_slave_backend_servers

    def validate(self):
        if self.master_slave_backend_servers:
            self.master_slave_backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.master_slave_backend_servers is not None:
            result['MasterSlaveBackendServers'] = self.master_slave_backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('MasterSlaveBackendServers') is not None:
            temp_model = CreateMasterSlaveServerGroupResponseBodyMasterSlaveBackendServers()
            self.master_slave_backend_servers = temp_model.from_map(m['MasterSlaveBackendServers'])
        return self


class CreateMasterSlaveServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMasterSlaveServerGroupResponseBody = None,
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
            temp_model = CreateMasterSlaveServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRulesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        rule_list: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol
        self.rule_list = rule_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('RuleList') is not None:
            self.rule_list = m.get('RuleList')
        return self


class CreateRulesResponseBodyRulesRule(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        rule: List[CreateRulesResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = CreateRulesResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class CreateRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: CreateRulesResponseBodyRules = None,
    ):
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rules') is not None:
            temp_model = CreateRulesResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class CreateRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRulesResponseBody = None,
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
            temp_model = CreateRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTLSCipherPolicyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        name: str = None,
        ciphers: List[str] = None,
        tlsversions: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.name = name
        self.ciphers = ciphers
        self.tlsversions = tlsversions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')
        return self


class CreateTLSCipherPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tlscipher_policy_id: str = None,
    ):
        self.request_id = request_id
        self.tlscipher_policy_id = tlscipher_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tlscipher_policy_id is not None:
            result['TLSCipherPolicyId'] = self.tlscipher_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TLSCipherPolicyId') is not None:
            self.tlscipher_policy_id = m.get('TLSCipherPolicyId')
        return self


class CreateTLSCipherPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTLSCipherPolicyResponseBody = None,
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
            temp_model = CreateTLSCipherPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVServerGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        vserver_group_name: str = None,
        backend_servers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.vserver_group_name = vserver_group_name
        self.backend_servers = backend_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')
        return self


class CreateVServerGroupResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class CreateVServerGroupResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[CreateVServerGroupResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = CreateVServerGroupResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class CreateVServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        request_id: str = None,
        backend_servers: CreateVServerGroupResponseBodyBackendServers = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.request_id = request_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackendServers') is not None:
            temp_model = CreateVServerGroupResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class CreateVServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVServerGroupResponseBody = None,
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
            temp_model = CreateVServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessControlListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
        acl_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id
        self.acl_id = acl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class DeleteAccessControlListResponseBody(TeaModel):
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


class DeleteAccessControlListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAccessControlListResponseBody = None,
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
            temp_model = DeleteAccessControlListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCACertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        cacertificate_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.cacertificate_id = cacertificate_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        return self


class DeleteCACertificateResponseBody(TeaModel):
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


class DeleteCACertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCACertificateResponseBody = None,
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
            temp_model = DeleteCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainExtensionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        domain_extension_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.domain_extension_id = domain_extension_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        return self


class DeleteDomainExtensionResponseBody(TeaModel):
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


class DeleteDomainExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDomainExtensionResponseBody = None,
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
            temp_model = DeleteDomainExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DeleteLoadBalancerResponseBody(TeaModel):
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


class DeleteLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLoadBalancerResponseBody = None,
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
            temp_model = DeleteLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoadBalancerListenerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DeleteLoadBalancerListenerResponseBody(TeaModel):
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


class DeleteLoadBalancerListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLoadBalancerListenerResponseBody = None,
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
            temp_model = DeleteLoadBalancerListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMasterSlaveServerGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        master_slave_server_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.master_slave_server_group_id = master_slave_server_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        return self


class DeleteMasterSlaveServerGroupResponseBody(TeaModel):
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


class DeleteMasterSlaveServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMasterSlaveServerGroupResponseBody = None,
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
            temp_model = DeleteMasterSlaveServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRulesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        rule_ids: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        return self


class DeleteRulesResponseBody(TeaModel):
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


class DeleteRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRulesResponseBody = None,
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
            temp_model = DeleteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServerCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        server_certificate_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.server_certificate_id = server_certificate_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DeleteServerCertificateResponseBody(TeaModel):
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


class DeleteServerCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServerCertificateResponseBody = None,
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
            temp_model = DeleteServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTLSCipherPolicyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tlscipher_policy_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tlscipher_policy_id = tlscipher_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tlscipher_policy_id is not None:
            result['TLSCipherPolicyId'] = self.tlscipher_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('TLSCipherPolicyId') is not None:
            self.tlscipher_policy_id = m.get('TLSCipherPolicyId')
        return self


class DeleteTLSCipherPolicyResponseBody(TeaModel):
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


class DeleteTLSCipherPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTLSCipherPolicyResponseBody = None,
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
            temp_model = DeleteTLSCipherPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVServerGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        return self


class DeleteVServerGroupResponseBody(TeaModel):
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


class DeleteVServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVServerGroupResponseBody = None,
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
            temp_model = DeleteVServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessControlListAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
        acl_id: str = None,
        acl_entry_comment: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id
        self.acl_id = acl_id
        self.acl_entry_comment = acl_entry_comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_entry_comment is not None:
            result['AclEntryComment'] = self.acl_entry_comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclEntryComment') is not None:
            self.acl_entry_comment = m.get('AclEntryComment')
        return self


class DescribeAccessControlListAttributeResponseBodyAclEntrysAclEntry(TeaModel):
    def __init__(
        self,
        acl_entry_comment: str = None,
        acl_entry_ip: str = None,
    ):
        self.acl_entry_comment = acl_entry_comment
        self.acl_entry_ip = acl_entry_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.acl_entry_comment is not None:
            result['AclEntryComment'] = self.acl_entry_comment
        if self.acl_entry_ip is not None:
            result['AclEntryIP'] = self.acl_entry_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryComment') is not None:
            self.acl_entry_comment = m.get('AclEntryComment')
        if m.get('AclEntryIP') is not None:
            self.acl_entry_ip = m.get('AclEntryIP')
        return self


class DescribeAccessControlListAttributeResponseBodyAclEntrys(TeaModel):
    def __init__(
        self,
        acl_entry: List[DescribeAccessControlListAttributeResponseBodyAclEntrysAclEntry] = None,
    ):
        self.acl_entry = acl_entry

    def validate(self):
        if self.acl_entry:
            for k in self.acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AclEntry'] = []
        if self.acl_entry is not None:
            for k in self.acl_entry:
                result['AclEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entry = []
        if m.get('AclEntry') is not None:
            for k in m.get('AclEntry'):
                temp_model = DescribeAccessControlListAttributeResponseBodyAclEntrysAclEntry()
                self.acl_entry.append(temp_model.from_map(k))
        return self


class DescribeAccessControlListAttributeResponseBodyRelatedListenersRelatedListener(TeaModel):
    def __init__(
        self,
        acl_type: str = None,
        protocol: str = None,
        load_balancer_id: str = None,
        listener_port: int = None,
    ):
        self.acl_type = acl_type
        self.protocol = protocol
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class DescribeAccessControlListAttributeResponseBodyRelatedListeners(TeaModel):
    def __init__(
        self,
        related_listener: List[DescribeAccessControlListAttributeResponseBodyRelatedListenersRelatedListener] = None,
    ):
        self.related_listener = related_listener

    def validate(self):
        if self.related_listener:
            for k in self.related_listener:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RelatedListener'] = []
        if self.related_listener is not None:
            for k in self.related_listener:
                result['RelatedListener'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_listener = []
        if m.get('RelatedListener') is not None:
            for k in m.get('RelatedListener'):
                temp_model = DescribeAccessControlListAttributeResponseBodyRelatedListenersRelatedListener()
                self.related_listener.append(temp_model.from_map(k))
        return self


class DescribeAccessControlListAttributeResponseBody(TeaModel):
    def __init__(
        self,
        acl_entrys: DescribeAccessControlListAttributeResponseBodyAclEntrys = None,
        request_id: str = None,
        resource_group_id: str = None,
        acl_id: str = None,
        address_ipversion: str = None,
        related_listeners: DescribeAccessControlListAttributeResponseBodyRelatedListeners = None,
        acl_name: str = None,
    ):
        self.acl_entrys = acl_entrys
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.acl_id = acl_id
        self.address_ipversion = address_ipversion
        self.related_listeners = related_listeners
        self.acl_name = acl_name

    def validate(self):
        if self.acl_entrys:
            self.acl_entrys.validate()
        if self.related_listeners:
            self.related_listeners.validate()

    def to_map(self):
        result = dict()
        if self.acl_entrys is not None:
            result['AclEntrys'] = self.acl_entrys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.related_listeners is not None:
            result['RelatedListeners'] = self.related_listeners.to_map()
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntrys') is not None:
            temp_model = DescribeAccessControlListAttributeResponseBodyAclEntrys()
            self.acl_entrys = temp_model.from_map(m['AclEntrys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('RelatedListeners') is not None:
            temp_model = DescribeAccessControlListAttributeResponseBodyRelatedListeners()
            self.related_listeners = temp_model.from_map(m['RelatedListeners'])
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        return self


class DescribeAccessControlListAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccessControlListAttributeResponseBody = None,
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
            temp_model = DescribeAccessControlListAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessControlListsRequestTag(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeAccessControlListsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
        acl_name: str = None,
        address_ipversion: str = None,
        page_size: int = None,
        page_number: int = None,
        resource_group_id: str = None,
        tag: List[DescribeAccessControlListsRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id
        self.acl_name = acl_name
        self.address_ipversion = address_ipversion
        self.page_size = page_size
        self.page_number = page_number
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeAccessControlListsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeAccessControlListsResponseBodyAclsAcl(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        address_ipversion: str = None,
        resource_group_id: str = None,
        acl_name: str = None,
    ):
        self.acl_id = acl_id
        self.address_ipversion = address_ipversion
        self.resource_group_id = resource_group_id
        self.acl_name = acl_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        return self


class DescribeAccessControlListsResponseBodyAcls(TeaModel):
    def __init__(
        self,
        acl: List[DescribeAccessControlListsResponseBodyAclsAcl] = None,
    ):
        self.acl = acl

    def validate(self):
        if self.acl:
            for k in self.acl:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Acl'] = []
        if self.acl is not None:
            for k in self.acl:
                result['Acl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl = []
        if m.get('Acl') is not None:
            for k in m.get('Acl'):
                temp_model = DescribeAccessControlListsResponseBodyAclsAcl()
                self.acl.append(temp_model.from_map(k))
        return self


class DescribeAccessControlListsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        acls: DescribeAccessControlListsResponseBodyAcls = None,
        count: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.acls = acls
        self.count = count

    def validate(self):
        if self.acls:
            self.acls.validate()

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
        if self.acls is not None:
            result['Acls'] = self.acls.to_map()
        if self.count is not None:
            result['Count'] = self.count
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
        if m.get('Acls') is not None:
            temp_model = DescribeAccessControlListsResponseBodyAcls()
            self.acls = temp_model.from_map(m['Acls'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeAccessControlListsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccessControlListsResponseBody = None,
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
            temp_model = DescribeAccessControlListsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        address_type: str = None,
        address_ipversion: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.address_type = address_type
        self.address_ipversion = address_ipversion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        return self


class DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResourcesSupportResource(TeaModel):
    def __init__(
        self,
        address_ipversion: str = None,
        address_type: str = None,
    ):
        self.address_ipversion = address_ipversion
        self.address_type = address_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        return self


class DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResources(TeaModel):
    def __init__(
        self,
        support_resource: List[DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k in m.get('SupportResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResource(TeaModel):
    def __init__(
        self,
        slave_zone_id: str = None,
        support_resources: DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResources = None,
        master_zone_id: str = None,
    ):
        self.slave_zone_id = slave_zone_id
        self.support_resources = support_resources
        self.master_zone_id = master_zone_id

    def validate(self):
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = dict()
        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')
        if m.get('SupportResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResourceSupportResources()
            self.support_resources = temp_model.from_map(m['SupportResources'])
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableResources(TeaModel):
    def __init__(
        self,
        available_resource: List[DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResource] = None,
    ):
        self.available_resource = available_resource

    def validate(self):
        if self.available_resource:
            for k in self.available_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AvailableResource'] = []
        if self.available_resource is not None:
            for k in self.available_resource:
                result['AvailableResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resource = []
        if m.get('AvailableResource') is not None:
            for k in m.get('AvailableResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_resources: DescribeAvailableResourceResponseBodyAvailableResources = None,
    ):
        self.request_id = request_id
        self.available_resources = available_resources

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableResources()
            self.available_resources = temp_model.from_map(m['AvailableResources'])
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableResourceResponseBody = None,
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCACertificatesRequestTag(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeCACertificatesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        cacertificate_id: str = None,
        resource_group_id: str = None,
        tag: List[DescribeCACertificatesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.cacertificate_id = cacertificate_id
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeCACertificatesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeCACertificatesResponseBodyCACertificatesCACertificate(TeaModel):
    def __init__(
        self,
        create_time_stamp: int = None,
        expire_time: str = None,
        create_time: str = None,
        expire_time_stamp: int = None,
        cacertificate_id: str = None,
        region_id: str = None,
        fingerprint: str = None,
        resource_group_id: str = None,
        common_name: str = None,
        cacertificate_name: str = None,
    ):
        self.create_time_stamp = create_time_stamp
        self.expire_time = expire_time
        self.create_time = create_time
        self.expire_time_stamp = expire_time_stamp
        self.cacertificate_id = cacertificate_id
        self.region_id = region_id
        self.fingerprint = fingerprint
        self.resource_group_id = resource_group_id
        self.common_name = common_name
        self.cacertificate_name = cacertificate_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time_stamp is not None:
            result['ExpireTimeStamp'] = self.expire_time_stamp
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.cacertificate_name is not None:
            result['CACertificateName'] = self.cacertificate_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTimeStamp') is not None:
            self.expire_time_stamp = m.get('ExpireTimeStamp')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('CACertificateName') is not None:
            self.cacertificate_name = m.get('CACertificateName')
        return self


class DescribeCACertificatesResponseBodyCACertificates(TeaModel):
    def __init__(
        self,
        cacertificate: List[DescribeCACertificatesResponseBodyCACertificatesCACertificate] = None,
    ):
        self.cacertificate = cacertificate

    def validate(self):
        if self.cacertificate:
            for k in self.cacertificate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CACertificate'] = []
        if self.cacertificate is not None:
            for k in self.cacertificate:
                result['CACertificate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cacertificate = []
        if m.get('CACertificate') is not None:
            for k in m.get('CACertificate'):
                temp_model = DescribeCACertificatesResponseBodyCACertificatesCACertificate()
                self.cacertificate.append(temp_model.from_map(k))
        return self


class DescribeCACertificatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cacertificates: DescribeCACertificatesResponseBodyCACertificates = None,
    ):
        self.request_id = request_id
        self.cacertificates = cacertificates

    def validate(self):
        if self.cacertificates:
            self.cacertificates.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cacertificates is not None:
            result['CACertificates'] = self.cacertificates.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CACertificates') is not None:
            temp_model = DescribeCACertificatesResponseBodyCACertificates()
            self.cacertificates = temp_model.from_map(m['CACertificates'])
        return self


class DescribeCACertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCACertificatesResponseBody = None,
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
            temp_model = DescribeCACertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainExtensionAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        domain_extension_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.domain_extension_id = domain_extension_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        return self


class DescribeDomainExtensionAttributeResponseBody(TeaModel):
    def __init__(
        self,
        listener_port: int = None,
        domain_extension_id: str = None,
        request_id: str = None,
        server_certificate_id: str = None,
        load_balancer_id: str = None,
        domain: str = None,
    ):
        self.listener_port = listener_port
        self.domain_extension_id = domain_extension_id
        self.request_id = request_id
        self.server_certificate_id = server_certificate_id
        self.load_balancer_id = load_balancer_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainExtensionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainExtensionAttributeResponseBody = None,
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
            temp_model = DescribeDomainExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainExtensionsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        domain_extension_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.domain_extension_id = domain_extension_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        return self


class DescribeDomainExtensionsResponseBodyDomainExtensionsDomainExtension(TeaModel):
    def __init__(
        self,
        domain: str = None,
        server_certificate_id: str = None,
        domain_extension_id: str = None,
    ):
        self.domain = domain
        self.server_certificate_id = server_certificate_id
        self.domain_extension_id = domain_extension_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        return self


class DescribeDomainExtensionsResponseBodyDomainExtensions(TeaModel):
    def __init__(
        self,
        domain_extension: List[DescribeDomainExtensionsResponseBodyDomainExtensionsDomainExtension] = None,
    ):
        self.domain_extension = domain_extension

    def validate(self):
        if self.domain_extension:
            for k in self.domain_extension:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainExtension'] = []
        if self.domain_extension is not None:
            for k in self.domain_extension:
                result['DomainExtension'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_extension = []
        if m.get('DomainExtension') is not None:
            for k in m.get('DomainExtension'):
                temp_model = DescribeDomainExtensionsResponseBodyDomainExtensionsDomainExtension()
                self.domain_extension.append(temp_model.from_map(k))
        return self


class DescribeDomainExtensionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_extensions: DescribeDomainExtensionsResponseBodyDomainExtensions = None,
    ):
        self.request_id = request_id
        self.domain_extensions = domain_extensions

    def validate(self):
        if self.domain_extensions:
            self.domain_extensions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_extensions is not None:
            result['DomainExtensions'] = self.domain_extensions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainExtensions') is not None:
            temp_model = DescribeDomainExtensionsResponseBodyDomainExtensions()
            self.domain_extensions = temp_model.from_map(m['DomainExtensions'])
        return self


class DescribeDomainExtensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainExtensionsResponseBody = None,
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
            temp_model = DescribeDomainExtensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        listener_protocol: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.listener_protocol = listener_protocol
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeHealthStatusResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        eni_host: str = None,
        protocol: str = None,
        server_health_status: str = None,
        listener_port: int = None,
        server_ip: str = None,
        port: int = None,
        server_id: str = None,
    ):
        self.type = type
        self.eni_host = eni_host
        self.protocol = protocol
        self.server_health_status = server_health_status
        self.listener_port = listener_port
        self.server_ip = server_ip
        self.port = port
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.eni_host is not None:
            result['EniHost'] = self.eni_host
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EniHost') is not None:
            self.eni_host = m.get('EniHost')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class DescribeHealthStatusResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[DescribeHealthStatusResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = DescribeHealthStatusResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class DescribeHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        backend_servers: DescribeHealthStatusResponseBodyBackendServers = None,
    ):
        self.request_id = request_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackendServers') is not None:
            temp_model = DescribeHealthStatusResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class DescribeHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHealthStatusResponseBody = None,
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
            temp_model = DescribeHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeListenerAccessControlAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeListenerAccessControlAttributeResponseBody(TeaModel):
    def __init__(
        self,
        access_control_status: str = None,
        request_id: str = None,
        source_items: str = None,
    ):
        self.access_control_status = access_control_status
        self.request_id = request_id
        self.source_items = source_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_control_status is not None:
            result['AccessControlStatus'] = self.access_control_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_items is not None:
            result['SourceItems'] = self.source_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlStatus') is not None:
            self.access_control_status = m.get('AccessControlStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceItems') is not None:
            self.source_items = m.get('SourceItems')
        return self


class DescribeListenerAccessControlAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeListenerAccessControlAttributeResponseBody = None,
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
            temp_model = DescribeListenerAccessControlAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        include_reserved_data: bool = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.include_reserved_data = include_reserved_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.include_reserved_data is not None:
            result['IncludeReservedData'] = self.include_reserved_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('IncludeReservedData') is not None:
            self.include_reserved_data = m.get('IncludeReservedData')
        return self


class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal(TeaModel):
    def __init__(
        self,
        listener_protocal: str = None,
        listener_port: int = None,
    ):
        self.listener_protocal = listener_protocal
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.listener_protocal is not None:
            result['ListenerProtocal'] = self.listener_protocal
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerProtocal') is not None:
            self.listener_protocal = m.get('ListenerProtocal')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal(TeaModel):
    def __init__(
        self,
        listener_port_and_protocal: List[DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal] = None,
    ):
        self.listener_port_and_protocal = listener_port_and_protocal

    def validate(self):
        if self.listener_port_and_protocal:
            for k in self.listener_port_and_protocal:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ListenerPortAndProtocal'] = []
        if self.listener_port_and_protocal is not None:
            for k in self.listener_port_and_protocal:
                result['ListenerPortAndProtocal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_port_and_protocal = []
        if m.get('ListenerPortAndProtocal') is not None:
            for k in m.get('ListenerPortAndProtocal'):
                temp_model = DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal()
                self.listener_port_and_protocal.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class DescribeLoadBalancerAttributeResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancerAttributeResponseBodyListenerPorts(TeaModel):
    def __init__(
        self,
        listener_port: List[int] = None,
    ):
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol(TeaModel):
    def __init__(
        self,
        listener_protocol: str = None,
        listener_forward: str = None,
        description: str = None,
        listener_port: int = None,
        forward_port: int = None,
    ):
        self.listener_protocol = listener_protocol
        self.listener_forward = listener_forward
        self.description = description
        self.listener_port = listener_port
        self.forward_port = forward_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        return self


class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol(TeaModel):
    def __init__(
        self,
        listener_port_and_protocol: List[DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol] = None,
    ):
        self.listener_port_and_protocol = listener_port_and_protocol

    def validate(self):
        if self.listener_port_and_protocol:
            for k in self.listener_port_and_protocol:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ListenerPortAndProtocol'] = []
        if self.listener_port_and_protocol is not None:
            for k in self.listener_port_and_protocol:
                result['ListenerPortAndProtocol'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_port_and_protocol = []
        if m.get('ListenerPortAndProtocol') is not None:
            for k in m.get('ListenerPortAndProtocol'):
                temp_model = DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol()
                self.listener_port_and_protocol.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        address: str = None,
        resource_group_id: str = None,
        listener_ports_and_protocal: DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal = None,
        backend_servers: DescribeLoadBalancerAttributeResponseBodyBackendServers = None,
        load_balancer_spec: str = None,
        modification_protection_reason: str = None,
        listener_ports: DescribeLoadBalancerAttributeResponseBodyListenerPorts = None,
        request_id: str = None,
        v_switch_id: str = None,
        renewal_status: str = None,
        pay_type: str = None,
        internet_charge_type: str = None,
        vpc_id: str = None,
        delete_protection: str = None,
        end_time_stamp: int = None,
        load_balancer_status: str = None,
        auto_release_time: int = None,
        renewal_duration: int = None,
        end_time: str = None,
        address_ipversion: str = None,
        load_balancer_id: str = None,
        listener_ports_and_protocol: DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol = None,
        modification_protection_status: str = None,
        network_type: str = None,
        bandwidth: int = None,
        master_zone_id: str = None,
        create_time: str = None,
        renewal_cyc_unit: str = None,
        slave_zone_id: str = None,
        region_id_alias: str = None,
        load_balancer_name: str = None,
        region_id: str = None,
        address_type: str = None,
        create_time_stamp: int = None,
    ):
        self.address = address
        self.resource_group_id = resource_group_id
        self.listener_ports_and_protocal = listener_ports_and_protocal
        self.backend_servers = backend_servers
        self.load_balancer_spec = load_balancer_spec
        self.modification_protection_reason = modification_protection_reason
        self.listener_ports = listener_ports
        self.request_id = request_id
        self.v_switch_id = v_switch_id
        self.renewal_status = renewal_status
        self.pay_type = pay_type
        self.internet_charge_type = internet_charge_type
        self.vpc_id = vpc_id
        self.delete_protection = delete_protection
        self.end_time_stamp = end_time_stamp
        self.load_balancer_status = load_balancer_status
        self.auto_release_time = auto_release_time
        self.renewal_duration = renewal_duration
        self.end_time = end_time
        self.address_ipversion = address_ipversion
        self.load_balancer_id = load_balancer_id
        self.listener_ports_and_protocol = listener_ports_and_protocol
        self.modification_protection_status = modification_protection_status
        self.network_type = network_type
        self.bandwidth = bandwidth
        self.master_zone_id = master_zone_id
        self.create_time = create_time
        self.renewal_cyc_unit = renewal_cyc_unit
        self.slave_zone_id = slave_zone_id
        self.region_id_alias = region_id_alias
        self.load_balancer_name = load_balancer_name
        self.region_id = region_id
        self.address_type = address_type
        self.create_time_stamp = create_time_stamp

    def validate(self):
        if self.listener_ports_and_protocal:
            self.listener_ports_and_protocal.validate()
        if self.backend_servers:
            self.backend_servers.validate()
        if self.listener_ports:
            self.listener_ports.validate()
        if self.listener_ports_and_protocol:
            self.listener_ports_and_protocol.validate()

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.listener_ports_and_protocal is not None:
            result['ListenerPortsAndProtocal'] = self.listener_ports_and_protocal.to_map()
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason
        if self.listener_ports is not None:
            result['ListenerPorts'] = self.listener_ports.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection
        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time
        if self.renewal_duration is not None:
            result['RenewalDuration'] = self.renewal_duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_ports_and_protocol is not None:
            result['ListenerPortsAndProtocol'] = self.listener_ports_and_protocol.to_map()
        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.renewal_cyc_unit is not None:
            result['RenewalCycUnit'] = self.renewal_cyc_unit
        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id
        if self.region_id_alias is not None:
            result['RegionIdAlias'] = self.region_id_alias
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ListenerPortsAndProtocal') is not None:
            temp_model = DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal()
            self.listener_ports_and_protocal = temp_model.from_map(m['ListenerPortsAndProtocal'])
        if m.get('BackendServers') is not None:
            temp_model = DescribeLoadBalancerAttributeResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')
        if m.get('ListenerPorts') is not None:
            temp_model = DescribeLoadBalancerAttributeResponseBodyListenerPorts()
            self.listener_ports = temp_model.from_map(m['ListenerPorts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')
        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')
        if m.get('RenewalDuration') is not None:
            self.renewal_duration = m.get('RenewalDuration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPortsAndProtocol') is not None:
            temp_model = DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol()
            self.listener_ports_and_protocol = temp_model.from_map(m['ListenerPortsAndProtocol'])
        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RenewalCycUnit') is not None:
            self.renewal_cyc_unit = m.get('RenewalCycUnit')
        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')
        if m.get('RegionIdAlias') is not None:
            self.region_id_alias = m.get('RegionIdAlias')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        return self


class DescribeLoadBalancerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerAttributeResponseBody = None,
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
            temp_model = DescribeLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerHTTPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeLoadBalancerHTTPListenerAttributeResponseBodyRulesRule(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        domain: str = None,
        url: str = None,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.domain = domain
        self.url = url
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.url is not None:
            result['Url'] = self.url
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeLoadBalancerHTTPListenerAttributeResponseBodyRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeLoadBalancerHTTPListenerAttributeResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeLoadBalancerHTTPListenerAttributeResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancerHTTPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        cookie_timeout: int = None,
        vserver_group_id: str = None,
        description: str = None,
        unhealthy_threshold: int = None,
        health_check_uri: str = None,
        scheduler: str = None,
        health_check: str = None,
        idle_timeout: int = None,
        backend_server_port: int = None,
        xforwarded_for__slbid: str = None,
        health_check_connect_port: int = None,
        bandwidth: int = None,
        security_status: str = None,
        gzip: str = None,
        sticky_session_type: str = None,
        xforwarded_for__slbip: str = None,
        health_check_http_code: str = None,
        status: str = None,
        cookie: str = None,
        request_timeout: int = None,
        listener_port: int = None,
        health_check_interval: int = None,
        request_id: str = None,
        acl_id: str = None,
        health_check_timeout: int = None,
        rules: DescribeLoadBalancerHTTPListenerAttributeResponseBodyRules = None,
        listener_forward: str = None,
        sticky_session: str = None,
        acl_status: str = None,
        forward_port: int = None,
        healthy_threshold: int = None,
        xforwarded_for: str = None,
        health_check_domain: str = None,
        acl_type: str = None,
        xforwarded_for_proto: str = None,
    ):
        self.cookie_timeout = cookie_timeout
        self.vserver_group_id = vserver_group_id
        self.description = description
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_uri = health_check_uri
        self.scheduler = scheduler
        self.health_check = health_check
        self.idle_timeout = idle_timeout
        self.backend_server_port = backend_server_port
        self.xforwarded_for__slbid = xforwarded_for__slbid
        self.health_check_connect_port = health_check_connect_port
        self.bandwidth = bandwidth
        self.security_status = security_status
        self.gzip = gzip
        self.sticky_session_type = sticky_session_type
        self.xforwarded_for__slbip = xforwarded_for__slbip
        self.health_check_http_code = health_check_http_code
        self.status = status
        self.cookie = cookie
        self.request_timeout = request_timeout
        self.listener_port = listener_port
        self.health_check_interval = health_check_interval
        self.request_id = request_id
        self.acl_id = acl_id
        self.health_check_timeout = health_check_timeout
        self.rules = rules
        self.listener_forward = listener_forward
        self.sticky_session = sticky_session
        self.acl_status = acl_status
        self.forward_port = forward_port
        self.healthy_threshold = healthy_threshold
        self.xforwarded_for = xforwarded_for
        self.health_check_domain = health_check_domain
        self.acl_type = acl_type
        self.xforwarded_for_proto = xforwarded_for_proto

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.xforwarded_for__slbid is not None:
            result['XForwardedFor_SLBID'] = self.xforwarded_for__slbid
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.security_status is not None:
            result['SecurityStatus'] = self.security_status
        if self.gzip is not None:
            result['Gzip'] = self.gzip
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.xforwarded_for__slbip is not None:
            result['XForwardedFor_SLBIP'] = self.xforwarded_for__slbip
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.status is not None:
            result['Status'] = self.status
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.xforwarded_for_proto is not None:
            result['XForwardedFor_proto'] = self.xforwarded_for_proto
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('XForwardedFor_SLBID') is not None:
            self.xforwarded_for__slbid = m.get('XForwardedFor_SLBID')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('SecurityStatus') is not None:
            self.security_status = m.get('SecurityStatus')
        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('XForwardedFor_SLBIP') is not None:
            self.xforwarded_for__slbip = m.get('XForwardedFor_SLBIP')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('Rules') is not None:
            temp_model = DescribeLoadBalancerHTTPListenerAttributeResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('XForwardedFor_proto') is not None:
            self.xforwarded_for_proto = m.get('XForwardedFor_proto')
        return self


class DescribeLoadBalancerHTTPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerHTTPListenerAttributeResponseBody = None,
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
            temp_model = DescribeLoadBalancerHTTPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerHTTPSListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponseBodyDomainExtensionsDomainExtension(TeaModel):
    def __init__(
        self,
        domain: str = None,
        server_certificate_id: str = None,
        domain_extension_id: str = None,
    ):
        self.domain = domain
        self.server_certificate_id = server_certificate_id
        self.domain_extension_id = domain_extension_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponseBodyDomainExtensions(TeaModel):
    def __init__(
        self,
        domain_extension: List[DescribeLoadBalancerHTTPSListenerAttributeResponseBodyDomainExtensionsDomainExtension] = None,
    ):
        self.domain_extension = domain_extension

    def validate(self):
        if self.domain_extension:
            for k in self.domain_extension:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainExtension'] = []
        if self.domain_extension is not None:
            for k in self.domain_extension:
                result['DomainExtension'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_extension = []
        if m.get('DomainExtension') is not None:
            for k in m.get('DomainExtension'):
                temp_model = DescribeLoadBalancerHTTPSListenerAttributeResponseBodyDomainExtensionsDomainExtension()
                self.domain_extension.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponseBodyRulesRule(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        domain: str = None,
        url: str = None,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.domain = domain
        self.url = url
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.url is not None:
            result['Url'] = self.url
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponseBodyRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeLoadBalancerHTTPSListenerAttributeResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeLoadBalancerHTTPSListenerAttributeResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        unhealthy_threshold: int = None,
        health_check_uri: str = None,
        health_check: str = None,
        domain_extensions: DescribeLoadBalancerHTTPSListenerAttributeResponseBodyDomainExtensions = None,
        backend_server_port: int = None,
        xforwarded_for__slbport: str = None,
        sticky_session_type: str = None,
        status: str = None,
        cookie: str = None,
        request_timeout: int = None,
        tlscipher_policy: str = None,
        health_check_interval: int = None,
        request_id: str = None,
        cacertificate_id: str = None,
        health_check_timeout: int = None,
        acl_status: str = None,
        healthy_threshold: int = None,
        health_check_domain: str = None,
        acl_type: str = None,
        xforwarded_for_proto: str = None,
        enable_http_2: str = None,
        cookie_timeout: int = None,
        vserver_group_id: str = None,
        description: str = None,
        scheduler: str = None,
        idle_timeout: int = None,
        xforwarded_for__slbid: str = None,
        health_check_connect_port: int = None,
        bandwidth: int = None,
        security_status: str = None,
        gzip: str = None,
        server_certificate_id: str = None,
        xforwarded_for__slbip: str = None,
        health_check_http_code: str = None,
        listener_port: int = None,
        xforwarded_for__client_cert_subject_dn: str = None,
        acl_id: str = None,
        rules: DescribeLoadBalancerHTTPSListenerAttributeResponseBodyRules = None,
        xforwarded_for__client_cert_issuer_dn: str = None,
        sticky_session: str = None,
        xforwarded_for: str = None,
        xforwarded_for__client_src_port: str = None,
        xforwarded_for__client_cert_client_verify: str = None,
        xforwarded_for__client_cert_fingerprint: str = None,
    ):
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_uri = health_check_uri
        self.health_check = health_check
        self.domain_extensions = domain_extensions
        self.backend_server_port = backend_server_port
        self.xforwarded_for__slbport = xforwarded_for__slbport
        self.sticky_session_type = sticky_session_type
        self.status = status
        self.cookie = cookie
        self.request_timeout = request_timeout
        self.tlscipher_policy = tlscipher_policy
        self.health_check_interval = health_check_interval
        self.request_id = request_id
        self.cacertificate_id = cacertificate_id
        self.health_check_timeout = health_check_timeout
        self.acl_status = acl_status
        self.healthy_threshold = healthy_threshold
        self.health_check_domain = health_check_domain
        self.acl_type = acl_type
        self.xforwarded_for_proto = xforwarded_for_proto
        self.enable_http_2 = enable_http_2
        self.cookie_timeout = cookie_timeout
        self.vserver_group_id = vserver_group_id
        self.description = description
        self.scheduler = scheduler
        self.idle_timeout = idle_timeout
        self.xforwarded_for__slbid = xforwarded_for__slbid
        self.health_check_connect_port = health_check_connect_port
        self.bandwidth = bandwidth
        self.security_status = security_status
        self.gzip = gzip
        self.server_certificate_id = server_certificate_id
        self.xforwarded_for__slbip = xforwarded_for__slbip
        self.health_check_http_code = health_check_http_code
        self.listener_port = listener_port
        self.xforwarded_for__client_cert_subject_dn = xforwarded_for__client_cert_subject_dn
        self.acl_id = acl_id
        self.rules = rules
        self.xforwarded_for__client_cert_issuer_dn = xforwarded_for__client_cert_issuer_dn
        self.sticky_session = sticky_session
        self.xforwarded_for = xforwarded_for
        self.xforwarded_for__client_src_port = xforwarded_for__client_src_port
        self.xforwarded_for__client_cert_client_verify = xforwarded_for__client_cert_client_verify
        self.xforwarded_for__client_cert_fingerprint = xforwarded_for__client_cert_fingerprint

    def validate(self):
        if self.domain_extensions:
            self.domain_extensions.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.domain_extensions is not None:
            result['DomainExtensions'] = self.domain_extensions.to_map()
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.xforwarded_for__slbport is not None:
            result['XForwardedFor_SLBPORT'] = self.xforwarded_for__slbport
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.status is not None:
            result['Status'] = self.status
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.tlscipher_policy is not None:
            result['TLSCipherPolicy'] = self.tlscipher_policy
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.xforwarded_for_proto is not None:
            result['XForwardedFor_proto'] = self.xforwarded_for_proto
        if self.enable_http_2 is not None:
            result['EnableHttp2'] = self.enable_http_2
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.xforwarded_for__slbid is not None:
            result['XForwardedFor_SLBID'] = self.xforwarded_for__slbid
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.security_status is not None:
            result['SecurityStatus'] = self.security_status
        if self.gzip is not None:
            result['Gzip'] = self.gzip
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.xforwarded_for__slbip is not None:
            result['XForwardedFor_SLBIP'] = self.xforwarded_for__slbip
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.xforwarded_for__client_cert_subject_dn is not None:
            result['XForwardedFor_ClientCertSubjectDN'] = self.xforwarded_for__client_cert_subject_dn
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.xforwarded_for__client_cert_issuer_dn is not None:
            result['XForwardedFor_ClientCertIssuerDN'] = self.xforwarded_for__client_cert_issuer_dn
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        if self.xforwarded_for__client_src_port is not None:
            result['XForwardedFor_ClientSrcPort'] = self.xforwarded_for__client_src_port
        if self.xforwarded_for__client_cert_client_verify is not None:
            result['XForwardedFor_ClientCertClientVerify'] = self.xforwarded_for__client_cert_client_verify
        if self.xforwarded_for__client_cert_fingerprint is not None:
            result['XForwardedFor_ClientCertFingerprint'] = self.xforwarded_for__client_cert_fingerprint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('DomainExtensions') is not None:
            temp_model = DescribeLoadBalancerHTTPSListenerAttributeResponseBodyDomainExtensions()
            self.domain_extensions = temp_model.from_map(m['DomainExtensions'])
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('XForwardedFor_SLBPORT') is not None:
            self.xforwarded_for__slbport = m.get('XForwardedFor_SLBPORT')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('TLSCipherPolicy') is not None:
            self.tlscipher_policy = m.get('TLSCipherPolicy')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('XForwardedFor_proto') is not None:
            self.xforwarded_for_proto = m.get('XForwardedFor_proto')
        if m.get('EnableHttp2') is not None:
            self.enable_http_2 = m.get('EnableHttp2')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('XForwardedFor_SLBID') is not None:
            self.xforwarded_for__slbid = m.get('XForwardedFor_SLBID')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('SecurityStatus') is not None:
            self.security_status = m.get('SecurityStatus')
        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('XForwardedFor_SLBIP') is not None:
            self.xforwarded_for__slbip = m.get('XForwardedFor_SLBIP')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('XForwardedFor_ClientCertSubjectDN') is not None:
            self.xforwarded_for__client_cert_subject_dn = m.get('XForwardedFor_ClientCertSubjectDN')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Rules') is not None:
            temp_model = DescribeLoadBalancerHTTPSListenerAttributeResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('XForwardedFor_ClientCertIssuerDN') is not None:
            self.xforwarded_for__client_cert_issuer_dn = m.get('XForwardedFor_ClientCertIssuerDN')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        if m.get('XForwardedFor_ClientSrcPort') is not None:
            self.xforwarded_for__client_src_port = m.get('XForwardedFor_ClientSrcPort')
        if m.get('XForwardedFor_ClientCertClientVerify') is not None:
            self.xforwarded_for__client_cert_client_verify = m.get('XForwardedFor_ClientCertClientVerify')
        if m.get('XForwardedFor_ClientCertFingerprint') is not None:
            self.xforwarded_for__client_cert_fingerprint = m.get('XForwardedFor_ClientCertFingerprint')
        return self


class DescribeLoadBalancerHTTPSListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerHTTPSListenerAttributeResponseBody = None,
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
            temp_model = DescribeLoadBalancerHTTPSListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancersRequestTag(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeLoadBalancersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        server_id: str = None,
        address_ipversion: str = None,
        load_balancer_status: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        server_intranet_address: str = None,
        address_type: str = None,
        internet_charge_type: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        network_type: str = None,
        address: str = None,
        master_zone_id: str = None,
        slave_zone_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        pay_type: str = None,
        resource_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        support_private_link: bool = None,
        fuzzy: str = None,
        business_status: str = None,
        tag: List[DescribeLoadBalancersRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.server_id = server_id
        self.address_ipversion = address_ipversion
        self.load_balancer_status = load_balancer_status
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.server_intranet_address = server_intranet_address
        self.address_type = address_type
        self.internet_charge_type = internet_charge_type
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.network_type = network_type
        self.address = address
        self.master_zone_id = master_zone_id
        self.slave_zone_id = slave_zone_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.pay_type = pay_type
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.support_private_link = support_private_link
        self.fuzzy = fuzzy
        self.business_status = business_status
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.server_intranet_address is not None:
            result['ServerIntranetAddress'] = self.server_intranet_address
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.address is not None:
            result['Address'] = self.address
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.support_private_link is not None:
            result['SupportPrivateLink'] = self.support_private_link
        if self.fuzzy is not None:
            result['Fuzzy'] = self.fuzzy
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('ServerIntranetAddress') is not None:
            self.server_intranet_address = m.get('ServerIntranetAddress')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SupportPrivateLink') is not None:
            self.support_private_link = m.get('SupportPrivateLink')
        if m.get('Fuzzy') is not None:
            self.fuzzy = m.get('Fuzzy')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        create_time_stamp: int = None,
        load_balancer_id: str = None,
        create_time: str = None,
        pay_type: str = None,
        address_type: str = None,
        network_type: str = None,
        region_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        address_ipversion: str = None,
        v_switch_id: str = None,
        load_balancer_status: str = None,
        load_balancer_name: str = None,
        resource_group_id: str = None,
        internet_charge_type: str = None,
        address: str = None,
        slave_zone_id: str = None,
        region_id_alias: str = None,
        master_zone_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.create_time_stamp = create_time_stamp
        self.load_balancer_id = load_balancer_id
        self.create_time = create_time
        self.pay_type = pay_type
        self.address_type = address_type
        self.network_type = network_type
        self.region_id = region_id
        self.modification_protection_reason = modification_protection_reason
        self.modification_protection_status = modification_protection_status
        self.address_ipversion = address_ipversion
        self.v_switch_id = v_switch_id
        self.load_balancer_status = load_balancer_status
        self.load_balancer_name = load_balancer_name
        self.resource_group_id = resource_group_id
        self.internet_charge_type = internet_charge_type
        self.address = address
        self.slave_zone_id = slave_zone_id
        self.region_id_alias = region_id_alias
        self.master_zone_id = master_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason
        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.address is not None:
            result['Address'] = self.address
        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id
        if self.region_id_alias is not None:
            result['RegionIdAlias'] = self.region_id_alias
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')
        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')
        if m.get('RegionIdAlias') is not None:
            self.region_id_alias = m.get('RegionIdAlias')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        return self


class DescribeLoadBalancersResponseBodyLoadBalancers(TeaModel):
    def __init__(
        self,
        load_balancer: List[DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer] = None,
    ):
        self.load_balancer = load_balancer

    def validate(self):
        if self.load_balancer:
            for k in self.load_balancer:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LoadBalancer'] = []
        if self.load_balancer is not None:
            for k in self.load_balancer:
                result['LoadBalancer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer = []
        if m.get('LoadBalancer') is not None:
            for k in m.get('LoadBalancer'):
                temp_model = DescribeLoadBalancersResponseBodyLoadBalancersLoadBalancer()
                self.load_balancer.append(temp_model.from_map(k))
        return self


class DescribeLoadBalancersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        load_balancers: DescribeLoadBalancersResponseBodyLoadBalancers = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.load_balancers = load_balancers

    def validate(self):
        if self.load_balancers:
            self.load_balancers.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('LoadBalancers') is not None:
            temp_model = DescribeLoadBalancersResponseBodyLoadBalancers()
            self.load_balancers = temp_model.from_map(m['LoadBalancers'])
        return self


class DescribeLoadBalancersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancersResponseBody = None,
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
            temp_model = DescribeLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerTCPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeLoadBalancerTCPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        description: str = None,
        syn_proxy: str = None,
        unhealthy_threshold: int = None,
        health_check_uri: str = None,
        scheduler: str = None,
        health_check: str = None,
        backend_server_port: int = None,
        persistence_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_method: str = None,
        bandwidth: int = None,
        health_check_http_code: str = None,
        established_timeout: int = None,
        status: str = None,
        listener_port: int = None,
        health_check_interval: int = None,
        request_id: str = None,
        acl_id: str = None,
        health_check_connect_timeout: int = None,
        acl_status: str = None,
        healthy_threshold: int = None,
        master_slave_server_group_id: str = None,
        health_check_domain: str = None,
        acl_type: str = None,
        health_check_type: str = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.description = description
        self.syn_proxy = syn_proxy
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_uri = health_check_uri
        self.scheduler = scheduler
        self.health_check = health_check
        self.backend_server_port = backend_server_port
        self.persistence_timeout = persistence_timeout
        self.health_check_connect_port = health_check_connect_port
        self.health_check_method = health_check_method
        self.bandwidth = bandwidth
        self.health_check_http_code = health_check_http_code
        self.established_timeout = established_timeout
        self.status = status
        self.listener_port = listener_port
        self.health_check_interval = health_check_interval
        self.request_id = request_id
        self.acl_id = acl_id
        self.health_check_connect_timeout = health_check_connect_timeout
        self.acl_status = acl_status
        self.healthy_threshold = healthy_threshold
        self.master_slave_server_group_id = master_slave_server_group_id
        self.health_check_domain = health_check_domain
        self.acl_type = acl_type
        self.health_check_type = health_check_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.syn_proxy is not None:
            result['SynProxy'] = self.syn_proxy
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.status is not None:
            result['Status'] = self.status
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SynProxy') is not None:
            self.syn_proxy = m.get('SynProxy')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        return self


class DescribeLoadBalancerTCPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerTCPListenerAttributeResponseBody = None,
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
            temp_model = DescribeLoadBalancerTCPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoadBalancerUDPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeLoadBalancerUDPListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        description: str = None,
        unhealthy_threshold: int = None,
        scheduler: str = None,
        health_check: str = None,
        backend_server_port: int = None,
        health_check_connect_port: int = None,
        bandwidth: int = None,
        status: str = None,
        listener_port: int = None,
        health_check_interval: int = None,
        request_id: str = None,
        acl_id: str = None,
        health_check_connect_timeout: int = None,
        acl_status: str = None,
        health_check_req: str = None,
        health_check_exp: str = None,
        healthy_threshold: int = None,
        master_slave_server_group_id: str = None,
        acl_type: str = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.description = description
        self.unhealthy_threshold = unhealthy_threshold
        self.scheduler = scheduler
        self.health_check = health_check
        self.backend_server_port = backend_server_port
        self.health_check_connect_port = health_check_connect_port
        self.bandwidth = bandwidth
        self.status = status
        self.listener_port = listener_port
        self.health_check_interval = health_check_interval
        self.request_id = request_id
        self.acl_id = acl_id
        self.health_check_connect_timeout = health_check_connect_timeout
        self.acl_status = acl_status
        self.health_check_req = health_check_req
        self.health_check_exp = health_check_exp
        self.healthy_threshold = healthy_threshold
        self.master_slave_server_group_id = master_slave_server_group_id
        self.acl_type = acl_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.status is not None:
            result['Status'] = self.status
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req
        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')
        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        return self


class DescribeLoadBalancerUDPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoadBalancerUDPListenerAttributeResponseBody = None,
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
            temp_model = DescribeLoadBalancerUDPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMasterSlaveServerGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        master_slave_server_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.master_slave_server_group_id = master_slave_server_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        return self


class DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_type: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id
        self.server_type = server_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        return self


class DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServers(TeaModel):
    def __init__(
        self,
        master_slave_backend_server: List[DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer] = None,
    ):
        self.master_slave_backend_server = master_slave_backend_server

    def validate(self):
        if self.master_slave_backend_server:
            for k in self.master_slave_backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MasterSlaveBackendServer'] = []
        if self.master_slave_backend_server is not None:
            for k in self.master_slave_backend_server:
                result['MasterSlaveBackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_slave_backend_server = []
        if m.get('MasterSlaveBackendServer') is not None:
            for k in m.get('MasterSlaveBackendServer'):
                temp_model = DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServersMasterSlaveBackendServer()
                self.master_slave_backend_server.append(temp_model.from_map(k))
        return self


class DescribeMasterSlaveServerGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        master_slave_server_group_id: str = None,
        load_balancer_id: str = None,
        master_slave_server_group_name: str = None,
        master_slave_backend_servers: DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServers = None,
    ):
        self.request_id = request_id
        self.master_slave_server_group_id = master_slave_server_group_id
        self.load_balancer_id = load_balancer_id
        self.master_slave_server_group_name = master_slave_server_group_name
        self.master_slave_backend_servers = master_slave_backend_servers

    def validate(self):
        if self.master_slave_backend_servers:
            self.master_slave_backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.master_slave_server_group_name is not None:
            result['MasterSlaveServerGroupName'] = self.master_slave_server_group_name
        if self.master_slave_backend_servers is not None:
            result['MasterSlaveBackendServers'] = self.master_slave_backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('MasterSlaveServerGroupName') is not None:
            self.master_slave_server_group_name = m.get('MasterSlaveServerGroupName')
        if m.get('MasterSlaveBackendServers') is not None:
            temp_model = DescribeMasterSlaveServerGroupAttributeResponseBodyMasterSlaveBackendServers()
            self.master_slave_backend_servers = temp_model.from_map(m['MasterSlaveBackendServers'])
        return self


class DescribeMasterSlaveServerGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMasterSlaveServerGroupAttributeResponseBody = None,
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
            temp_model = DescribeMasterSlaveServerGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMasterSlaveServerGroupsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        include_listener: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.include_listener = include_listener

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.include_listener is not None:
            result['IncludeListener'] = self.include_listener
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('IncludeListener') is not None:
            self.include_listener = m.get('IncludeListener')
        return self


class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListenersListener(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListeners(TeaModel):
    def __init__(
        self,
        listener: List[DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListenersListener] = None,
    ):
        self.listener = listener

    def validate(self):
        if self.listener:
            for k in self.listener:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Listener'] = []
        if self.listener is not None:
            for k in self.listener:
                result['Listener'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener = []
        if m.get('Listener') is not None:
            for k in m.get('Listener'):
                temp_model = DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListenersListener()
                self.listener.append(temp_model.from_map(k))
        return self


class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjects(TeaModel):
    def __init__(
        self,
        listeners: DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListeners = None,
    ):
        self.listeners = listeners

    def validate(self):
        if self.listeners:
            self.listeners.validate()

    def to_map(self):
        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            temp_model = DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListeners()
            self.listeners = temp_model.from_map(m['Listeners'])
        return self


class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroup(TeaModel):
    def __init__(
        self,
        master_slave_server_group_id: str = None,
        associated_objects: DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjects = None,
        master_slave_server_group_name: str = None,
    ):
        self.master_slave_server_group_id = master_slave_server_group_id
        self.associated_objects = associated_objects
        self.master_slave_server_group_name = master_slave_server_group_name

    def validate(self):
        if self.associated_objects:
            self.associated_objects.validate()

    def to_map(self):
        result = dict()
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.associated_objects is not None:
            result['AssociatedObjects'] = self.associated_objects.to_map()
        if self.master_slave_server_group_name is not None:
            result['MasterSlaveServerGroupName'] = self.master_slave_server_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('AssociatedObjects') is not None:
            temp_model = DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjects()
            self.associated_objects = temp_model.from_map(m['AssociatedObjects'])
        if m.get('MasterSlaveServerGroupName') is not None:
            self.master_slave_server_group_name = m.get('MasterSlaveServerGroupName')
        return self


class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroups(TeaModel):
    def __init__(
        self,
        master_slave_server_group: List[DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroup] = None,
    ):
        self.master_slave_server_group = master_slave_server_group

    def validate(self):
        if self.master_slave_server_group:
            for k in self.master_slave_server_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MasterSlaveServerGroup'] = []
        if self.master_slave_server_group is not None:
            for k in self.master_slave_server_group:
                result['MasterSlaveServerGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_slave_server_group = []
        if m.get('MasterSlaveServerGroup') is not None:
            for k in m.get('MasterSlaveServerGroup'):
                temp_model = DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroup()
                self.master_slave_server_group.append(temp_model.from_map(k))
        return self


class DescribeMasterSlaveServerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        master_slave_server_groups: DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroups = None,
    ):
        self.request_id = request_id
        self.master_slave_server_groups = master_slave_server_groups

    def validate(self):
        if self.master_slave_server_groups:
            self.master_slave_server_groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.master_slave_server_groups is not None:
            result['MasterSlaveServerGroups'] = self.master_slave_server_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MasterSlaveServerGroups') is not None:
            temp_model = DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroups()
            self.master_slave_server_groups = temp_model.from_map(m['MasterSlaveServerGroups'])
        return self


class DescribeMasterSlaveServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMasterSlaveServerGroupsResponseBody = None,
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
            temp_model = DescribeMasterSlaveServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
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


class DescribeRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        rule_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeRuleAttributeResponseBody(TeaModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        vserver_group_id: str = None,
        listener_port: str = None,
        health_check_interval: int = None,
        request_id: str = None,
        unhealthy_threshold: int = None,
        health_check_uri: str = None,
        scheduler: str = None,
        rule_id: str = None,
        health_check: str = None,
        load_balancer_id: str = None,
        health_check_timeout: int = None,
        url: str = None,
        sticky_session: str = None,
        health_check_connect_port: int = None,
        healthy_threshold: int = None,
        listener_sync: str = None,
        health_check_domain: str = None,
        sticky_session_type: str = None,
        domain: str = None,
        health_check_http_code: str = None,
        rule_name: str = None,
    ):
        self.cookie = cookie
        self.cookie_timeout = cookie_timeout
        self.vserver_group_id = vserver_group_id
        self.listener_port = listener_port
        self.health_check_interval = health_check_interval
        self.request_id = request_id
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_uri = health_check_uri
        self.scheduler = scheduler
        self.rule_id = rule_id
        self.health_check = health_check
        self.load_balancer_id = load_balancer_id
        self.health_check_timeout = health_check_timeout
        self.url = url
        self.sticky_session = sticky_session
        self.health_check_connect_port = health_check_connect_port
        self.healthy_threshold = healthy_threshold
        self.listener_sync = listener_sync
        self.health_check_domain = health_check_domain
        self.sticky_session_type = sticky_session_type
        self.domain = domain
        self.health_check_http_code = health_check_http_code
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.url is not None:
            result['Url'] = self.url
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.listener_sync is not None:
            result['ListenerSync'] = self.listener_sync
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('ListenerSync') is not None:
            self.listener_sync = m.get('ListenerSync')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRuleAttributeResponseBody = None,
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
            temp_model = DescribeRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRulesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        listener_protocol: str = None,
        listener_port: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.listener_protocol = listener_protocol
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class DescribeRulesResponseBodyRulesRule(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        health_check_http_code: str = None,
        domain: str = None,
        cookie: str = None,
        url: str = None,
        health_check_interval: int = None,
        health_check_uri: str = None,
        rule_id: str = None,
        rule_name: str = None,
        sticky_session_type: str = None,
        scheduler: str = None,
        health_check_connect_port: int = None,
        health_check_timeout: int = None,
        listener_sync: str = None,
        healthy_threshold: int = None,
        cookie_timeout: int = None,
        health_check_domain: str = None,
        unhealthy_threshold: int = None,
        sticky_session: str = None,
        health_check: str = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.health_check_http_code = health_check_http_code
        self.domain = domain
        self.cookie = cookie
        self.url = url
        self.health_check_interval = health_check_interval
        self.health_check_uri = health_check_uri
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.sticky_session_type = sticky_session_type
        self.scheduler = scheduler
        self.health_check_connect_port = health_check_connect_port
        self.health_check_timeout = health_check_timeout
        self.listener_sync = listener_sync
        self.healthy_threshold = healthy_threshold
        self.cookie_timeout = cookie_timeout
        self.health_check_domain = health_check_domain
        self.unhealthy_threshold = unhealthy_threshold
        self.sticky_session = sticky_session
        self.health_check = health_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.url is not None:
            result['Url'] = self.url
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.listener_sync is not None:
            result['ListenerSync'] = self.listener_sync
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('ListenerSync') is not None:
            self.listener_sync = m.get('ListenerSync')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        return self


class DescribeRulesResponseBodyRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeRulesResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeRulesResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: DescribeRulesResponseBodyRules = None,
    ):
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rules') is not None:
            temp_model = DescribeRulesResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class DescribeRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRulesResponseBody = None,
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
            temp_model = DescribeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServerCertificatesRequestTag(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeServerCertificatesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        server_certificate_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        resource_group_id: str = None,
        tag: List[DescribeServerCertificatesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.server_certificate_id = server_certificate_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeServerCertificatesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateSubjectAlternativeNames(TeaModel):
    def __init__(
        self,
        subject_alternative_name: List[str] = None,
    ):
        self.subject_alternative_name = subject_alternative_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subject_alternative_name is not None:
            result['SubjectAlternativeName'] = self.subject_alternative_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubjectAlternativeName') is not None:
            self.subject_alternative_name = m.get('SubjectAlternativeName')
        return self


class DescribeServerCertificatesResponseBodyServerCertificatesServerCertificate(TeaModel):
    def __init__(
        self,
        ali_cloud_certificate_name: str = None,
        create_time_stamp: int = None,
        expire_time: str = None,
        create_time: str = None,
        server_certificate_id: str = None,
        expire_time_stamp: int = None,
        region_id: str = None,
        server_certificate_name: str = None,
        fingerprint: str = None,
        subject_alternative_names: DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateSubjectAlternativeNames = None,
        common_name: str = None,
        resource_group_id: str = None,
        is_ali_cloud_certificate: int = None,
        ali_cloud_certificate_id: str = None,
    ):
        self.ali_cloud_certificate_name = ali_cloud_certificate_name
        self.create_time_stamp = create_time_stamp
        self.expire_time = expire_time
        self.create_time = create_time
        self.server_certificate_id = server_certificate_id
        self.expire_time_stamp = expire_time_stamp
        self.region_id = region_id
        self.server_certificate_name = server_certificate_name
        self.fingerprint = fingerprint
        self.subject_alternative_names = subject_alternative_names
        self.common_name = common_name
        self.resource_group_id = resource_group_id
        self.is_ali_cloud_certificate = is_ali_cloud_certificate
        self.ali_cloud_certificate_id = ali_cloud_certificate_id

    def validate(self):
        if self.subject_alternative_names:
            self.subject_alternative_names.validate()

    def to_map(self):
        result = dict()
        if self.ali_cloud_certificate_name is not None:
            result['AliCloudCertificateName'] = self.ali_cloud_certificate_name
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.expire_time_stamp is not None:
            result['ExpireTimeStamp'] = self.expire_time_stamp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_certificate_name is not None:
            result['ServerCertificateName'] = self.server_certificate_name
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names.to_map()
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.is_ali_cloud_certificate is not None:
            result['IsAliCloudCertificate'] = self.is_ali_cloud_certificate
        if self.ali_cloud_certificate_id is not None:
            result['AliCloudCertificateId'] = self.ali_cloud_certificate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliCloudCertificateName') is not None:
            self.ali_cloud_certificate_name = m.get('AliCloudCertificateName')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('ExpireTimeStamp') is not None:
            self.expire_time_stamp = m.get('ExpireTimeStamp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerCertificateName') is not None:
            self.server_certificate_name = m.get('ServerCertificateName')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('SubjectAlternativeNames') is not None:
            temp_model = DescribeServerCertificatesResponseBodyServerCertificatesServerCertificateSubjectAlternativeNames()
            self.subject_alternative_names = temp_model.from_map(m['SubjectAlternativeNames'])
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('IsAliCloudCertificate') is not None:
            self.is_ali_cloud_certificate = m.get('IsAliCloudCertificate')
        if m.get('AliCloudCertificateId') is not None:
            self.ali_cloud_certificate_id = m.get('AliCloudCertificateId')
        return self


class DescribeServerCertificatesResponseBodyServerCertificates(TeaModel):
    def __init__(
        self,
        server_certificate: List[DescribeServerCertificatesResponseBodyServerCertificatesServerCertificate] = None,
    ):
        self.server_certificate = server_certificate

    def validate(self):
        if self.server_certificate:
            for k in self.server_certificate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ServerCertificate'] = []
        if self.server_certificate is not None:
            for k in self.server_certificate:
                result['ServerCertificate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_certificate = []
        if m.get('ServerCertificate') is not None:
            for k in m.get('ServerCertificate'):
                temp_model = DescribeServerCertificatesResponseBodyServerCertificatesServerCertificate()
                self.server_certificate.append(temp_model.from_map(k))
        return self


class DescribeServerCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_certificates: DescribeServerCertificatesResponseBodyServerCertificates = None,
    ):
        self.request_id = request_id
        self.server_certificates = server_certificates

    def validate(self):
        if self.server_certificates:
            self.server_certificates.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_certificates is not None:
            result['ServerCertificates'] = self.server_certificates.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerCertificates') is not None:
            temp_model = DescribeServerCertificatesResponseBodyServerCertificates()
            self.server_certificates = temp_model.from_map(m['ServerCertificates'])
        return self


class DescribeServerCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServerCertificatesResponseBody = None,
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
            temp_model = DescribeServerCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        load_balancer_id: str = None,
        tags: str = None,
        distinct_key: bool = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.load_balancer_id = load_balancer_id
        self.tags = tags
        self.distinct_key = distinct_key
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.distinct_key is not None:
            result['DistinctKey'] = self.distinct_key
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DistinctKey') is not None:
            self.distinct_key = m.get('DistinctKey')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeTagsResponseBodyTagSetsTagSet(TeaModel):
    def __init__(
        self,
        instance_count: int = None,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.instance_count = instance_count
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagsResponseBodyTagSets(TeaModel):
    def __init__(
        self,
        tag_set: List[DescribeTagsResponseBodyTagSetsTagSet] = None,
    ):
        self.tag_set = tag_set

    def validate(self):
        if self.tag_set:
            for k in self.tag_set:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagSet'] = []
        if self.tag_set is not None:
            for k in self.tag_set:
                result['TagSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_set = []
        if m.get('TagSet') is not None:
            for k in m.get('TagSet'):
                temp_model = DescribeTagsResponseBodyTagSetsTagSet()
                self.tag_set.append(temp_model.from_map(k))
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        tag_sets: DescribeTagsResponseBodyTagSets = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.tag_sets = tag_sets

    def validate(self):
        if self.tag_sets:
            self.tag_sets.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.tag_sets is not None:
            result['TagSets'] = self.tag_sets.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TagSets') is not None:
            temp_model = DescribeTagsResponseBodyTagSets()
            self.tag_sets = temp_model.from_map(m['TagSets'])
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagsResponseBody = None,
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
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVServerGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        return self


class DescribeVServerGroupAttributeResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class DescribeVServerGroupAttributeResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[DescribeVServerGroupAttributeResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = DescribeVServerGroupAttributeResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class DescribeVServerGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        request_id: str = None,
        vserver_group_name: str = None,
        load_balancer_id: str = None,
        backend_servers: DescribeVServerGroupAttributeResponseBodyBackendServers = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.request_id = request_id
        self.vserver_group_name = vserver_group_name
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            temp_model = DescribeVServerGroupAttributeResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class DescribeVServerGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVServerGroupAttributeResponseBody = None,
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
            temp_model = DescribeVServerGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVServerGroupsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        include_rule: bool = None,
        include_listener: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.include_rule = include_rule
        self.include_listener = include_listener

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.include_rule is not None:
            result['IncludeRule'] = self.include_rule
        if self.include_listener is not None:
            result['IncludeListener'] = self.include_listener
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('IncludeRule') is not None:
            self.include_rule = m.get('IncludeRule')
        if m.get('IncludeListener') is not None:
            self.include_listener = m.get('IncludeListener')
        return self


class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListenersListener(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListeners(TeaModel):
    def __init__(
        self,
        listener: List[DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListenersListener] = None,
    ):
        self.listener = listener

    def validate(self):
        if self.listener:
            for k in self.listener:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Listener'] = []
        if self.listener is not None:
            for k in self.listener:
                result['Listener'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener = []
        if m.get('Listener') is not None:
            for k in m.get('Listener'):
                temp_model = DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListenersListener()
                self.listener.append(temp_model.from_map(k))
        return self


class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRulesRule(TeaModel):
    def __init__(
        self,
        domain: str = None,
        url: str = None,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.domain = domain
        self.url = url
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.url is not None:
            result['Url'] = self.url
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjects(TeaModel):
    def __init__(
        self,
        listeners: DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListeners = None,
        rules: DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRules = None,
    ):
        self.listeners = listeners
        self.rules = rules

    def validate(self):
        if self.listeners:
            self.listeners.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners.to_map()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            temp_model = DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListeners()
            self.listeners = temp_model.from_map(m['Listeners'])
        if m.get('Rules') is not None:
            temp_model = DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroup(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        vserver_group_name: str = None,
        associated_objects: DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjects = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.vserver_group_name = vserver_group_name
        self.associated_objects = associated_objects

    def validate(self):
        if self.associated_objects:
            self.associated_objects.validate()

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name
        if self.associated_objects is not None:
            result['AssociatedObjects'] = self.associated_objects.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')
        if m.get('AssociatedObjects') is not None:
            temp_model = DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjects()
            self.associated_objects = temp_model.from_map(m['AssociatedObjects'])
        return self


class DescribeVServerGroupsResponseBodyVServerGroups(TeaModel):
    def __init__(
        self,
        vserver_group: List[DescribeVServerGroupsResponseBodyVServerGroupsVServerGroup] = None,
    ):
        self.vserver_group = vserver_group

    def validate(self):
        if self.vserver_group:
            for k in self.vserver_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VServerGroup'] = []
        if self.vserver_group is not None:
            for k in self.vserver_group:
                result['VServerGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vserver_group = []
        if m.get('VServerGroup') is not None:
            for k in m.get('VServerGroup'):
                temp_model = DescribeVServerGroupsResponseBodyVServerGroupsVServerGroup()
                self.vserver_group.append(temp_model.from_map(k))
        return self


class DescribeVServerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vserver_groups: DescribeVServerGroupsResponseBodyVServerGroups = None,
    ):
        self.request_id = request_id
        self.vserver_groups = vserver_groups

    def validate(self):
        if self.vserver_groups:
            self.vserver_groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vserver_groups is not None:
            result['VServerGroups'] = self.vserver_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VServerGroups') is not None:
            temp_model = DescribeVServerGroupsResponseBodyVServerGroups()
            self.vserver_groups = temp_model.from_map(m['VServerGroups'])
        return self


class DescribeVServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVServerGroupsResponseBody = None,
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
            temp_model = DescribeVServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseBodyZonesZoneSlaveZonesSlaveZone(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZonesZoneSlaveZones(TeaModel):
    def __init__(
        self,
        slave_zone: List[DescribeZonesResponseBodyZonesZoneSlaveZonesSlaveZone] = None,
    ):
        self.slave_zone = slave_zone

    def validate(self):
        if self.slave_zone:
            for k in self.slave_zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SlaveZone'] = []
        if self.slave_zone is not None:
            for k in self.slave_zone:
                result['SlaveZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slave_zone = []
        if m.get('SlaveZone') is not None:
            for k in m.get('SlaveZone'):
                temp_model = DescribeZonesResponseBodyZonesZoneSlaveZonesSlaveZone()
                self.slave_zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
        slave_zones: DescribeZonesResponseBodyZonesZoneSlaveZones = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id
        self.slave_zones = slave_zones

    def validate(self):
        if self.slave_zones:
            self.slave_zones.validate()

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.slave_zones is not None:
            result['SlaveZones'] = self.slave_zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SlaveZones') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneSlaveZones()
            self.slave_zones = temp_model.from_map(m['SlaveZones'])
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZonesResponseBody = None,
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTLSCipherPoliciesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tlscipher_policy_id: str = None,
        name: str = None,
        include_listener: bool = None,
        next_token: str = None,
        max_items: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tlscipher_policy_id = tlscipher_policy_id
        self.name = name
        self.include_listener = include_listener
        self.next_token = next_token
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tlscipher_policy_id is not None:
            result['TLSCipherPolicyId'] = self.tlscipher_policy_id
        if self.name is not None:
            result['Name'] = self.name
        if self.include_listener is not None:
            result['IncludeListener'] = self.include_listener
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('TLSCipherPolicyId') is not None:
            self.tlscipher_policy_id = m.get('TLSCipherPolicyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IncludeListener') is not None:
            self.include_listener = m.get('IncludeListener')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListTLSCipherPoliciesResponseBodyTLSCipherPoliciesRelateListeners(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        load_balancer_id: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.load_balancer_id = load_balancer_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ListTLSCipherPoliciesResponseBodyTLSCipherPolicies(TeaModel):
    def __init__(
        self,
        status: str = None,
        relate_listeners: List[ListTLSCipherPoliciesResponseBodyTLSCipherPoliciesRelateListeners] = None,
        create_time: int = None,
        ciphers: List[str] = None,
        instance_id: str = None,
        name: str = None,
        tlsversions: List[str] = None,
    ):
        self.status = status
        self.relate_listeners = relate_listeners
        self.create_time = create_time
        self.ciphers = ciphers
        self.instance_id = instance_id
        self.name = name
        self.tlsversions = tlsversions

    def validate(self):
        if self.relate_listeners:
            for k in self.relate_listeners:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        result['RelateListeners'] = []
        if self.relate_listeners is not None:
            for k in self.relate_listeners:
                result['RelateListeners'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.relate_listeners = []
        if m.get('RelateListeners') is not None:
            for k in m.get('RelateListeners'):
                temp_model = ListTLSCipherPoliciesResponseBodyTLSCipherPoliciesRelateListeners()
                self.relate_listeners.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')
        return self


class ListTLSCipherPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        next_token: str = None,
        request_id: str = None,
        tlscipher_policies: List[ListTLSCipherPoliciesResponseBodyTLSCipherPolicies] = None,
        is_truncated: bool = None,
    ):
        self.total_count = total_count
        self.next_token = next_token
        self.request_id = request_id
        self.tlscipher_policies = tlscipher_policies
        self.is_truncated = is_truncated

    def validate(self):
        if self.tlscipher_policies:
            for k in self.tlscipher_policies:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TLSCipherPolicies'] = []
        if self.tlscipher_policies is not None:
            for k in self.tlscipher_policies:
                result['TLSCipherPolicies'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tlscipher_policies = []
        if m.get('TLSCipherPolicies') is not None:
            for k in m.get('TLSCipherPolicies'):
                temp_model = ListTLSCipherPoliciesResponseBodyTLSCipherPolicies()
                self.tlscipher_policies.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        return self


class ListTLSCipherPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTLSCipherPoliciesResponseBody = None,
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
            temp_model = ListTLSCipherPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLoadBalancerInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_spec: str = None,
        auto_pay: bool = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_spec = load_balancer_spec
        self.auto_pay = auto_pay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        return self


class ModifyLoadBalancerInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyLoadBalancerInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLoadBalancerInstanceSpecResponseBody = None,
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
            temp_model = ModifyLoadBalancerInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLoadBalancerInternetSpecRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        internet_charge_type: str = None,
        bandwidth: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        auto_pay: bool = None,
        ratio: int = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.internet_charge_type = internet_charge_type
        self.bandwidth = bandwidth
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.auto_pay = auto_pay
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        return self


class ModifyLoadBalancerInternetSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyLoadBalancerInternetSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLoadBalancerInternetSpecResponseBody = None,
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
            temp_model = ModifyLoadBalancerInternetSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLoadBalancerPayTypeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        load_balancer_id: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        duration: int = None,
        auto_pay: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.load_balancer_id = load_balancer_id
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.auto_pay = auto_pay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        return self


class ModifyLoadBalancerPayTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyLoadBalancerPayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLoadBalancerPayTypeResponseBody = None,
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
            temp_model = ModifyLoadBalancerPayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVServerGroupBackendServersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group_id: str = None,
        old_backend_servers: str = None,
        new_backend_servers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group_id = vserver_group_id
        self.old_backend_servers = old_backend_servers
        self.new_backend_servers = new_backend_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.old_backend_servers is not None:
            result['OldBackendServers'] = self.old_backend_servers
        if self.new_backend_servers is not None:
            result['NewBackendServers'] = self.new_backend_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('OldBackendServers') is not None:
            self.old_backend_servers = m.get('OldBackendServers')
        if m.get('NewBackendServers') is not None:
            self.new_backend_servers = m.get('NewBackendServers')
        return self


class ModifyVServerGroupBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class ModifyVServerGroupBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[ModifyVServerGroupBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = ModifyVServerGroupBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class ModifyVServerGroupBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        request_id: str = None,
        backend_servers: ModifyVServerGroupBackendServersResponseBodyBackendServers = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.request_id = request_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackendServers') is not None:
            temp_model = ModifyVServerGroupBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class ModifyVServerGroupBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyVServerGroupBackendServersResponseBody = None,
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
            temp_model = ModifyVServerGroupBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAccessControlListEntryRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
        acl_id: str = None,
        acl_entrys: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id
        self.acl_id = acl_id
        self.acl_entrys = acl_entrys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_entrys is not None:
            result['AclEntrys'] = self.acl_entrys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclEntrys') is not None:
            self.acl_entrys = m.get('AclEntrys')
        return self


class RemoveAccessControlListEntryResponseBody(TeaModel):
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


class RemoveAccessControlListEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAccessControlListEntryResponseBody = None,
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
            temp_model = RemoveAccessControlListEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBackendServersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        backend_servers: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class RemoveBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class RemoveBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[RemoveBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = RemoveBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class RemoveBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        load_balancer_id: str = None,
        backend_servers: RemoveBackendServersResponseBodyBackendServers = None,
    ):
        self.request_id = request_id
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            temp_model = RemoveBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class RemoveBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveBackendServersResponseBody = None,
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
            temp_model = RemoveBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveListenerWhiteListItemRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        source_items: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        listener_protocol: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.source_items = source_items
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.listener_protocol = listener_protocol
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.source_items is not None:
            result['SourceItems'] = self.source_items
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('SourceItems') is not None:
            self.source_items = m.get('SourceItems')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class RemoveListenerWhiteListItemResponseBody(TeaModel):
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


class RemoveListenerWhiteListItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveListenerWhiteListItemResponseBody = None,
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
            temp_model = RemoveListenerWhiteListItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTagsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        load_balancer_id: str = None,
        tags: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.load_balancer_id = load_balancer_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class RemoveTagsResponseBody(TeaModel):
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


class RemoveTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveTagsResponseBody = None,
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
            temp_model = RemoveTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVServerGroupBackendServersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group_id: str = None,
        backend_servers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group_id = vserver_group_id
        self.backend_servers = backend_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')
        return self


class RemoveVServerGroupBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class RemoveVServerGroupBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[RemoveVServerGroupBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = RemoveVServerGroupBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class RemoveVServerGroupBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        request_id: str = None,
        backend_servers: RemoveVServerGroupBackendServersResponseBodyBackendServers = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.request_id = request_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackendServers') is not None:
            temp_model = RemoveVServerGroupBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class RemoveVServerGroupBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveVServerGroupBackendServersResponseBody = None,
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
            temp_model = RemoveVServerGroupBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessControlListAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        region_id: str = None,
        acl_id: str = None,
        acl_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.region_id = region_id
        self.acl_id = acl_id
        self.acl_name = acl_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        return self


class SetAccessControlListAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        acl_id: str = None,
    ):
        self.request_id = request_id
        self.acl_id = acl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class SetAccessControlListAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAccessControlListAttributeResponseBody = None,
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
            temp_model = SetAccessControlListAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetBackendServersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        backend_servers: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SetBackendServersResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: str = None,
        description: str = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class SetBackendServersResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[SetBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = SetBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class SetBackendServersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        load_balancer_id: str = None,
        backend_servers: SetBackendServersResponseBodyBackendServers = None,
    ):
        self.request_id = request_id
        self.load_balancer_id = load_balancer_id
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('BackendServers') is not None:
            temp_model = SetBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class SetBackendServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetBackendServersResponseBody = None,
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
            temp_model = SetBackendServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCACertificateNameRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        cacertificate_id: str = None,
        cacertificate_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.cacertificate_id = cacertificate_id
        self.cacertificate_name = cacertificate_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.cacertificate_name is not None:
            result['CACertificateName'] = self.cacertificate_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('CACertificateName') is not None:
            self.cacertificate_name = m.get('CACertificateName')
        return self


class SetCACertificateNameResponseBody(TeaModel):
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


class SetCACertificateNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetCACertificateNameResponseBody = None,
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
            temp_model = SetCACertificateNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainExtensionAttributeRequestServerCertificate(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetDomainExtensionAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        domain_extension_id: str = None,
        server_certificate_id: str = None,
        certificate_id: List[str] = None,
        server_certificate: List[SetDomainExtensionAttributeRequestServerCertificate] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.domain_extension_id = domain_extension_id
        self.server_certificate_id = server_certificate_id
        self.certificate_id = certificate_id
        self.server_certificate = server_certificate

    def validate(self):
        if self.server_certificate:
            for k in self.server_certificate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        result['ServerCertificate'] = []
        if self.server_certificate is not None:
            for k in self.server_certificate:
                result['ServerCertificate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        self.server_certificate = []
        if m.get('ServerCertificate') is not None:
            for k in m.get('ServerCertificate'):
                temp_model = SetDomainExtensionAttributeRequestServerCertificate()
                self.server_certificate.append(temp_model.from_map(k))
        return self


class SetDomainExtensionAttributeResponseBody(TeaModel):
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


class SetDomainExtensionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDomainExtensionAttributeResponseBody = None,
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
            temp_model = SetDomainExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetListenerAccessControlStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        access_control_status: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        listener_protocol: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.access_control_status = access_control_status
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.listener_protocol = listener_protocol
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.access_control_status is not None:
            result['AccessControlStatus'] = self.access_control_status
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('AccessControlStatus') is not None:
            self.access_control_status = m.get('AccessControlStatus')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SetListenerAccessControlStatusResponseBody(TeaModel):
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


class SetListenerAccessControlStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetListenerAccessControlStatusResponseBody = None,
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
            temp_model = SetListenerAccessControlStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerDeleteProtectionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        delete_protection: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.delete_protection = delete_protection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.delete_protection is not None:
            result['DeleteProtection'] = self.delete_protection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('DeleteProtection') is not None:
            self.delete_protection = m.get('DeleteProtection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SetLoadBalancerDeleteProtectionResponseBody(TeaModel):
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


class SetLoadBalancerDeleteProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerDeleteProtectionResponseBody = None,
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
            temp_model = SetLoadBalancerDeleteProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerHTTPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        bandwidth: int = None,
        xforwarded_for: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        cookie_timeout: int = None,
        cookie: str = None,
        health_check: str = None,
        health_check_type: str = None,
        health_check_method: str = None,
        health_check_domain: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_timeout: int = None,
        health_check_interval: int = None,
        health_check_connect_port: int = None,
        health_check_http_code: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        vserver_group: str = None,
        vserver_group_id: str = None,
        tags: str = None,
        xforwarded_for__slbip: str = None,
        xforwarded_for__slbid: str = None,
        xforwarded_for_proto: str = None,
        gzip: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        idle_timeout: int = None,
        request_timeout: int = None,
        description: str = None,
        xforwarded_for__slbport: str = None,
        xforwarded_for__client_src_port: str = None,
        forward_code: int = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.bandwidth = bandwidth
        self.xforwarded_for = xforwarded_for
        self.scheduler = scheduler
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        self.cookie_timeout = cookie_timeout
        self.cookie = cookie
        self.health_check = health_check
        self.health_check_type = health_check_type
        self.health_check_method = health_check_method
        self.health_check_domain = health_check_domain
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_timeout = health_check_timeout
        self.health_check_interval = health_check_interval
        self.health_check_connect_port = health_check_connect_port
        self.health_check_http_code = health_check_http_code
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.vserver_group = vserver_group
        self.vserver_group_id = vserver_group_id
        self.tags = tags
        self.xforwarded_for__slbip = xforwarded_for__slbip
        self.xforwarded_for__slbid = xforwarded_for__slbid
        self.xforwarded_for_proto = xforwarded_for_proto
        self.gzip = gzip
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.idle_timeout = idle_timeout
        self.request_timeout = request_timeout
        self.description = description
        self.xforwarded_for__slbport = xforwarded_for__slbport
        self.xforwarded_for__client_src_port = xforwarded_for__client_src_port
        self.forward_code = forward_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.vserver_group is not None:
            result['VServerGroup'] = self.vserver_group
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.xforwarded_for__slbip is not None:
            result['XForwardedFor_SLBIP'] = self.xforwarded_for__slbip
        if self.xforwarded_for__slbid is not None:
            result['XForwardedFor_SLBID'] = self.xforwarded_for__slbid
        if self.xforwarded_for_proto is not None:
            result['XForwardedFor_proto'] = self.xforwarded_for_proto
        if self.gzip is not None:
            result['Gzip'] = self.gzip
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.description is not None:
            result['Description'] = self.description
        if self.xforwarded_for__slbport is not None:
            result['XForwardedFor_SLBPORT'] = self.xforwarded_for__slbport
        if self.xforwarded_for__client_src_port is not None:
            result['XForwardedFor_ClientSrcPort'] = self.xforwarded_for__client_src_port
        if self.forward_code is not None:
            result['ForwardCode'] = self.forward_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('VServerGroup') is not None:
            self.vserver_group = m.get('VServerGroup')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('XForwardedFor_SLBIP') is not None:
            self.xforwarded_for__slbip = m.get('XForwardedFor_SLBIP')
        if m.get('XForwardedFor_SLBID') is not None:
            self.xforwarded_for__slbid = m.get('XForwardedFor_SLBID')
        if m.get('XForwardedFor_proto') is not None:
            self.xforwarded_for_proto = m.get('XForwardedFor_proto')
        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('XForwardedFor_SLBPORT') is not None:
            self.xforwarded_for__slbport = m.get('XForwardedFor_SLBPORT')
        if m.get('XForwardedFor_ClientSrcPort') is not None:
            self.xforwarded_for__client_src_port = m.get('XForwardedFor_ClientSrcPort')
        if m.get('ForwardCode') is not None:
            self.forward_code = m.get('ForwardCode')
        return self


class SetLoadBalancerHTTPListenerAttributeResponseBody(TeaModel):
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


class SetLoadBalancerHTTPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerHTTPListenerAttributeResponseBody = None,
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
            temp_model = SetLoadBalancerHTTPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerHTTPSListenerAttributeRequestServerCertificate(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetLoadBalancerHTTPSListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        bandwidth: int = None,
        backend_protocol: str = None,
        xforwarded_for: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        cookie_timeout: int = None,
        cookie: str = None,
        health_check: str = None,
        health_check_type: str = None,
        health_check_method: str = None,
        health_check_domain: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_timeout: int = None,
        health_check_interval: int = None,
        health_check_connect_port: int = None,
        health_check_http_code: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        server_certificate_id: str = None,
        cacertificate_id: str = None,
        vserver_group: str = None,
        vserver_group_id: str = None,
        tags: str = None,
        xforwarded_for__slbip: str = None,
        xforwarded_for__slbid: str = None,
        xforwarded_for_proto: str = None,
        gzip: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        idle_timeout: int = None,
        request_timeout: int = None,
        enable_http_2: str = None,
        tlscipher_policy: str = None,
        description: str = None,
        xforwarded_for__slbport: str = None,
        xforwarded_for__client_src_port: str = None,
        xforwarded_for__client_cert_subject_dn: str = None,
        xforwarded_for__client_cert_issuer_dn: str = None,
        xforwarded_for__client_cert_fingerprint: str = None,
        xforwarded_for__client_cert_client_verify: str = None,
        xforwarded_for__client_cert_subject_dnalias: str = None,
        xforwarded_for__client_cert_issuer_dnalias: str = None,
        xforwarded_for__client_cert_fingerprint_alias: str = None,
        xforwarded_for__client_cert_client_verify_alias: str = None,
        server_certificate: List[SetLoadBalancerHTTPSListenerAttributeRequestServerCertificate] = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.bandwidth = bandwidth
        self.backend_protocol = backend_protocol
        self.xforwarded_for = xforwarded_for
        self.scheduler = scheduler
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        self.cookie_timeout = cookie_timeout
        self.cookie = cookie
        self.health_check = health_check
        self.health_check_type = health_check_type
        self.health_check_method = health_check_method
        self.health_check_domain = health_check_domain
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_timeout = health_check_timeout
        self.health_check_interval = health_check_interval
        self.health_check_connect_port = health_check_connect_port
        self.health_check_http_code = health_check_http_code
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.server_certificate_id = server_certificate_id
        self.cacertificate_id = cacertificate_id
        self.vserver_group = vserver_group
        self.vserver_group_id = vserver_group_id
        self.tags = tags
        self.xforwarded_for__slbip = xforwarded_for__slbip
        self.xforwarded_for__slbid = xforwarded_for__slbid
        self.xforwarded_for_proto = xforwarded_for_proto
        self.gzip = gzip
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.idle_timeout = idle_timeout
        self.request_timeout = request_timeout
        self.enable_http_2 = enable_http_2
        self.tlscipher_policy = tlscipher_policy
        self.description = description
        self.xforwarded_for__slbport = xforwarded_for__slbport
        self.xforwarded_for__client_src_port = xforwarded_for__client_src_port
        self.xforwarded_for__client_cert_subject_dn = xforwarded_for__client_cert_subject_dn
        self.xforwarded_for__client_cert_issuer_dn = xforwarded_for__client_cert_issuer_dn
        self.xforwarded_for__client_cert_fingerprint = xforwarded_for__client_cert_fingerprint
        self.xforwarded_for__client_cert_client_verify = xforwarded_for__client_cert_client_verify
        self.xforwarded_for__client_cert_subject_dnalias = xforwarded_for__client_cert_subject_dnalias
        self.xforwarded_for__client_cert_issuer_dnalias = xforwarded_for__client_cert_issuer_dnalias
        self.xforwarded_for__client_cert_fingerprint_alias = xforwarded_for__client_cert_fingerprint_alias
        self.xforwarded_for__client_cert_client_verify_alias = xforwarded_for__client_cert_client_verify_alias
        self.server_certificate = server_certificate

    def validate(self):
        if self.server_certificate:
            for k in self.server_certificate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol
        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.vserver_group is not None:
            result['VServerGroup'] = self.vserver_group
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.xforwarded_for__slbip is not None:
            result['XForwardedFor_SLBIP'] = self.xforwarded_for__slbip
        if self.xforwarded_for__slbid is not None:
            result['XForwardedFor_SLBID'] = self.xforwarded_for__slbid
        if self.xforwarded_for_proto is not None:
            result['XForwardedFor_proto'] = self.xforwarded_for_proto
        if self.gzip is not None:
            result['Gzip'] = self.gzip
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout
        if self.enable_http_2 is not None:
            result['EnableHttp2'] = self.enable_http_2
        if self.tlscipher_policy is not None:
            result['TLSCipherPolicy'] = self.tlscipher_policy
        if self.description is not None:
            result['Description'] = self.description
        if self.xforwarded_for__slbport is not None:
            result['XForwardedFor_SLBPORT'] = self.xforwarded_for__slbport
        if self.xforwarded_for__client_src_port is not None:
            result['XForwardedFor_ClientSrcPort'] = self.xforwarded_for__client_src_port
        if self.xforwarded_for__client_cert_subject_dn is not None:
            result['XForwardedFor_ClientCertSubjectDN'] = self.xforwarded_for__client_cert_subject_dn
        if self.xforwarded_for__client_cert_issuer_dn is not None:
            result['XForwardedFor_ClientCertIssuerDN'] = self.xforwarded_for__client_cert_issuer_dn
        if self.xforwarded_for__client_cert_fingerprint is not None:
            result['XForwardedFor_ClientCertFingerprint'] = self.xforwarded_for__client_cert_fingerprint
        if self.xforwarded_for__client_cert_client_verify is not None:
            result['XForwardedFor_ClientCertClientVerify'] = self.xforwarded_for__client_cert_client_verify
        if self.xforwarded_for__client_cert_subject_dnalias is not None:
            result['XForwardedFor_ClientCertSubjectDNAlias'] = self.xforwarded_for__client_cert_subject_dnalias
        if self.xforwarded_for__client_cert_issuer_dnalias is not None:
            result['XForwardedFor_ClientCertIssuerDNAlias'] = self.xforwarded_for__client_cert_issuer_dnalias
        if self.xforwarded_for__client_cert_fingerprint_alias is not None:
            result['XForwardedFor_ClientCertFingerprintAlias'] = self.xforwarded_for__client_cert_fingerprint_alias
        if self.xforwarded_for__client_cert_client_verify_alias is not None:
            result['XForwardedFor_ClientCertClientVerifyAlias'] = self.xforwarded_for__client_cert_client_verify_alias
        result['ServerCertificate'] = []
        if self.server_certificate is not None:
            for k in self.server_certificate:
                result['ServerCertificate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')
        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('VServerGroup') is not None:
            self.vserver_group = m.get('VServerGroup')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('XForwardedFor_SLBIP') is not None:
            self.xforwarded_for__slbip = m.get('XForwardedFor_SLBIP')
        if m.get('XForwardedFor_SLBID') is not None:
            self.xforwarded_for__slbid = m.get('XForwardedFor_SLBID')
        if m.get('XForwardedFor_proto') is not None:
            self.xforwarded_for_proto = m.get('XForwardedFor_proto')
        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')
        if m.get('EnableHttp2') is not None:
            self.enable_http_2 = m.get('EnableHttp2')
        if m.get('TLSCipherPolicy') is not None:
            self.tlscipher_policy = m.get('TLSCipherPolicy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('XForwardedFor_SLBPORT') is not None:
            self.xforwarded_for__slbport = m.get('XForwardedFor_SLBPORT')
        if m.get('XForwardedFor_ClientSrcPort') is not None:
            self.xforwarded_for__client_src_port = m.get('XForwardedFor_ClientSrcPort')
        if m.get('XForwardedFor_ClientCertSubjectDN') is not None:
            self.xforwarded_for__client_cert_subject_dn = m.get('XForwardedFor_ClientCertSubjectDN')
        if m.get('XForwardedFor_ClientCertIssuerDN') is not None:
            self.xforwarded_for__client_cert_issuer_dn = m.get('XForwardedFor_ClientCertIssuerDN')
        if m.get('XForwardedFor_ClientCertFingerprint') is not None:
            self.xforwarded_for__client_cert_fingerprint = m.get('XForwardedFor_ClientCertFingerprint')
        if m.get('XForwardedFor_ClientCertClientVerify') is not None:
            self.xforwarded_for__client_cert_client_verify = m.get('XForwardedFor_ClientCertClientVerify')
        if m.get('XForwardedFor_ClientCertSubjectDNAlias') is not None:
            self.xforwarded_for__client_cert_subject_dnalias = m.get('XForwardedFor_ClientCertSubjectDNAlias')
        if m.get('XForwardedFor_ClientCertIssuerDNAlias') is not None:
            self.xforwarded_for__client_cert_issuer_dnalias = m.get('XForwardedFor_ClientCertIssuerDNAlias')
        if m.get('XForwardedFor_ClientCertFingerprintAlias') is not None:
            self.xforwarded_for__client_cert_fingerprint_alias = m.get('XForwardedFor_ClientCertFingerprintAlias')
        if m.get('XForwardedFor_ClientCertClientVerifyAlias') is not None:
            self.xforwarded_for__client_cert_client_verify_alias = m.get('XForwardedFor_ClientCertClientVerifyAlias')
        self.server_certificate = []
        if m.get('ServerCertificate') is not None:
            for k in m.get('ServerCertificate'):
                temp_model = SetLoadBalancerHTTPSListenerAttributeRequestServerCertificate()
                self.server_certificate.append(temp_model.from_map(k))
        return self


class SetLoadBalancerHTTPSListenerAttributeResponseBody(TeaModel):
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


class SetLoadBalancerHTTPSListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerHTTPSListenerAttributeResponseBody = None,
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
            temp_model = SetLoadBalancerHTTPSListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerModificationProtectionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        modification_protection_status: str = None,
        owner_account: str = None,
        modification_protection_reason: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.modification_protection_status = modification_protection_status
        self.owner_account = owner_account
        self.modification_protection_reason = modification_protection_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')
        return self


class SetLoadBalancerModificationProtectionResponseBody(TeaModel):
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


class SetLoadBalancerModificationProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerModificationProtectionResponseBody = None,
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
            temp_model = SetLoadBalancerModificationProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerNameRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SetLoadBalancerNameResponseBody(TeaModel):
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


class SetLoadBalancerNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerNameResponseBody = None,
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
            temp_model = SetLoadBalancerNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        load_balancer_status: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.load_balancer_status = load_balancer_status
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SetLoadBalancerStatusResponseBody(TeaModel):
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


class SetLoadBalancerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerStatusResponseBody = None,
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
            temp_model = SetLoadBalancerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerTCPListenerAttributeRequestPortRange(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetLoadBalancerTCPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        bandwidth: int = None,
        scheduler: str = None,
        persistence_timeout: int = None,
        established_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_connect_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_interval: int = None,
        health_check_domain: str = None,
        health_check_uri: str = None,
        health_check_http_code: str = None,
        health_check_type: str = None,
        health_check_method: str = None,
        syn_proxy: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group: str = None,
        vserver_group_id: str = None,
        master_slave_server_group_id: str = None,
        master_slave_server_group: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        description: str = None,
        connection_drain: str = None,
        connection_drain_timeout: int = None,
        port_range: List[SetLoadBalancerTCPListenerAttributeRequestPortRange] = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.bandwidth = bandwidth
        self.scheduler = scheduler
        self.persistence_timeout = persistence_timeout
        self.established_timeout = established_timeout
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_connect_timeout = health_check_connect_timeout
        self.health_check_connect_port = health_check_connect_port
        self.health_check_interval = health_check_interval
        self.health_check_domain = health_check_domain
        self.health_check_uri = health_check_uri
        self.health_check_http_code = health_check_http_code
        self.health_check_type = health_check_type
        self.health_check_method = health_check_method
        self.syn_proxy = syn_proxy
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group = vserver_group
        self.vserver_group_id = vserver_group_id
        self.master_slave_server_group_id = master_slave_server_group_id
        self.master_slave_server_group = master_slave_server_group
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.description = description
        self.connection_drain = connection_drain
        self.connection_drain_timeout = connection_drain_timeout
        self.port_range = port_range

    def validate(self):
        if self.port_range:
            for k in self.port_range:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method
        if self.syn_proxy is not None:
            result['SynProxy'] = self.syn_proxy
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group is not None:
            result['VServerGroup'] = self.vserver_group
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.master_slave_server_group is not None:
            result['MasterSlaveServerGroup'] = self.master_slave_server_group
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.connection_drain is not None:
            result['ConnectionDrain'] = self.connection_drain
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        result['PortRange'] = []
        if self.port_range is not None:
            for k in self.port_range:
                result['PortRange'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')
        if m.get('SynProxy') is not None:
            self.syn_proxy = m.get('SynProxy')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroup') is not None:
            self.vserver_group = m.get('VServerGroup')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('MasterSlaveServerGroup') is not None:
            self.master_slave_server_group = m.get('MasterSlaveServerGroup')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConnectionDrain') is not None:
            self.connection_drain = m.get('ConnectionDrain')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        self.port_range = []
        if m.get('PortRange') is not None:
            for k in m.get('PortRange'):
                temp_model = SetLoadBalancerTCPListenerAttributeRequestPortRange()
                self.port_range.append(temp_model.from_map(k))
        return self


class SetLoadBalancerTCPListenerAttributeResponseBody(TeaModel):
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


class SetLoadBalancerTCPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerTCPListenerAttributeResponseBody = None,
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
            temp_model = SetLoadBalancerTCPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetLoadBalancerUDPListenerAttributeRequestPortRange(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SetLoadBalancerUDPListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        bandwidth: int = None,
        scheduler: str = None,
        persistence_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_connect_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        health_check_exp: str = None,
        max_connection: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group: str = None,
        vserver_group_id: str = None,
        master_slave_server_group_id: str = None,
        master_slave_server_group: str = None,
        acl_id: str = None,
        acl_type: str = None,
        acl_status: str = None,
        vpc_ids: str = None,
        description: str = None,
        connection_drain: str = None,
        connection_drain_timeout: int = None,
        port_range: List[SetLoadBalancerUDPListenerAttributeRequestPortRange] = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.bandwidth = bandwidth
        self.scheduler = scheduler
        self.persistence_timeout = persistence_timeout
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_connect_timeout = health_check_connect_timeout
        self.health_check_connect_port = health_check_connect_port
        self.health_check_interval = health_check_interval
        self.health_check_req = health_check_req
        self.health_check_exp = health_check_exp
        self.max_connection = max_connection
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group = vserver_group
        self.vserver_group_id = vserver_group_id
        self.master_slave_server_group_id = master_slave_server_group_id
        self.master_slave_server_group = master_slave_server_group
        self.acl_id = acl_id
        self.acl_type = acl_type
        self.acl_status = acl_status
        self.vpc_ids = vpc_ids
        self.description = description
        self.connection_drain = connection_drain
        self.connection_drain_timeout = connection_drain_timeout
        self.port_range = port_range

    def validate(self):
        if self.port_range:
            for k in self.port_range:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_req is not None:
            result['healthCheckReq'] = self.health_check_req
        if self.health_check_exp is not None:
            result['healthCheckExp'] = self.health_check_exp
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group is not None:
            result['VServerGroup'] = self.vserver_group
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id
        if self.master_slave_server_group is not None:
            result['MasterSlaveServerGroup'] = self.master_slave_server_group
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.connection_drain is not None:
            result['ConnectionDrain'] = self.connection_drain
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        result['PortRange'] = []
        if self.port_range is not None:
            for k in self.port_range:
                result['PortRange'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('healthCheckReq') is not None:
            self.health_check_req = m.get('healthCheckReq')
        if m.get('healthCheckExp') is not None:
            self.health_check_exp = m.get('healthCheckExp')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroup') is not None:
            self.vserver_group = m.get('VServerGroup')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')
        if m.get('MasterSlaveServerGroup') is not None:
            self.master_slave_server_group = m.get('MasterSlaveServerGroup')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ConnectionDrain') is not None:
            self.connection_drain = m.get('ConnectionDrain')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        self.port_range = []
        if m.get('PortRange') is not None:
            for k in m.get('PortRange'):
                temp_model = SetLoadBalancerUDPListenerAttributeRequestPortRange()
                self.port_range.append(temp_model.from_map(k))
        return self


class SetLoadBalancerUDPListenerAttributeResponseBody(TeaModel):
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


class SetLoadBalancerUDPListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetLoadBalancerUDPListenerAttributeResponseBody = None,
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
            temp_model = SetLoadBalancerUDPListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        rule_id: str = None,
        vserver_group_id: str = None,
        rule_name: str = None,
        listener_sync: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        cookie_timeout: int = None,
        cookie: str = None,
        health_check: str = None,
        health_check_domain: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
        health_check_timeout: int = None,
        health_check_interval: int = None,
        health_check_connect_port: int = None,
        health_check_http_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.rule_id = rule_id
        self.vserver_group_id = vserver_group_id
        self.rule_name = rule_name
        self.listener_sync = listener_sync
        self.scheduler = scheduler
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        self.cookie_timeout = cookie_timeout
        self.cookie = cookie
        self.health_check = health_check
        self.health_check_domain = health_check_domain
        self.health_check_uri = health_check_uri
        self.healthy_threshold = healthy_threshold
        self.unhealthy_threshold = unhealthy_threshold
        self.health_check_timeout = health_check_timeout
        self.health_check_interval = health_check_interval
        self.health_check_connect_port = health_check_connect_port
        self.health_check_http_code = health_check_http_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.listener_sync is not None:
            result['ListenerSync'] = self.listener_sync
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.cookie is not None:
            result['Cookie'] = self.cookie
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ListenerSync') is not None:
            self.listener_sync = m.get('ListenerSync')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        return self


class SetRuleResponseBody(TeaModel):
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


class SetRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRuleResponseBody = None,
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
            temp_model = SetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetServerCertificateNameRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        server_certificate_id: str = None,
        server_certificate_name: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.server_certificate_id = server_certificate_id
        self.server_certificate_name = server_certificate_name
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.server_certificate_name is not None:
            result['ServerCertificateName'] = self.server_certificate_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('ServerCertificateName') is not None:
            self.server_certificate_name = m.get('ServerCertificateName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SetServerCertificateNameResponseBody(TeaModel):
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


class SetServerCertificateNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetServerCertificateNameResponseBody = None,
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
            temp_model = SetServerCertificateNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTLSCipherPolicyAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tlscipher_policy_id: str = None,
        name: str = None,
        tlsversions: List[str] = None,
        ciphers: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tlscipher_policy_id = tlscipher_policy_id
        self.name = name
        self.tlsversions = tlsversions
        self.ciphers = ciphers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tlscipher_policy_id is not None:
            result['TLSCipherPolicyId'] = self.tlscipher_policy_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('TLSCipherPolicyId') is not None:
            self.tlscipher_policy_id = m.get('TLSCipherPolicyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        return self


class SetTLSCipherPolicyAttributeResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetTLSCipherPolicyAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetTLSCipherPolicyAttributeResponseBody = None,
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
            temp_model = SetTLSCipherPolicyAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVServerGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        vserver_group_id: str = None,
        vserver_group_name: str = None,
        backend_servers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.vserver_group_id = vserver_group_id
        self.vserver_group_name = vserver_group_name
        self.backend_servers = backend_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')
        if m.get('BackendServers') is not None:
            self.backend_servers = m.get('BackendServers')
        return self


class SetVServerGroupAttributeResponseBodyBackendServersBackendServer(TeaModel):
    def __init__(
        self,
        type: str = None,
        weight: int = None,
        description: str = None,
        port: int = None,
        server_id: str = None,
    ):
        self.type = type
        self.weight = weight
        self.description = description
        self.port = port
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class SetVServerGroupAttributeResponseBodyBackendServers(TeaModel):
    def __init__(
        self,
        backend_server: List[SetVServerGroupAttributeResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k in m.get('BackendServer'):
                temp_model = SetVServerGroupAttributeResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        return self


class SetVServerGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        vserver_group_id: str = None,
        request_id: str = None,
        vserver_group_name: str = None,
        backend_servers: SetVServerGroupAttributeResponseBodyBackendServers = None,
    ):
        self.vserver_group_id = vserver_group_id
        self.request_id = request_id
        self.vserver_group_name = vserver_group_name
        self.backend_servers = backend_servers

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')
        if m.get('BackendServers') is not None:
            temp_model = SetVServerGroupAttributeResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m['BackendServers'])
        return self


class SetVServerGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetVServerGroupAttributeResponseBody = None,
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
            temp_model = SetVServerGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartLoadBalancerListenerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        listener_protocol: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.listener_protocol = listener_protocol
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class StartLoadBalancerListenerResponseBody(TeaModel):
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


class StartLoadBalancerListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartLoadBalancerListenerResponseBody = None,
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
            temp_model = StartLoadBalancerListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLoadBalancerListenerRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        load_balancer_id: str = None,
        listener_port: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        listener_protocol: str = None,
        tags: str = None,
    ):
        self.region_id = region_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.load_balancer_id = load_balancer_id
        self.listener_port = listener_port
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.listener_protocol = listener_protocol
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class StopLoadBalancerListenerResponseBody(TeaModel):
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


class StopLoadBalancerListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopLoadBalancerListenerResponseBody = None,
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
            temp_model = StopLoadBalancerListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCACertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        access_key_id: str = None,
        region_id: str = None,
        cacertificate: str = None,
        cacertificate_name: str = None,
        resource_group_id: str = None,
        standard_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.region_id = region_id
        self.cacertificate = cacertificate
        self.cacertificate_name = cacertificate_name
        self.resource_group_id = resource_group_id
        self.standard_type = standard_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cacertificate is not None:
            result['CACertificate'] = self.cacertificate
        if self.cacertificate_name is not None:
            result['CACertificateName'] = self.cacertificate_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.standard_type is not None:
            result['StandardType'] = self.standard_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CACertificate') is not None:
            self.cacertificate = m.get('CACertificate')
        if m.get('CACertificateName') is not None:
            self.cacertificate_name = m.get('CACertificateName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StandardType') is not None:
            self.standard_type = m.get('StandardType')
        return self


class UploadCACertificateResponseBody(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        expire_time_stamp: int = None,
        cacertificate_id: str = None,
        create_time: str = None,
        cacertificate_name: str = None,
        expire_time: str = None,
        create_time_stamp: int = None,
        common_name: str = None,
    ):
        self.fingerprint = fingerprint
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.expire_time_stamp = expire_time_stamp
        self.cacertificate_id = cacertificate_id
        self.create_time = create_time
        self.cacertificate_name = cacertificate_name
        self.expire_time = expire_time
        self.create_time_stamp = create_time_stamp
        self.common_name = common_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.expire_time_stamp is not None:
            result['ExpireTimeStamp'] = self.expire_time_stamp
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cacertificate_name is not None:
            result['CACertificateName'] = self.cacertificate_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ExpireTimeStamp') is not None:
            self.expire_time_stamp = m.get('ExpireTimeStamp')
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CACertificateName') is not None:
            self.cacertificate_name = m.get('CACertificateName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        return self


class UploadCACertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadCACertificateResponseBody = None,
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
            temp_model = UploadCACertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadServerCertificateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        ali_cloud_certificate_id: str = None,
        ali_cloud_certificate_name: str = None,
        ali_cloud_certificate_region_id: str = None,
        server_certificate: str = None,
        private_key: str = None,
        server_certificate_name: str = None,
        owner_account: str = None,
        access_key_id: str = None,
        tags: str = None,
        resource_group_id: str = None,
        standard_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.ali_cloud_certificate_id = ali_cloud_certificate_id
        self.ali_cloud_certificate_name = ali_cloud_certificate_name
        self.ali_cloud_certificate_region_id = ali_cloud_certificate_region_id
        self.server_certificate = server_certificate
        self.private_key = private_key
        self.server_certificate_name = server_certificate_name
        self.owner_account = owner_account
        self.access_key_id = access_key_id
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.standard_type = standard_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ali_cloud_certificate_id is not None:
            result['AliCloudCertificateId'] = self.ali_cloud_certificate_id
        if self.ali_cloud_certificate_name is not None:
            result['AliCloudCertificateName'] = self.ali_cloud_certificate_name
        if self.ali_cloud_certificate_region_id is not None:
            result['AliCloudCertificateRegionId'] = self.ali_cloud_certificate_region_id
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.server_certificate_name is not None:
            result['ServerCertificateName'] = self.server_certificate_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.standard_type is not None:
            result['StandardType'] = self.standard_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AliCloudCertificateId') is not None:
            self.ali_cloud_certificate_id = m.get('AliCloudCertificateId')
        if m.get('AliCloudCertificateName') is not None:
            self.ali_cloud_certificate_name = m.get('AliCloudCertificateName')
        if m.get('AliCloudCertificateRegionId') is not None:
            self.ali_cloud_certificate_region_id = m.get('AliCloudCertificateRegionId')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('ServerCertificateName') is not None:
            self.server_certificate_name = m.get('ServerCertificateName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StandardType') is not None:
            self.standard_type = m.get('StandardType')
        return self


class UploadServerCertificateResponseBodySubjectAlternativeNames(TeaModel):
    def __init__(
        self,
        subject_alternative_name: List[str] = None,
    ):
        self.subject_alternative_name = subject_alternative_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subject_alternative_name is not None:
            result['SubjectAlternativeName'] = self.subject_alternative_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubjectAlternativeName') is not None:
            self.subject_alternative_name = m.get('SubjectAlternativeName')
        return self


class UploadServerCertificateResponseBody(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        expire_time_stamp: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        create_time: str = None,
        subject_alternative_names: UploadServerCertificateResponseBodySubjectAlternativeNames = None,
        ali_cloud_certificate_id: str = None,
        ali_cloud_certificate_name: str = None,
        is_ali_cloud_certificate: int = None,
        server_certificate_id: str = None,
        server_certificate_name: str = None,
        region_id: str = None,
        expire_time: str = None,
        create_time_stamp: int = None,
        common_name: str = None,
    ):
        self.fingerprint = fingerprint
        self.expire_time_stamp = expire_time_stamp
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.create_time = create_time
        self.subject_alternative_names = subject_alternative_names
        self.ali_cloud_certificate_id = ali_cloud_certificate_id
        self.ali_cloud_certificate_name = ali_cloud_certificate_name
        self.is_ali_cloud_certificate = is_ali_cloud_certificate
        self.server_certificate_id = server_certificate_id
        self.server_certificate_name = server_certificate_name
        self.region_id = region_id
        self.expire_time = expire_time
        self.create_time_stamp = create_time_stamp
        self.common_name = common_name

    def validate(self):
        if self.subject_alternative_names:
            self.subject_alternative_names.validate()

    def to_map(self):
        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.expire_time_stamp is not None:
            result['ExpireTimeStamp'] = self.expire_time_stamp
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names.to_map()
        if self.ali_cloud_certificate_id is not None:
            result['AliCloudCertificateId'] = self.ali_cloud_certificate_id
        if self.ali_cloud_certificate_name is not None:
            result['AliCloudCertificateName'] = self.ali_cloud_certificate_name
        if self.is_ali_cloud_certificate is not None:
            result['IsAliCloudCertificate'] = self.is_ali_cloud_certificate
        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id
        if self.server_certificate_name is not None:
            result['ServerCertificateName'] = self.server_certificate_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('ExpireTimeStamp') is not None:
            self.expire_time_stamp = m.get('ExpireTimeStamp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SubjectAlternativeNames') is not None:
            temp_model = UploadServerCertificateResponseBodySubjectAlternativeNames()
            self.subject_alternative_names = temp_model.from_map(m['SubjectAlternativeNames'])
        if m.get('AliCloudCertificateId') is not None:
            self.ali_cloud_certificate_id = m.get('AliCloudCertificateId')
        if m.get('AliCloudCertificateName') is not None:
            self.ali_cloud_certificate_name = m.get('AliCloudCertificateName')
        if m.get('IsAliCloudCertificate') is not None:
            self.is_ali_cloud_certificate = m.get('IsAliCloudCertificate')
        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')
        if m.get('ServerCertificateName') is not None:
            self.server_certificate_name = m.get('ServerCertificateName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        return self


class UploadServerCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadServerCertificateResponseBody = None,
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
            temp_model = UploadServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


