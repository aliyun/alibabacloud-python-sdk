# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class FindAllServiceRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, name=None, alias_name=None, source_type=None,
                 is_health=None):
        # pageNumber
        self.page_number = page_number  # type: int
        # pageSize
        self.page_size = page_size      # type: str
        # name
        self.name = name                # type: str
        # aliasName
        self.alias_name = alias_name    # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # isHealth
        self.is_health = is_health      # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('pageNumber') is not None:
            self.page_number = map.get('pageNumber')
        if map.get('pageSize') is not None:
            self.page_size = map.get('pageSize')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        return self


class FindAllServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: FindAllServiceResponseBodyData
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindAllServiceResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindAllServiceResponseBodyDataListServiceEnds(TeaModel):
    def __init__(self, creation_date_time=None, id=None, ip_address=None, port=None, service_id=None, status=None,
                 update_date_time=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # ipAddress
        self.ip_address = ip_address    # type: str
        # port
        self.port = port                # type: str
        # serviceId
        self.service_id = service_id    # type: int
        # status
        self.status = status            # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('ipAddress') is not None:
            self.ip_address = map.get('ipAddress')
        if map.get('port') is not None:
            self.port = map.get('port')
        if map.get('serviceId') is not None:
            self.service_id = map.get('serviceId')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindAllServiceResponseBodyDataList(TeaModel):
    def __init__(self, alias_name=None, creation_date_time=None, description=None, id=None, is_auto_refresh=None,
                 is_health=None, name=None, registry_id=None, service_ends=None, service_name_in_registry=None,
                 source_type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # isHealth
        self.is_health = is_health      # type: bool
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: str
        # serviceEnds
        self.service_ends = service_ends  # type: List[FindAllServiceResponseBodyDataListServiceEnds]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = FindAllServiceResponseBodyDataListServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindAllServiceResponseBodyData(TeaModel):
    def __init__(self, list=None, total_count=None):
        # list
        self.list = list                # type: List[FindAllServiceResponseBodyDataList]
        # totalCount
        self.total_count = total_count  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindAllServiceResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if map.get('totalCount') is not None:
            self.total_count = map.get('totalCount')
        return self


class FindAllServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindAllServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindAllServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateApiRequest(TeaModel):
    def __init__(self, alias_name=None, attached_services=None, base_path=None, description=None, name=None,
                 status=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # attachedServices
        self.attached_services = attached_services  # type: List[int]
        # basePath
        self.base_path = base_path      # type: str
        # description
        self.description = description  # type: str
        # name
        self.name = name                # type: str
        # status
        self.status = status            # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('attachedServices') is not None:
            self.attached_services = map.get('attachedServices')
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class CreateApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreateApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetGatewayByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[GetGatewayByIdResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetGatewayByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class GetGatewayByIdResponseBodyDataArmsInfo(TeaModel):
    def __init__(self, app_id=None, app_name=None, description=None, license_key=None):
        # appId
        self.app_id = app_id            # type: str
        # appName
        self.app_name = app_name        # type: str
        # description
        self.description = description  # type: str
        # licenseKey
        self.license_key = license_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.description is not None:
            result['description'] = self.description
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        return result

    def from_map(self, map={}):
        if map.get('appId') is not None:
            self.app_id = map.get('appId')
        if map.get('appName') is not None:
            self.app_name = map.get('appName')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('licenseKey') is not None:
            self.license_key = map.get('licenseKey')
        return self


class GetGatewayByIdResponseBodyData(TeaModel):
    def __init__(self, arms_info=None, auto_create_slb=None, base_path=None, creation_date_time=None,
                 edas_namespace_id=None, gateway_type=None, id=None, name=None, pod_cidr=None, region=None, region_name=None,
                 replica=None, runtime_on=None, security_group=None, slb=None, slb_access_addr=None, status=None, vpc=None,
                 vswitch=None):
        # armsInfo
        self.arms_info = arms_info      # type: GetGatewayByIdResponseBodyDataArmsInfo
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb  # type: bool
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id  # type: str
        # gatewayType
        self.gateway_type = gateway_type  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # podCidr
        self.pod_cidr = pod_cidr        # type: str
        # region
        self.region = region            # type: str
        # regionName
        self.region_name = region_name  # type: str
        # replica
        self.replica = replica          # type: int
        # runtimeOn
        self.runtime_on = runtime_on    # type: str
        # securityGroup
        self.security_group = security_group  # type: str
        # slb
        self.slb = slb                  # type: str
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr  # type: str
        # status
        self.status = status            # type: str
        # vpc
        self.vpc = vpc                  # type: str
        # vswitch
        self.vswitch = vswitch          # type: str

    def validate(self):
        if self.arms_info:
            self.arms_info.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('armsInfo') is not None:
            temp_model = GetGatewayByIdResponseBodyDataArmsInfo()
            self.arms_info = temp_model.from_map(map['armsInfo'])
        if map.get('autoCreateSlb') is not None:
            self.auto_create_slb = map.get('autoCreateSlb')
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('edasNamespaceId') is not None:
            self.edas_namespace_id = map.get('edasNamespaceId')
        if map.get('gatewayType') is not None:
            self.gateway_type = map.get('gatewayType')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('podCidr') is not None:
            self.pod_cidr = map.get('podCidr')
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('regionName') is not None:
            self.region_name = map.get('regionName')
        if map.get('replica') is not None:
            self.replica = map.get('replica')
        if map.get('runtimeOn') is not None:
            self.runtime_on = map.get('runtimeOn')
        if map.get('securityGroup') is not None:
            self.security_group = map.get('securityGroup')
        if map.get('slb') is not None:
            self.slb = map.get('slb')
        if map.get('slbAccessAddr') is not None:
            self.slb_access_addr = map.get('slbAccessAddr')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('vpc') is not None:
            self.vpc = map.get('vpc')
        if map.get('vswitch') is not None:
            self.vswitch = map.get('vswitch')
        return self


class GetGatewayByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetGatewayByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetGatewayByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(self, alias_name=None, content=None, gateway_id=None, id=None, name=None, policy_group=None,
                 type=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # content
        self.content = content          # type: str
        # gatewayId
        self.gateway_id = gateway_id    # type: int
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # type
        self.type = type                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('content') is not None:
            self.content = map.get('content')
        if map.get('gatewayId') is not None:
            self.gateway_id = map.get('gatewayId')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreatePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetServiceInstanceForRegistryByServiceNameRequest(TeaModel):
    def __init__(self, service_name=None):
        # serviceName
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, map={}):
        if map.get('serviceName') is not None:
            self.service_name = map.get('serviceName')
        return self


class GetServiceInstanceForRegistryByServiceNameResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[GetServiceInstanceForRegistryByServiceNameResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetServiceInstanceForRegistryByServiceNameResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class GetServiceInstanceForRegistryByServiceNameResponseBodyData(TeaModel):
    def __init__(self, id=None, meta_info=None, service_ends=None, service_name=None):
        # id
        self.id = id                    # type: int
        # metaInfo
        self.meta_info = meta_info      # type: str
        self.service_ends = service_ends  # type: List[str]
        # serviceName
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.id is not None:
            result['id'] = self.id
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info
        if self.service_ends is not None:
            result['serviceEnds'] = self.service_ends
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, map={}):
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('metaInfo') is not None:
            self.meta_info = map.get('metaInfo')
        if map.get('serviceEnds') is not None:
            self.service_ends = map.get('serviceEnds')
        if map.get('serviceName') is not None:
            self.service_name = map.get('serviceName')
        return self


class GetServiceInstanceForRegistryByServiceNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetServiceInstanceForRegistryByServiceNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetServiceInstanceForRegistryByServiceNameResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateRegistryRequest(TeaModel):
    def __init__(self, address=None, description=None, gateway_id=None, id=None, name=None, type=None):
        # address
        self.address = address          # type: str
        # description
        self.description = description  # type: str
        # gatewayId
        self.gateway_id = gateway_id    # type: int
        # id
        self.id = id                    # type: str
        # name
        self.name = name                # type: str
        # type
        self.type = type                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('address') is not None:
            self.address = map.get('address')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('gatewayId') is not None:
            self.gateway_id = map.get('gatewayId')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class UpdateRegistryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class UpdateRegistryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateRegistryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateGatewayRequest(TeaModel):
    def __init__(self, auto_create_slb=None, base_path=None, edas_namespace_id=None, gateway_type=None, name=None,
                 pod_cidr=None, region=None, region_name=None, replica=None, runtime_on=None, security_group=None, slb=None,
                 slb_spec=None, vpc=None, vswitch=None, zone=None):
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb  # type: bool
        # basePath
        self.base_path = base_path      # type: str
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id  # type: str
        # gatewayType
        self.gateway_type = gateway_type  # type: str
        # name
        self.name = name                # type: str
        # podCidr
        self.pod_cidr = pod_cidr        # type: str
        # region
        self.region = region            # type: str
        # regionName
        self.region_name = region_name  # type: str
        # replica
        self.replica = replica          # type: int
        # runtimeOn
        self.runtime_on = runtime_on    # type: str
        # securityGroup
        self.security_group = security_group  # type: str
        # slb
        self.slb = slb                  # type: str
        # slbSpec
        self.slb_spec = slb_spec        # type: str
        # vpc
        self.vpc = vpc                  # type: str
        # vswitch
        self.vswitch = vswitch          # type: str
        # zone
        self.zone = zone                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('autoCreateSlb') is not None:
            self.auto_create_slb = map.get('autoCreateSlb')
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('edasNamespaceId') is not None:
            self.edas_namespace_id = map.get('edasNamespaceId')
        if map.get('gatewayType') is not None:
            self.gateway_type = map.get('gatewayType')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('podCidr') is not None:
            self.pod_cidr = map.get('podCidr')
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('regionName') is not None:
            self.region_name = map.get('regionName')
        if map.get('replica') is not None:
            self.replica = map.get('replica')
        if map.get('runtimeOn') is not None:
            self.runtime_on = map.get('runtimeOn')
        if map.get('securityGroup') is not None:
            self.security_group = map.get('securityGroup')
        if map.get('slb') is not None:
            self.slb = map.get('slb')
        if map.get('slbSpec') is not None:
            self.slb_spec = map.get('slbSpec')
        if map.get('vpc') is not None:
            self.vpc = map.get('vpc')
        if map.get('vswitch') is not None:
            self.vswitch = map.get('vswitch')
        if map.get('zone') is not None:
            self.zone = map.get('zone')
        return self


class CreateGatewayResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreateGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateGatewayResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CheckServiceHealthRequest(TeaModel):
    def __init__(self, id=None, operation_ids=None):
        # id
        self.id = id                    # type: int
        # operationIds
        self.operation_ids = operation_ids  # type: List[int]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.id is not None:
            result['id'] = self.id
        if self.operation_ids is not None:
            result['operationIds'] = self.operation_ids
        return result

    def from_map(self, map={}):
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('operationIds') is not None:
            self.operation_ids = map.get('operationIds')
        return self


class CheckServiceHealthResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[CheckServiceHealthResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = CheckServiceHealthResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CheckServiceHealthResponseBodyDataServiceEnds(TeaModel):
    def __init__(self, creation_date_time=None, id=None, ip_address=None, port=None, service_id=None, status=None,
                 update_date_time=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # ipAddress
        self.ip_address = ip_address    # type: str
        # port
        self.port = port                # type: str
        # serviceId
        self.service_id = service_id    # type: int
        # status
        self.status = status            # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('ipAddress') is not None:
            self.ip_address = map.get('ipAddress')
        if map.get('port') is not None:
            self.port = map.get('port')
        if map.get('serviceId') is not None:
            self.service_id = map.get('serviceId')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class CheckServiceHealthResponseBodyData(TeaModel):
    def __init__(self, alias_name=None, creation_date_time=None, description=None, id=None, is_auto_refresh=None,
                 is_health=None, name=None, registry_id=None, service_ends=None, service_name_in_registry=None,
                 source_type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # isHealth
        self.is_health = is_health      # type: bool
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: str
        # serviceEnds
        self.service_ends = service_ends  # type: List[CheckServiceHealthResponseBodyDataServiceEnds]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = CheckServiceHealthResponseBodyDataServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class CheckServiceHealthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CheckServiceHealthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CheckServiceHealthResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreatePolicyToApiRequest(TeaModel):
    def __init__(self, creation_date_time=None, direction=None, policy_alias_name=None, policy_content=None,
                 policy_group=None, policy_id=None, policy_name=None, priority=None, scope=None, status=None, type=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: int
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class CreatePolicyToApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreatePolicyToApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreatePolicyToApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreatePolicyToApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DetachPolicyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class DetachPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DetachPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class FindTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindTemplateResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class ValidateRegistryAddressRequest(TeaModel):
    def __init__(self, address=None, type=None):
        # address
        self.address = address          # type: str
        # type
        self.type = type                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.address is not None:
            result['address'] = self.address
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('address') is not None:
            self.address = map.get('address')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class ValidateRegistryAddressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class ValidateRegistryAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ValidateRegistryAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ValidateRegistryAddressResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetApiDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[GetApiDetailResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetApiDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class GetApiDetailResponseBodyDataAttachedServicesServiceEnds(TeaModel):
    def __init__(self, creation_date_time=None, id=None, ip_address=None, port=None, service_id=None, status=None,
                 update_date_time=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # ipAddress
        self.ip_address = ip_address    # type: str
        # port
        self.port = port                # type: str
        # serviceId
        self.service_id = service_id    # type: int
        # status
        self.status = status            # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('ipAddress') is not None:
            self.ip_address = map.get('ipAddress')
        if map.get('port') is not None:
            self.port = map.get('port')
        if map.get('serviceId') is not None:
            self.service_id = map.get('serviceId')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class GetApiDetailResponseBodyDataAttachedServices(TeaModel):
    def __init__(self, alias_name=None, creation_date_time=None, description=None, id=None, is_auto_refresh=None,
                 is_health=None, name=None, registry_id=None, service_ends=None, service_name_in_registry=None,
                 source_type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # isHealth
        self.is_health = is_health      # type: bool
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: str
        # serviceEnds
        self.service_ends = service_ends  # type: List[GetApiDetailResponseBodyDataAttachedServicesServiceEnds]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = GetApiDetailResponseBodyDataAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class GetApiDetailResponseBodyDataOwneredPolicies(TeaModel):
    def __init__(self, api_id=None, api_name=None, creation_date_time=None, direction=None, id=None,
                 policy_alias_name=None, policy_content=None, policy_group=None, policy_id=None, policy_name=None, priority=None,
                 scope=None, status=None, type=None, update_date_time=None):
        # apiId
        self.api_id = api_id            # type: int
        # apiName
        self.api_name = api_name        # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # id
        self.id = id                    # type: int
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: str
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('apiId') is not None:
            self.api_id = map.get('apiId')
        if map.get('apiName') is not None:
            self.api_name = map.get('apiName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class GetApiDetailResponseBodyDataPublishedGateway(TeaModel):
    def __init__(self, arms_info=None, auto_create_slb=None, base_path=None, creation_date_time=None,
                 edas_namespace_id=None, gateway_type=None, id=None, name=None, pod_cidr=None, region=None, region_name=None,
                 replica=None, runtime_on=None, security_group=None, slb=None, slb_access_addr=None, status=None, vpc=None,
                 vswitch=None):
        # armsInfo
        self.arms_info = arms_info      # type: str
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb  # type: bool
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id  # type: str
        # gatewayType
        self.gateway_type = gateway_type  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # podCidr
        self.pod_cidr = pod_cidr        # type: str
        # region
        self.region = region            # type: str
        # regionName
        self.region_name = region_name  # type: str
        # replica
        self.replica = replica          # type: int
        # runtimeOn
        self.runtime_on = runtime_on    # type: str
        # securityGroup
        self.security_group = security_group  # type: str
        # slb
        self.slb = slb                  # type: str
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr  # type: str
        # status
        self.status = status            # type: str
        # vpc
        self.vpc = vpc                  # type: str
        # vswitch
        self.vswitch = vswitch          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('armsInfo') is not None:
            self.arms_info = map.get('armsInfo')
        if map.get('autoCreateSlb') is not None:
            self.auto_create_slb = map.get('autoCreateSlb')
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('edasNamespaceId') is not None:
            self.edas_namespace_id = map.get('edasNamespaceId')
        if map.get('gatewayType') is not None:
            self.gateway_type = map.get('gatewayType')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('podCidr') is not None:
            self.pod_cidr = map.get('podCidr')
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('regionName') is not None:
            self.region_name = map.get('regionName')
        if map.get('replica') is not None:
            self.replica = map.get('replica')
        if map.get('runtimeOn') is not None:
            self.runtime_on = map.get('runtimeOn')
        if map.get('securityGroup') is not None:
            self.security_group = map.get('securityGroup')
        if map.get('slb') is not None:
            self.slb = map.get('slb')
        if map.get('slbAccessAddr') is not None:
            self.slb_access_addr = map.get('slbAccessAddr')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('vpc') is not None:
            self.vpc = map.get('vpc')
        if map.get('vswitch') is not None:
            self.vswitch = map.get('vswitch')
        return self


class GetApiDetailResponseBodyData(TeaModel):
    def __init__(self, alias_name=None, attached_services=None, base_path=None, creation_date_time=None,
                 description=None, id=None, name=None, ownered_policies=None, published_gateway=None, status=None,
                 update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # attachedServices
        self.attached_services = attached_services  # type: List[GetApiDetailResponseBodyDataAttachedServices]
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # owneredPolicies
        self.ownered_policies = ownered_policies  # type: List[GetApiDetailResponseBodyDataOwneredPolicies]
        # A short description of struct
        self.published_gateway = published_gateway  # type: GetApiDetailResponseBodyDataPublishedGateway
        # status
        self.status = status            # type: str
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        self.attached_services = []
        if map.get('attachedServices') is not None:
            for k in map.get('attachedServices'):
                temp_model = GetApiDetailResponseBodyDataAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        self.ownered_policies = []
        if map.get('owneredPolicies') is not None:
            for k in map.get('owneredPolicies'):
                temp_model = GetApiDetailResponseBodyDataOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        if map.get('publishedGateway') is not None:
            temp_model = GetApiDetailResponseBodyDataPublishedGateway()
            self.published_gateway = temp_model.from_map(map['publishedGateway'])
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class GetApiDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetApiDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetApiDetailResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateSpecialRouteForRegistryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreateSpecialRouteForRegistryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateSpecialRouteForRegistryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateSpecialRouteForRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class PublishApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class PublishApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: PublishApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = PublishApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateGatewayLogEtlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreateGatewayLogEtlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateGatewayLogEtlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateGatewayLogEtlResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class FindPoliciesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, name=None, alias_name=None, type=None, group=None):
        # pageNumber
        self.page_number = page_number  # type: int
        # pageSize
        self.page_size = page_size      # type: int
        # name
        self.name = name                # type: str
        # aliasName
        self.alias_name = alias_name    # type: str
        # type
        self.type = type                # type: int
        # group
        self.group = group              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('pageNumber') is not None:
            self.page_number = map.get('pageNumber')
        if map.get('pageSize') is not None:
            self.page_size = map.get('pageSize')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('group') is not None:
            self.group = map.get('group')
        return self


class FindPoliciesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: FindPoliciesResponseBodyData
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindPoliciesResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindPoliciesResponseBodyDataListAttachedApi(TeaModel):
    def __init__(self, api_id=None, api_name=None, creation_date_time=None, direction=None, id=None,
                 policy_alias_name=None, policy_content=None, policy_group=None, policy_id=None, policy_name=None, priority=None,
                 scope=None, status=None, type=None, update_date_time=None):
        # apiId
        self.api_id = api_id            # type: int
        # apiName
        self.api_name = api_name        # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # id
        self.id = id                    # type: int
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: str
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('apiId') is not None:
            self.api_id = map.get('apiId')
        if map.get('apiName') is not None:
            self.api_name = map.get('apiName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindPoliciesResponseBodyDataList(TeaModel):
    def __init__(self, alias_name=None, attached_api=None, content=None, creation_date_time=None, id=None, name=None,
                 policy_group=None, policy_type_name=None, type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # attachedApi
        self.attached_api = attached_api  # type: List[FindPoliciesResponseBodyDataListAttachedApi]
        # content
        self.content = content          # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyTypeName
        self.policy_type_name = policy_type_name  # type: str
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.attached_api:
            for k in self.attached_api:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        self.attached_api = []
        if map.get('attachedApi') is not None:
            for k in map.get('attachedApi'):
                temp_model = FindPoliciesResponseBodyDataListAttachedApi()
                self.attached_api.append(temp_model.from_map(k))
        if map.get('content') is not None:
            self.content = map.get('content')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyTypeName') is not None:
            self.policy_type_name = map.get('policyTypeName')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindPoliciesResponseBodyData(TeaModel):
    def __init__(self, list=None, total_count=None):
        # list
        self.list = list                # type: List[FindPoliciesResponseBodyDataList]
        # totalCount
        self.total_count = total_count  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindPoliciesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if map.get('totalCount') is not None:
            self.total_count = map.get('totalCount')
        return self


class FindPoliciesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindPoliciesResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class AttachPolicyRequest(TeaModel):
    def __init__(self, data=None):
        # data
        self.data = data                # type: List[AttachPolicyRequestData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = AttachPolicyRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class AttachPolicyRequestData(TeaModel):
    def __init__(self, creation_date_time=None, direction=None, policy_alias_name=None, policy_content=None,
                 policy_group=None, policy_id=None, policy_name=None, priority=None, scope=None, status=None, type=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: int
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class AttachPolicyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class AttachPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AttachPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class FindRegistryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[FindRegistryResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = FindRegistryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindRegistryResponseBodyData(TeaModel):
    def __init__(self, address=None, creation_date_time=None, description=None, gateway_id=None, id=None, name=None,
                 type=None, update_date_time=None):
        # address
        self.address = address          # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # gatewayId
        self.gateway_id = gateway_id    # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('address') is not None:
            self.address = map.get('address')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('gatewayId') is not None:
            self.gateway_id = map.get('gatewayId')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindRegistryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindRegistryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetAuthTicketByIdHeaders(TeaModel):
    def __init__(self, common_headers=None, cookie=None):
        self.common_headers = common_headers  # type: Dict[str, str]
        # cookie
        self.cookie = cookie            # type: Dict[str, Any]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.cookie is not None:
            result['cookie'] = self.cookie
        return result

    def from_map(self, map={}):
        if map.get('commonHeaders') is not None:
            self.common_headers = map.get('commonHeaders')
        if map.get('cookie') is not None:
            self.cookie = map.get('cookie')
        return self


class GetAuthTicketByIdShrinkHeaders(TeaModel):
    def __init__(self, common_headers=None, cookie_shrink=None):
        self.common_headers = common_headers  # type: Dict[str, str]
        # cookie
        self.cookie_shrink = cookie_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.cookie_shrink is not None:
            result['cookie'] = self.cookie_shrink
        return result

    def from_map(self, map={}):
        if map.get('commonHeaders') is not None:
            self.common_headers = map.get('commonHeaders')
        if map.get('cookie') is not None:
            self.cookie_shrink = map.get('cookie')
        return self


class GetAuthTicketByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[GetAuthTicketByIdResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetAuthTicketByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class GetAuthTicketByIdResponseBodyData(TeaModel):
    def __init__(self, client_token=None, comment=None, id=None, name=None, server_key=None, ticket_type=None,
                 valid_end_time=None, valid_start_time=None):
        # clientToken
        self.client_token = client_token  # type: str
        # comment
        self.comment = comment          # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # serverKey
        self.server_key = server_key    # type: str
        # ticketType
        self.ticket_type = ticket_type  # type: str
        # validEndTime
        self.valid_end_time = valid_end_time  # type: str
        # validStartTime
        self.valid_start_time = valid_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('clientToken') is not None:
            self.client_token = map.get('clientToken')
        if map.get('comment') is not None:
            self.comment = map.get('comment')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('serverKey') is not None:
            self.server_key = map.get('serverKey')
        if map.get('ticketType') is not None:
            self.ticket_type = map.get('ticketType')
        if map.get('validEndTime') is not None:
            self.valid_end_time = map.get('validEndTime')
        if map.get('validStartTime') is not None:
            self.valid_start_time = map.get('validStartTime')
        return self


class GetAuthTicketByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetAuthTicketByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAuthTicketByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateRegistryRequest(TeaModel):
    def __init__(self, address=None, description=None, gateway_id=None, id=None, name=None, type=None):
        # address
        self.address = address          # type: str
        # description
        self.description = description  # type: str
        # gatewayId
        self.gateway_id = gateway_id    # type: int
        # id
        self.id = id                    # type: str
        # name
        self.name = name                # type: str
        # type
        self.type = type                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('address') is not None:
            self.address = map.get('address')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('gatewayId') is not None:
            self.gateway_id = map.get('gatewayId')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class CreateRegistryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreateRegistryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateRegistryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class RecycleApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class RecycleApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: RecycleApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = RecycleApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateAuthTicketRequest(TeaModel):
    def __init__(self, comment=None, gateway_id=None, name=None, ticket_type=None, valid_duration=None):
        # comment
        self.comment = comment          # type: str
        # gatewayId
        self.gateway_id = gateway_id    # type: int
        # name
        self.name = name                # type: str
        # ticketType
        self.ticket_type = ticket_type  # type: str
        self.valid_duration = valid_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.comment is not None:
            result['comment'] = self.comment
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.ticket_type is not None:
            result['ticketType'] = self.ticket_type
        if self.valid_duration is not None:
            result['validDuration'] = self.valid_duration
        return result

    def from_map(self, map={}):
        if map.get('comment') is not None:
            self.comment = map.get('comment')
        if map.get('gatewayId') is not None:
            self.gateway_id = map.get('gatewayId')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('ticketType') is not None:
            self.ticket_type = map.get('ticketType')
        if map.get('validDuration') is not None:
            self.valid_duration = map.get('validDuration')
        return self


class CreateAuthTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreateAuthTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateAuthTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateAuthTicketResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeleteGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class FindServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[FindServiceResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = FindServiceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindServiceResponseBodyDataServiceEnds(TeaModel):
    def __init__(self, creation_date_time=None, id=None, ip_address=None, port=None, service_id=None, status=None,
                 update_date_time=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # ipAddress
        self.ip_address = ip_address    # type: str
        # port
        self.port = port                # type: str
        # serviceId
        self.service_id = service_id    # type: int
        # status
        self.status = status            # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('ipAddress') is not None:
            self.ip_address = map.get('ipAddress')
        if map.get('port') is not None:
            self.port = map.get('port')
        if map.get('serviceId') is not None:
            self.service_id = map.get('serviceId')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindServiceResponseBodyData(TeaModel):
    def __init__(self, alias_name=None, creation_date_time=None, description=None, id=None, is_auto_refresh=None,
                 is_health=None, name=None, registry_id=None, service_ends=None, service_name_in_registry=None,
                 source_type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # isHealth
        self.is_health = is_health      # type: bool
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: str
        # serviceEnds
        self.service_ends = service_ends  # type: List[FindServiceResponseBodyDataServiceEnds]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = FindServiceResponseBodyDataServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeletePolicyByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class DeletePolicyByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeletePolicyByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeletePolicyByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class DeleteApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeleteApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class FindAuthTicketsRequest(TeaModel):
    def __init__(self, gateway_id=None, name=None, page_number=None, page_size=None):
        # gatewayId
        self.gateway_id = gateway_id    # type: int
        # name
        self.name = name                # type: str
        # pageNumber
        self.page_number = page_number  # type: int
        # pageSize
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        if map.get('gatewayId') is not None:
            self.gateway_id = map.get('gatewayId')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('pageNumber') is not None:
            self.page_number = map.get('pageNumber')
        if map.get('pageSize') is not None:
            self.page_size = map.get('pageSize')
        return self


class FindAuthTicketsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: FindAuthTicketsResponseBodyData
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindAuthTicketsResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindAuthTicketsResponseBodyDataList(TeaModel):
    def __init__(self, client_token=None, comment=None, id=None, name=None, server_key=None, ticket_type=None,
                 valid_end_time=None, valid_start_time=None):
        # clientToken
        self.client_token = client_token  # type: str
        # comment
        self.comment = comment          # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # serverKey
        self.server_key = server_key    # type: str
        # ticketType
        self.ticket_type = ticket_type  # type: str
        # validEndTime
        self.valid_end_time = valid_end_time  # type: str
        # validStartTime
        self.valid_start_time = valid_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('clientToken') is not None:
            self.client_token = map.get('clientToken')
        if map.get('comment') is not None:
            self.comment = map.get('comment')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('serverKey') is not None:
            self.server_key = map.get('serverKey')
        if map.get('ticketType') is not None:
            self.ticket_type = map.get('ticketType')
        if map.get('validEndTime') is not None:
            self.valid_end_time = map.get('validEndTime')
        if map.get('validStartTime') is not None:
            self.valid_start_time = map.get('validStartTime')
        return self


class FindAuthTicketsResponseBodyData(TeaModel):
    def __init__(self, list=None, total_count=None):
        # list
        self.list = list                # type: List[FindAuthTicketsResponseBodyDataList]
        # totalCount
        self.total_count = total_count  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindAuthTicketsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if map.get('totalCount') is not None:
            self.total_count = map.get('totalCount')
        return self


class FindAuthTicketsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindAuthTicketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindAuthTicketsResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdatePolicyRequest(TeaModel):
    def __init__(self, alias_name=None, content=None, id=None, name=None, policy_group=None, type=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # content
        self.content = content          # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # type
        self.type = type                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('content') is not None:
            self.content = map.get('content')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class UpdatePolicyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class UpdatePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdatePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdatePolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateAuthTicketRequest(TeaModel):
    def __init__(self, comment=None, id=None):
        # comment
        self.comment = comment          # type: str
        # id
        self.id = id                    # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.comment is not None:
            result['comment'] = self.comment
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, map={}):
        if map.get('comment') is not None:
            self.comment = map.get('comment')
        if map.get('id') is not None:
            self.id = map.get('id')
        return self


class UpdateAuthTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class UpdateAuthTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateAuthTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateAuthTicketResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class InstallArmsAgentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class InstallArmsAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: InstallArmsAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = InstallArmsAgentResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteAuthTicketResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class DeleteAuthTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeleteAuthTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteAuthTicketResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetPolicyByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[GetPolicyByIdResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetPolicyByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class GetPolicyByIdResponseBodyDataAttachedApi(TeaModel):
    def __init__(self, api_id=None, api_name=None, creation_date_time=None, direction=None, id=None,
                 policy_alias_name=None, policy_content=None, policy_group=None, policy_id=None, policy_name=None, priority=None,
                 scope=None, status=None, type=None, update_date_time=None):
        # apiId
        self.api_id = api_id            # type: int
        # apiName
        self.api_name = api_name        # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # id
        self.id = id                    # type: int
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: str
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('apiId') is not None:
            self.api_id = map.get('apiId')
        if map.get('apiName') is not None:
            self.api_name = map.get('apiName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class GetPolicyByIdResponseBodyData(TeaModel):
    def __init__(self, alias_name=None, attached_api=None, content=None, creation_date_time=None, id=None, name=None,
                 policy_group=None, policy_type_name=None, type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # attachedApi
        self.attached_api = attached_api  # type: List[GetPolicyByIdResponseBodyDataAttachedApi]
        # content
        self.content = content          # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyTypeName
        self.policy_type_name = policy_type_name  # type: str
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.attached_api:
            for k in self.attached_api:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        self.attached_api = []
        if map.get('attachedApi') is not None:
            for k in map.get('attachedApi'):
                temp_model = GetPolicyByIdResponseBodyDataAttachedApi()
                self.attached_api.append(temp_model.from_map(k))
        if map.get('content') is not None:
            self.content = map.get('content')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyTypeName') is not None:
            self.policy_type_name = map.get('policyTypeName')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class GetPolicyByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetPolicyByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetPolicyByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteRegistryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class DeleteRegistryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeleteRegistryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetPolicyOwnedByApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, DataValue]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for v in self.data.values():
                if v:
                    v.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                result['data'][k] = v.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = {}
        if map.get('data') is not None:
            for k, v in map.get('data').items():
                temp_model = DataValue()
                self.data[k] = temp_model.from_map(v)
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class GetPolicyOwnedByApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetPolicyOwnedByApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetPolicyOwnedByApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateApiRequest(TeaModel):
    def __init__(self, alias_name=None, attached_services=None, base_path=None, creation_date_time=None,
                 description=None, id=None, name=None, ownered_policies=None, published_gateway=None, status=None,
                 update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # attachedServices
        self.attached_services = attached_services  # type: List[UpdateApiRequestAttachedServices]
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # owneredPolicies
        self.ownered_policies = ownered_policies  # type: List[UpdateApiRequestOwneredPolicies]
        # A short description of struct
        self.published_gateway = published_gateway  # type: UpdateApiRequestPublishedGateway
        # status
        self.status = status            # type: str
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        self.attached_services = []
        if map.get('attachedServices') is not None:
            for k in map.get('attachedServices'):
                temp_model = UpdateApiRequestAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        self.ownered_policies = []
        if map.get('owneredPolicies') is not None:
            for k in map.get('owneredPolicies'):
                temp_model = UpdateApiRequestOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        if map.get('publishedGateway') is not None:
            temp_model = UpdateApiRequestPublishedGateway()
            self.published_gateway = temp_model.from_map(map['publishedGateway'])
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class UpdateApiRequestAttachedServicesServiceEnds(TeaModel):
    def __init__(self, creation_date_time=None, id=None, ip_address=None, port=None, service_id=None, status=None,
                 update_date_time=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # ipAddress
        self.ip_address = ip_address    # type: str
        # port
        self.port = port                # type: str
        # serviceId
        self.service_id = service_id    # type: int
        # status
        self.status = status            # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('ipAddress') is not None:
            self.ip_address = map.get('ipAddress')
        if map.get('port') is not None:
            self.port = map.get('port')
        if map.get('serviceId') is not None:
            self.service_id = map.get('serviceId')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class UpdateApiRequestAttachedServices(TeaModel):
    def __init__(self, alias_name=None, creation_date_time=None, description=None, id=None, is_auto_refresh=None,
                 is_health=None, name=None, registry_id=None, service_ends=None, service_name_in_registry=None,
                 source_type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # isHealth
        self.is_health = is_health      # type: bool
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: str
        # serviceEnds
        self.service_ends = service_ends  # type: List[UpdateApiRequestAttachedServicesServiceEnds]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = UpdateApiRequestAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class UpdateApiRequestOwneredPolicies(TeaModel):
    def __init__(self, api_id=None, api_name=None, creation_date_time=None, direction=None, id=None,
                 policy_alias_name=None, policy_content=None, policy_group=None, policy_id=None, policy_name=None, priority=None,
                 scope=None, status=None, type=None, update_date_time=None):
        # apiId
        self.api_id = api_id            # type: int
        # apiName
        self.api_name = api_name        # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # id
        self.id = id                    # type: int
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: str
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('apiId') is not None:
            self.api_id = map.get('apiId')
        if map.get('apiName') is not None:
            self.api_name = map.get('apiName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class UpdateApiRequestPublishedGateway(TeaModel):
    def __init__(self, arms_info=None, auto_create_slb=None, base_path=None, creation_date_time=None,
                 edas_namespace_id=None, gateway_type=None, id=None, name=None, pod_cidr=None, region=None, region_name=None,
                 replica=None, runtime_on=None, security_group=None, slb=None, slb_access_addr=None, status=None, vpc=None,
                 vswitch=None):
        # armsInfo
        self.arms_info = arms_info      # type: str
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb  # type: bool
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id  # type: str
        # gatewayType
        self.gateway_type = gateway_type  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # podCidr
        self.pod_cidr = pod_cidr        # type: str
        # region
        self.region = region            # type: str
        # regionName
        self.region_name = region_name  # type: str
        # replica
        self.replica = replica          # type: int
        # runtimeOn
        self.runtime_on = runtime_on    # type: str
        # securityGroup
        self.security_group = security_group  # type: str
        # slb
        self.slb = slb                  # type: str
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr  # type: str
        # status
        self.status = status            # type: str
        # vpc
        self.vpc = vpc                  # type: str
        # vswitch
        self.vswitch = vswitch          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('armsInfo') is not None:
            self.arms_info = map.get('armsInfo')
        if map.get('autoCreateSlb') is not None:
            self.auto_create_slb = map.get('autoCreateSlb')
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('edasNamespaceId') is not None:
            self.edas_namespace_id = map.get('edasNamespaceId')
        if map.get('gatewayType') is not None:
            self.gateway_type = map.get('gatewayType')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('podCidr') is not None:
            self.pod_cidr = map.get('podCidr')
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('regionName') is not None:
            self.region_name = map.get('regionName')
        if map.get('replica') is not None:
            self.replica = map.get('replica')
        if map.get('runtimeOn') is not None:
            self.runtime_on = map.get('runtimeOn')
        if map.get('securityGroup') is not None:
            self.security_group = map.get('securityGroup')
        if map.get('slb') is not None:
            self.slb = map.get('slb')
        if map.get('slbAccessAddr') is not None:
            self.slb_access_addr = map.get('slbAccessAddr')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('vpc') is not None:
            self.vpc = map.get('vpc')
        if map.get('vswitch') is not None:
            self.vswitch = map.get('vswitch')
        return self


class UpdateApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class UpdateApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, alias_name=None, description=None, is_auto_refresh=None, meta_info=None, name=None,
                 registry_id=None, service_ends=None, service_name_in_registry=None, source_type=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # description
        self.description = description  # type: str
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # metaInfo
        self.meta_info = meta_info      # type: List[str]
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: int
        # serviceEnds
        self.service_ends = service_ends  # type: List[str]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('metaInfo') is not None:
            self.meta_info = map.get('metaInfo')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        if map.get('serviceEnds') is not None:
            self.service_ends = map.get('serviceEnds')
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class SaveAllPoliciesRequest(TeaModel):
    def __init__(self, data=None):
        # data
        self.data = data                # type: List[SaveAllPoliciesRequestData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = SaveAllPoliciesRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class SaveAllPoliciesRequestData(TeaModel):
    def __init__(self, api_id=None, api_name=None, creation_date_time=None, direction=None, id=None,
                 policy_alias_name=None, policy_content=None, policy_group=None, policy_id=None, policy_name=None, priority=None,
                 scope=None, status=None, type=None, update_date_time=None):
        # apiId
        self.api_id = api_id            # type: int
        # apiName
        self.api_name = api_name        # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # id
        self.id = id                    # type: int
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: str
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('apiId') is not None:
            self.api_id = map.get('apiId')
        if map.get('apiName') is not None:
            self.api_name = map.get('apiName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class SaveAllPoliciesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class SaveAllPoliciesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: SaveAllPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = SaveAllPoliciesResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateGatewayRequest(TeaModel):
    def __init__(self, id=None, replica=None):
        # id
        self.id = id                    # type: int
        # replica
        self.replica = replica          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.id is not None:
            result['id'] = self.id
        if self.replica is not None:
            result['replica'] = self.replica
        return result

    def from_map(self, map={}):
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('replica') is not None:
            self.replica = map.get('replica')
        return self


class UpdateGatewayResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class UpdateGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateGatewayResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(self, alias_name=None, creation_date_time=None, description=None, id=None, is_auto_refresh=None,
                 is_health=None, name=None, registry_id=None, service_ends=None, service_name_in_registry=None,
                 source_type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # isHealth
        self.is_health = is_health      # type: bool
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: int
        # serviceEnds
        self.service_ends = service_ends  # type: List[str]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        if map.get('serviceEnds') is not None:
            self.service_ends = map.get('serviceEnds')
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class FindApisByPagingRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, status=None, name=None, alias_name=None):
        # pageNumber
        self.page_number = page_number  # type: int
        # pageSize
        self.page_size = page_size      # type: int
        # status
        self.status = status            # type: str
        # name
        self.name = name                # type: str
        # aliasName
        self.alias_name = alias_name    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('pageNumber') is not None:
            self.page_number = map.get('pageNumber')
        if map.get('pageSize') is not None:
            self.page_size = map.get('pageSize')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        return self


class FindApisByPagingResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: FindApisByPagingResponseBodyData
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindApisByPagingResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindApisByPagingResponseBodyDataListAttachedServicesServiceEnds(TeaModel):
    def __init__(self, creation_date_time=None, id=None, ip_address=None, port=None, service_id=None, status=None,
                 update_date_time=None):
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # id
        self.id = id                    # type: int
        # ipAddress
        self.ip_address = ip_address    # type: str
        # port
        self.port = port                # type: str
        # serviceId
        self.service_id = service_id    # type: int
        # status
        self.status = status            # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('ipAddress') is not None:
            self.ip_address = map.get('ipAddress')
        if map.get('port') is not None:
            self.port = map.get('port')
        if map.get('serviceId') is not None:
            self.service_id = map.get('serviceId')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyDataListAttachedServices(TeaModel):
    def __init__(self, alias_name=None, creation_date_time=None, description=None, id=None, is_auto_refresh=None,
                 is_health=None, name=None, registry_id=None, service_ends=None, service_name_in_registry=None,
                 source_type=None, update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # isAutoRefresh
        self.is_auto_refresh = is_auto_refresh  # type: bool
        # isHealth
        self.is_health = is_health      # type: bool
        # name
        self.name = name                # type: str
        # registryId
        self.registry_id = registry_id  # type: str
        # serviceEnds
        self.service_ends = service_ends  # type: List[FindApisByPagingResponseBodyDataListAttachedServicesServiceEnds]
        # serviceNameInRegistry
        self.service_name_in_registry = service_name_in_registry  # type: str
        # sourceType
        self.source_type = source_type  # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        if self.service_ends:
            for k in self.service_ends:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('isAutoRefresh') is not None:
            self.is_auto_refresh = map.get('isAutoRefresh')
        if map.get('isHealth') is not None:
            self.is_health = map.get('isHealth')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('registryId') is not None:
            self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = FindApisByPagingResponseBodyDataListAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        if map.get('serviceNameInRegistry') is not None:
            self.service_name_in_registry = map.get('serviceNameInRegistry')
        if map.get('sourceType') is not None:
            self.source_type = map.get('sourceType')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyDataListOwneredPolicies(TeaModel):
    def __init__(self, api_id=None, api_name=None, creation_date_time=None, direction=None, id=None,
                 policy_alias_name=None, policy_content=None, policy_group=None, policy_id=None, policy_name=None, priority=None,
                 scope=None, status=None, type=None, update_date_time=None):
        # apiId
        self.api_id = api_id            # type: int
        # apiName
        self.api_name = api_name        # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # id
        self.id = id                    # type: int
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: str
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('apiId') is not None:
            self.api_id = map.get('apiId')
        if map.get('apiName') is not None:
            self.api_name = map.get('apiName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyDataListPublishedGateway(TeaModel):
    def __init__(self, arms_info=None, auto_create_slb=None, base_path=None, creation_date_time=None,
                 edas_namespace_id=None, gateway_type=None, id=None, name=None, pod_cidr=None, region=None, region_name=None,
                 replica=None, runtime_on=None, security_group=None, slb=None, slb_access_addr=None, status=None, vpc=None,
                 vswitch=None):
        # armsInfo
        self.arms_info = arms_info      # type: str
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb  # type: bool
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id  # type: str
        # gatewayType
        self.gateway_type = gateway_type  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # podCidr
        self.pod_cidr = pod_cidr        # type: str
        # region
        self.region = region            # type: str
        # regionName
        self.region_name = region_name  # type: str
        # replica
        self.replica = replica          # type: int
        # runtimeOn
        self.runtime_on = runtime_on    # type: str
        # securityGroup
        self.security_group = security_group  # type: str
        # slb
        self.slb = slb                  # type: str
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr  # type: str
        # status
        self.status = status            # type: str
        # vpc
        self.vpc = vpc                  # type: str
        # vswitch
        self.vswitch = vswitch          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('armsInfo') is not None:
            self.arms_info = map.get('armsInfo')
        if map.get('autoCreateSlb') is not None:
            self.auto_create_slb = map.get('autoCreateSlb')
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('edasNamespaceId') is not None:
            self.edas_namespace_id = map.get('edasNamespaceId')
        if map.get('gatewayType') is not None:
            self.gateway_type = map.get('gatewayType')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('podCidr') is not None:
            self.pod_cidr = map.get('podCidr')
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('regionName') is not None:
            self.region_name = map.get('regionName')
        if map.get('replica') is not None:
            self.replica = map.get('replica')
        if map.get('runtimeOn') is not None:
            self.runtime_on = map.get('runtimeOn')
        if map.get('securityGroup') is not None:
            self.security_group = map.get('securityGroup')
        if map.get('slb') is not None:
            self.slb = map.get('slb')
        if map.get('slbAccessAddr') is not None:
            self.slb_access_addr = map.get('slbAccessAddr')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('vpc') is not None:
            self.vpc = map.get('vpc')
        if map.get('vswitch') is not None:
            self.vswitch = map.get('vswitch')
        return self


class FindApisByPagingResponseBodyDataList(TeaModel):
    def __init__(self, alias_name=None, attached_services=None, base_path=None, creation_date_time=None,
                 description=None, id=None, name=None, ownered_policies=None, published_gateway=None, status=None,
                 update_date_time=None):
        # aliasName
        self.alias_name = alias_name    # type: str
        # attachedServices
        self.attached_services = attached_services  # type: List[FindApisByPagingResponseBodyDataListAttachedServices]
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # owneredPolicies
        self.ownered_policies = ownered_policies  # type: List[FindApisByPagingResponseBodyDataListOwneredPolicies]
        # A short description of struct
        self.published_gateway = published_gateway  # type: FindApisByPagingResponseBodyDataListPublishedGateway
        # status
        self.status = status            # type: str
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('aliasName') is not None:
            self.alias_name = map.get('aliasName')
        self.attached_services = []
        if map.get('attachedServices') is not None:
            for k in map.get('attachedServices'):
                temp_model = FindApisByPagingResponseBodyDataListAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        self.ownered_policies = []
        if map.get('owneredPolicies') is not None:
            for k in map.get('owneredPolicies'):
                temp_model = FindApisByPagingResponseBodyDataListOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        if map.get('publishedGateway') is not None:
            temp_model = FindApisByPagingResponseBodyDataListPublishedGateway()
            self.published_gateway = temp_model.from_map(map['publishedGateway'])
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class FindApisByPagingResponseBodyData(TeaModel):
    def __init__(self, list=None, total_count=None):
        # list
        self.list = list                # type: List[FindApisByPagingResponseBodyDataList]
        # totalCount
        self.total_count = total_count  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindApisByPagingResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if map.get('totalCount') is not None:
            self.total_count = map.get('totalCount')
        return self


class FindApisByPagingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindApisByPagingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindApisByPagingResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpdateServiceEndsRequest(TeaModel):
    def __init__(self, id=None, service_nodes=None):
        # id
        self.id = id                    # type: int
        # serviceNodes
        self.service_nodes = service_nodes  # type: List[UpdateServiceEndsRequestServiceNodes]

    def validate(self):
        if self.service_nodes:
            for k in self.service_nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.id is not None:
            result['id'] = self.id
        result['serviceNodes'] = []
        if self.service_nodes is not None:
            for k in self.service_nodes:
                result['serviceNodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('id') is not None:
            self.id = map.get('id')
        self.service_nodes = []
        if map.get('serviceNodes') is not None:
            for k in map.get('serviceNodes'):
                temp_model = UpdateServiceEndsRequestServiceNodes()
                self.service_nodes.append(temp_model.from_map(k))
        return self


class UpdateServiceEndsRequestServiceNodes(TeaModel):
    def __init__(self, port=None, ip_address=None, status=None):
        # port
        self.port = port                # type: str
        # ipAddress
        self.ip_address = ip_address    # type: str
        # status
        self.status = status            # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.port is not None:
            result['port'] = self.port
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('port') is not None:
            self.port = map.get('port')
        if map.get('ipAddress') is not None:
            self.ip_address = map.get('ipAddress')
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class UpdateServiceEndsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: Dict[str, Any]
        # message
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class UpdateServiceEndsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: UpdateServiceEndsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateServiceEndsResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class FindGatewaysRequest(TeaModel):
    def __init__(self, gateway_unique_id=None, name=None, region=None, gateway_types=None, status=None,
                 page_number=None, page_size=None, namespace=None):
        # gatewayUniqueId
        self.gateway_unique_id = gateway_unique_id  # type: str
        # name
        self.name = name                # type: str
        # region
        self.region = region            # type: str
        # gatewayTypes
        self.gateway_types = gateway_types  # type: str
        # status
        self.status = status            # type: str
        # pageNumber
        self.page_number = page_number  # type: str
        # pageSize
        self.page_size = page_size      # type: str
        # namespace
        self.namespace = namespace      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('gatewayUniqueId') is not None:
            self.gateway_unique_id = map.get('gatewayUniqueId')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('gatewayTypes') is not None:
            self.gateway_types = map.get('gatewayTypes')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('pageNumber') is not None:
            self.page_number = map.get('pageNumber')
        if map.get('pageSize') is not None:
            self.page_size = map.get('pageSize')
        if map.get('namespace') is not None:
            self.namespace = map.get('namespace')
        return self


class FindGatewaysResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: FindGatewaysResponseBodyData
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindGatewaysResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class FindGatewaysResponseBodyDataListArmsInfo(TeaModel):
    def __init__(self, app_id=None, app_name=None, description=None, license_key=None):
        # appId
        self.app_id = app_id            # type: str
        # appName
        self.app_name = app_name        # type: str
        # description
        self.description = description  # type: str
        # licenseKey
        self.license_key = license_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.description is not None:
            result['description'] = self.description
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        return result

    def from_map(self, map={}):
        if map.get('appId') is not None:
            self.app_id = map.get('appId')
        if map.get('appName') is not None:
            self.app_name = map.get('appName')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('licenseKey') is not None:
            self.license_key = map.get('licenseKey')
        return self


class FindGatewaysResponseBodyDataList(TeaModel):
    def __init__(self, arms_info=None, auto_create_slb=None, base_path=None, creation_date_time=None,
                 edas_namespace_id=None, gateway_type=None, id=None, name=None, pod_cidr=None, region=None, region_name=None,
                 replica=None, runtime_on=None, security_group=None, slb=None, slb_access_addr=None, status=None, vpc=None,
                 vswitch=None):
        # armsInfo
        self.arms_info = arms_info      # type: FindGatewaysResponseBodyDataListArmsInfo
        # autoCreateSlb
        self.auto_create_slb = auto_create_slb  # type: bool
        # basePath
        self.base_path = base_path      # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # edasNamespaceId
        self.edas_namespace_id = edas_namespace_id  # type: str
        # gatewayType
        self.gateway_type = gateway_type  # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # podCidr
        self.pod_cidr = pod_cidr        # type: str
        # region
        self.region = region            # type: str
        # regionName
        self.region_name = region_name  # type: str
        # replica
        self.replica = replica          # type: int
        # runtimeOn
        self.runtime_on = runtime_on    # type: str
        # securityGroup
        self.security_group = security_group  # type: str
        # slb
        self.slb = slb                  # type: str
        # slbAccessAddr
        self.slb_access_addr = slb_access_addr  # type: str
        # status
        self.status = status            # type: str
        # vpc
        self.vpc = vpc                  # type: str
        # vswitch
        self.vswitch = vswitch          # type: str

    def validate(self):
        if self.arms_info:
            self.arms_info.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('armsInfo') is not None:
            temp_model = FindGatewaysResponseBodyDataListArmsInfo()
            self.arms_info = temp_model.from_map(map['armsInfo'])
        if map.get('autoCreateSlb') is not None:
            self.auto_create_slb = map.get('autoCreateSlb')
        if map.get('basePath') is not None:
            self.base_path = map.get('basePath')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('edasNamespaceId') is not None:
            self.edas_namespace_id = map.get('edasNamespaceId')
        if map.get('gatewayType') is not None:
            self.gateway_type = map.get('gatewayType')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('podCidr') is not None:
            self.pod_cidr = map.get('podCidr')
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('regionName') is not None:
            self.region_name = map.get('regionName')
        if map.get('replica') is not None:
            self.replica = map.get('replica')
        if map.get('runtimeOn') is not None:
            self.runtime_on = map.get('runtimeOn')
        if map.get('securityGroup') is not None:
            self.security_group = map.get('securityGroup')
        if map.get('slb') is not None:
            self.slb = map.get('slb')
        if map.get('slbAccessAddr') is not None:
            self.slb_access_addr = map.get('slbAccessAddr')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('vpc') is not None:
            self.vpc = map.get('vpc')
        if map.get('vswitch') is not None:
            self.vswitch = map.get('vswitch')
        return self


class FindGatewaysResponseBodyData(TeaModel):
    def __init__(self, list=None, total_count=None):
        # list
        self.list = list                # type: List[FindGatewaysResponseBodyDataList]
        # totalCount
        self.total_count = total_count  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindGatewaysResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if map.get('totalCount') is not None:
            self.total_count = map.get('totalCount')
        return self


class FindGatewaysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: FindGatewaysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindGatewaysResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetAllRegistryRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, name=None, type=None, group_by=None):
        # pageNumber
        self.page_number = page_number  # type: int
        # pageSize
        self.page_size = page_size      # type: int
        # name
        self.name = name                # type: str
        # type
        self.type = type                # type: int
        # groupBy
        self.group_by = group_by        # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('pageNumber') is not None:
            self.page_number = map.get('pageNumber')
        if map.get('pageSize') is not None:
            self.page_size = map.get('pageSize')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('groupBy') is not None:
            self.group_by = map.get('groupBy')
        return self


class GetAllRegistryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: GetAllRegistryResponseBodyData
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = GetAllRegistryResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class GetAllRegistryResponseBodyDataList(TeaModel):
    def __init__(self, address=None, creation_date_time=None, description=None, gateway_id=None, id=None, name=None,
                 type=None, update_date_time=None):
        # address
        self.address = address          # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # description
        self.description = description  # type: str
        # gatewayId
        self.gateway_id = gateway_id    # type: str
        # id
        self.id = id                    # type: int
        # name
        self.name = name                # type: str
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('address') is not None:
            self.address = map.get('address')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('gatewayId') is not None:
            self.gateway_id = map.get('gatewayId')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self


class GetAllRegistryResponseBodyData(TeaModel):
    def __init__(self, list=None, total_count=None):
        # list
        self.list = list                # type: List[GetAllRegistryResponseBodyDataList]
        # totalCount
        self.total_count = total_count  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = GetAllRegistryResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if map.get('totalCount') is not None:
            self.total_count = map.get('totalCount')
        return self


class GetAllRegistryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetAllRegistryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAllRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class PullServiceInfoFromRegistryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        # code
        self.code = code                # type: int
        # data
        self.data = data                # type: List[PullServiceInfoFromRegistryResponseBodyData]
        # message
        self.message = message          # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = PullServiceInfoFromRegistryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if map.get('message') is not None:
            self.message = map.get('message')
        return self


class PullServiceInfoFromRegistryResponseBodyData(TeaModel):
    def __init__(self, id=None, meta_info=None, service_ends=None, service_name=None):
        # id
        self.id = id                    # type: int
        # metaInfo
        self.meta_info = meta_info      # type: str
        self.service_ends = service_ends  # type: List[str]
        # serviceName
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.id is not None:
            result['id'] = self.id
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info
        if self.service_ends is not None:
            result['serviceEnds'] = self.service_ends
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, map={}):
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('metaInfo') is not None:
            self.meta_info = map.get('metaInfo')
        if map.get('serviceEnds') is not None:
            self.service_ends = map.get('serviceEnds')
        if map.get('serviceName') is not None:
            self.service_name = map.get('serviceName')
        return self


class PullServiceInfoFromRegistryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: PullServiceInfoFromRegistryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = PullServiceInfoFromRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DataValue(TeaModel):
    def __init__(self, api_id=None, api_name=None, creation_date_time=None, direction=None, id=None,
                 policy_alias_name=None, policy_content=None, policy_group=None, policy_id=None, policy_name=None, priority=None,
                 scope=None, status=None, type=None, update_date_time=None):
        # apiId
        self.api_id = api_id            # type: int
        # apiName
        self.api_name = api_name        # type: str
        # creationDateTime
        self.creation_date_time = creation_date_time  # type: str
        # direction
        self.direction = direction      # type: str
        # id
        self.id = id                    # type: int
        # policyAliasName
        self.policy_alias_name = policy_alias_name  # type: str
        # policyContent
        self.policy_content = policy_content  # type: str
        # policyGroup
        self.policy_group = policy_group  # type: str
        # policyId
        self.policy_id = policy_id      # type: str
        # policyName
        self.policy_name = policy_name  # type: str
        # priority
        self.priority = priority        # type: int
        # scope
        self.scope = scope              # type: str
        # status
        self.status = status            # type: bool
        # type
        self.type = type                # type: int
        # updateDateTime
        self.update_date_time = update_date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('apiId') is not None:
            self.api_id = map.get('apiId')
        if map.get('apiName') is not None:
            self.api_name = map.get('apiName')
        if map.get('creationDateTime') is not None:
            self.creation_date_time = map.get('creationDateTime')
        if map.get('direction') is not None:
            self.direction = map.get('direction')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('policyAliasName') is not None:
            self.policy_alias_name = map.get('policyAliasName')
        if map.get('policyContent') is not None:
            self.policy_content = map.get('policyContent')
        if map.get('policyGroup') is not None:
            self.policy_group = map.get('policyGroup')
        if map.get('policyId') is not None:
            self.policy_id = map.get('policyId')
        if map.get('policyName') is not None:
            self.policy_name = map.get('policyName')
        if map.get('priority') is not None:
            self.priority = map.get('priority')
        if map.get('scope') is not None:
            self.scope = map.get('scope')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updateDateTime') is not None:
            self.update_date_time = map.get('updateDateTime')
        return self
