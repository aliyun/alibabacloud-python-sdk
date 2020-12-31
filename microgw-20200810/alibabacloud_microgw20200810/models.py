# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class FindAllServiceRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: str = None,
        name: str = None,
        alias_name: str = None,
        source_type: int = None,
        is_health: bool = None,
    ):
        # pageNumber
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        # name
        self.name = name
        # aliasName
        self.alias_name = alias_name
        # sourceType
        self.source_type = source_type
        # isHealth
        self.is_health = is_health

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        return self


class FindAllServiceResponseBodyDataListServiceEnds(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        id: int = None,
        ip_address: str = None,
        port: str = None,
        service_id: int = None,
        status: int = None,
        update_date_time: str = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # ipAddress
        self.ip_address = ip_address
        # port
        self.port = port
        # serviceId
        self.service_id = service_id
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.port is not None:
            result['port'] = self.port
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindAllServiceResponseBodyDataList(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        is_auto_refresh: bool = None,
        is_health: bool = None,
        name: str = None,
        registry_id: str = None,
        service_ends: List[FindAllServiceResponseBodyDataListServiceEnds] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # isHealth
        self.is_health = is_health
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        self.service_ends = []
        if m.get('serviceEnds') is not None:
            for k in m.get('serviceEnds'):
                temp_model = FindAllServiceResponseBodyDataListServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindAllServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[FindAllServiceResponseBodyDataList] = None,
        total_count: int = None,
    ):
        # list
        self.list = list
        # totalCount
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = FindAllServiceResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class FindAllServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FindAllServiceResponseBodyData = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = FindAllServiceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindAllServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindAllServiceResponseBody = None,
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
            temp_model = FindAllServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        attached_services: List[int] = None,
        base_path: str = None,
        description: str = None,
        name: str = None,
        status: int = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # attachedServices
        self.attached_services = attached_services
        # basePath
        self.base_path = base_path
        # description
        self.description = description
        # name
        self.name = name
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.attached_services is not None:
            result['attachedServices'] = self.attached_services
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('attachedServices') is not None:
            self.attached_services = m.get('attachedServices')
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateApiResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApiResponseBody = None,
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
            temp_model = CreateApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayByIdResponseBodyDataArmsInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        description: str = None,
        license_key: str = None,
    ):
        # appId
        self.app_id = app_id
        # appName
        self.app_name = app_name
        # description
        self.description = description
        # licenseKey
        self.license_key = license_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.description is not None:
            result['description'] = self.description
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        return self


class GetGatewayByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        arms_info: GetGatewayByIdResponseBodyDataArmsInfo = None,
        auto_create_slb: bool = None,
        base_path: str = None,
        creation_date_time: str = None,
        edas_namespace_id: str = None,
        gateway_type: str = None,
        id: int = None,
        name: str = None,
        pod_cidr: str = None,
        region: str = None,
        region_name: str = None,
        replica: int = None,
        runtime_on: str = None,
        security_group: str = None,
        slb: str = None,
        slb_access_addr: str = None,
        status: str = None,
        vpc: str = None,
        vswitch: str = None,
    ):
        # armsInfo
        self.arms_info = arms_info
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id
        # gatewayType
        self.gateway_type = gateway_type
        # id
        self.id = id
        # name
        self.name = name
        # podCidr
        self.pod_cidr = pod_cidr
        # region
        self.region = region
        # regionName
        self.region_name = region_name
        # replica
        self.replica = replica
        # runtimeOn
        self.runtime_on = runtime_on
        # securityGroup
        self.security_group = security_group
        # slb
        self.slb = slb
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr
        # status
        self.status = status
        # vpc
        self.vpc = vpc
        # vswitch
        self.vswitch = vswitch

    def validate(self):
        if self.arms_info:
            self.arms_info.validate()

    def to_map(self):
        result = dict()
        if self.arms_info is not None:
            result['armsInfo'] = self.arms_info.to_map()
        if self.auto_create_slb is not None:
            result['autoCreateSlb'] = self.auto_create_slb
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.edas_namespace_id is not None:
            result['edasNamespaceId'] = self.edas_namespace_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.pod_cidr is not None:
            result['podCidr'] = self.pod_cidr
        if self.region is not None:
            result['region'] = self.region
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.replica is not None:
            result['replica'] = self.replica
        if self.runtime_on is not None:
            result['runtimeOn'] = self.runtime_on
        if self.security_group is not None:
            result['securityGroup'] = self.security_group
        if self.slb is not None:
            result['slb'] = self.slb
        if self.slb_access_addr is not None:
            result['slbAccessAddr'] = self.slb_access_addr
        if self.status is not None:
            result['status'] = self.status
        if self.vpc is not None:
            result['vpc'] = self.vpc
        if self.vswitch is not None:
            result['vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsInfo') is not None:
            temp_model = GetGatewayByIdResponseBodyDataArmsInfo()
            self.arms_info = temp_model.from_map(m['armsInfo'])
        if m.get('autoCreateSlb') is not None:
            self.auto_create_slb = m.get('autoCreateSlb')
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('edasNamespaceId') is not None:
            self.edas_namespace_id = m.get('edasNamespaceId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('podCidr') is not None:
            self.pod_cidr = m.get('podCidr')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('runtimeOn') is not None:
            self.runtime_on = m.get('runtimeOn')
        if m.get('securityGroup') is not None:
            self.security_group = m.get('securityGroup')
        if m.get('slb') is not None:
            self.slb = m.get('slb')
        if m.get('slbAccessAddr') is not None:
            self.slb_access_addr = m.get('slbAccessAddr')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('vpc') is not None:
            self.vpc = m.get('vpc')
        if m.get('vswitch') is not None:
            self.vswitch = m.get('vswitch')
        return self


class GetGatewayByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetGatewayByIdResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetGatewayByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetGatewayByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGatewayByIdResponseBody = None,
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
            temp_model = GetGatewayByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        content: str = None,
        gateway_id: int = None,
        id: int = None,
        name: str = None,
        policy_group: str = None,
        type: int = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # content
        self.content = content
        # gatewayId
        self.gateway_id = gateway_id
        # id
        self.id = id
        # name
        self.name = name
        # policyGroup
        self.policy_group = policy_group
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.content is not None:
            result['content'] = self.content
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePolicyResponseBody = None,
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceForRegistryByServiceNameRequest(TeaModel):
    def __init__(
        self,
        service_name: str = None,
    ):
        # serviceName
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class GetServiceInstanceForRegistryByServiceNameResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        meta_info: str = None,
        service_ends: List[str] = None,
        service_name: str = None,
    ):
        # id
        self.id = id
        # metaInfo
        self.meta_info = meta_info
        self.service_ends = service_ends
        # serviceName
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info
        if self.service_ends is not None:
            result['serviceEnds'] = self.service_ends
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('metaInfo') is not None:
            self.meta_info = m.get('metaInfo')
        if m.get('serviceEnds') is not None:
            self.service_ends = m.get('serviceEnds')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class GetServiceInstanceForRegistryByServiceNameResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetServiceInstanceForRegistryByServiceNameResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetServiceInstanceForRegistryByServiceNameResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetServiceInstanceForRegistryByServiceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceInstanceForRegistryByServiceNameResponseBody = None,
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
            temp_model = GetServiceInstanceForRegistryByServiceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceResponseBody = None,
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRegistryRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        description: str = None,
        gateway_id: int = None,
        id: str = None,
        name: str = None,
        type: int = None,
    ):
        # address
        self.address = address
        # description
        self.description = description
        # gatewayId
        self.gateway_id = gateway_id
        # id
        self.id = id
        # name
        self.name = name
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.description is not None:
            result['description'] = self.description
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateRegistryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateRegistryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRegistryResponseBody = None,
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
            temp_model = UpdateRegistryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayRequest(TeaModel):
    def __init__(
        self,
        auto_create_slb: bool = None,
        base_path: str = None,
        edas_namespace_id: str = None,
        gateway_type: str = None,
        name: str = None,
        pod_cidr: str = None,
        region: str = None,
        region_name: str = None,
        replica: int = None,
        runtime_on: str = None,
        security_group: str = None,
        slb: str = None,
        slb_spec: str = None,
        vpc: str = None,
        vswitch: str = None,
        zone: str = None,
    ):
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb
        # basePath
        self.base_path = base_path
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id
        # gatewayType
        self.gateway_type = gateway_type
        # name
        self.name = name
        # podCidr
        self.pod_cidr = pod_cidr
        # region
        self.region = region
        # regionName
        self.region_name = region_name
        # replica
        self.replica = replica
        # runtimeOn
        self.runtime_on = runtime_on
        # securityGroup
        self.security_group = security_group
        # slb
        self.slb = slb
        # slbSpec
        self.slb_spec = slb_spec
        # vpc
        self.vpc = vpc
        # vswitch
        self.vswitch = vswitch
        # zone
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auto_create_slb is not None:
            result['autoCreateSlb'] = self.auto_create_slb
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.edas_namespace_id is not None:
            result['edasNamespaceId'] = self.edas_namespace_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.name is not None:
            result['name'] = self.name
        if self.pod_cidr is not None:
            result['podCidr'] = self.pod_cidr
        if self.region is not None:
            result['region'] = self.region
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.replica is not None:
            result['replica'] = self.replica
        if self.runtime_on is not None:
            result['runtimeOn'] = self.runtime_on
        if self.security_group is not None:
            result['securityGroup'] = self.security_group
        if self.slb is not None:
            result['slb'] = self.slb
        if self.slb_spec is not None:
            result['slbSpec'] = self.slb_spec
        if self.vpc is not None:
            result['vpc'] = self.vpc
        if self.vswitch is not None:
            result['vswitch'] = self.vswitch
        if self.zone is not None:
            result['zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoCreateSlb') is not None:
            self.auto_create_slb = m.get('autoCreateSlb')
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('edasNamespaceId') is not None:
            self.edas_namespace_id = m.get('edasNamespaceId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('podCidr') is not None:
            self.pod_cidr = m.get('podCidr')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('runtimeOn') is not None:
            self.runtime_on = m.get('runtimeOn')
        if m.get('securityGroup') is not None:
            self.security_group = m.get('securityGroup')
        if m.get('slb') is not None:
            self.slb = m.get('slb')
        if m.get('slbSpec') is not None:
            self.slb_spec = m.get('slbSpec')
        if m.get('vpc') is not None:
            self.vpc = m.get('vpc')
        if m.get('vswitch') is not None:
            self.vswitch = m.get('vswitch')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        return self


class CreateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGatewayResponseBody = None,
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
            temp_model = CreateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceHealthRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        operation_ids: List[int] = None,
    ):
        # id
        self.id = id
        # operationIds
        self.operation_ids = operation_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.operation_ids is not None:
            result['operationIds'] = self.operation_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('operationIds') is not None:
            self.operation_ids = m.get('operationIds')
        return self


class CheckServiceHealthResponseBodyDataServiceEnds(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        id: int = None,
        ip_address: str = None,
        port: str = None,
        service_id: int = None,
        status: int = None,
        update_date_time: str = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # ipAddress
        self.ip_address = ip_address
        # port
        self.port = port
        # serviceId
        self.service_id = service_id
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.port is not None:
            result['port'] = self.port
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class CheckServiceHealthResponseBodyData(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        is_auto_refresh: bool = None,
        is_health: bool = None,
        name: str = None,
        registry_id: str = None,
        service_ends: List[CheckServiceHealthResponseBodyDataServiceEnds] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # isHealth
        self.is_health = is_health
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        self.service_ends = []
        if m.get('serviceEnds') is not None:
            for k in m.get('serviceEnds'):
                temp_model = CheckServiceHealthResponseBodyDataServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class CheckServiceHealthResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[CheckServiceHealthResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = CheckServiceHealthResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CheckServiceHealthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckServiceHealthResponseBody = None,
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
            temp_model = CheckServiceHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyToApiRequest(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        direction: str = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: int = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreatePolicyToApiResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreatePolicyToApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePolicyToApiResponseBody = None,
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
            temp_model = CreatePolicyToApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DetachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachPolicyResponseBody = None,
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
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindTemplateResponseBody = None,
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
            temp_model = FindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateRegistryAddressRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        type: int = None,
    ):
        # address
        self.address = address
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ValidateRegistryAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ValidateRegistryAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateRegistryAddressResponseBody = None,
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
            temp_model = ValidateRegistryAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApiDetailResponseBodyDataAttachedServicesServiceEnds(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        id: int = None,
        ip_address: str = None,
        port: str = None,
        service_id: int = None,
        status: int = None,
        update_date_time: str = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # ipAddress
        self.ip_address = ip_address
        # port
        self.port = port
        # serviceId
        self.service_id = service_id
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.port is not None:
            result['port'] = self.port
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetApiDetailResponseBodyDataAttachedServices(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        is_auto_refresh: bool = None,
        is_health: bool = None,
        name: str = None,
        registry_id: str = None,
        service_ends: List[GetApiDetailResponseBodyDataAttachedServicesServiceEnds] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # isHealth
        self.is_health = is_health
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        self.service_ends = []
        if m.get('serviceEnds') is not None:
            for k in m.get('serviceEnds'):
                temp_model = GetApiDetailResponseBodyDataAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetApiDetailResponseBodyDataOwneredPolicies(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        creation_date_time: str = None,
        direction: str = None,
        id: int = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # apiId
        self.api_id = api_id
        # apiName
        self.api_name = api_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # id
        self.id = id
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetApiDetailResponseBodyDataPublishedGateway(TeaModel):
    def __init__(
        self,
        arms_info: str = None,
        auto_create_slb: bool = None,
        base_path: str = None,
        creation_date_time: str = None,
        edas_namespace_id: str = None,
        gateway_type: str = None,
        id: int = None,
        name: str = None,
        pod_cidr: str = None,
        region: str = None,
        region_name: str = None,
        replica: int = None,
        runtime_on: str = None,
        security_group: str = None,
        slb: str = None,
        slb_access_addr: str = None,
        status: str = None,
        vpc: str = None,
        vswitch: str = None,
    ):
        # armsInfo
        self.arms_info = arms_info
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id
        # gatewayType
        self.gateway_type = gateway_type
        # id
        self.id = id
        # name
        self.name = name
        # podCidr
        self.pod_cidr = pod_cidr
        # region
        self.region = region
        # regionName
        self.region_name = region_name
        # replica
        self.replica = replica
        # runtimeOn
        self.runtime_on = runtime_on
        # securityGroup
        self.security_group = security_group
        # slb
        self.slb = slb
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr
        # status
        self.status = status
        # vpc
        self.vpc = vpc
        # vswitch
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.arms_info is not None:
            result['armsInfo'] = self.arms_info
        if self.auto_create_slb is not None:
            result['autoCreateSlb'] = self.auto_create_slb
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.edas_namespace_id is not None:
            result['edasNamespaceId'] = self.edas_namespace_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.pod_cidr is not None:
            result['podCidr'] = self.pod_cidr
        if self.region is not None:
            result['region'] = self.region
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.replica is not None:
            result['replica'] = self.replica
        if self.runtime_on is not None:
            result['runtimeOn'] = self.runtime_on
        if self.security_group is not None:
            result['securityGroup'] = self.security_group
        if self.slb is not None:
            result['slb'] = self.slb
        if self.slb_access_addr is not None:
            result['slbAccessAddr'] = self.slb_access_addr
        if self.status is not None:
            result['status'] = self.status
        if self.vpc is not None:
            result['vpc'] = self.vpc
        if self.vswitch is not None:
            result['vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsInfo') is not None:
            self.arms_info = m.get('armsInfo')
        if m.get('autoCreateSlb') is not None:
            self.auto_create_slb = m.get('autoCreateSlb')
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('edasNamespaceId') is not None:
            self.edas_namespace_id = m.get('edasNamespaceId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('podCidr') is not None:
            self.pod_cidr = m.get('podCidr')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('runtimeOn') is not None:
            self.runtime_on = m.get('runtimeOn')
        if m.get('securityGroup') is not None:
            self.security_group = m.get('securityGroup')
        if m.get('slb') is not None:
            self.slb = m.get('slb')
        if m.get('slbAccessAddr') is not None:
            self.slb_access_addr = m.get('slbAccessAddr')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('vpc') is not None:
            self.vpc = m.get('vpc')
        if m.get('vswitch') is not None:
            self.vswitch = m.get('vswitch')
        return self


class GetApiDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        attached_services: List[GetApiDetailResponseBodyDataAttachedServices] = None,
        base_path: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        ownered_policies: List[GetApiDetailResponseBodyDataOwneredPolicies] = None,
        published_gateway: GetApiDetailResponseBodyDataPublishedGateway = None,
        status: str = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # attachedServices
        self.attached_services = attached_services
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # name
        self.name = name
        # owneredPolicies
        self.ownered_policies = ownered_policies
        # A short description of struct
        self.published_gateway = published_gateway
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.attached_services:
            for k in self.attached_services:
                if k:
                    k.validate()
        if self.ownered_policies:
            for k in self.ownered_policies:
                if k:
                    k.validate()
        if self.published_gateway:
            self.published_gateway.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        result['attachedServices'] = []
        if self.attached_services is not None:
            for k in self.attached_services:
                result['attachedServices'].append(k.to_map() if k else None)
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        result['owneredPolicies'] = []
        if self.ownered_policies is not None:
            for k in self.ownered_policies:
                result['owneredPolicies'].append(k.to_map() if k else None)
        if self.published_gateway is not None:
            result['publishedGateway'] = self.published_gateway.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        self.attached_services = []
        if m.get('attachedServices') is not None:
            for k in m.get('attachedServices'):
                temp_model = GetApiDetailResponseBodyDataAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.ownered_policies = []
        if m.get('owneredPolicies') is not None:
            for k in m.get('owneredPolicies'):
                temp_model = GetApiDetailResponseBodyDataOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        if m.get('publishedGateway') is not None:
            temp_model = GetApiDetailResponseBodyDataPublishedGateway()
            self.published_gateway = temp_model.from_map(m['publishedGateway'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetApiDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetApiDetailResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetApiDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetApiDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetApiDetailResponseBody = None,
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
            temp_model = GetApiDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpecialRouteForRegistryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateSpecialRouteForRegistryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSpecialRouteForRegistryResponseBody = None,
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
            temp_model = CreateSpecialRouteForRegistryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishApiResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PublishApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishApiResponseBody = None,
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
            temp_model = PublishApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayLogEtlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateGatewayLogEtlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGatewayLogEtlResponseBody = None,
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
            temp_model = CreateGatewayLogEtlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindPoliciesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        name: str = None,
        alias_name: str = None,
        type: int = None,
        group: str = None,
    ):
        # pageNumber
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        # name
        self.name = name
        # aliasName
        self.alias_name = alias_name
        # type
        self.type = type
        # group
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.type is not None:
            result['type'] = self.type
        if self.group is not None:
            result['group'] = self.group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('group') is not None:
            self.group = m.get('group')
        return self


class FindPoliciesResponseBodyDataListAttachedApi(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        creation_date_time: str = None,
        direction: str = None,
        id: int = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # apiId
        self.api_id = api_id
        # apiName
        self.api_name = api_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # id
        self.id = id
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindPoliciesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        attached_api: List[FindPoliciesResponseBodyDataListAttachedApi] = None,
        content: str = None,
        creation_date_time: str = None,
        id: int = None,
        name: str = None,
        policy_group: str = None,
        policy_type_name: str = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # attachedApi
        self.attached_api = attached_api
        # content
        self.content = content
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # name
        self.name = name
        # policyGroup
        self.policy_group = policy_group
        # policyTypeName
        self.policy_type_name = policy_type_name
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.attached_api:
            for k in self.attached_api:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        result['attachedApi'] = []
        if self.attached_api is not None:
            for k in self.attached_api:
                result['attachedApi'].append(k.to_map() if k else None)
        if self.content is not None:
            result['content'] = self.content
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_type_name is not None:
            result['policyTypeName'] = self.policy_type_name
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        self.attached_api = []
        if m.get('attachedApi') is not None:
            for k in m.get('attachedApi'):
                temp_model = FindPoliciesResponseBodyDataListAttachedApi()
                self.attached_api.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyTypeName') is not None:
            self.policy_type_name = m.get('policyTypeName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindPoliciesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[FindPoliciesResponseBodyDataList] = None,
        total_count: int = None,
    ):
        # list
        self.list = list
        # totalCount
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = FindPoliciesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class FindPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FindPoliciesResponseBodyData = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = FindPoliciesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindPoliciesResponseBody = None,
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
            temp_model = FindPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachPolicyRequestData(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        direction: str = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: int = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AttachPolicyRequest(TeaModel):
    def __init__(
        self,
        data: List[AttachPolicyRequestData] = None,
    ):
        # data
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = AttachPolicyRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class AttachPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class AttachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachPolicyResponseBody = None,
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
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindRegistryResponseBodyData(TeaModel):
    def __init__(
        self,
        address: str = None,
        creation_date_time: str = None,
        description: str = None,
        gateway_id: str = None,
        id: int = None,
        name: str = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # address
        self.address = address
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # gatewayId
        self.gateway_id = gateway_id
        # id
        self.id = id
        # name
        self.name = name
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindRegistryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[FindRegistryResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FindRegistryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindRegistryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindRegistryResponseBody = None,
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
            temp_model = FindRegistryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTicketByIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        cookie: Dict[str, Any] = None,
    ):
        self.common_headers = common_headers
        # cookie
        self.cookie = cookie

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.cookie is not None:
            result['cookie'] = self.cookie
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('cookie') is not None:
            self.cookie = m.get('cookie')
        return self


class GetAuthTicketByIdShrinkHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        cookie_shrink: str = None,
    ):
        self.common_headers = common_headers
        # cookie
        self.cookie_shrink = cookie_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.cookie_shrink is not None:
            result['cookie'] = self.cookie_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('cookie') is not None:
            self.cookie_shrink = m.get('cookie')
        return self


class GetAuthTicketByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        comment: str = None,
        id: int = None,
        name: str = None,
        server_key: str = None,
        ticket_type: str = None,
        valid_end_time: str = None,
        valid_start_time: str = None,
    ):
        # clientToken
        self.client_token = client_token
        # comment
        self.comment = comment
        # id
        self.id = id
        # name
        self.name = name
        # serverKey
        self.server_key = server_key
        # ticketType
        self.ticket_type = ticket_type
        # validEndTime
        self.valid_end_time = valid_end_time
        # validStartTime
        self.valid_start_time = valid_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.comment is not None:
            result['comment'] = self.comment
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.server_key is not None:
            result['serverKey'] = self.server_key
        if self.ticket_type is not None:
            result['ticketType'] = self.ticket_type
        if self.valid_end_time is not None:
            result['validEndTime'] = self.valid_end_time
        if self.valid_start_time is not None:
            result['validStartTime'] = self.valid_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serverKey') is not None:
            self.server_key = m.get('serverKey')
        if m.get('ticketType') is not None:
            self.ticket_type = m.get('ticketType')
        if m.get('validEndTime') is not None:
            self.valid_end_time = m.get('validEndTime')
        if m.get('validStartTime') is not None:
            self.valid_start_time = m.get('validStartTime')
        return self


class GetAuthTicketByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetAuthTicketByIdResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetAuthTicketByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAuthTicketByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthTicketByIdResponseBody = None,
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
            temp_model = GetAuthTicketByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRegistryRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        description: str = None,
        gateway_id: int = None,
        id: str = None,
        name: str = None,
        type: int = None,
    ):
        # address
        self.address = address
        # description
        self.description = description
        # gatewayId
        self.gateway_id = gateway_id
        # id
        self.id = id
        # name
        self.name = name
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.description is not None:
            result['description'] = self.description
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateRegistryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateRegistryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRegistryResponseBody = None,
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
            temp_model = CreateRegistryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecycleApiResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RecycleApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecycleApiResponseBody = None,
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
            temp_model = RecycleApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthTicketRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        gateway_id: int = None,
        name: str = None,
        ticket_type: str = None,
        duration: int = None,
        jwt_signature_type_enum: str = None,
    ):
        # comment
        self.comment = comment
        # gatewayId
        self.gateway_id = gateway_id
        # name
        self.name = name
        # ticketType
        self.ticket_type = ticket_type
        self.duration = duration
        self.jwt_signature_type_enum = jwt_signature_type_enum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.ticket_type is not None:
            result['ticketType'] = self.ticket_type
        if self.duration is not None:
            result['duration'] = self.duration
        if self.jwt_signature_type_enum is not None:
            result['jwtSignatureTypeEnum'] = self.jwt_signature_type_enum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ticketType') is not None:
            self.ticket_type = m.get('ticketType')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('jwtSignatureTypeEnum') is not None:
            self.jwt_signature_type_enum = m.get('jwtSignatureTypeEnum')
        return self


class CreateAuthTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateAuthTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAuthTicketResponseBody = None,
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
            temp_model = CreateAuthTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGatewayResponseBody = None,
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
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindServiceResponseBodyDataServiceEnds(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        id: int = None,
        ip_address: str = None,
        port: str = None,
        service_id: int = None,
        status: int = None,
        update_date_time: str = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # ipAddress
        self.ip_address = ip_address
        # port
        self.port = port
        # serviceId
        self.service_id = service_id
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.port is not None:
            result['port'] = self.port
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        is_auto_refresh: bool = None,
        is_health: bool = None,
        name: str = None,
        registry_id: str = None,
        service_ends: List[FindServiceResponseBodyDataServiceEnds] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # isHealth
        self.is_health = is_health
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        self.service_ends = []
        if m.get('serviceEnds') is not None:
            for k in m.get('serviceEnds'):
                temp_model = FindServiceResponseBodyDataServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[FindServiceResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FindServiceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindServiceResponseBody = None,
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
            temp_model = FindServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeletePolicyByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePolicyByIdResponseBody = None,
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
            temp_model = DeletePolicyByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApiResponseBody = None,
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
            temp_model = DeleteApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindAuthTicketsRequest(TeaModel):
    def __init__(
        self,
        gateway_id: int = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # gatewayId
        self.gateway_id = gateway_id
        # name
        self.name = name
        # pageNumber
        self.page_number = page_number
        # pageSize
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class FindAuthTicketsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        comment: str = None,
        id: int = None,
        name: str = None,
        server_key: str = None,
        ticket_type: str = None,
        valid_end_time: str = None,
        valid_start_time: str = None,
    ):
        # clientToken
        self.client_token = client_token
        # comment
        self.comment = comment
        # id
        self.id = id
        # name
        self.name = name
        # serverKey
        self.server_key = server_key
        # ticketType
        self.ticket_type = ticket_type
        # validEndTime
        self.valid_end_time = valid_end_time
        # validStartTime
        self.valid_start_time = valid_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.comment is not None:
            result['comment'] = self.comment
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.server_key is not None:
            result['serverKey'] = self.server_key
        if self.ticket_type is not None:
            result['ticketType'] = self.ticket_type
        if self.valid_end_time is not None:
            result['validEndTime'] = self.valid_end_time
        if self.valid_start_time is not None:
            result['validStartTime'] = self.valid_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serverKey') is not None:
            self.server_key = m.get('serverKey')
        if m.get('ticketType') is not None:
            self.ticket_type = m.get('ticketType')
        if m.get('validEndTime') is not None:
            self.valid_end_time = m.get('validEndTime')
        if m.get('validStartTime') is not None:
            self.valid_start_time = m.get('validStartTime')
        return self


class FindAuthTicketsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[FindAuthTicketsResponseBodyDataList] = None,
        total_count: int = None,
    ):
        # list
        self.list = list
        # totalCount
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = FindAuthTicketsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class FindAuthTicketsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FindAuthTicketsResponseBodyData = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = FindAuthTicketsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindAuthTicketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindAuthTicketsResponseBody = None,
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
            temp_model = FindAuthTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        content: str = None,
        id: int = None,
        name: str = None,
        policy_group: str = None,
        type: int = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # content
        self.content = content
        # id
        self.id = id
        # name
        self.name = name
        # policyGroup
        self.policy_group = policy_group
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.content is not None:
            result['content'] = self.content
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePolicyResponseBody = None,
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
            temp_model = UpdatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthTicketRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        id: int = None,
    ):
        # comment
        self.comment = comment
        # id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UpdateAuthTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateAuthTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAuthTicketResponseBody = None,
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
            temp_model = UpdateAuthTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallArmsAgentResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class InstallArmsAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InstallArmsAgentResponseBody = None,
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
            temp_model = InstallArmsAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthTicketResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteAuthTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAuthTicketResponseBody = None,
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
            temp_model = DeleteAuthTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyByIdResponseBodyDataAttachedApi(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        creation_date_time: str = None,
        direction: str = None,
        id: int = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # apiId
        self.api_id = api_id
        # apiName
        self.api_name = api_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # id
        self.id = id
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetPolicyByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        attached_api: List[GetPolicyByIdResponseBodyDataAttachedApi] = None,
        content: str = None,
        creation_date_time: str = None,
        id: int = None,
        name: str = None,
        policy_group: str = None,
        policy_type_name: str = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # attachedApi
        self.attached_api = attached_api
        # content
        self.content = content
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # name
        self.name = name
        # policyGroup
        self.policy_group = policy_group
        # policyTypeName
        self.policy_type_name = policy_type_name
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.attached_api:
            for k in self.attached_api:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        result['attachedApi'] = []
        if self.attached_api is not None:
            for k in self.attached_api:
                result['attachedApi'].append(k.to_map() if k else None)
        if self.content is not None:
            result['content'] = self.content
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_type_name is not None:
            result['policyTypeName'] = self.policy_type_name
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        self.attached_api = []
        if m.get('attachedApi') is not None:
            for k in m.get('attachedApi'):
                temp_model = GetPolicyByIdResponseBodyDataAttachedApi()
                self.attached_api.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyTypeName') is not None:
            self.policy_type_name = m.get('policyTypeName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetPolicyByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetPolicyByIdResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetPolicyByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetPolicyByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPolicyByIdResponseBody = None,
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
            temp_model = GetPolicyByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeleteRegistryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRegistryResponseBody = None,
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
            temp_model = DeleteRegistryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DataScopesValue(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        creation_date_time: str = None,
        direction: str = None,
        id: int = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # apiId
        self.api_id = api_id
        # apiName
        self.api_name = api_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # id
        self.id = id
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetPolicyOwnedByApiResponseBodyData(TeaModel):
    def __init__(
        self,
        scopes: Dict[str, List[DataScopesValue]] = None,
    ):
        self.scopes = scopes

    def validate(self):
        if self.scopes:
            for v in self.scopes.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        result = dict()
        result['scopes'] = {}
        if self.scopes is not None:
            for k, v in self.scopes.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['scopes'][k] = l1
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scopes = {}
        if m.get('scopes') is not None:
            for k, v in m.get('scopes').items():
                l1 = []
                for k1 in v:
                    temp_model = DataScopesValue()
                    l1.append(temp_model.from_map(k1))
                self.scopes['k'] = l1
        return self


class GetPolicyOwnedByApiResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetPolicyOwnedByApiResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetPolicyOwnedByApiResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetPolicyOwnedByApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPolicyOwnedByApiResponseBody = None,
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
            temp_model = GetPolicyOwnedByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApiRequestAttachedServicesServiceEnds(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        id: int = None,
        ip_address: str = None,
        port: str = None,
        service_id: int = None,
        status: int = None,
        update_date_time: str = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # ipAddress
        self.ip_address = ip_address
        # port
        self.port = port
        # serviceId
        self.service_id = service_id
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.port is not None:
            result['port'] = self.port
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class UpdateApiRequestAttachedServices(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        is_auto_refresh: bool = None,
        is_health: bool = None,
        name: str = None,
        registry_id: str = None,
        service_ends: List[UpdateApiRequestAttachedServicesServiceEnds] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # isHealth
        self.is_health = is_health
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        self.service_ends = []
        if m.get('serviceEnds') is not None:
            for k in m.get('serviceEnds'):
                temp_model = UpdateApiRequestAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class UpdateApiRequestOwneredPolicies(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        creation_date_time: str = None,
        direction: str = None,
        id: int = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # apiId
        self.api_id = api_id
        # apiName
        self.api_name = api_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # id
        self.id = id
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class UpdateApiRequestPublishedGateway(TeaModel):
    def __init__(
        self,
        arms_info: str = None,
        auto_create_slb: bool = None,
        base_path: str = None,
        creation_date_time: str = None,
        edas_namespace_id: str = None,
        gateway_type: str = None,
        id: int = None,
        name: str = None,
        pod_cidr: str = None,
        region: str = None,
        region_name: str = None,
        replica: int = None,
        runtime_on: str = None,
        security_group: str = None,
        slb: str = None,
        slb_access_addr: str = None,
        status: str = None,
        vpc: str = None,
        vswitch: str = None,
    ):
        # armsInfo
        self.arms_info = arms_info
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id
        # gatewayType
        self.gateway_type = gateway_type
        # id
        self.id = id
        # name
        self.name = name
        # podCidr
        self.pod_cidr = pod_cidr
        # region
        self.region = region
        # regionName
        self.region_name = region_name
        # replica
        self.replica = replica
        # runtimeOn
        self.runtime_on = runtime_on
        # securityGroup
        self.security_group = security_group
        # slb
        self.slb = slb
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr
        # status
        self.status = status
        # vpc
        self.vpc = vpc
        # vswitch
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.arms_info is not None:
            result['armsInfo'] = self.arms_info
        if self.auto_create_slb is not None:
            result['autoCreateSlb'] = self.auto_create_slb
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.edas_namespace_id is not None:
            result['edasNamespaceId'] = self.edas_namespace_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.pod_cidr is not None:
            result['podCidr'] = self.pod_cidr
        if self.region is not None:
            result['region'] = self.region
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.replica is not None:
            result['replica'] = self.replica
        if self.runtime_on is not None:
            result['runtimeOn'] = self.runtime_on
        if self.security_group is not None:
            result['securityGroup'] = self.security_group
        if self.slb is not None:
            result['slb'] = self.slb
        if self.slb_access_addr is not None:
            result['slbAccessAddr'] = self.slb_access_addr
        if self.status is not None:
            result['status'] = self.status
        if self.vpc is not None:
            result['vpc'] = self.vpc
        if self.vswitch is not None:
            result['vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsInfo') is not None:
            self.arms_info = m.get('armsInfo')
        if m.get('autoCreateSlb') is not None:
            self.auto_create_slb = m.get('autoCreateSlb')
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('edasNamespaceId') is not None:
            self.edas_namespace_id = m.get('edasNamespaceId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('podCidr') is not None:
            self.pod_cidr = m.get('podCidr')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('runtimeOn') is not None:
            self.runtime_on = m.get('runtimeOn')
        if m.get('securityGroup') is not None:
            self.security_group = m.get('securityGroup')
        if m.get('slb') is not None:
            self.slb = m.get('slb')
        if m.get('slbAccessAddr') is not None:
            self.slb_access_addr = m.get('slbAccessAddr')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('vpc') is not None:
            self.vpc = m.get('vpc')
        if m.get('vswitch') is not None:
            self.vswitch = m.get('vswitch')
        return self


class UpdateApiRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        attached_services: List[UpdateApiRequestAttachedServices] = None,
        base_path: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        ownered_policies: List[UpdateApiRequestOwneredPolicies] = None,
        published_gateway: UpdateApiRequestPublishedGateway = None,
        status: str = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # attachedServices
        self.attached_services = attached_services
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # name
        self.name = name
        # owneredPolicies
        self.ownered_policies = ownered_policies
        # A short description of struct
        self.published_gateway = published_gateway
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.attached_services:
            for k in self.attached_services:
                if k:
                    k.validate()
        if self.ownered_policies:
            for k in self.ownered_policies:
                if k:
                    k.validate()
        if self.published_gateway:
            self.published_gateway.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        result['attachedServices'] = []
        if self.attached_services is not None:
            for k in self.attached_services:
                result['attachedServices'].append(k.to_map() if k else None)
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        result['owneredPolicies'] = []
        if self.ownered_policies is not None:
            for k in self.ownered_policies:
                result['owneredPolicies'].append(k.to_map() if k else None)
        if self.published_gateway is not None:
            result['publishedGateway'] = self.published_gateway.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        self.attached_services = []
        if m.get('attachedServices') is not None:
            for k in m.get('attachedServices'):
                temp_model = UpdateApiRequestAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.ownered_policies = []
        if m.get('owneredPolicies') is not None:
            for k in m.get('owneredPolicies'):
                temp_model = UpdateApiRequestOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        if m.get('publishedGateway') is not None:
            temp_model = UpdateApiRequestPublishedGateway()
            self.published_gateway = temp_model.from_map(m['publishedGateway'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class UpdateApiResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApiResponseBody = None,
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
            temp_model = UpdateApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        description: str = None,
        is_auto_refresh: bool = None,
        meta_info: List[str] = None,
        name: str = None,
        registry_id: int = None,
        service_ends: List[str] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # description
        self.description = description
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # metaInfo
        self.meta_info = meta_info
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.description is not None:
            result['description'] = self.description
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        if self.service_ends is not None:
            result['serviceEnds'] = self.service_ends
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('metaInfo') is not None:
            self.meta_info = m.get('metaInfo')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        if m.get('serviceEnds') is not None:
            self.service_ends = m.get('serviceEnds')
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceResponseBody = None,
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAllPoliciesRequestData(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        creation_date_time: str = None,
        direction: str = None,
        id: int = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # apiId
        self.api_id = api_id
        # apiName
        self.api_name = api_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # id
        self.id = id
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class SaveAllPoliciesRequest(TeaModel):
    def __init__(
        self,
        data: List[SaveAllPoliciesRequestData] = None,
    ):
        # data
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = SaveAllPoliciesRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class SaveAllPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class SaveAllPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveAllPoliciesResponseBody = None,
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
            temp_model = SaveAllPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        replica: str = None,
    ):
        # id
        self.id = id
        # replica
        self.replica = replica

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.replica is not None:
            result['replica'] = self.replica
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        return self


class UpdateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGatewayResponseBody = None,
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
            temp_model = UpdateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        is_auto_refresh: bool = None,
        is_health: bool = None,
        name: str = None,
        registry_id: int = None,
        service_ends: List[str] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # isHealth
        self.is_health = is_health
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        if self.service_ends is not None:
            result['serviceEnds'] = self.service_ends
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        if m.get('serviceEnds') is not None:
            self.service_ends = m.get('serviceEnds')
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceResponseBody = None,
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindApisByPagingRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        name: str = None,
        alias_name: str = None,
    ):
        # pageNumber
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        # status
        self.status = status
        # name
        self.name = name
        # aliasName
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        return self


class FindApisByPagingResponseBodyDataListAttachedServicesServiceEnds(TeaModel):
    def __init__(
        self,
        creation_date_time: str = None,
        id: int = None,
        ip_address: str = None,
        port: str = None,
        service_id: int = None,
        status: int = None,
        update_date_time: str = None,
    ):
        # creationDateTime
        self.creation_date_time = creation_date_time
        # id
        self.id = id
        # ipAddress
        self.ip_address = ip_address
        # port
        self.port = port
        # serviceId
        self.service_id = service_id
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.id is not None:
            result['id'] = self.id
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.port is not None:
            result['port'] = self.port
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyDataListAttachedServices(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        is_auto_refresh: bool = None,
        is_health: bool = None,
        name: str = None,
        registry_id: str = None,
        service_ends: List[FindApisByPagingResponseBodyDataListAttachedServicesServiceEnds] = None,
        service_name_in_registry: str = None,
        source_type: int = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh
        # isHealth
        self.is_health = is_health
        # name
        self.name = name
        # registryId
        self.registry_id = registry_id
        # serviceEnds
        self.service_ends = service_ends
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry
        # sourceType
        self.source_type = source_type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_auto_refresh is not None:
            result['isAutoRefresh'] = self.is_auto_refresh
        if self.is_health is not None:
            result['isHealth'] = self.is_health
        if self.name is not None:
            result['name'] = self.name
        if self.registry_id is not None:
            result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        if self.service_name_in_registry is not None:
            result['serviceNameInRegistry'] = self.service_name_in_registry
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isAutoRefresh') is not None:
            self.is_auto_refresh = m.get('isAutoRefresh')
        if m.get('isHealth') is not None:
            self.is_health = m.get('isHealth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('registryId') is not None:
            self.registry_id = m.get('registryId')
        self.service_ends = []
        if m.get('serviceEnds') is not None:
            for k in m.get('serviceEnds'):
                temp_model = FindApisByPagingResponseBodyDataListAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if m.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('serviceNameInRegistry')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyDataListOwneredPolicies(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        creation_date_time: str = None,
        direction: str = None,
        id: int = None,
        policy_alias_name: str = None,
        policy_content: str = None,
        policy_group: str = None,
        policy_id: str = None,
        policy_name: str = None,
        priority: int = None,
        scope: str = None,
        status: bool = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # apiId
        self.api_id = api_id
        # apiName
        self.api_name = api_name
        # creationDateTime
        self.creation_date_time = creation_date_time
        # direction
        self.direction = direction
        # id
        self.id = id
        # policyAliasName
        self.policy_alias_name = policy_alias_name
        # policyContent
        self.policy_content = policy_content
        # policyGroup
        self.policy_group = policy_group
        # policyId
        self.policy_id = policy_id
        # policyName
        self.policy_name = policy_name
        # priority
        self.priority = priority
        # scope
        self.scope = scope
        # status
        self.status = status
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.policy_alias_name is not None:
            result['policyAliasName'] = self.policy_alias_name
        if self.policy_content is not None:
            result['policyContent'] = self.policy_content
        if self.policy_group is not None:
            result['policyGroup'] = self.policy_group
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.priority is not None:
            result['priority'] = self.priority
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('policyAliasName') is not None:
            self.policy_alias_name = m.get('policyAliasName')
        if m.get('policyContent') is not None:
            self.policy_content = m.get('policyContent')
        if m.get('policyGroup') is not None:
            self.policy_group = m.get('policyGroup')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyDataListPublishedGateway(TeaModel):
    def __init__(
        self,
        arms_info: str = None,
        auto_create_slb: bool = None,
        base_path: str = None,
        creation_date_time: str = None,
        edas_namespace_id: str = None,
        gateway_type: str = None,
        id: int = None,
        name: str = None,
        pod_cidr: str = None,
        region: str = None,
        region_name: str = None,
        replica: int = None,
        runtime_on: str = None,
        security_group: str = None,
        slb: str = None,
        slb_access_addr: str = None,
        status: str = None,
        vpc: str = None,
        vswitch: str = None,
    ):
        # armsInfo
        self.arms_info = arms_info
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id
        # gatewayType
        self.gateway_type = gateway_type
        # id
        self.id = id
        # name
        self.name = name
        # podCidr
        self.pod_cidr = pod_cidr
        # region
        self.region = region
        # regionName
        self.region_name = region_name
        # replica
        self.replica = replica
        # runtimeOn
        self.runtime_on = runtime_on
        # securityGroup
        self.security_group = security_group
        # slb
        self.slb = slb
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr
        # status
        self.status = status
        # vpc
        self.vpc = vpc
        # vswitch
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.arms_info is not None:
            result['armsInfo'] = self.arms_info
        if self.auto_create_slb is not None:
            result['autoCreateSlb'] = self.auto_create_slb
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.edas_namespace_id is not None:
            result['edasNamespaceId'] = self.edas_namespace_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.pod_cidr is not None:
            result['podCidr'] = self.pod_cidr
        if self.region is not None:
            result['region'] = self.region
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.replica is not None:
            result['replica'] = self.replica
        if self.runtime_on is not None:
            result['runtimeOn'] = self.runtime_on
        if self.security_group is not None:
            result['securityGroup'] = self.security_group
        if self.slb is not None:
            result['slb'] = self.slb
        if self.slb_access_addr is not None:
            result['slbAccessAddr'] = self.slb_access_addr
        if self.status is not None:
            result['status'] = self.status
        if self.vpc is not None:
            result['vpc'] = self.vpc
        if self.vswitch is not None:
            result['vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsInfo') is not None:
            self.arms_info = m.get('armsInfo')
        if m.get('autoCreateSlb') is not None:
            self.auto_create_slb = m.get('autoCreateSlb')
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('edasNamespaceId') is not None:
            self.edas_namespace_id = m.get('edasNamespaceId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('podCidr') is not None:
            self.pod_cidr = m.get('podCidr')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('runtimeOn') is not None:
            self.runtime_on = m.get('runtimeOn')
        if m.get('securityGroup') is not None:
            self.security_group = m.get('securityGroup')
        if m.get('slb') is not None:
            self.slb = m.get('slb')
        if m.get('slbAccessAddr') is not None:
            self.slb_access_addr = m.get('slbAccessAddr')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('vpc') is not None:
            self.vpc = m.get('vpc')
        if m.get('vswitch') is not None:
            self.vswitch = m.get('vswitch')
        return self


class FindApisByPagingResponseBodyDataList(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        attached_services: List[FindApisByPagingResponseBodyDataListAttachedServices] = None,
        base_path: str = None,
        creation_date_time: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        ownered_policies: List[FindApisByPagingResponseBodyDataListOwneredPolicies] = None,
        published_gateway: FindApisByPagingResponseBodyDataListPublishedGateway = None,
        status: str = None,
        update_date_time: str = None,
    ):
        # aliasName
        self.alias_name = alias_name
        # attachedServices
        self.attached_services = attached_services
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # id
        self.id = id
        # name
        self.name = name
        # owneredPolicies
        self.ownered_policies = ownered_policies
        # A short description of struct
        self.published_gateway = published_gateway
        # status
        self.status = status
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        if self.attached_services:
            for k in self.attached_services:
                if k:
                    k.validate()
        if self.ownered_policies:
            for k in self.ownered_policies:
                if k:
                    k.validate()
        if self.published_gateway:
            self.published_gateway.validate()

    def to_map(self):
        result = dict()
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        result['attachedServices'] = []
        if self.attached_services is not None:
            for k in self.attached_services:
                result['attachedServices'].append(k.to_map() if k else None)
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        result['owneredPolicies'] = []
        if self.ownered_policies is not None:
            for k in self.ownered_policies:
                result['owneredPolicies'].append(k.to_map() if k else None)
        if self.published_gateway is not None:
            result['publishedGateway'] = self.published_gateway.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        self.attached_services = []
        if m.get('attachedServices') is not None:
            for k in m.get('attachedServices'):
                temp_model = FindApisByPagingResponseBodyDataListAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.ownered_policies = []
        if m.get('owneredPolicies') is not None:
            for k in m.get('owneredPolicies'):
                temp_model = FindApisByPagingResponseBodyDataListOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        if m.get('publishedGateway') is not None:
            temp_model = FindApisByPagingResponseBodyDataListPublishedGateway()
            self.published_gateway = temp_model.from_map(m['publishedGateway'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[FindApisByPagingResponseBodyDataList] = None,
        total_count: int = None,
    ):
        # list
        self.list = list
        # totalCount
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = FindApisByPagingResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class FindApisByPagingResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FindApisByPagingResponseBodyData = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = FindApisByPagingResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindApisByPagingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindApisByPagingResponseBody = None,
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
            temp_model = FindApisByPagingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceEndsRequestServiceNodes(TeaModel):
    def __init__(
        self,
        port: str = None,
        ip_address: str = None,
        status: int = None,
    ):
        # port
        self.port = port
        # ipAddress
        self.ip_address = ip_address
        # status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateServiceEndsRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        service_nodes: List[UpdateServiceEndsRequestServiceNodes] = None,
    ):
        # id
        self.id = id
        # serviceNodes
        self.service_nodes = service_nodes

    def validate(self):
        if self.service_nodes:
            for k in self.service_nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        result['serviceNodes'] = []
        if self.service_nodes is not None:
            for k in self.service_nodes:
                result['serviceNodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        self.service_nodes = []
        if m.get('serviceNodes') is not None:
            for k in m.get('serviceNodes'):
                temp_model = UpdateServiceEndsRequestServiceNodes()
                self.service_nodes.append(temp_model.from_map(k))
        return self


class UpdateServiceEndsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateServiceEndsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceEndsResponseBody = None,
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
            temp_model = UpdateServiceEndsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindGatewaysRequest(TeaModel):
    def __init__(
        self,
        gateway_unique_id: str = None,
        name: str = None,
        region: str = None,
        gateway_types: str = None,
        status: str = None,
        page_number: str = None,
        page_size: str = None,
        namespace: str = None,
    ):
        # gatewayUniqueId
        self.gateway_unique_id = gateway_unique_id
        # name
        self.name = name
        # region
        self.region = region
        # gatewayTypes
        self.gateway_types = gateway_types
        # status
        self.status = status
        # pageNumber
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        # namespace
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gateway_unique_id is not None:
            result['gatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['name'] = self.name
        if self.region is not None:
            result['region'] = self.region
        if self.gateway_types is not None:
            result['gatewayTypes'] = self.gateway_types
        if self.status is not None:
            result['status'] = self.status
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('gatewayUniqueId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('gatewayTypes') is not None:
            self.gateway_types = m.get('gatewayTypes')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class FindGatewaysResponseBodyDataListArmsInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        description: str = None,
        license_key: str = None,
    ):
        # appId
        self.app_id = app_id
        # appName
        self.app_name = app_name
        # description
        self.description = description
        # licenseKey
        self.license_key = license_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.description is not None:
            result['description'] = self.description
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        return self


class FindGatewaysResponseBodyDataList(TeaModel):
    def __init__(
        self,
        arms_info: FindGatewaysResponseBodyDataListArmsInfo = None,
        auto_create_slb: bool = None,
        base_path: str = None,
        creation_date_time: str = None,
        edas_namespace_id: str = None,
        gateway_type: str = None,
        id: int = None,
        name: str = None,
        pod_cidr: str = None,
        region: str = None,
        region_name: str = None,
        replica: int = None,
        runtime_on: str = None,
        security_group: str = None,
        slb: str = None,
        slb_access_addr: str = None,
        status: str = None,
        vpc: str = None,
        vswitch: str = None,
    ):
        # armsInfo
        self.arms_info = arms_info
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb
        # basePath
        self.base_path = base_path
        # creationDateTime
        self.creation_date_time = creation_date_time
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id
        # gatewayType
        self.gateway_type = gateway_type
        # id
        self.id = id
        # name
        self.name = name
        # podCidr
        self.pod_cidr = pod_cidr
        # region
        self.region = region
        # regionName
        self.region_name = region_name
        # replica
        self.replica = replica
        # runtimeOn
        self.runtime_on = runtime_on
        # securityGroup
        self.security_group = security_group
        # slb
        self.slb = slb
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr
        # status
        self.status = status
        # vpc
        self.vpc = vpc
        # vswitch
        self.vswitch = vswitch

    def validate(self):
        if self.arms_info:
            self.arms_info.validate()

    def to_map(self):
        result = dict()
        if self.arms_info is not None:
            result['armsInfo'] = self.arms_info.to_map()
        if self.auto_create_slb is not None:
            result['autoCreateSlb'] = self.auto_create_slb
        if self.base_path is not None:
            result['basePath'] = self.base_path
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.edas_namespace_id is not None:
            result['edasNamespaceId'] = self.edas_namespace_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.pod_cidr is not None:
            result['podCidr'] = self.pod_cidr
        if self.region is not None:
            result['region'] = self.region
        if self.region_name is not None:
            result['regionName'] = self.region_name
        if self.replica is not None:
            result['replica'] = self.replica
        if self.runtime_on is not None:
            result['runtimeOn'] = self.runtime_on
        if self.security_group is not None:
            result['securityGroup'] = self.security_group
        if self.slb is not None:
            result['slb'] = self.slb
        if self.slb_access_addr is not None:
            result['slbAccessAddr'] = self.slb_access_addr
        if self.status is not None:
            result['status'] = self.status
        if self.vpc is not None:
            result['vpc'] = self.vpc
        if self.vswitch is not None:
            result['vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('armsInfo') is not None:
            temp_model = FindGatewaysResponseBodyDataListArmsInfo()
            self.arms_info = temp_model.from_map(m['armsInfo'])
        if m.get('autoCreateSlb') is not None:
            self.auto_create_slb = m.get('autoCreateSlb')
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('edasNamespaceId') is not None:
            self.edas_namespace_id = m.get('edasNamespaceId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('podCidr') is not None:
            self.pod_cidr = m.get('podCidr')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('runtimeOn') is not None:
            self.runtime_on = m.get('runtimeOn')
        if m.get('securityGroup') is not None:
            self.security_group = m.get('securityGroup')
        if m.get('slb') is not None:
            self.slb = m.get('slb')
        if m.get('slbAccessAddr') is not None:
            self.slb_access_addr = m.get('slbAccessAddr')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('vpc') is not None:
            self.vpc = m.get('vpc')
        if m.get('vswitch') is not None:
            self.vswitch = m.get('vswitch')
        return self


class FindGatewaysResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[FindGatewaysResponseBodyDataList] = None,
        total_count: int = None,
    ):
        # list
        self.list = list
        # totalCount
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = FindGatewaysResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class FindGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FindGatewaysResponseBodyData = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = FindGatewaysResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class FindGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindGatewaysResponseBody = None,
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
            temp_model = FindGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllRegistryRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        name: str = None,
        type: int = None,
        group_by: bool = None,
    ):
        # pageNumber
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        # name
        self.name = name
        # type
        self.type = type
        # groupBy
        self.group_by = group_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        return self


class GetAllRegistryResponseBodyDataList(TeaModel):
    def __init__(
        self,
        address: str = None,
        creation_date_time: str = None,
        description: str = None,
        gateway_id: str = None,
        id: int = None,
        name: str = None,
        type: int = None,
        update_date_time: str = None,
    ):
        # address
        self.address = address
        # creationDateTime
        self.creation_date_time = creation_date_time
        # description
        self.description = description
        # gatewayId
        self.gateway_id = gateway_id
        # id
        self.id = id
        # name
        self.name = name
        # type
        self.type = type
        # updateDateTime
        self.update_date_time = update_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.description is not None:
            result['description'] = self.description
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.update_date_time is not None:
            result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateDateTime') is not None:
            self.update_date_time = m.get('updateDateTime')
        return self


class GetAllRegistryResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetAllRegistryResponseBodyDataList] = None,
        total_count: int = None,
    ):
        # list
        self.list = list
        # totalCount
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetAllRegistryResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetAllRegistryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAllRegistryResponseBodyData = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetAllRegistryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAllRegistryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllRegistryResponseBody = None,
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
            temp_model = GetAllRegistryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullServiceInfoFromRegistryResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        meta_info: str = None,
        service_ends: List[str] = None,
        service_name: str = None,
    ):
        # id
        self.id = id
        # metaInfo
        self.meta_info = meta_info
        self.service_ends = service_ends
        # serviceName
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info
        if self.service_ends is not None:
            result['serviceEnds'] = self.service_ends
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('metaInfo') is not None:
            self.meta_info = m.get('metaInfo')
        if m.get('serviceEnds') is not None:
            self.service_ends = m.get('serviceEnds')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class PullServiceInfoFromRegistryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[PullServiceInfoFromRegistryResponseBodyData] = None,
        message: str = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # message
        self.message = message

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = PullServiceInfoFromRegistryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PullServiceInfoFromRegistryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PullServiceInfoFromRegistryResponseBody = None,
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
            temp_model = PullServiceInfoFromRegistryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


