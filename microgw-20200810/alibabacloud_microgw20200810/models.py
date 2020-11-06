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
        result['pageNumber'] = self.page_number
        result['pageSize'] = self.page_size
        result['name'] = self.name
        result['aliasName'] = self.alias_name
        result['sourceType'] = self.source_type
        result['isHealth'] = self.is_health
        return result

    def from_map(self, map={}):
        self.page_number = map.get('pageNumber')
        self.page_size = map.get('pageSize')
        self.name = map.get('name')
        self.alias_name = map.get('aliasName')
        self.source_type = map.get('sourceType')
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
        result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindAllServiceResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        else:
            self.data = None
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
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['ipAddress'] = self.ip_address
        result['port'] = self.port
        result['serviceId'] = self.service_id
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.ip_address = map.get('ipAddress')
        self.port = map.get('port')
        self.service_id = map.get('serviceId')
        self.status = map.get('status')
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
        result['aliasName'] = self.alias_name
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['isAutoRefresh'] = self.is_auto_refresh
        result['isHealth'] = self.is_health
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        else:
            result['serviceEnds'] = None
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.is_health = map.get('isHealth')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = FindAllServiceResponseBodyDataListServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        else:
            self.service_ends = None
        self.service_name_in_registry = map.get('serviceNameInRegistry')
        self.source_type = map.get('sourceType')
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
        else:
            result['list'] = None
        result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindAllServiceResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindAllServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['aliasName'] = self.alias_name
        result['attachedServices'] = self.attached_services
        result['basePath'] = self.base_path
        result['description'] = self.description
        result['name'] = self.name
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.attached_services = map.get('attachedServices')
        self.base_path = map.get('basePath')
        self.description = map.get('description')
        self.name = map.get('name')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetGatewayByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['appId'] = self.app_id
        result['appName'] = self.app_name
        result['description'] = self.description
        result['licenseKey'] = self.license_key
        return result

    def from_map(self, map={}):
        self.app_id = map.get('appId')
        self.app_name = map.get('appName')
        self.description = map.get('description')
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
        else:
            result['armsInfo'] = None
        result['autoCreateSlb'] = self.auto_create_slb
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['edasNamespaceId'] = self.edas_namespace_id
        result['gatewayType'] = self.gateway_type
        result['id'] = self.id
        result['name'] = self.name
        result['podCidr'] = self.pod_cidr
        result['region'] = self.region
        result['regionName'] = self.region_name
        result['replica'] = self.replica
        result['runtimeOn'] = self.runtime_on
        result['securityGroup'] = self.security_group
        result['slb'] = self.slb
        result['slbAccessAddr'] = self.slb_access_addr
        result['status'] = self.status
        result['vpc'] = self.vpc
        result['vswitch'] = self.vswitch
        return result

    def from_map(self, map={}):
        if map.get('armsInfo') is not None:
            temp_model = GetGatewayByIdResponseBodyDataArmsInfo()
            self.arms_info = temp_model.from_map(map['armsInfo'])
        else:
            self.arms_info = None
        self.auto_create_slb = map.get('autoCreateSlb')
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.edas_namespace_id = map.get('edasNamespaceId')
        self.gateway_type = map.get('gatewayType')
        self.id = map.get('id')
        self.name = map.get('name')
        self.pod_cidr = map.get('podCidr')
        self.region = map.get('region')
        self.region_name = map.get('regionName')
        self.replica = map.get('replica')
        self.runtime_on = map.get('runtimeOn')
        self.security_group = map.get('securityGroup')
        self.slb = map.get('slb')
        self.slb_access_addr = map.get('slbAccessAddr')
        self.status = map.get('status')
        self.vpc = map.get('vpc')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetGatewayByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['aliasName'] = self.alias_name
        result['content'] = self.content
        result['gatewayId'] = self.gateway_id
        result['id'] = self.id
        result['name'] = self.name
        result['policyGroup'] = self.policy_group
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.content = map.get('content')
        self.gateway_id = map.get('gatewayId')
        self.id = map.get('id')
        self.name = map.get('name')
        self.policy_group = map.get('policyGroup')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetServiceInstanceForRegistryByServiceNameRequest(TeaModel):
    def __init__(self, service_name=None):
        # serviceName
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['serviceName'] = self.service_name
        return result

    def from_map(self, map={}):
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetServiceInstanceForRegistryByServiceNameResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['id'] = self.id
        result['metaInfo'] = self.meta_info
        result['serviceEnds'] = self.service_ends
        result['serviceName'] = self.service_name
        return result

    def from_map(self, map={}):
        self.id = map.get('id')
        self.meta_info = map.get('metaInfo')
        self.service_ends = map.get('serviceEnds')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetServiceInstanceForRegistryByServiceNameResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['address'] = self.address
        result['description'] = self.description
        result['gatewayId'] = self.gateway_id
        result['id'] = self.id
        result['name'] = self.name
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.address = map.get('address')
        self.description = map.get('description')
        self.gateway_id = map.get('gatewayId')
        self.id = map.get('id')
        self.name = map.get('name')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['autoCreateSlb'] = self.auto_create_slb
        result['basePath'] = self.base_path
        result['edasNamespaceId'] = self.edas_namespace_id
        result['gatewayType'] = self.gateway_type
        result['name'] = self.name
        result['podCidr'] = self.pod_cidr
        result['region'] = self.region
        result['regionName'] = self.region_name
        result['replica'] = self.replica
        result['runtimeOn'] = self.runtime_on
        result['securityGroup'] = self.security_group
        result['slb'] = self.slb
        result['slbSpec'] = self.slb_spec
        result['vpc'] = self.vpc
        result['vswitch'] = self.vswitch
        result['zone'] = self.zone
        return result

    def from_map(self, map={}):
        self.auto_create_slb = map.get('autoCreateSlb')
        self.base_path = map.get('basePath')
        self.edas_namespace_id = map.get('edasNamespaceId')
        self.gateway_type = map.get('gatewayType')
        self.name = map.get('name')
        self.pod_cidr = map.get('podCidr')
        self.region = map.get('region')
        self.region_name = map.get('regionName')
        self.replica = map.get('replica')
        self.runtime_on = map.get('runtimeOn')
        self.security_group = map.get('securityGroup')
        self.slb = map.get('slb')
        self.slb_spec = map.get('slbSpec')
        self.vpc = map.get('vpc')
        self.vswitch = map.get('vswitch')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateGatewayResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['id'] = self.id
        result['operationIds'] = self.operation_ids
        return result

    def from_map(self, map={}):
        self.id = map.get('id')
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = CheckServiceHealthResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['ipAddress'] = self.ip_address
        result['port'] = self.port
        result['serviceId'] = self.service_id
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.ip_address = map.get('ipAddress')
        self.port = map.get('port')
        self.service_id = map.get('serviceId')
        self.status = map.get('status')
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
        result['aliasName'] = self.alias_name
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['isAutoRefresh'] = self.is_auto_refresh
        result['isHealth'] = self.is_health
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        else:
            result['serviceEnds'] = None
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.is_health = map.get('isHealth')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = CheckServiceHealthResponseBodyDataServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        else:
            self.service_ends = None
        self.service_name_in_registry = map.get('serviceNameInRegistry')
        self.source_type = map.get('sourceType')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CheckServiceHealthResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreatePolicyToApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindTemplateResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['address'] = self.address
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.address = map.get('address')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ValidateRegistryAddressResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetApiDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['ipAddress'] = self.ip_address
        result['port'] = self.port
        result['serviceId'] = self.service_id
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.ip_address = map.get('ipAddress')
        self.port = map.get('port')
        self.service_id = map.get('serviceId')
        self.status = map.get('status')
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
        result['aliasName'] = self.alias_name
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['isAutoRefresh'] = self.is_auto_refresh
        result['isHealth'] = self.is_health
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        else:
            result['serviceEnds'] = None
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.is_health = map.get('isHealth')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = GetApiDetailResponseBodyDataAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        else:
            self.service_ends = None
        self.service_name_in_registry = map.get('serviceNameInRegistry')
        self.source_type = map.get('sourceType')
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
        result['apiId'] = self.api_id
        result['apiName'] = self.api_name
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['id'] = self.id
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.api_id = map.get('apiId')
        self.api_name = map.get('apiName')
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.id = map.get('id')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
        self.type = map.get('type')
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
        result['armsInfo'] = self.arms_info
        result['autoCreateSlb'] = self.auto_create_slb
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['edasNamespaceId'] = self.edas_namespace_id
        result['gatewayType'] = self.gateway_type
        result['id'] = self.id
        result['name'] = self.name
        result['podCidr'] = self.pod_cidr
        result['region'] = self.region
        result['regionName'] = self.region_name
        result['replica'] = self.replica
        result['runtimeOn'] = self.runtime_on
        result['securityGroup'] = self.security_group
        result['slb'] = self.slb
        result['slbAccessAddr'] = self.slb_access_addr
        result['status'] = self.status
        result['vpc'] = self.vpc
        result['vswitch'] = self.vswitch
        return result

    def from_map(self, map={}):
        self.arms_info = map.get('armsInfo')
        self.auto_create_slb = map.get('autoCreateSlb')
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.edas_namespace_id = map.get('edasNamespaceId')
        self.gateway_type = map.get('gatewayType')
        self.id = map.get('id')
        self.name = map.get('name')
        self.pod_cidr = map.get('podCidr')
        self.region = map.get('region')
        self.region_name = map.get('regionName')
        self.replica = map.get('replica')
        self.runtime_on = map.get('runtimeOn')
        self.security_group = map.get('securityGroup')
        self.slb = map.get('slb')
        self.slb_access_addr = map.get('slbAccessAddr')
        self.status = map.get('status')
        self.vpc = map.get('vpc')
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
        result['aliasName'] = self.alias_name
        result['attachedServices'] = []
        if self.attached_services is not None:
            for k in self.attached_services:
                result['attachedServices'].append(k.to_map() if k else None)
        else:
            result['attachedServices'] = None
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['name'] = self.name
        result['owneredPolicies'] = []
        if self.ownered_policies is not None:
            for k in self.ownered_policies:
                result['owneredPolicies'].append(k.to_map() if k else None)
        else:
            result['owneredPolicies'] = None
        if self.published_gateway is not None:
            result['publishedGateway'] = self.published_gateway.to_map()
        else:
            result['publishedGateway'] = None
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.attached_services = []
        if map.get('attachedServices') is not None:
            for k in map.get('attachedServices'):
                temp_model = GetApiDetailResponseBodyDataAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        else:
            self.attached_services = None
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.name = map.get('name')
        self.ownered_policies = []
        if map.get('owneredPolicies') is not None:
            for k in map.get('owneredPolicies'):
                temp_model = GetApiDetailResponseBodyDataOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        else:
            self.ownered_policies = None
        if map.get('publishedGateway') is not None:
            temp_model = GetApiDetailResponseBodyDataPublishedGateway()
            self.published_gateway = temp_model.from_map(map['publishedGateway'])
        else:
            self.published_gateway = None
        self.status = map.get('status')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetApiDetailResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateSpecialRouteForRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = PublishApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateGatewayLogEtlResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['pageNumber'] = self.page_number
        result['pageSize'] = self.page_size
        result['name'] = self.name
        result['aliasName'] = self.alias_name
        result['type'] = self.type
        result['group'] = self.group
        return result

    def from_map(self, map={}):
        self.page_number = map.get('pageNumber')
        self.page_size = map.get('pageSize')
        self.name = map.get('name')
        self.alias_name = map.get('aliasName')
        self.type = map.get('type')
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
        result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindPoliciesResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        else:
            self.data = None
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
        result['apiId'] = self.api_id
        result['apiName'] = self.api_name
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['id'] = self.id
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.api_id = map.get('apiId')
        self.api_name = map.get('apiName')
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.id = map.get('id')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
        self.type = map.get('type')
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
        result['aliasName'] = self.alias_name
        result['attachedApi'] = []
        if self.attached_api is not None:
            for k in self.attached_api:
                result['attachedApi'].append(k.to_map() if k else None)
        else:
            result['attachedApi'] = None
        result['content'] = self.content
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['name'] = self.name
        result['policyGroup'] = self.policy_group
        result['policyTypeName'] = self.policy_type_name
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.attached_api = []
        if map.get('attachedApi') is not None:
            for k in map.get('attachedApi'):
                temp_model = FindPoliciesResponseBodyDataListAttachedApi()
                self.attached_api.append(temp_model.from_map(k))
        else:
            self.attached_api = None
        self.content = map.get('content')
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.name = map.get('name')
        self.policy_group = map.get('policyGroup')
        self.policy_type_name = map.get('policyTypeName')
        self.type = map.get('type')
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
        else:
            result['list'] = None
        result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindPoliciesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindPoliciesResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        else:
            result['data'] = None
        return result

    def from_map(self, map={}):
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = AttachPolicyRequestData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = FindRegistryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['address'] = self.address
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['gatewayId'] = self.gateway_id
        result['id'] = self.id
        result['name'] = self.name
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.address = map.get('address')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.gateway_id = map.get('gatewayId')
        self.id = map.get('id')
        self.name = map.get('name')
        self.type = map.get('type')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetAuthTicketByIdHeaders(TeaModel):
    def __init__(self, cookie=None):
        # cookie
        self.cookie = cookie            # type: Dict[str, Any]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cookie'] = self.cookie
        return result

    def from_map(self, map={}):
        self.cookie = map.get('cookie')
        return self


class GetAuthTicketByIdShrinkHeaders(TeaModel):
    def __init__(self, cookie_shrink=None):
        # cookie
        self.cookie_shrink = cookie_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cookie'] = self.cookie_shrink
        return result

    def from_map(self, map={}):
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetAuthTicketByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['clientToken'] = self.client_token
        result['comment'] = self.comment
        result['id'] = self.id
        result['name'] = self.name
        result['serverKey'] = self.server_key
        result['ticketType'] = self.ticket_type
        result['validEndTime'] = self.valid_end_time
        result['validStartTime'] = self.valid_start_time
        return result

    def from_map(self, map={}):
        self.client_token = map.get('clientToken')
        self.comment = map.get('comment')
        self.id = map.get('id')
        self.name = map.get('name')
        self.server_key = map.get('serverKey')
        self.ticket_type = map.get('ticketType')
        self.valid_end_time = map.get('validEndTime')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAuthTicketByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['address'] = self.address
        result['description'] = self.description
        result['gatewayId'] = self.gateway_id
        result['id'] = self.id
        result['name'] = self.name
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.address = map.get('address')
        self.description = map.get('description')
        self.gateway_id = map.get('gatewayId')
        self.id = map.get('id')
        self.name = map.get('name')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = RecycleApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['comment'] = self.comment
        result['gatewayId'] = self.gateway_id
        result['name'] = self.name
        result['ticketType'] = self.ticket_type
        result['validDuration'] = self.valid_duration
        return result

    def from_map(self, map={}):
        self.comment = map.get('comment')
        self.gateway_id = map.get('gatewayId')
        self.name = map.get('name')
        self.ticket_type = map.get('ticketType')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateAuthTicketResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = FindServiceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['ipAddress'] = self.ip_address
        result['port'] = self.port
        result['serviceId'] = self.service_id
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.ip_address = map.get('ipAddress')
        self.port = map.get('port')
        self.service_id = map.get('serviceId')
        self.status = map.get('status')
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
        result['aliasName'] = self.alias_name
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['isAutoRefresh'] = self.is_auto_refresh
        result['isHealth'] = self.is_health
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        else:
            result['serviceEnds'] = None
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.is_health = map.get('isHealth')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = FindServiceResponseBodyDataServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        else:
            self.service_ends = None
        self.service_name_in_registry = map.get('serviceNameInRegistry')
        self.source_type = map.get('sourceType')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeletePolicyByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['gatewayId'] = self.gateway_id
        result['name'] = self.name
        result['pageNumber'] = self.page_number
        result['pageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.gateway_id = map.get('gatewayId')
        self.name = map.get('name')
        self.page_number = map.get('pageNumber')
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
        result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindAuthTicketsResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        else:
            self.data = None
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
        result['clientToken'] = self.client_token
        result['comment'] = self.comment
        result['id'] = self.id
        result['name'] = self.name
        result['serverKey'] = self.server_key
        result['ticketType'] = self.ticket_type
        result['validEndTime'] = self.valid_end_time
        result['validStartTime'] = self.valid_start_time
        return result

    def from_map(self, map={}):
        self.client_token = map.get('clientToken')
        self.comment = map.get('comment')
        self.id = map.get('id')
        self.name = map.get('name')
        self.server_key = map.get('serverKey')
        self.ticket_type = map.get('ticketType')
        self.valid_end_time = map.get('validEndTime')
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
        else:
            result['list'] = None
        result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindAuthTicketsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindAuthTicketsResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['aliasName'] = self.alias_name
        result['content'] = self.content
        result['id'] = self.id
        result['name'] = self.name
        result['policyGroup'] = self.policy_group
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.content = map.get('content')
        self.id = map.get('id')
        self.name = map.get('name')
        self.policy_group = map.get('policyGroup')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdatePolicyResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['comment'] = self.comment
        result['id'] = self.id
        return result

    def from_map(self, map={}):
        self.comment = map.get('comment')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateAuthTicketResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = InstallArmsAgentResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteAuthTicketResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = GetPolicyByIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['apiId'] = self.api_id
        result['apiName'] = self.api_name
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['id'] = self.id
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.api_id = map.get('apiId')
        self.api_name = map.get('apiName')
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.id = map.get('id')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
        self.type = map.get('type')
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
        result['aliasName'] = self.alias_name
        result['attachedApi'] = []
        if self.attached_api is not None:
            for k in self.attached_api:
                result['attachedApi'].append(k.to_map() if k else None)
        else:
            result['attachedApi'] = None
        result['content'] = self.content
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['name'] = self.name
        result['policyGroup'] = self.policy_group
        result['policyTypeName'] = self.policy_type_name
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.attached_api = []
        if map.get('attachedApi') is not None:
            for k in map.get('attachedApi'):
                temp_model = GetPolicyByIdResponseBodyDataAttachedApi()
                self.attached_api.append(temp_model.from_map(k))
        else:
            self.attached_api = None
        self.content = map.get('content')
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.name = map.get('name')
        self.policy_group = map.get('policyGroup')
        self.policy_type_name = map.get('policyTypeName')
        self.type = map.get('type')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetPolicyByIdResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                result['data'][k] = v.to_map()
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = {}
        if map.get('data') is not None:
            for k, v in map.get('data').items():
                temp_model = DataValue()
                self.data[k] = temp_model.from_map(v)
        else:
            self.data = None
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetPolicyOwnedByApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['aliasName'] = self.alias_name
        result['attachedServices'] = []
        if self.attached_services is not None:
            for k in self.attached_services:
                result['attachedServices'].append(k.to_map() if k else None)
        else:
            result['attachedServices'] = None
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['name'] = self.name
        result['owneredPolicies'] = []
        if self.ownered_policies is not None:
            for k in self.ownered_policies:
                result['owneredPolicies'].append(k.to_map() if k else None)
        else:
            result['owneredPolicies'] = None
        if self.published_gateway is not None:
            result['publishedGateway'] = self.published_gateway.to_map()
        else:
            result['publishedGateway'] = None
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.attached_services = []
        if map.get('attachedServices') is not None:
            for k in map.get('attachedServices'):
                temp_model = UpdateApiRequestAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        else:
            self.attached_services = None
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.name = map.get('name')
        self.ownered_policies = []
        if map.get('owneredPolicies') is not None:
            for k in map.get('owneredPolicies'):
                temp_model = UpdateApiRequestOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        else:
            self.ownered_policies = None
        if map.get('publishedGateway') is not None:
            temp_model = UpdateApiRequestPublishedGateway()
            self.published_gateway = temp_model.from_map(map['publishedGateway'])
        else:
            self.published_gateway = None
        self.status = map.get('status')
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
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['ipAddress'] = self.ip_address
        result['port'] = self.port
        result['serviceId'] = self.service_id
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.ip_address = map.get('ipAddress')
        self.port = map.get('port')
        self.service_id = map.get('serviceId')
        self.status = map.get('status')
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
        result['aliasName'] = self.alias_name
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['isAutoRefresh'] = self.is_auto_refresh
        result['isHealth'] = self.is_health
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        else:
            result['serviceEnds'] = None
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.is_health = map.get('isHealth')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = UpdateApiRequestAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        else:
            self.service_ends = None
        self.service_name_in_registry = map.get('serviceNameInRegistry')
        self.source_type = map.get('sourceType')
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
        result['apiId'] = self.api_id
        result['apiName'] = self.api_name
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['id'] = self.id
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.api_id = map.get('apiId')
        self.api_name = map.get('apiName')
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.id = map.get('id')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
        self.type = map.get('type')
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
        result['armsInfo'] = self.arms_info
        result['autoCreateSlb'] = self.auto_create_slb
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['edasNamespaceId'] = self.edas_namespace_id
        result['gatewayType'] = self.gateway_type
        result['id'] = self.id
        result['name'] = self.name
        result['podCidr'] = self.pod_cidr
        result['region'] = self.region
        result['regionName'] = self.region_name
        result['replica'] = self.replica
        result['runtimeOn'] = self.runtime_on
        result['securityGroup'] = self.security_group
        result['slb'] = self.slb
        result['slbAccessAddr'] = self.slb_access_addr
        result['status'] = self.status
        result['vpc'] = self.vpc
        result['vswitch'] = self.vswitch
        return result

    def from_map(self, map={}):
        self.arms_info = map.get('armsInfo')
        self.auto_create_slb = map.get('autoCreateSlb')
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.edas_namespace_id = map.get('edasNamespaceId')
        self.gateway_type = map.get('gatewayType')
        self.id = map.get('id')
        self.name = map.get('name')
        self.pod_cidr = map.get('podCidr')
        self.region = map.get('region')
        self.region_name = map.get('regionName')
        self.replica = map.get('replica')
        self.runtime_on = map.get('runtimeOn')
        self.security_group = map.get('securityGroup')
        self.slb = map.get('slb')
        self.slb_access_addr = map.get('slbAccessAddr')
        self.status = map.get('status')
        self.vpc = map.get('vpc')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateApiResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['aliasName'] = self.alias_name
        result['description'] = self.description
        result['isAutoRefresh'] = self.is_auto_refresh
        result['metaInfo'] = self.meta_info
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = self.service_ends
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.description = map.get('description')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.meta_info = map.get('metaInfo')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = map.get('serviceEnds')
        self.service_name_in_registry = map.get('serviceNameInRegistry')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        else:
            result['data'] = None
        return result

    def from_map(self, map={}):
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = SaveAllPoliciesRequestData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['apiId'] = self.api_id
        result['apiName'] = self.api_name
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['id'] = self.id
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.api_id = map.get('apiId')
        self.api_name = map.get('apiName')
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.id = map.get('id')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
        self.type = map.get('type')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = SaveAllPoliciesResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['id'] = self.id
        result['replica'] = self.replica
        return result

    def from_map(self, map={}):
        self.id = map.get('id')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateGatewayResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['aliasName'] = self.alias_name
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['isAutoRefresh'] = self.is_auto_refresh
        result['isHealth'] = self.is_health
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = self.service_ends
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.is_health = map.get('isHealth')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = map.get('serviceEnds')
        self.service_name_in_registry = map.get('serviceNameInRegistry')
        self.source_type = map.get('sourceType')
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
        result['code'] = self.code
        result['data'] = self.data
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = map.get('data')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['pageNumber'] = self.page_number
        result['pageSize'] = self.page_size
        result['status'] = self.status
        result['name'] = self.name
        result['aliasName'] = self.alias_name
        return result

    def from_map(self, map={}):
        self.page_number = map.get('pageNumber')
        self.page_size = map.get('pageSize')
        self.status = map.get('status')
        self.name = map.get('name')
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
        result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindApisByPagingResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        else:
            self.data = None
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
        result['creationDateTime'] = self.creation_date_time
        result['id'] = self.id
        result['ipAddress'] = self.ip_address
        result['port'] = self.port
        result['serviceId'] = self.service_id
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.creation_date_time = map.get('creationDateTime')
        self.id = map.get('id')
        self.ip_address = map.get('ipAddress')
        self.port = map.get('port')
        self.service_id = map.get('serviceId')
        self.status = map.get('status')
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
        result['aliasName'] = self.alias_name
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['isAutoRefresh'] = self.is_auto_refresh
        result['isHealth'] = self.is_health
        result['name'] = self.name
        result['registryId'] = self.registry_id
        result['serviceEnds'] = []
        if self.service_ends is not None:
            for k in self.service_ends:
                result['serviceEnds'].append(k.to_map() if k else None)
        else:
            result['serviceEnds'] = None
        result['serviceNameInRegistry'] = self.service_name_in_registry
        result['sourceType'] = self.source_type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.is_auto_refresh = map.get('isAutoRefresh')
        self.is_health = map.get('isHealth')
        self.name = map.get('name')
        self.registry_id = map.get('registryId')
        self.service_ends = []
        if map.get('serviceEnds') is not None:
            for k in map.get('serviceEnds'):
                temp_model = FindApisByPagingResponseBodyDataListAttachedServicesServiceEnds()
                self.service_ends.append(temp_model.from_map(k))
        else:
            self.service_ends = None
        self.service_name_in_registry = map.get('serviceNameInRegistry')
        self.source_type = map.get('sourceType')
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
        result['apiId'] = self.api_id
        result['apiName'] = self.api_name
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['id'] = self.id
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.api_id = map.get('apiId')
        self.api_name = map.get('apiName')
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.id = map.get('id')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
        self.type = map.get('type')
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
        result['armsInfo'] = self.arms_info
        result['autoCreateSlb'] = self.auto_create_slb
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['edasNamespaceId'] = self.edas_namespace_id
        result['gatewayType'] = self.gateway_type
        result['id'] = self.id
        result['name'] = self.name
        result['podCidr'] = self.pod_cidr
        result['region'] = self.region
        result['regionName'] = self.region_name
        result['replica'] = self.replica
        result['runtimeOn'] = self.runtime_on
        result['securityGroup'] = self.security_group
        result['slb'] = self.slb
        result['slbAccessAddr'] = self.slb_access_addr
        result['status'] = self.status
        result['vpc'] = self.vpc
        result['vswitch'] = self.vswitch
        return result

    def from_map(self, map={}):
        self.arms_info = map.get('armsInfo')
        self.auto_create_slb = map.get('autoCreateSlb')
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.edas_namespace_id = map.get('edasNamespaceId')
        self.gateway_type = map.get('gatewayType')
        self.id = map.get('id')
        self.name = map.get('name')
        self.pod_cidr = map.get('podCidr')
        self.region = map.get('region')
        self.region_name = map.get('regionName')
        self.replica = map.get('replica')
        self.runtime_on = map.get('runtimeOn')
        self.security_group = map.get('securityGroup')
        self.slb = map.get('slb')
        self.slb_access_addr = map.get('slbAccessAddr')
        self.status = map.get('status')
        self.vpc = map.get('vpc')
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
        result['aliasName'] = self.alias_name
        result['attachedServices'] = []
        if self.attached_services is not None:
            for k in self.attached_services:
                result['attachedServices'].append(k.to_map() if k else None)
        else:
            result['attachedServices'] = None
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['id'] = self.id
        result['name'] = self.name
        result['owneredPolicies'] = []
        if self.ownered_policies is not None:
            for k in self.ownered_policies:
                result['owneredPolicies'].append(k.to_map() if k else None)
        else:
            result['owneredPolicies'] = None
        if self.published_gateway is not None:
            result['publishedGateway'] = self.published_gateway.to_map()
        else:
            result['publishedGateway'] = None
        result['status'] = self.status
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.alias_name = map.get('aliasName')
        self.attached_services = []
        if map.get('attachedServices') is not None:
            for k in map.get('attachedServices'):
                temp_model = FindApisByPagingResponseBodyDataListAttachedServices()
                self.attached_services.append(temp_model.from_map(k))
        else:
            self.attached_services = None
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.id = map.get('id')
        self.name = map.get('name')
        self.ownered_policies = []
        if map.get('owneredPolicies') is not None:
            for k in map.get('owneredPolicies'):
                temp_model = FindApisByPagingResponseBodyDataListOwneredPolicies()
                self.ownered_policies.append(temp_model.from_map(k))
        else:
            self.ownered_policies = None
        if map.get('publishedGateway') is not None:
            temp_model = FindApisByPagingResponseBodyDataListPublishedGateway()
            self.published_gateway = temp_model.from_map(map['publishedGateway'])
        else:
            self.published_gateway = None
        self.status = map.get('status')
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
        else:
            result['list'] = None
        result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindApisByPagingResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindApisByPagingResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class FindGatewaysRequest(TeaModel):
    def __init__(self, gateway_unique_id=None, name=None, region=None, gateway_types=None, status=None,
                 page_number=None, page_size=None):
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

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['gatewayUniqueId'] = self.gateway_unique_id
        result['name'] = self.name
        result['region'] = self.region
        result['gatewayTypes'] = self.gateway_types
        result['status'] = self.status
        result['pageNumber'] = self.page_number
        result['pageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.gateway_unique_id = map.get('gatewayUniqueId')
        self.name = map.get('name')
        self.region = map.get('region')
        self.gateway_types = map.get('gatewayTypes')
        self.status = map.get('status')
        self.page_number = map.get('pageNumber')
        self.page_size = map.get('pageSize')
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
        result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = FindGatewaysResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        else:
            self.data = None
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
        result['appId'] = self.app_id
        result['appName'] = self.app_name
        result['description'] = self.description
        result['licenseKey'] = self.license_key
        return result

    def from_map(self, map={}):
        self.app_id = map.get('appId')
        self.app_name = map.get('appName')
        self.description = map.get('description')
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
        else:
            result['armsInfo'] = None
        result['autoCreateSlb'] = self.auto_create_slb
        result['basePath'] = self.base_path
        result['creationDateTime'] = self.creation_date_time
        result['edasNamespaceId'] = self.edas_namespace_id
        result['gatewayType'] = self.gateway_type
        result['id'] = self.id
        result['name'] = self.name
        result['podCidr'] = self.pod_cidr
        result['region'] = self.region
        result['regionName'] = self.region_name
        result['replica'] = self.replica
        result['runtimeOn'] = self.runtime_on
        result['securityGroup'] = self.security_group
        result['slb'] = self.slb
        result['slbAccessAddr'] = self.slb_access_addr
        result['status'] = self.status
        result['vpc'] = self.vpc
        result['vswitch'] = self.vswitch
        return result

    def from_map(self, map={}):
        if map.get('armsInfo') is not None:
            temp_model = FindGatewaysResponseBodyDataListArmsInfo()
            self.arms_info = temp_model.from_map(map['armsInfo'])
        else:
            self.arms_info = None
        self.auto_create_slb = map.get('autoCreateSlb')
        self.base_path = map.get('basePath')
        self.creation_date_time = map.get('creationDateTime')
        self.edas_namespace_id = map.get('edasNamespaceId')
        self.gateway_type = map.get('gatewayType')
        self.id = map.get('id')
        self.name = map.get('name')
        self.pod_cidr = map.get('podCidr')
        self.region = map.get('region')
        self.region_name = map.get('regionName')
        self.replica = map.get('replica')
        self.runtime_on = map.get('runtimeOn')
        self.security_group = map.get('securityGroup')
        self.slb = map.get('slb')
        self.slb_access_addr = map.get('slbAccessAddr')
        self.status = map.get('status')
        self.vpc = map.get('vpc')
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
        else:
            result['list'] = None
        result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = FindGatewaysResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = FindGatewaysResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['pageNumber'] = self.page_number
        result['pageSize'] = self.page_size
        result['name'] = self.name
        result['type'] = self.type
        result['groupBy'] = self.group_by
        return result

    def from_map(self, map={}):
        self.page_number = map.get('pageNumber')
        self.page_size = map.get('pageSize')
        self.name = map.get('name')
        self.type = map.get('type')
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
        result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        if map.get('data') is not None:
            temp_model = GetAllRegistryResponseBodyData()
            self.data = temp_model.from_map(map['data'])
        else:
            self.data = None
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
        result['address'] = self.address
        result['creationDateTime'] = self.creation_date_time
        result['description'] = self.description
        result['gatewayId'] = self.gateway_id
        result['id'] = self.id
        result['name'] = self.name
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.address = map.get('address')
        self.creation_date_time = map.get('creationDateTime')
        self.description = map.get('description')
        self.gateway_id = map.get('gatewayId')
        self.id = map.get('id')
        self.name = map.get('name')
        self.type = map.get('type')
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
        else:
            result['list'] = None
        result['totalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = GetAllRegistryResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAllRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        else:
            result['data'] = None
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.data = []
        if map.get('data') is not None:
            for k in map.get('data'):
                temp_model = PullServiceInfoFromRegistryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
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
        result['id'] = self.id
        result['metaInfo'] = self.meta_info
        result['serviceEnds'] = self.service_ends
        result['serviceName'] = self.service_name
        return result

    def from_map(self, map={}):
        self.id = map.get('id')
        self.meta_info = map.get('metaInfo')
        self.service_ends = map.get('serviceEnds')
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
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = PullServiceInfoFromRegistryResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
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
        result['apiId'] = self.api_id
        result['apiName'] = self.api_name
        result['creationDateTime'] = self.creation_date_time
        result['direction'] = self.direction
        result['id'] = self.id
        result['policyAliasName'] = self.policy_alias_name
        result['policyContent'] = self.policy_content
        result['policyGroup'] = self.policy_group
        result['policyId'] = self.policy_id
        result['policyName'] = self.policy_name
        result['priority'] = self.priority
        result['scope'] = self.scope
        result['status'] = self.status
        result['type'] = self.type
        result['updateDateTime'] = self.update_date_time
        return result

    def from_map(self, map={}):
        self.api_id = map.get('apiId')
        self.api_name = map.get('apiName')
        self.creation_date_time = map.get('creationDateTime')
        self.direction = map.get('direction')
        self.id = map.get('id')
        self.policy_alias_name = map.get('policyAliasName')
        self.policy_content = map.get('policyContent')
        self.policy_group = map.get('policyGroup')
        self.policy_id = map.get('policyId')
        self.policy_name = map.get('policyName')
        self.priority = map.get('priority')
        self.scope = map.get('scope')
        self.status = map.get('status')
        self.type = map.get('type')
        self.update_date_time = map.get('updateDateTime')
        return self
