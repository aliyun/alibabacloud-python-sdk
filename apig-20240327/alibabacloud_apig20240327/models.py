# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AiServiceConfig(TeaModel):
    def __init__(
        self,
        address: str = None,
        api_keys: List[str] = None,
        enable_health_check: bool = None,
        protocols: List[str] = None,
        provider: str = None,
    ):
        self.address = address
        self.api_keys = api_keys
        self.enable_health_check = enable_health_check
        self.protocols = protocols
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys
        if self.enable_health_check is not None:
            result['enableHealthCheck'] = self.enable_health_check
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.provider is not None:
            result['provider'] = self.provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')
        if m.get('enableHealthCheck') is not None:
            self.enable_health_check = m.get('enableHealthCheck')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        return self


class AkSkIdentityConfig(TeaModel):
    def __init__(
        self,
        ak: str = None,
        generate_mode: str = None,
        sk: str = None,
        type: str = None,
    ):
        self.ak = ak
        self.generate_mode = generate_mode
        self.sk = sk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak is not None:
            result['ak'] = self.ak
        if self.generate_mode is not None:
            result['generateMode'] = self.generate_mode
        if self.sk is not None:
            result['sk'] = self.sk
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')
        if m.get('generateMode') is not None:
            self.generate_mode = m.get('generateMode')
        if m.get('sk') is not None:
            self.sk = m.get('sk')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ApiKeyIdentityConfigApikeySource(TeaModel):
    def __init__(
        self,
        source: str = None,
        value: str = None,
    ):
        self.source = source
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ApiKeyIdentityConfigCredentials(TeaModel):
    def __init__(
        self,
        apikey: str = None,
        generate_mode: str = None,
    ):
        self.apikey = apikey
        self.generate_mode = generate_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apikey is not None:
            result['apikey'] = self.apikey
        if self.generate_mode is not None:
            result['generateMode'] = self.generate_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apikey') is not None:
            self.apikey = m.get('apikey')
        if m.get('generateMode') is not None:
            self.generate_mode = m.get('generateMode')
        return self


class ApiKeyIdentityConfig(TeaModel):
    def __init__(
        self,
        apikey_source: ApiKeyIdentityConfigApikeySource = None,
        credentials: List[ApiKeyIdentityConfigCredentials] = None,
        type: str = None,
    ):
        self.apikey_source = apikey_source
        self.credentials = credentials
        self.type = type

    def validate(self):
        if self.apikey_source:
            self.apikey_source.validate()
        if self.credentials:
            for k in self.credentials:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apikey_source is not None:
            result['apikeySource'] = self.apikey_source.to_map()
        result['credentials'] = []
        if self.credentials is not None:
            for k in self.credentials:
                result['credentials'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apikeySource') is not None:
            temp_model = ApiKeyIdentityConfigApikeySource()
            self.apikey_source = temp_model.from_map(m['apikeySource'])
        self.credentials = []
        if m.get('credentials') is not None:
            for k in m.get('credentials'):
                temp_model = ApiKeyIdentityConfigCredentials()
                self.credentials.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ApiRouteConflictInfoConflictsDetailsConflictingMatchOperationInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        operation_id: str = None,
    ):
        self.name = name
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        return self


class HttpRouteMatchHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpRouteMatchPath(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpRouteMatchQueryParams(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpRouteMatch(TeaModel):
    def __init__(
        self,
        headers: List[HttpRouteMatchHeaders] = None,
        ignore_uri_case: bool = None,
        methods: List[str] = None,
        path: HttpRouteMatchPath = None,
        query_params: List[HttpRouteMatchQueryParams] = None,
    ):
        self.headers = headers
        self.ignore_uri_case = ignore_uri_case
        self.methods = methods
        self.path = path
        self.query_params = query_params

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()
        if self.path:
            self.path.validate()
        if self.query_params:
            for k in self.query_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        if self.ignore_uri_case is not None:
            result['ignoreUriCase'] = self.ignore_uri_case
        if self.methods is not None:
            result['methods'] = self.methods
        if self.path is not None:
            result['path'] = self.path.to_map()
        result['queryParams'] = []
        if self.query_params is not None:
            for k in self.query_params:
                result['queryParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('headers') is not None:
            for k in m.get('headers'):
                temp_model = HttpRouteMatchHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('ignoreUriCase') is not None:
            self.ignore_uri_case = m.get('ignoreUriCase')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        if m.get('path') is not None:
            temp_model = HttpRouteMatchPath()
            self.path = temp_model.from_map(m['path'])
        self.query_params = []
        if m.get('queryParams') is not None:
            for k in m.get('queryParams'):
                temp_model = HttpRouteMatchQueryParams()
                self.query_params.append(temp_model.from_map(k))
        return self


class ApiRouteConflictInfoConflictsDetailsConflictingMatch(TeaModel):
    def __init__(
        self,
        match: HttpRouteMatch = None,
        operation_info: ApiRouteConflictInfoConflictsDetailsConflictingMatchOperationInfo = None,
    ):
        self.match = match
        self.operation_info = operation_info

    def validate(self):
        if self.match:
            self.match.validate()
        if self.operation_info:
            self.operation_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.operation_info is not None:
            result['operationInfo'] = self.operation_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('operationInfo') is not None:
            temp_model = ApiRouteConflictInfoConflictsDetailsConflictingMatchOperationInfo()
            self.operation_info = temp_model.from_map(m['operationInfo'])
        return self


class ApiRouteConflictInfoConflictsDetailsDetectedMatchOperationInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        operation_id: str = None,
    ):
        self.name = name
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        return self


class ApiRouteConflictInfoConflictsDetailsDetectedMatch(TeaModel):
    def __init__(
        self,
        match: HttpRouteMatch = None,
        operation_info: ApiRouteConflictInfoConflictsDetailsDetectedMatchOperationInfo = None,
    ):
        self.match = match
        self.operation_info = operation_info

    def validate(self):
        if self.match:
            self.match.validate()
        if self.operation_info:
            self.operation_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.operation_info is not None:
            result['operationInfo'] = self.operation_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('operationInfo') is not None:
            temp_model = ApiRouteConflictInfoConflictsDetailsDetectedMatchOperationInfo()
            self.operation_info = temp_model.from_map(m['operationInfo'])
        return self


class ApiRouteConflictInfoConflictsDetails(TeaModel):
    def __init__(
        self,
        conflicting_match: ApiRouteConflictInfoConflictsDetailsConflictingMatch = None,
        detected_match: ApiRouteConflictInfoConflictsDetailsDetectedMatch = None,
        level: str = None,
    ):
        self.conflicting_match = conflicting_match
        self.detected_match = detected_match
        self.level = level

    def validate(self):
        if self.conflicting_match:
            self.conflicting_match.validate()
        if self.detected_match:
            self.detected_match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conflicting_match is not None:
            result['conflictingMatch'] = self.conflicting_match.to_map()
        if self.detected_match is not None:
            result['detectedMatch'] = self.detected_match.to_map()
        if self.level is not None:
            result['level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conflictingMatch') is not None:
            temp_model = ApiRouteConflictInfoConflictsDetailsConflictingMatch()
            self.conflicting_match = temp_model.from_map(m['conflictingMatch'])
        if m.get('detectedMatch') is not None:
            temp_model = ApiRouteConflictInfoConflictsDetailsDetectedMatch()
            self.detected_match = temp_model.from_map(m['detectedMatch'])
        if m.get('level') is not None:
            self.level = m.get('level')
        return self


class ApiRouteConflictInfoConflictsEnvironmentInfo(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
        name: str = None,
    ):
        self.environment_id = environment_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ApiRouteConflictInfoConflictsRouteInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        route_id: str = None,
    ):
        self.name = name
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.route_id is not None:
            result['routeId'] = self.route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')
        return self


class ApiRouteConflictInfoConflicts(TeaModel):
    def __init__(
        self,
        details: List[ApiRouteConflictInfoConflictsDetails] = None,
        environment_info: ApiRouteConflictInfoConflictsEnvironmentInfo = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        route_info: ApiRouteConflictInfoConflictsRouteInfo = None,
    ):
        self.details = details
        self.environment_info = environment_info
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.route_info = route_info

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.route_info:
            self.route_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['details'] = []
        if self.details is not None:
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.route_info is not None:
            result['routeInfo'] = self.route_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('details') is not None:
            for k in m.get('details'):
                temp_model = ApiRouteConflictInfoConflictsDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('environmentInfo') is not None:
            temp_model = ApiRouteConflictInfoConflictsEnvironmentInfo()
            self.environment_info = temp_model.from_map(m['environmentInfo'])
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('routeInfo') is not None:
            temp_model = ApiRouteConflictInfoConflictsRouteInfo()
            self.route_info = temp_model.from_map(m['routeInfo'])
        return self


class ApiRouteConflictInfoDomainInfo(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
    ):
        self.domain_id = domain_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ApiRouteConflictInfo(TeaModel):
    def __init__(
        self,
        conflicts: List[ApiRouteConflictInfoConflicts] = None,
        domain_info: ApiRouteConflictInfoDomainInfo = None,
    ):
        self.conflicts = conflicts
        self.domain_info = domain_info

    def validate(self):
        if self.conflicts:
            for k in self.conflicts:
                if k:
                    k.validate()
        if self.domain_info:
            self.domain_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conflicts'] = []
        if self.conflicts is not None:
            for k in self.conflicts:
                result['conflicts'].append(k.to_map() if k else None)
        if self.domain_info is not None:
            result['domainInfo'] = self.domain_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conflicts = []
        if m.get('conflicts') is not None:
            for k in m.get('conflicts'):
                temp_model = ApiRouteConflictInfoConflicts()
                self.conflicts.append(temp_model.from_map(k))
        if m.get('domainInfo') is not None:
            temp_model = ApiRouteConflictInfoDomainInfo()
            self.domain_info = temp_model.from_map(m['domainInfo'])
        return self


class Attachment(TeaModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        attach_resource_type: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_attachment_id: str = None,
    ):
        self.attach_resource_ids = attach_resource_ids
        self.attach_resource_type = attach_resource_type
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.policy_attachment_id = policy_attachment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.policy_attachment_id is not None:
            result['policyAttachmentId'] = self.policy_attachment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')
        return self


class AuthConfig(TeaModel):
    def __init__(
        self,
        auth_mode: str = None,
        auth_type: str = None,
    ):
        self.auth_mode = auth_mode
        self.auth_type = auth_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_mode is not None:
            result['authMode'] = self.auth_mode
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMode') is not None:
            self.auth_mode = m.get('authMode')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        return self


class AuthorizationResourceInfo(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
        parent_resource_id: str = None,
        resource_id: str = None,
    ):
        self.environment_id = environment_id
        self.parent_resource_id = parent_resource_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.parent_resource_id is not None:
            result['parentResourceId'] = self.parent_resource_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('parentResourceId') is not None:
            self.parent_resource_id = m.get('parentResourceId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        return self


class BackendServices(TeaModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.name = name
        self.port = port
        self.protocol = protocol
        self.service_id = service_id
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class Backend(TeaModel):
    def __init__(
        self,
        scene: str = None,
        services: List[BackendServices] = None,
    ):
        self.scene = scene
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = BackendServices()
                self.services.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleResult(TeaModel):
    def __init__(
        self,
        existed: bool = None,
    ):
        self.existed = existed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.existed is not None:
            result['existed'] = self.existed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('existed') is not None:
            self.existed = m.get('existed')
        return self


class ConsumerInfo(TeaModel):
    def __init__(
        self,
        consumer_id: str = None,
        enable: bool = None,
        name: str = None,
    ):
        self.consumer_id = consumer_id
        self.enable = enable
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id
        if self.enable is not None:
            result['enable'] = self.enable
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DashboardFilter(TeaModel):
    def __init__(
        self,
        route_name: str = None,
    ):
        self.route_name = route_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_name is not None:
            result['routeName'] = self.route_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')
        return self


class DomainInfo(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        client_cacert: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        domain_id: str = None,
        force_https: bool = None,
        m_tlsenabled: bool = None,
        name: str = None,
        protocol: str = None,
        resource_group_id: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.cert_identifier = cert_identifier
        self.client_cacert = client_cacert
        self.create_from = create_from
        self.create_timestamp = create_timestamp
        self.domain_id = domain_id
        self.force_https = force_https
        self.m_tlsenabled = m_tlsenabled
        self.name = name
        self.protocol = protocol
        self.resource_group_id = resource_group_id
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.client_cacert is not None:
            result['clientCACert'] = self.client_cacert
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.m_tlsenabled is not None:
            result['mTLSEnabled'] = self.m_tlsenabled
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('clientCACert') is not None:
            self.client_cacert = m.get('clientCACert')
        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('mTLSEnabled') is not None:
            self.m_tlsenabled = m.get('mTLSEnabled')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GatewayInfoVpcInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        vpc_id: str = None,
    ):
        self.name = name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GatewayInfo(TeaModel):
    def __init__(
        self,
        engine_version: str = None,
        gateway_id: str = None,
        name: str = None,
        vpc_info: GatewayInfoVpcInfo = None,
    ):
        self.engine_version = engine_version
        self.gateway_id = gateway_id
        self.name = name
        self.vpc_info = vpc_info

    def validate(self):
        if self.vpc_info:
            self.vpc_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_info is not None:
            result['vpcInfo'] = self.vpc_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcInfo') is not None:
            temp_model = GatewayInfoVpcInfo()
            self.vpc_info = temp_model.from_map(m['vpcInfo'])
        return self


class SubDomainInfo(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.network_type = network_type
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class EnvironmentInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        create_timestamp: int = None,
        default: bool = None,
        description: str = None,
        environment_id: str = None,
        gateway_info: GatewayInfo = None,
        name: str = None,
        resource_group_id: str = None,
        sub_domain_infos: List[SubDomainInfo] = None,
        update_timestamp: int = None,
    ):
        self.alias = alias
        self.create_timestamp = create_timestamp
        self.default = default
        self.description = description
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.resource_group_id = resource_group_id
        self.sub_domain_infos = sub_domain_infos
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.sub_domain_infos:
            for k in self.sub_domain_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['subDomainInfos'] = []
        if self.sub_domain_infos is not None:
            for k in self.sub_domain_infos:
                result['subDomainInfos'].append(k.to_map() if k else None)
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayInfo') is not None:
            temp_model = GatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k in m.get('subDomainInfos'):
                temp_model = SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k))
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GatewayLogConfigSlsConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class GatewayLogConfig(TeaModel):
    def __init__(
        self,
        sls_config: GatewayLogConfigSlsConfig = None,
    ):
        self.sls_config = sls_config

    def validate(self):
        if self.sls_config:
            self.sls_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_config is not None:
            result['slsConfig'] = self.sls_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('slsConfig') is not None:
            temp_model = GatewayLogConfigSlsConfig()
            self.sls_config = temp_model.from_map(m['slsConfig'])
        return self


class HttpApiApiInfoEnvironmentsGatewayInfo(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
    ):
        self.gateway_id = gateway_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class HttpApiBackendMatchCondition(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.operator = operator
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class HttpApiBackendMatchConditions(TeaModel):
    def __init__(
        self,
        conditions: List[HttpApiBackendMatchCondition] = None,
        default: bool = None,
    ):
        self.conditions = conditions
        self.default = default

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.default is not None:
            result['default'] = self.default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = HttpApiBackendMatchCondition()
                self.conditions.append(temp_model.from_map(k))
        if m.get('default') is not None:
            self.default = m.get('default')
        return self


class HttpApiApiInfoEnvironmentsServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        port: str = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.name = name
        self.port = port
        self.protocol = protocol
        self.service_id = service_id
        self.version = version
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiApiInfoEnvironmentsSubDomains(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.network_type = network_type
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class HttpApiDomainInfo(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class HttpApiApiInfoEnvironments(TeaModel):
    def __init__(
        self,
        alias: str = None,
        backend_scene: str = None,
        backend_type: str = None,
        custom_domains: List[HttpApiDomainInfo] = None,
        deploy_status: str = None,
        environment_id: str = None,
        gateway_info: HttpApiApiInfoEnvironmentsGatewayInfo = None,
        name: str = None,
        service_configs: List[HttpApiApiInfoEnvironmentsServiceConfigs] = None,
        sub_domains: List[HttpApiApiInfoEnvironmentsSubDomains] = None,
    ):
        self.alias = alias
        self.backend_scene = backend_scene
        self.backend_type = backend_type
        self.custom_domains = custom_domains
        self.deploy_status = deploy_status
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.service_configs = service_configs
        self.sub_domains = sub_domains

    def validate(self):
        if self.custom_domains:
            for k in self.custom_domains:
                if k:
                    k.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()
        if self.sub_domains:
            for k in self.sub_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene
        if self.backend_type is not None:
            result['backendType'] = self.backend_type
        result['customDomains'] = []
        if self.custom_domains is not None:
            for k in self.custom_domains:
                result['customDomains'].append(k.to_map() if k else None)
        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        result['subDomains'] = []
        if self.sub_domains is not None:
            for k in self.sub_domains:
                result['subDomains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')
        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k in m.get('customDomains'):
                temp_model = HttpApiDomainInfo()
                self.custom_domains.append(temp_model.from_map(k))
        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayInfo') is not None:
            temp_model = HttpApiApiInfoEnvironmentsGatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = HttpApiApiInfoEnvironmentsServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k in m.get('subDomains'):
                temp_model = HttpApiApiInfoEnvironmentsSubDomains()
                self.sub_domains.append(temp_model.from_map(k))
        return self


class HttpApiApiInfoIngressInfoEnvironmentInfo(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
    ):
        self.environment_id = environment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        return self


class HttpApiApiInfoIngressInfoK8sClusterInfo(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        return self


class HttpApiApiInfoIngressInfo(TeaModel):
    def __init__(
        self,
        environment_info: HttpApiApiInfoIngressInfoEnvironmentInfo = None,
        ingress_class: str = None,
        k_8s_cluster_info: HttpApiApiInfoIngressInfoK8sClusterInfo = None,
        override_ingress_ip: bool = None,
        source_id: str = None,
        watch_namespace: str = None,
    ):
        self.environment_info = environment_info
        self.ingress_class = ingress_class
        self.k_8s_cluster_info = k_8s_cluster_info
        self.override_ingress_ip = override_ingress_ip
        self.source_id = source_id
        self.watch_namespace = watch_namespace

    def validate(self):
        if self.environment_info:
            self.environment_info.validate()
        if self.k_8s_cluster_info:
            self.k_8s_cluster_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()
        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class
        if self.k_8s_cluster_info is not None:
            result['k8sClusterInfo'] = self.k_8s_cluster_info.to_map()
        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentInfo') is not None:
            temp_model = HttpApiApiInfoIngressInfoEnvironmentInfo()
            self.environment_info = temp_model.from_map(m['environmentInfo'])
        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')
        if m.get('k8sClusterInfo') is not None:
            temp_model = HttpApiApiInfoIngressInfoK8sClusterInfo()
            self.k_8s_cluster_info = temp_model.from_map(m['k8sClusterInfo'])
        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')
        return self


class HttpApiApiInfoDeployCntMapValue(TeaModel):
    def __init__(
        self,
        deployed_cnt: int = None,
        cnt: int = None,
    ):
        self.deployed_cnt = deployed_cnt
        self.cnt = cnt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployed_cnt is not None:
            result['deployedCnt'] = self.deployed_cnt
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployedCnt') is not None:
            self.deployed_cnt = m.get('deployedCnt')
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')
        return self


class HttpApiMockContract(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        response_code: int = None,
        response_content: str = None,
    ):
        self.enable = enable
        self.response_code = response_code
        self.response_content = response_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.response_code is not None:
            result['responseCode'] = self.response_code
        if self.response_content is not None:
            result['responseContent'] = self.response_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('responseCode') is not None:
            self.response_code = m.get('responseCode')
        if m.get('responseContent') is not None:
            self.response_content = m.get('responseContent')
        return self


class HttpApiDeployConfigCustomDomainInfos(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class HttpApiDeployConfigPolicyConfigsAiFallbackConfig(TeaModel):
    def __init__(
        self,
        service_ids: List[str] = None,
    ):
        self.service_ids = service_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')
        return self


class HttpApiDeployConfigPolicyConfigs(TeaModel):
    def __init__(
        self,
        ai_fallback_config: HttpApiDeployConfigPolicyConfigsAiFallbackConfig = None,
        enable: bool = None,
        type: str = None,
    ):
        self.ai_fallback_config = ai_fallback_config
        self.enable = enable
        self.type = type

    def validate(self):
        if self.ai_fallback_config:
            self.ai_fallback_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_fallback_config is not None:
            result['aiFallbackConfig'] = self.ai_fallback_config.to_map()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiFallbackConfig') is not None:
            temp_model = HttpApiDeployConfigPolicyConfigsAiFallbackConfig()
            self.ai_fallback_config = temp_model.from_map(m['aiFallbackConfig'])
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class HttpApiDeployConfigServiceConfigs(TeaModel):
    def __init__(
        self,
        model_name: str = None,
        model_name_pattern: str = None,
        service_id: str = None,
        weight: int = None,
    ):
        self.model_name = model_name
        self.model_name_pattern = model_name_pattern
        self.service_id = service_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.model_name_pattern is not None:
            result['modelNamePattern'] = self.model_name_pattern
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('modelNamePattern') is not None:
            self.model_name_pattern = m.get('modelNamePattern')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiDeployConfigSubDomains(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.network_type = network_type
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class HttpApiDeployConfig(TeaModel):
    def __init__(
        self,
        auto_deploy: bool = None,
        backend_scene: str = None,
        custom_domain_ids: List[str] = None,
        custom_domain_infos: List[HttpApiDeployConfigCustomDomainInfos] = None,
        environment_id: str = None,
        gateway_id: str = None,
        gateway_info: GatewayInfo = None,
        mock: HttpApiMockContract = None,
        policy_configs: List[HttpApiDeployConfigPolicyConfigs] = None,
        route_backend: Backend = None,
        service_configs: List[HttpApiDeployConfigServiceConfigs] = None,
        sub_domains: List[HttpApiDeployConfigSubDomains] = None,
    ):
        self.auto_deploy = auto_deploy
        self.backend_scene = backend_scene
        self.custom_domain_ids = custom_domain_ids
        self.custom_domain_infos = custom_domain_infos
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.gateway_info = gateway_info
        self.mock = mock
        self.policy_configs = policy_configs
        self.route_backend = route_backend
        self.service_configs = service_configs
        self.sub_domains = sub_domains

    def validate(self):
        if self.custom_domain_infos:
            for k in self.custom_domain_infos:
                if k:
                    k.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.mock:
            self.mock.validate()
        if self.policy_configs:
            for k in self.policy_configs:
                if k:
                    k.validate()
        if self.route_backend:
            self.route_backend.validate()
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()
        if self.sub_domains:
            for k in self.sub_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deploy is not None:
            result['autoDeploy'] = self.auto_deploy
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene
        if self.custom_domain_ids is not None:
            result['customDomainIds'] = self.custom_domain_ids
        result['customDomainInfos'] = []
        if self.custom_domain_infos is not None:
            for k in self.custom_domain_infos:
                result['customDomainInfos'].append(k.to_map() if k else None)
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.mock is not None:
            result['mock'] = self.mock.to_map()
        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k in self.policy_configs:
                result['policyConfigs'].append(k.to_map() if k else None)
        if self.route_backend is not None:
            result['routeBackend'] = self.route_backend.to_map()
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        result['subDomains'] = []
        if self.sub_domains is not None:
            for k in self.sub_domains:
                result['subDomains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDeploy') is not None:
            self.auto_deploy = m.get('autoDeploy')
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')
        self.custom_domain_infos = []
        if m.get('customDomainInfos') is not None:
            for k in m.get('customDomainInfos'):
                temp_model = HttpApiDeployConfigCustomDomainInfos()
                self.custom_domain_infos.append(temp_model.from_map(k))
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayInfo') is not None:
            temp_model = GatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('mock') is not None:
            temp_model = HttpApiMockContract()
            self.mock = temp_model.from_map(m['mock'])
        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k in m.get('policyConfigs'):
                temp_model = HttpApiDeployConfigPolicyConfigs()
                self.policy_configs.append(temp_model.from_map(k))
        if m.get('routeBackend') is not None:
            temp_model = Backend()
            self.route_backend = temp_model.from_map(m['routeBackend'])
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = HttpApiDeployConfigServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k in m.get('subDomains'):
                temp_model = HttpApiDeployConfigSubDomains()
                self.sub_domains.append(temp_model.from_map(k))
        return self


class HttpApiVersionInfo(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        header_name: str = None,
        query_name: str = None,
        scheme: str = None,
        version: str = None,
    ):
        self.enable = enable
        self.header_name = header_name
        self.query_name = query_name
        self.scheme = scheme
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.header_name is not None:
            result['headerName'] = self.header_name
        if self.query_name is not None:
            result['queryName'] = self.query_name
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('headerName') is not None:
            self.header_name = m.get('headerName')
        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class HttpApiApiInfo(TeaModel):
    def __init__(
        self,
        ai_protocols: List[str] = None,
        auth_config: AuthConfig = None,
        base_path: str = None,
        deploy_cnt_map: Dict[str, HttpApiApiInfoDeployCntMapValue] = None,
        deploy_configs: List[HttpApiDeployConfig] = None,
        description: str = None,
        enabel_auth: bool = None,
        environments: List[HttpApiApiInfoEnvironments] = None,
        gateway_id: str = None,
        http_api_id: str = None,
        ingress_info: HttpApiApiInfoIngressInfo = None,
        name: str = None,
        protocols: List[str] = None,
        resource_group_id: str = None,
        type: str = None,
        version_info: HttpApiVersionInfo = None,
    ):
        self.ai_protocols = ai_protocols
        self.auth_config = auth_config
        self.base_path = base_path
        self.deploy_cnt_map = deploy_cnt_map
        self.deploy_configs = deploy_configs
        self.description = description
        self.enabel_auth = enabel_auth
        self.environments = environments
        self.gateway_id = gateway_id
        self.http_api_id = http_api_id
        self.ingress_info = ingress_info
        self.name = name
        self.protocols = protocols
        self.resource_group_id = resource_group_id
        self.type = type
        self.version_info = version_info

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_cnt_map:
            for v in self.deploy_cnt_map.values():
                if v:
                    v.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()
        if self.environments:
            for k in self.environments:
                if k:
                    k.validate()
        if self.ingress_info:
            self.ingress_info.validate()
        if self.version_info:
            self.version_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.base_path is not None:
            result['basePath'] = self.base_path
        result['deployCntMap'] = {}
        if self.deploy_cnt_map is not None:
            for k, v in self.deploy_cnt_map.items():
                result['deployCntMap'][k] = v.to_map()
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.enabel_auth is not None:
            result['enabelAuth'] = self.enabel_auth
        result['environments'] = []
        if self.environments is not None:
            for k in self.environments:
                result['environments'].append(k.to_map() if k else None)
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id
        if self.ingress_info is not None:
            result['ingressInfo'] = self.ingress_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.type is not None:
            result['type'] = self.type
        if self.version_info is not None:
            result['versionInfo'] = self.version_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        self.deploy_cnt_map = {}
        if m.get('deployCntMap') is not None:
            for k, v in m.get('deployCntMap').items():
                temp_model = HttpApiApiInfoDeployCntMapValue()
                self.deploy_cnt_map[k] = temp_model.from_map(v)
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enabelAuth') is not None:
            self.enabel_auth = m.get('enabelAuth')
        self.environments = []
        if m.get('environments') is not None:
            for k in m.get('environments'):
                temp_model = HttpApiApiInfoEnvironments()
                self.environments.append(temp_model.from_map(k))
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')
        if m.get('ingressInfo') is not None:
            temp_model = HttpApiApiInfoIngressInfo()
            self.ingress_info = temp_model.from_map(m['ingressInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('versionInfo') is not None:
            temp_model = HttpApiVersionInfo()
            self.version_info = temp_model.from_map(m['versionInfo'])
        return self


class HttpApiInfoByName(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
        type: str = None,
        version_enabled: bool = None,
        versioned_http_apis: List[HttpApiApiInfo] = None,
    ):
        self.gateway_id = gateway_id
        self.name = name
        self.type = type
        self.version_enabled = version_enabled
        self.versioned_http_apis = versioned_http_apis

    def validate(self):
        if self.versioned_http_apis:
            for k in self.versioned_http_apis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.version_enabled is not None:
            result['versionEnabled'] = self.version_enabled
        result['versionedHttpApis'] = []
        if self.versioned_http_apis is not None:
            for k in self.versioned_http_apis:
                result['versionedHttpApis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('versionEnabled') is not None:
            self.version_enabled = m.get('versionEnabled')
        self.versioned_http_apis = []
        if m.get('versionedHttpApis') is not None:
            for k in m.get('versionedHttpApis'):
                temp_model = HttpApiApiInfo()
                self.versioned_http_apis.append(temp_model.from_map(k))
        return self


class HttpApiParameter(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        example_value: str = None,
        name: str = None,
        required: bool = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.example_value = example_value
        # This parameter is required.
        self.name = name
        self.required = required
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.description is not None:
            result['description'] = self.description
        if self.example_value is not None:
            result['exampleValue'] = self.example_value
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exampleValue') is not None:
            self.example_value = m.get('exampleValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class HttpApiRequestContractBody(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        description: str = None,
        example: str = None,
        json_schema: str = None,
    ):
        self.content_type = content_type
        self.description = description
        self.example = example
        self.json_schema = json_schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.description is not None:
            result['description'] = self.description
        if self.example is not None:
            result['example'] = self.example
        if self.json_schema is not None:
            result['jsonSchema'] = self.json_schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('example') is not None:
            self.example = m.get('example')
        if m.get('jsonSchema') is not None:
            self.json_schema = m.get('jsonSchema')
        return self


class HttpApiRequestContract(TeaModel):
    def __init__(
        self,
        body: HttpApiRequestContractBody = None,
        header_parameters: List[HttpApiParameter] = None,
        path_parameters: List[HttpApiParameter] = None,
        query_parameters: List[HttpApiParameter] = None,
    ):
        self.body = body
        self.header_parameters = header_parameters
        self.path_parameters = path_parameters
        self.query_parameters = query_parameters

    def validate(self):
        if self.body:
            self.body.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.path_parameters:
            for k in self.path_parameters:
                if k:
                    k.validate()
        if self.query_parameters:
            for k in self.query_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        result['headerParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['headerParameters'].append(k.to_map() if k else None)
        result['pathParameters'] = []
        if self.path_parameters is not None:
            for k in self.path_parameters:
                result['pathParameters'].append(k.to_map() if k else None)
        result['queryParameters'] = []
        if self.query_parameters is not None:
            for k in self.query_parameters:
                result['queryParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = HttpApiRequestContractBody()
            self.body = temp_model.from_map(m['body'])
        self.header_parameters = []
        if m.get('headerParameters') is not None:
            for k in m.get('headerParameters'):
                temp_model = HttpApiParameter()
                self.header_parameters.append(temp_model.from_map(k))
        self.path_parameters = []
        if m.get('pathParameters') is not None:
            for k in m.get('pathParameters'):
                temp_model = HttpApiParameter()
                self.path_parameters.append(temp_model.from_map(k))
        self.query_parameters = []
        if m.get('queryParameters') is not None:
            for k in m.get('queryParameters'):
                temp_model = HttpApiParameter()
                self.query_parameters.append(temp_model.from_map(k))
        return self


class HttpApiResponseContractItems(TeaModel):
    def __init__(
        self,
        code: int = None,
        description: str = None,
        example: str = None,
        json_schema: str = None,
    ):
        self.code = code
        self.description = description
        self.example = example
        self.json_schema = json_schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.example is not None:
            result['example'] = self.example
        if self.json_schema is not None:
            result['jsonSchema'] = self.json_schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('example') is not None:
            self.example = m.get('example')
        if m.get('jsonSchema') is not None:
            self.json_schema = m.get('jsonSchema')
        return self


class HttpApiResponseContract(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        items: List[HttpApiResponseContractItems] = None,
    ):
        # This parameter is required.
        self.content_type = content_type
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = HttpApiResponseContractItems()
                self.items.append(temp_model.from_map(k))
        return self


class HttpApiOperation(TeaModel):
    def __init__(
        self,
        auth_config: AuthConfig = None,
        deploy_configs: List[HttpApiDeployConfig] = None,
        description: str = None,
        enable_auth: bool = None,
        method: str = None,
        mock: HttpApiMockContract = None,
        name: str = None,
        path: str = None,
        request: HttpApiRequestContract = None,
        response: HttpApiResponseContract = None,
    ):
        self.auth_config = auth_config
        self.deploy_configs = deploy_configs
        self.description = description
        self.enable_auth = enable_auth
        # This parameter is required.
        self.method = method
        self.mock = mock
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.path = path
        self.request = request
        self.response = response

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()
        if self.mock:
            self.mock.validate()
        if self.request:
            self.request.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth
        if self.method is not None:
            result['method'] = self.method
        if self.mock is not None:
            result['mock'] = self.mock.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.path is not None:
            result['path'] = self.path
        if self.request is not None:
            result['request'] = self.request.to_map()
        if self.response is not None:
            result['response'] = self.response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('mock') is not None:
            temp_model = HttpApiMockContract()
            self.mock = temp_model.from_map(m['mock'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('request') is not None:
            temp_model = HttpApiRequestContract()
            self.request = temp_model.from_map(m['request'])
        if m.get('response') is not None:
            temp_model = HttpApiResponseContract()
            self.response = temp_model.from_map(m['response'])
        return self


class HttpApiOperationInfo(TeaModel):
    def __init__(
        self,
        auth_config: AuthConfig = None,
        create_timestamp: int = None,
        deploy_configs: List[HttpApiDeployConfig] = None,
        description: str = None,
        enable_auth: bool = None,
        method: str = None,
        mock: HttpApiMockContract = None,
        name: str = None,
        operation_id: str = None,
        path: str = None,
        request: HttpApiRequestContract = None,
        response: HttpApiResponseContract = None,
        status: str = None,
    ):
        self.auth_config = auth_config
        self.create_timestamp = create_timestamp
        self.deploy_configs = deploy_configs
        self.description = description
        self.enable_auth = enable_auth
        self.method = method
        self.mock = mock
        self.name = name
        self.operation_id = operation_id
        self.path = path
        self.request = request
        self.response = response
        self.status = status

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()
        if self.mock:
            self.mock.validate()
        if self.request:
            self.request.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth
        if self.method is not None:
            result['method'] = self.method
        if self.mock is not None:
            result['mock'] = self.mock.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        if self.path is not None:
            result['path'] = self.path
        if self.request is not None:
            result['request'] = self.request.to_map()
        if self.response is not None:
            result['response'] = self.response.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('mock') is not None:
            temp_model = HttpApiMockContract()
            self.mock = temp_model.from_map(m['mock'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('request') is not None:
            temp_model = HttpApiRequestContract()
            self.request = temp_model.from_map(m['request'])
        if m.get('response') is not None:
            temp_model = HttpApiResponseContract()
            self.response = temp_model.from_map(m['response'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        namespace: str = None,
        port: int = None,
        protocol: str = None,
        weight: str = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.name = name
        self.namespace = namespace
        self.port = port
        self.protocol = protocol
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        qualifier: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.name = name
        self.qualifier = qualifier
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        group_name: str = None,
        match: HttpApiBackendMatchConditions = None,
        name: str = None,
        namespace: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.group_name = group_name
        self.match = match
        self.name = name
        self.namespace = namespace
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoCloudProductConfig(TeaModel):
    def __init__(
        self,
        cloud_product_type: str = None,
        container_service_configs: List[HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs] = None,
        function_configs: List[HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs] = None,
        mse_nacos_configs: List[HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs] = None,
    ):
        self.cloud_product_type = cloud_product_type
        self.container_service_configs = container_service_configs
        self.function_configs = function_configs
        self.mse_nacos_configs = mse_nacos_configs

    def validate(self):
        if self.container_service_configs:
            for k in self.container_service_configs:
                if k:
                    k.validate()
        if self.function_configs:
            for k in self.function_configs:
                if k:
                    k.validate()
        if self.mse_nacos_configs:
            for k in self.mse_nacos_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_product_type is not None:
            result['cloudProductType'] = self.cloud_product_type
        result['containerServiceConfigs'] = []
        if self.container_service_configs is not None:
            for k in self.container_service_configs:
                result['containerServiceConfigs'].append(k.to_map() if k else None)
        result['functionConfigs'] = []
        if self.function_configs is not None:
            for k in self.function_configs:
                result['functionConfigs'].append(k.to_map() if k else None)
        result['mseNacosConfigs'] = []
        if self.mse_nacos_configs is not None:
            for k in self.mse_nacos_configs:
                result['mseNacosConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloudProductType') is not None:
            self.cloud_product_type = m.get('cloudProductType')
        self.container_service_configs = []
        if m.get('containerServiceConfigs') is not None:
            for k in m.get('containerServiceConfigs'):
                temp_model = HttpApiPublishRevisionInfoCloudProductConfigContainerServiceConfigs()
                self.container_service_configs.append(temp_model.from_map(k))
        self.function_configs = []
        if m.get('functionConfigs') is not None:
            for k in m.get('functionConfigs'):
                temp_model = HttpApiPublishRevisionInfoCloudProductConfigFunctionConfigs()
                self.function_configs.append(temp_model.from_map(k))
        self.mse_nacos_configs = []
        if m.get('mseNacosConfigs') is not None:
            for k in m.get('mseNacosConfigs'):
                temp_model = HttpApiPublishRevisionInfoCloudProductConfigMseNacosConfigs()
                self.mse_nacos_configs.append(temp_model.from_map(k))
        return self


class HttpApiPublishRevisionInfoDnsConfigs(TeaModel):
    def __init__(
        self,
        dns_list: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.dns_list = dns_list
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_list is not None:
            result['dnsList'] = self.dns_list
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dnsList') is not None:
            self.dns_list = m.get('dnsList')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
    ):
        self.gateway_id = gateway_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class HttpApiPublishRevisionInfoEnvironmentInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        gateway_info: HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo = None,
        name: str = None,
    ):
        self.alias = alias
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayInfo') is not None:
            temp_model = HttpApiPublishRevisionInfoEnvironmentInfoGatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class HttpApiPublishRevisionInfoServiceConfigs(TeaModel):
    def __init__(
        self,
        gateway_service_id: str = None,
        match: HttpApiBackendMatchConditions = None,
        port: int = None,
        protocol: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.gateway_service_id = gateway_service_id
        self.match = match
        self.port = port
        self.protocol = protocol
        self.version = version
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_service_id is not None:
            result['gatewayServiceId'] = self.gateway_service_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayServiceId') is not None:
            self.gateway_service_id = m.get('gatewayServiceId')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfoVipConfigs(TeaModel):
    def __init__(
        self,
        endpoints: List[str] = None,
        match: HttpApiBackendMatchConditions = None,
        weight: int = None,
    ):
        self.endpoints = endpoints
        self.match = match
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoints is not None:
            result['endpoints'] = self.endpoints
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class HttpApiPublishRevisionInfo(TeaModel):
    def __init__(
        self,
        backend_scene: str = None,
        backend_type: str = None,
        cloud_product_config: HttpApiPublishRevisionInfoCloudProductConfig = None,
        create_timestamp: int = None,
        custom_domains: List[HttpApiDomainInfo] = None,
        dns_configs: List[HttpApiPublishRevisionInfoDnsConfigs] = None,
        environment_info: HttpApiPublishRevisionInfoEnvironmentInfo = None,
        is_current_version: bool = None,
        operations: List[HttpApiOperationInfo] = None,
        revision_id: str = None,
        service_configs: List[HttpApiPublishRevisionInfoServiceConfigs] = None,
        sub_domains: List[HttpApiDomainInfo] = None,
        vip_configs: List[HttpApiPublishRevisionInfoVipConfigs] = None,
    ):
        self.backend_scene = backend_scene
        self.backend_type = backend_type
        self.cloud_product_config = cloud_product_config
        self.create_timestamp = create_timestamp
        self.custom_domains = custom_domains
        self.dns_configs = dns_configs
        self.environment_info = environment_info
        self.is_current_version = is_current_version
        self.operations = operations
        self.revision_id = revision_id
        self.service_configs = service_configs
        self.sub_domains = sub_domains
        self.vip_configs = vip_configs

    def validate(self):
        if self.cloud_product_config:
            self.cloud_product_config.validate()
        if self.custom_domains:
            for k in self.custom_domains:
                if k:
                    k.validate()
        if self.dns_configs:
            for k in self.dns_configs:
                if k:
                    k.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.operations:
            for k in self.operations:
                if k:
                    k.validate()
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()
        if self.sub_domains:
            for k in self.sub_domains:
                if k:
                    k.validate()
        if self.vip_configs:
            for k in self.vip_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene
        if self.backend_type is not None:
            result['backendType'] = self.backend_type
        if self.cloud_product_config is not None:
            result['cloudProductConfig'] = self.cloud_product_config.to_map()
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        result['customDomains'] = []
        if self.custom_domains is not None:
            for k in self.custom_domains:
                result['customDomains'].append(k.to_map() if k else None)
        result['dnsConfigs'] = []
        if self.dns_configs is not None:
            for k in self.dns_configs:
                result['dnsConfigs'].append(k.to_map() if k else None)
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()
        if self.is_current_version is not None:
            result['isCurrentVersion'] = self.is_current_version
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
        if self.revision_id is not None:
            result['revisionId'] = self.revision_id
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        result['subDomains'] = []
        if self.sub_domains is not None:
            for k in self.sub_domains:
                result['subDomains'].append(k.to_map() if k else None)
        result['vipConfigs'] = []
        if self.vip_configs is not None:
            for k in self.vip_configs:
                result['vipConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('backendType') is not None:
            self.backend_type = m.get('backendType')
        if m.get('cloudProductConfig') is not None:
            temp_model = HttpApiPublishRevisionInfoCloudProductConfig()
            self.cloud_product_config = temp_model.from_map(m['cloudProductConfig'])
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k in m.get('customDomains'):
                temp_model = HttpApiDomainInfo()
                self.custom_domains.append(temp_model.from_map(k))
        self.dns_configs = []
        if m.get('dnsConfigs') is not None:
            for k in m.get('dnsConfigs'):
                temp_model = HttpApiPublishRevisionInfoDnsConfigs()
                self.dns_configs.append(temp_model.from_map(k))
        if m.get('environmentInfo') is not None:
            temp_model = HttpApiPublishRevisionInfoEnvironmentInfo()
            self.environment_info = temp_model.from_map(m['environmentInfo'])
        if m.get('isCurrentVersion') is not None:
            self.is_current_version = m.get('isCurrentVersion')
        self.operations = []
        if m.get('operations') is not None:
            for k in m.get('operations'):
                temp_model = HttpApiOperationInfo()
                self.operations.append(temp_model.from_map(k))
        if m.get('revisionId') is not None:
            self.revision_id = m.get('revisionId')
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = HttpApiPublishRevisionInfoServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k in m.get('subDomains'):
                temp_model = HttpApiDomainInfo()
                self.sub_domains.append(temp_model.from_map(k))
        self.vip_configs = []
        if m.get('vipConfigs') is not None:
            for k in m.get('vipConfigs'):
                temp_model = HttpApiPublishRevisionInfoVipConfigs()
                self.vip_configs.append(temp_model.from_map(k))
        return self


class HttpApiVersionConfig(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        header_name: str = None,
        query_name: str = None,
        scheme: str = None,
        version: str = None,
    ):
        self.enable = enable
        self.header_name = header_name
        self.query_name = query_name
        self.scheme = scheme
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.header_name is not None:
            result['headerName'] = self.header_name
        if self.query_name is not None:
            result['queryName'] = self.query_name
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('headerName') is not None:
            self.header_name = m.get('headerName')
        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class HttpDubboTranscoderMothedMapListParamMapsList(TeaModel):
    def __init__(
        self,
        extract_key: str = None,
        extract_key_spec: str = None,
        mapping_type: str = None,
    ):
        self.extract_key = extract_key
        self.extract_key_spec = extract_key_spec
        self.mapping_type = mapping_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extract_key is not None:
            result['extractKey'] = self.extract_key
        if self.extract_key_spec is not None:
            result['extractKeySpec'] = self.extract_key_spec
        if self.mapping_type is not None:
            result['mappingType'] = self.mapping_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extractKey') is not None:
            self.extract_key = m.get('extractKey')
        if m.get('extractKeySpec') is not None:
            self.extract_key_spec = m.get('extractKeySpec')
        if m.get('mappingType') is not None:
            self.mapping_type = m.get('mappingType')
        return self


class HttpDubboTranscoderMothedMapList(TeaModel):
    def __init__(
        self,
        dubbo_mothed_name: str = None,
        http_mothed: str = None,
        mothedpath: str = None,
        param_maps_list: List[HttpDubboTranscoderMothedMapListParamMapsList] = None,
        pass_through_all_headers: str = None,
        pass_through_list: List[str] = None,
    ):
        self.dubbo_mothed_name = dubbo_mothed_name
        self.http_mothed = http_mothed
        self.mothedpath = mothedpath
        self.param_maps_list = param_maps_list
        self.pass_through_all_headers = pass_through_all_headers
        self.pass_through_list = pass_through_list

    def validate(self):
        if self.param_maps_list:
            for k in self.param_maps_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_mothed_name is not None:
            result['dubboMothedName'] = self.dubbo_mothed_name
        if self.http_mothed is not None:
            result['httpMothed'] = self.http_mothed
        if self.mothedpath is not None:
            result['mothedpath'] = self.mothedpath
        result['paramMapsList'] = []
        if self.param_maps_list is not None:
            for k in self.param_maps_list:
                result['paramMapsList'].append(k.to_map() if k else None)
        if self.pass_through_all_headers is not None:
            result['passThroughAllHeaders'] = self.pass_through_all_headers
        if self.pass_through_list is not None:
            result['passThroughList'] = self.pass_through_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dubboMothedName') is not None:
            self.dubbo_mothed_name = m.get('dubboMothedName')
        if m.get('httpMothed') is not None:
            self.http_mothed = m.get('httpMothed')
        if m.get('mothedpath') is not None:
            self.mothedpath = m.get('mothedpath')
        self.param_maps_list = []
        if m.get('paramMapsList') is not None:
            for k in m.get('paramMapsList'):
                temp_model = HttpDubboTranscoderMothedMapListParamMapsList()
                self.param_maps_list.append(temp_model.from_map(k))
        if m.get('passThroughAllHeaders') is not None:
            self.pass_through_all_headers = m.get('passThroughAllHeaders')
        if m.get('passThroughList') is not None:
            self.pass_through_list = m.get('passThroughList')
        return self


class HttpDubboTranscoder(TeaModel):
    def __init__(
        self,
        dubbo_service_group: str = None,
        dubbo_service_name: str = None,
        dubbo_service_version: str = None,
        mothed_map_list: List[HttpDubboTranscoderMothedMapList] = None,
    ):
        self.dubbo_service_group = dubbo_service_group
        self.dubbo_service_name = dubbo_service_name
        self.dubbo_service_version = dubbo_service_version
        self.mothed_map_list = mothed_map_list

    def validate(self):
        if self.mothed_map_list:
            for k in self.mothed_map_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_service_group is not None:
            result['dubboServiceGroup'] = self.dubbo_service_group
        if self.dubbo_service_name is not None:
            result['dubboServiceName'] = self.dubbo_service_name
        if self.dubbo_service_version is not None:
            result['dubboServiceVersion'] = self.dubbo_service_version
        result['mothedMapList'] = []
        if self.mothed_map_list is not None:
            for k in self.mothed_map_list:
                result['mothedMapList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dubboServiceGroup') is not None:
            self.dubbo_service_group = m.get('dubboServiceGroup')
        if m.get('dubboServiceName') is not None:
            self.dubbo_service_name = m.get('dubboServiceName')
        if m.get('dubboServiceVersion') is not None:
            self.dubbo_service_version = m.get('dubboServiceVersion')
        self.mothed_map_list = []
        if m.get('mothedMapList') is not None:
            for k in m.get('mothedMapList'):
                temp_model = HttpDubboTranscoderMothedMapList()
                self.mothed_map_list.append(temp_model.from_map(k))
        return self


class HttpRouteDomainInfos(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class HttpRouteEnvironmentInfoGatewayInfo(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
    ):
        self.gateway_id = gateway_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class HttpRouteEnvironmentInfoSubDomains(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.network_type = network_type
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.name is not None:
            result['name'] = self.name
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class HttpRouteEnvironmentInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        gateway_info: HttpRouteEnvironmentInfoGatewayInfo = None,
        name: str = None,
        sub_domains: List[HttpRouteEnvironmentInfoSubDomains] = None,
    ):
        self.alias = alias
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.sub_domains = sub_domains

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.sub_domains:
            for k in self.sub_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        result['subDomains'] = []
        if self.sub_domains is not None:
            for k in self.sub_domains:
                result['subDomains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayInfo') is not None:
            temp_model = HttpRouteEnvironmentInfoGatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        self.sub_domains = []
        if m.get('subDomains') is not None:
            for k in m.get('subDomains'):
                temp_model = HttpRouteEnvironmentInfoSubDomains()
                self.sub_domains.append(temp_model.from_map(k))
        return self


class HttpRoute(TeaModel):
    def __init__(
        self,
        backend: Backend = None,
        create_timestamp: int = None,
        deploy_status: str = None,
        description: str = None,
        domain_infos: List[HttpRouteDomainInfos] = None,
        environment_info: HttpRouteEnvironmentInfo = None,
        gateway_status: Dict[str, str] = None,
        match: HttpRouteMatch = None,
        name: str = None,
        route_id: str = None,
        update_timestamp: int = None,
    ):
        self.backend = backend
        self.create_timestamp = create_timestamp
        self.deploy_status = deploy_status
        self.description = description
        self.domain_infos = domain_infos
        self.environment_info = environment_info
        self.gateway_status = gateway_status
        self.match = match
        self.name = name
        self.route_id = route_id
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.backend:
            self.backend.validate()
        if self.domain_infos:
            for k in self.domain_infos:
                if k:
                    k.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['backend'] = self.backend.to_map()
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status
        if self.description is not None:
            result['description'] = self.description
        result['domainInfos'] = []
        if self.domain_infos is not None:
            for k in self.domain_infos:
                result['domainInfos'].append(k.to_map() if k else None)
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()
        if self.gateway_status is not None:
            result['gatewayStatus'] = self.gateway_status
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.route_id is not None:
            result['routeId'] = self.route_id
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backend') is not None:
            temp_model = Backend()
            self.backend = temp_model.from_map(m['backend'])
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.domain_infos = []
        if m.get('domainInfos') is not None:
            for k in m.get('domainInfos'):
                temp_model = HttpRouteDomainInfos()
                self.domain_infos.append(temp_model.from_map(k))
        if m.get('environmentInfo') is not None:
            temp_model = HttpRouteEnvironmentInfo()
            self.environment_info = temp_model.from_map(m['environmentInfo'])
        if m.get('gatewayStatus') is not None:
            self.gateway_status = m.get('gatewayStatus')
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class JwtIdentityConfigJwtPayloadConfig(TeaModel):
    def __init__(
        self,
        payload_key_name: str = None,
        payload_key_value: str = None,
    ):
        self.payload_key_name = payload_key_name
        self.payload_key_value = payload_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payload_key_name is not None:
            result['payloadKeyName'] = self.payload_key_name
        if self.payload_key_value is not None:
            result['payloadKeyValue'] = self.payload_key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('payloadKeyName') is not None:
            self.payload_key_name = m.get('payloadKeyName')
        if m.get('payloadKeyValue') is not None:
            self.payload_key_value = m.get('payloadKeyValue')
        return self


class JwtIdentityConfigJwtTokenConfig(TeaModel):
    def __init__(
        self,
        key: str = None,
        pass_: bool = None,
        position: str = None,
        prefix: str = None,
    ):
        self.key = key
        self.pass_ = pass_
        self.position = position
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.pass_ is not None:
            result['pass'] = self.pass_
        if self.position is not None:
            result['position'] = self.position
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class JwtIdentityConfig(TeaModel):
    def __init__(
        self,
        jwks: str = None,
        jwt_payload_config: JwtIdentityConfigJwtPayloadConfig = None,
        jwt_token_config: JwtIdentityConfigJwtTokenConfig = None,
        secret_type: str = None,
        type: str = None,
    ):
        self.jwks = jwks
        self.jwt_payload_config = jwt_payload_config
        self.jwt_token_config = jwt_token_config
        self.secret_type = secret_type
        self.type = type

    def validate(self):
        if self.jwt_payload_config:
            self.jwt_payload_config.validate()
        if self.jwt_token_config:
            self.jwt_token_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwks is not None:
            result['jwks'] = self.jwks
        if self.jwt_payload_config is not None:
            result['jwtPayloadConfig'] = self.jwt_payload_config.to_map()
        if self.jwt_token_config is not None:
            result['jwtTokenConfig'] = self.jwt_token_config.to_map()
        if self.secret_type is not None:
            result['secretType'] = self.secret_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jwks') is not None:
            self.jwks = m.get('jwks')
        if m.get('jwtPayloadConfig') is not None:
            temp_model = JwtIdentityConfigJwtPayloadConfig()
            self.jwt_payload_config = temp_model.from_map(m['jwtPayloadConfig'])
        if m.get('jwtTokenConfig') is not None:
            temp_model = JwtIdentityConfigJwtTokenConfig()
            self.jwt_token_config = temp_model.from_map(m['jwtTokenConfig'])
        if m.get('secretType') is not None:
            self.secret_type = m.get('secretType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ParentResourceInfo(TeaModel):
    def __init__(
        self,
        api_info: HttpApiApiInfo = None,
        resource_type: str = None,
    ):
        self.api_info = api_info
        self.resource_type = resource_type

    def validate(self):
        if self.api_info:
            self.api_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_info is not None:
            result['apiInfo'] = self.api_info.to_map()
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiInfo') is not None:
            temp_model = HttpApiApiInfo()
            self.api_info = temp_model.from_map(m['apiInfo'])
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class PluginClassInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        config_example: str = None,
        description: str = None,
        execute_priority: int = None,
        execute_stage: str = None,
        image_name: str = None,
        inner_plugin: bool = None,
        mode: str = None,
        name: str = None,
        plugin_class_id: str = None,
        source: str = None,
        supported_min_gateway_version: str = None,
        type: str = None,
        version: str = None,
        version_description: str = None,
        wasm_language: str = None,
        wasm_url: str = None,
    ):
        self.alias = alias
        self.config_example = config_example
        self.description = description
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.image_name = image_name
        self.inner_plugin = inner_plugin
        self.mode = mode
        self.name = name
        self.plugin_class_id = plugin_class_id
        self.source = source
        self.supported_min_gateway_version = supported_min_gateway_version
        self.type = type
        self.version = version
        self.version_description = version_description
        self.wasm_language = wasm_language
        self.wasm_url = wasm_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.config_example is not None:
            result['configExample'] = self.config_example
        if self.description is not None:
            result['description'] = self.description
        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority
        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.inner_plugin is not None:
            result['innerPlugin'] = self.inner_plugin
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id
        if self.source is not None:
            result['source'] = self.source
        if self.supported_min_gateway_version is not None:
            result['supportedMinGatewayVersion'] = self.supported_min_gateway_version
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        if self.version_description is not None:
            result['versionDescription'] = self.version_description
        if self.wasm_language is not None:
            result['wasmLanguage'] = self.wasm_language
        if self.wasm_url is not None:
            result['wasmUrl'] = self.wasm_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('configExample') is not None:
            self.config_example = m.get('configExample')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')
        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('innerPlugin') is not None:
            self.inner_plugin = m.get('innerPlugin')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('supportedMinGatewayVersion') is not None:
            self.supported_min_gateway_version = m.get('supportedMinGatewayVersion')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')
        if m.get('wasmLanguage') is not None:
            self.wasm_language = m.get('wasmLanguage')
        if m.get('wasmUrl') is not None:
            self.wasm_url = m.get('wasmUrl')
        return self


class PolicyClassInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        attachable_resource_types: List[str] = None,
        class_id: str = None,
        config_example: str = None,
        deprecated: bool = None,
        description: str = None,
        direction: str = None,
        enable_log: bool = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.alias = alias
        self.attachable_resource_types = attachable_resource_types
        self.class_id = class_id
        self.config_example = config_example
        self.deprecated = deprecated
        self.description = description
        self.direction = direction
        self.enable_log = enable_log
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.attachable_resource_types is not None:
            result['attachableResourceTypes'] = self.attachable_resource_types
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.config_example is not None:
            result['configExample'] = self.config_example
        if self.deprecated is not None:
            result['deprecated'] = self.deprecated
        if self.description is not None:
            result['description'] = self.description
        if self.direction is not None:
            result['direction'] = self.direction
        if self.enable_log is not None:
            result['enableLog'] = self.enable_log
        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority
        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('attachableResourceTypes') is not None:
            self.attachable_resource_types = m.get('attachableResourceTypes')
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('configExample') is not None:
            self.config_example = m.get('configExample')
        if m.get('deprecated') is not None:
            self.deprecated = m.get('deprecated')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('enableLog') is not None:
            self.enable_log = m.get('enableLog')
        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')
        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class PolicyDetailInfo(TeaModel):
    def __init__(
        self,
        class_id: str = None,
        class_name: str = None,
        config: str = None,
        description: str = None,
        name: str = None,
        policy_id: str = None,
    ):
        self.class_id = class_id
        self.class_name = class_name
        self.config = config
        self.description = description
        self.name = name
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['classId'] = self.class_id
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classId') is not None:
            self.class_id = m.get('classId')
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class PolicyInfo(TeaModel):
    def __init__(
        self,
        attachments: List[Attachment] = None,
        class_alias: str = None,
        class_name: str = None,
        config: str = None,
        direction: str = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        policy_id: str = None,
        type: str = None,
    ):
        self.attachments = attachments
        self.class_alias = class_alias
        self.class_name = class_name
        self.config = config
        self.direction = direction
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.name = name
        self.policy_id = policy_id
        self.type = type

    def validate(self):
        if self.attachments:
            for k in self.attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['attachments'] = []
        if self.attachments is not None:
            for k in self.attachments:
                result['attachments'].append(k.to_map() if k else None)
        if self.class_alias is not None:
            result['classAlias'] = self.class_alias
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.config is not None:
            result['config'] = self.config
        if self.direction is not None:
            result['direction'] = self.direction
        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority
        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage
        if self.name is not None:
            result['name'] = self.name
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k in m.get('attachments'):
                temp_model = Attachment()
                self.attachments.append(temp_model.from_map(k))
        if m.get('classAlias') is not None:
            self.class_alias = m.get('classAlias')
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')
        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ResourceInfo(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        resource_version: str = None,
    ):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.resource_version = resource_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_name is not None:
            result['resourceName'] = self.resource_name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.resource_version is not None:
            result['resourceVersion'] = self.resource_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('resourceVersion') is not None:
            self.resource_version = m.get('resourceVersion')
        return self


class ResourceStatistic(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        self.resource_count = resource_count
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ServicePorts(TeaModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
    ):
        self.name = name
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class ServiceHealthCheck(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        healthy_threshold: int = None,
        http_host: str = None,
        http_path: str = None,
        interval: int = None,
        protocol: str = None,
        timeout: int = None,
        unhealthy_threshold: int = None,
    ):
        self.enable = enable
        self.healthy_threshold = healthy_threshold
        self.http_host = http_host
        self.http_path = http_path
        self.interval = interval
        self.protocol = protocol
        self.timeout = timeout
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold
        if self.http_host is not None:
            result['httpHost'] = self.http_host
        if self.http_path is not None:
            result['httpPath'] = self.http_path
        if self.interval is not None:
            result['interval'] = self.interval
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')
        if m.get('httpHost') is not None:
            self.http_host = m.get('httpHost')
        if m.get('httpPath') is not None:
            self.http_path = m.get('httpPath')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')
        return self


class Service(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        ai_service_config: AiServiceConfig = None,
        create_timestamp: int = None,
        gateway_id: str = None,
        group_name: str = None,
        health_check: ServiceHealthCheck = None,
        health_status: str = None,
        name: str = None,
        namespace: str = None,
        ports: List[ServicePorts] = None,
        protocol: str = None,
        qualifier: str = None,
        resource_group_id: str = None,
        service_id: str = None,
        source_type: str = None,
        unhealthy_endpoints: List[str] = None,
        update_timestamp: int = None,
    ):
        self.addresses = addresses
        self.ai_service_config = ai_service_config
        self.create_timestamp = create_timestamp
        self.gateway_id = gateway_id
        self.group_name = group_name
        self.health_check = health_check
        self.health_status = health_status
        self.name = name
        self.namespace = namespace
        self.ports = ports
        self.protocol = protocol
        self.qualifier = qualifier
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.source_type = source_type
        self.unhealthy_endpoints = unhealthy_endpoints
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.ai_service_config:
            self.ai_service_config.validate()
        if self.health_check:
            self.health_check.validate()
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['addresses'] = self.addresses
        if self.ai_service_config is not None:
            result['aiServiceConfig'] = self.ai_service_config.to_map()
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.health_check is not None:
            result['healthCheck'] = self.health_check.to_map()
        if self.health_status is not None:
            result['healthStatus'] = self.health_status
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.unhealthy_endpoints is not None:
            result['unhealthyEndpoints'] = self.unhealthy_endpoints
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')
        if m.get('aiServiceConfig') is not None:
            temp_model = AiServiceConfig()
            self.ai_service_config = temp_model.from_map(m['aiServiceConfig'])
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('healthCheck') is not None:
            temp_model = ServiceHealthCheck()
            self.health_check = temp_model.from_map(m['healthCheck'])
        if m.get('healthStatus') is not None:
            self.health_status = m.get('healthStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = ServicePorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('unhealthyEndpoints') is not None:
            self.unhealthy_endpoints = m.get('unhealthyEndpoints')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class ServiceLinkedRole(TeaModel):
    def __init__(
        self,
        arn: str = None,
        assume_role_policy_document: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
    ):
        self.arn = arn
        self.assume_role_policy_document = assume_role_policy_document
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['assumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['createDate'] = self.create_date
        if self.description is not None:
            result['description'] = self.description
        if self.is_service_linked_role is not None:
            result['isServiceLinkedRole'] = self.is_service_linked_role
        if self.role_id is not None:
            result['roleId'] = self.role_id
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.role_principal_name is not None:
            result['rolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('assumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('assumeRolePolicyDocument')
        if m.get('createDate') is not None:
            self.create_date = m.get('createDate')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('isServiceLinkedRole')
        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('rolePrincipalName') is not None:
            self.role_principal_name = m.get('rolePrincipalName')
        return self


class SslCertMetaInfo(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        cert_id: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        domain: str = None,
        domain_match_cert: bool = None,
        fingerprint: str = None,
        instance_id: str = None,
        is_chain_completed: bool = None,
        issuer: str = None,
        key_size: str = None,
        md_5: str = None,
        not_after_timestamp: int = None,
        not_before_timestamp: int = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
    ):
        self.algorithm = algorithm
        self.cert_id = cert_id
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.common_name = common_name
        self.domain = domain
        self.domain_match_cert = domain_match_cert
        self.fingerprint = fingerprint
        self.instance_id = instance_id
        self.is_chain_completed = is_chain_completed
        self.issuer = issuer
        self.key_size = key_size
        self.md_5 = md_5
        self.not_after_timestamp = not_after_timestamp
        self.not_before_timestamp = not_before_timestamp
        self.sans = sans
        self.serial_no = serial_no
        self.sha_2 = sha_2
        self.sign_algorithm = sign_algorithm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.cert_id is not None:
            result['certId'] = self.cert_id
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['certName'] = self.cert_name
        if self.common_name is not None:
            result['commonName'] = self.common_name
        if self.domain is not None:
            result['domain'] = self.domain
        if self.domain_match_cert is not None:
            result['domainMatchCert'] = self.domain_match_cert
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_chain_completed is not None:
            result['isChainCompleted'] = self.is_chain_completed
        if self.issuer is not None:
            result['issuer'] = self.issuer
        if self.key_size is not None:
            result['keySize'] = self.key_size
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.not_after_timestamp is not None:
            result['notAfterTimestamp'] = self.not_after_timestamp
        if self.not_before_timestamp is not None:
            result['notBeforeTimestamp'] = self.not_before_timestamp
        if self.sans is not None:
            result['sans'] = self.sans
        if self.serial_no is not None:
            result['serialNo'] = self.serial_no
        if self.sha_2 is not None:
            result['sha2'] = self.sha_2
        if self.sign_algorithm is not None:
            result['signAlgorithm'] = self.sign_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('certId') is not None:
            self.cert_id = m.get('certId')
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')
        if m.get('commonName') is not None:
            self.common_name = m.get('commonName')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('domainMatchCert') is not None:
            self.domain_match_cert = m.get('domainMatchCert')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isChainCompleted') is not None:
            self.is_chain_completed = m.get('isChainCompleted')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        if m.get('keySize') is not None:
            self.key_size = m.get('keySize')
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('notAfterTimestamp') is not None:
            self.not_after_timestamp = m.get('notAfterTimestamp')
        if m.get('notBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('notBeforeTimestamp')
        if m.get('sans') is not None:
            self.sans = m.get('sans')
        if m.get('serialNo') is not None:
            self.serial_no = m.get('serialNo')
        if m.get('sha2') is not None:
            self.sha_2 = m.get('sha2')
        if m.get('signAlgorithm') is not None:
            self.sign_algorithm = m.get('signAlgorithm')
        return self


class TlsCipherSuitesConfigTlsCipherSuite(TeaModel):
    def __init__(
        self,
        name: str = None,
        support_versions: List[str] = None,
    ):
        self.name = name
        self.support_versions = support_versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.support_versions is not None:
            result['supportVersions'] = self.support_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('supportVersions') is not None:
            self.support_versions = m.get('supportVersions')
        return self


class TlsCipherSuitesConfig(TeaModel):
    def __init__(
        self,
        config_type: str = None,
        tls_cipher_suite: List[TlsCipherSuitesConfigTlsCipherSuite] = None,
    ):
        self.config_type = config_type
        self.tls_cipher_suite = tls_cipher_suite

    def validate(self):
        if self.tls_cipher_suite:
            for k in self.tls_cipher_suite:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_type is not None:
            result['configType'] = self.config_type
        result['tlsCipherSuite'] = []
        if self.tls_cipher_suite is not None:
            for k in self.tls_cipher_suite:
                result['tlsCipherSuite'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        self.tls_cipher_suite = []
        if m.get('tlsCipherSuite') is not None:
            for k in m.get('tlsCipherSuite'):
                temp_model = TlsCipherSuitesConfigTlsCipherSuite()
                self.tls_cipher_suite.append(temp_model.from_map(k))
        return self


class AddGatewaySecurityGroupRuleRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        port_ranges: List[str] = None,
        security_group_id: str = None,
    ):
        # Description of the security group rule.
        self.description = description
        # Port ranges.
        self.port_ranges = port_ranges
        # Security group ID.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.port_ranges is not None:
            result['portRanges'] = self.port_ranges
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('portRanges') is not None:
            self.port_ranges = m.get('portRanges')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self


class AddGatewaySecurityGroupRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddGatewaySecurityGroupRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddGatewaySecurityGroupRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddGatewaySecurityGroupRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service: str = None,
    ):
        # Target resource group ID.
        self.resource_group_id = resource_group_id
        # Resource ID
        self.resource_id = resource_id
        # Resource type
        self.resource_type = resource_type
        # Service name, fixed value apig
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Request ID.
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        ca_cert_identifier: str = None,
        cert_identifier: str = None,
        client_cacert: str = None,
        force_https: bool = None,
        gateway_type: str = None,
        http_2option: str = None,
        m_tlsenabled: bool = None,
        name: str = None,
        protocol: str = None,
        resource_group_id: str = None,
        tls_cipher_suites_config: TlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        # The CA certificate ID.
        self.ca_cert_identifier = ca_cert_identifier
        # The certificate ID.
        self.cert_identifier = cert_identifier
        # The client CA certificate.
        self.client_cacert = client_cacert
        # Specifies whether to enable forcible HTTPS redirection.
        self.force_https = force_https
        self.gateway_type = gateway_type
        # The HTTP/2 configuration.
        # 
        # Valid values:
        # 
        # *   GlobalConfig
        # *   Close
        # *   Open
        self.http_2option = http_2option
        # Specifies whether to enable mutual authentication.
        self.m_tlsenabled = m_tlsenabled
        # The domain name.
        # 
        # This parameter is required.
        self.name = name
        # The protocol type supported by the domain name.
        # 
        # *   HTTP: Only HTTP is supported.
        # *   HTTPS: Only HTTPS is supported.
        # 
        # This parameter is required.
        self.protocol = protocol
        # The [resource group ID](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The cipher suite configuration.
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum version of the TLS protocol. Up to TLS 1.3 is supported.
        self.tls_max = tls_max
        # The minimum version of the TLS protocol. Down to TLS 1.0 is supported.
        self.tls_min = tls_min

    def validate(self):
        if self.tls_cipher_suites_config:
            self.tls_cipher_suites_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert_identifier is not None:
            result['caCertIdentifier'] = self.ca_cert_identifier
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.client_cacert is not None:
            result['clientCACert'] = self.client_cacert
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.http_2option is not None:
            result['http2Option'] = self.http_2option
        if self.m_tlsenabled is not None:
            result['mTLSEnabled'] = self.m_tlsenabled
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.tls_cipher_suites_config is not None:
            result['tlsCipherSuitesConfig'] = self.tls_cipher_suites_config.to_map()
        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max
        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caCertIdentifier') is not None:
            self.ca_cert_identifier = m.get('caCertIdentifier')
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('clientCACert') is not None:
            self.client_cacert = m.get('clientCACert')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')
        if m.get('mTLSEnabled') is not None:
            self.m_tlsenabled = m.get('mTLSEnabled')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('tlsCipherSuitesConfig') is not None:
            temp_model = TlsCipherSuitesConfig()
            self.tls_cipher_suites_config = temp_model.from_map(m['tlsCipherSuitesConfig'])
        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')
        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')
        return self


class CreateDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
    ):
        # The ID of the domain name.
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateDomainResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code returned.
        self.code = code
        # The response data.
        self.data = data
        # The response message returned.
        self.message = message
        # The request ID, which is used to trace the API call link.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateDomainResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        gateway_id: str = None,
        name: str = None,
        resource_group_id: str = None,
    ):
        # Environment alias.
        # 
        # This parameter is required.
        self.alias = alias
        # Description of the environment, which can include information such as the purpose of the environment and its owner.
        self.description = description
        # Gateway ID.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # Environment name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.description is not None:
            result['description'] = self.description
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class CreateEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
    ):
        # Environment ID.
        self.environment_id = environment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        return self


class CreateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateEnvironmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # Request ID, used for tracing the API call chain.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHttpApiRequestIngressConfig(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        environment_id: str = None,
        ingress_class: str = None,
        override_ingress_ip: bool = None,
        source_id: str = None,
        watch_namespace: str = None,
    ):
        self.cluster_id = cluster_id
        # The environment ID.
        self.environment_id = environment_id
        # The Ingress Class for listening.
        self.ingress_class = ingress_class
        # Specifies whether to update the address in Ingress Status.
        self.override_ingress_ip = override_ingress_ip
        # The source ID.
        self.source_id = source_id
        # The namespace for listening.
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class
        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')
        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')
        return self


class CreateHttpApiRequest(TeaModel):
    def __init__(
        self,
        ai_protocols: List[str] = None,
        auth_config: AuthConfig = None,
        base_path: str = None,
        deploy_configs: List[HttpApiDeployConfig] = None,
        description: str = None,
        enable_auth: bool = None,
        ingress_config: CreateHttpApiRequestIngressConfig = None,
        name: str = None,
        protocols: List[str] = None,
        resource_group_id: str = None,
        type: str = None,
        version_config: HttpApiVersionConfig = None,
    ):
        # The AI API protocols. Valid value:
        # 
        # *   OpenAI/v1
        self.ai_protocols = ai_protocols
        # The authentication configurations.
        self.auth_config = auth_config
        # The API base path, which must start with a forward slash (/).
        self.base_path = base_path
        # The API deployment configurations. Currently, only AI APIs support deployment configurations, and only a single deployment configuration can be passed.
        self.deploy_configs = deploy_configs
        # The API description.
        self.description = description
        # Specifies whether to enable authentication.
        self.enable_auth = enable_auth
        # The HTTP Ingress configurations.
        self.ingress_config = ingress_config
        # The API name.
        # 
        # This parameter is required.
        self.name = name
        # The protocols that are used to call the API.
        self.protocols = protocols
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The API type. Valid values:
        # 
        # *   Http
        # *   Rest
        # *   WebSocket
        # *   HttpIngress
        self.type = type
        # The versioning configuration of the API.
        self.version_config = version_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()
        if self.ingress_config:
            self.ingress_config.validate()
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.base_path is not None:
            result['basePath'] = self.base_path
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth
        if self.ingress_config is not None:
            result['ingressConfig'] = self.ingress_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.type is not None:
            result['type'] = self.type
        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')
        if m.get('ingressConfig') is not None:
            temp_model = CreateHttpApiRequestIngressConfig()
            self.ingress_config = temp_model.from_map(m['ingressConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('versionConfig') is not None:
            temp_model = HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m['versionConfig'])
        return self


class CreateHttpApiResponseBodyData(TeaModel):
    def __init__(
        self,
        http_api_id: str = None,
        name: str = None,
    ):
        # The HTTP API ID.
        self.http_api_id = http_api_id
        # The API name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateHttpApiResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The API information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateHttpApiResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHttpApiOperationRequest(TeaModel):
    def __init__(
        self,
        operations: List[HttpApiOperation] = None,
    ):
        # List of operation definitions.
        self.operations = operations

    def validate(self):
        if self.operations:
            for k in self.operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operations = []
        if m.get('operations') is not None:
            for k in m.get('operations'):
                temp_model = HttpApiOperation()
                self.operations.append(temp_model.from_map(k))
        return self


class CreateHttpApiOperationResponseBodyDataOperations(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
    ):
        # Operation ID.
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        return self


class CreateHttpApiOperationResponseBodyData(TeaModel):
    def __init__(
        self,
        operations: List[CreateHttpApiOperationResponseBodyDataOperations] = None,
    ):
        # Operation information.
        self.operations = operations

    def validate(self):
        if self.operations:
            for k in self.operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operations = []
        if m.get('operations') is not None:
            for k in m.get('operations'):
                temp_model = CreateHttpApiOperationResponseBodyDataOperations()
                self.operations.append(temp_model.from_map(k))
        return self


class CreateHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateHttpApiOperationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Operation information.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateHttpApiOperationResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHttpApiRouteRequestBackendConfigServices(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # The service port. If you want to use a dynamic port, do not pass this parameter.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.protocol = protocol
        # The service ID.
        self.service_id = service_id
        # The service version. Pass this parameter for tag-based routing.
        self.version = version
        # The percentage value of traffic.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class CreateHttpApiRouteRequestBackendConfig(TeaModel):
    def __init__(
        self,
        scene: str = None,
        services: List[CreateHttpApiRouteRequestBackendConfigServices] = None,
    ):
        # The scenario of the backend service.
        # 
        # *   SingleService
        # *   MultiServiceByRatio
        # *   Mock
        # *   Redirect
        self.scene = scene
        # The backend services.
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = CreateHttpApiRouteRequestBackendConfigServices()
                self.services.append(temp_model.from_map(k))
        return self


class CreateHttpApiRouteRequestMcpRouteConfig(TeaModel):
    def __init__(
        self,
        exposed_uri_path: str = None,
        protocol: str = None,
    ):
        self.exposed_uri_path = exposed_uri_path
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exposed_uri_path is not None:
            result['exposedUriPath'] = self.exposed_uri_path
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exposedUriPath') is not None:
            self.exposed_uri_path = m.get('exposedUriPath')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self


class CreateHttpApiRouteRequest(TeaModel):
    def __init__(
        self,
        backend_config: CreateHttpApiRouteRequestBackendConfig = None,
        deploy_configs: List[HttpApiDeployConfig] = None,
        description: str = None,
        domain_ids: List[str] = None,
        environment_id: str = None,
        match: HttpRouteMatch = None,
        mcp_route_config: CreateHttpApiRouteRequestMcpRouteConfig = None,
        name: str = None,
    ):
        # The backend service configurations of the route.
        self.backend_config = backend_config
        self.deploy_configs = deploy_configs
        # The route description.
        self.description = description
        # The domain name IDs.
        self.domain_ids = domain_ids
        # The environment ID.
        self.environment_id = environment_id
        # The rule for matching the route.
        self.match = match
        self.mcp_route_config = mcp_route_config
        # The route name.
        self.name = name

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()
        if self.match:
            self.match.validate()
        if self.mcp_route_config:
            self.mcp_route_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.mcp_route_config is not None:
            result['mcpRouteConfig'] = self.mcp_route_config.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = CreateHttpApiRouteRequestBackendConfig()
            self.backend_config = temp_model.from_map(m['backendConfig'])
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        if m.get('mcpRouteConfig') is not None:
            temp_model = CreateHttpApiRouteRequestMcpRouteConfig()
            self.mcp_route_config = temp_model.from_map(m['mcpRouteConfig'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateHttpApiRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        route_id: str = None,
    ):
        # The route ID.
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_id is not None:
            result['routeId'] = self.route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')
        return self


class CreateHttpApiRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateHttpApiRouteResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateHttpApiRouteResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateHttpApiRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHttpApiRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateHttpApiRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePluginAttachmentRequest(TeaModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        attach_resource_type: str = None,
        enable: bool = None,
        environment_id: str = None,
        gateway_id: str = None,
        plugin_config: str = None,
        plugin_id: str = None,
    ):
        self.attach_resource_ids = attach_resource_ids
        self.attach_resource_type = attach_resource_type
        self.enable = enable
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.plugin_config = plugin_config
        self.plugin_id = plugin_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.plugin_config is not None:
            result['pluginConfig'] = self.plugin_config
        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('pluginConfig') is not None:
            self.plugin_config = m.get('pluginConfig')
        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')
        return self


class CreatePluginAttachmentResponseBodyData(TeaModel):
    def __init__(
        self,
        plugin_attachment_id: str = None,
    ):
        self.plugin_attachment_id = plugin_attachment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_attachment_id is not None:
            result['pluginAttachmentId'] = self.plugin_attachment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pluginAttachmentId') is not None:
            self.plugin_attachment_id = m.get('pluginAttachmentId')
        return self


class CreatePluginAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreatePluginAttachmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreatePluginAttachmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePluginAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePluginAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreatePluginAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        config: str = None,
        description: str = None,
        name: str = None,
    ):
        # Policy type, including RateLimit, ConcurrencyLimit, CircuitBreaker, HttpRewrite, HeaderModify, Cors, Authentication, FlowCopy, Timeout, Retry, IpAccessControl, DirectResponse, Redirect, Fallback, ServiceTls, ServiceLb, ServicePortTls, Waf, JWTAuth, OIDCAuth, ExternalZAuth, AiProxy, ModelRouter, AiStatistics, AiSecurityGuard, AiFallback, ModelMapper, AiTokenRateLimit, AiCache, DynamicRoute
        # 
        # This parameter is required.
        self.class_name = class_name
        # Policy configuration
        # 
        # This parameter is required.
        self.config = config
        # Policy description
        self.description = description
        # Policy name
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreatePolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # Policy ID
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreatePolicyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreatePolicyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyAttachmentRequest(TeaModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_id: str = None,
    ):
        # Attached resource ID
        # 
        # This parameter is required.
        self.attach_resource_id = attach_resource_id
        # Attached resource type, such as HttpApi, GatewayRoute, Operation, GatewayService, GatewayServicePort, Gateway, Domain
        # 
        # This parameter is required.
        self.attach_resource_type = attach_resource_type
        # Environment ID
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # Gateway instance ID
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # Policy ID
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_id is not None:
            result['attachResourceId'] = self.attach_resource_id
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class CreatePolicyAttachmentResponseBodyData(TeaModel):
    def __init__(
        self,
        policy_attachment_id: str = None,
    ):
        # Policy Mount ID
        self.policy_attachment_id = policy_attachment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_attachment_id is not None:
            result['policyAttachmentId'] = self.policy_attachment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')
        return self


class CreatePolicyAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreatePolicyAttachmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreatePolicyAttachmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePolicyAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreatePolicyAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequestServiceConfigs(TeaModel):
    def __init__(
        self,
        addresses: List[str] = None,
        ai_service_config: AiServiceConfig = None,
        dns_servers: List[str] = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        qualifier: str = None,
    ):
        # The list of domain names or fixed addresses.
        self.addresses = addresses
        # The AI service configurations.
        self.ai_service_config = ai_service_config
        # The list of DNS service addresses.
        self.dns_servers = dns_servers
        # The service group name. This parameter is required if sourceType is set to MSE_NACOS.
        self.group_name = group_name
        # The service name.
        self.name = name
        # The service namespace. This parameter is required when sourceType is set to K8S or MSE_NACOS.
        # 
        # *   If sourceType is set to K8S, this parameter specifies the namespace where the K8s service resides.
        # *   If sourceType is set to MSE_NACOS, this parameter specifies a namespace in Nacos.
        self.namespace = namespace
        # The function version or alias.
        self.qualifier = qualifier

    def validate(self):
        if self.ai_service_config:
            self.ai_service_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['addresses'] = self.addresses
        if self.ai_service_config is not None:
            result['aiServiceConfig'] = self.ai_service_config.to_map()
        if self.dns_servers is not None:
            result['dnsServers'] = self.dns_servers
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addresses') is not None:
            self.addresses = m.get('addresses')
        if m.get('aiServiceConfig') is not None:
            temp_model = AiServiceConfig()
            self.ai_service_config = temp_model.from_map(m['aiServiceConfig'])
        if m.get('dnsServers') is not None:
            self.dns_servers = m.get('dnsServers')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        resource_group_id: str = None,
        service_configs: List[CreateServiceRequestServiceConfigs] = None,
        source_type: str = None,
    ):
        # The gateway instance ID.
        self.gateway_id = gateway_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of service configurations.
        self.service_configs = service_configs
        # The service source. Valid values:
        # 
        # *   MSE_NACOS: a service in an MSE Nacos instance
        # *   K8S: a service in a Kubernetes (K8s) cluster in Container Service for Kubernetes (ACK)
        # *   VIP: a fixed IP address
        # *   DNS: a Domain Name System (DNS) domain name
        # *   FC3: a service in Function Compute
        # *   SAE_K8S_SERVICE: a service in a K8s cluster in Serverless App Engine (SAE)
        # 
        # Enumerated values:
        # 
        # *   SAE_K8S_SERVICE
        # *   K8S
        # *   FC3
        # *   DNS
        # *   VIP
        # *   MSE_NACOS
        self.source_type = source_type

    def validate(self):
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = CreateServiceRequestServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class CreateServiceResponseBodyData(TeaModel):
    def __init__(
        self,
        service_ids: List[str] = None,
    ):
        # The list of service IDs.
        self.service_ids = service_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateServiceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID, used for tracing the API call chain.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID, used for tracing the request chain.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewaySecurityGroupRuleRequest(TeaModel):
    def __init__(
        self,
        cascading_delete: bool = None,
    ):
        # Whether to cascade delete the security group rules.
        self.cascading_delete = cascading_delete

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cascading_delete is not None:
            result['cascadingDelete'] = self.cascading_delete
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cascadingDelete') is not None:
            self.cascading_delete = m.get('cascadingDelete')
        return self


class DeleteGatewaySecurityGroupRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteGatewaySecurityGroupRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewaySecurityGroupRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteGatewaySecurityGroupRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message,
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHttpApiRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteHttpApiRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHttpApiRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteHttpApiRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePluginAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeletePluginAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePluginAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeletePluginAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeletePolicyAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeletePolicyAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployHttpApiRequestHttpApiConfig(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        route_ids: List[str] = None,
    ):
        self.gateway_id = gateway_id
        self.route_ids = route_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.route_ids is not None:
            result['routeIds'] = self.route_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('routeIds') is not None:
            self.route_ids = m.get('routeIds')
        return self


class DeployHttpApiRequestRestApiConfigEnvironmentServiceConfigs(TeaModel):
    def __init__(
        self,
        match: HttpApiBackendMatchConditions = None,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # Configuration of matching conditions related to API deployment.
        self.match = match
        # Service port, do not provide for dynamic ports.
        self.port = port
        # Service protocol:
        # - HTTP.
        # - HTTPS.
        self.protocol = protocol
        # Service ID.
        self.service_id = service_id
        # Service version.
        self.version = version
        # Weight, range [1,100], valid only in the by-ratio scenario.
        self.weight = weight

    def validate(self):
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match.to_map()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            temp_model = HttpApiBackendMatchConditions()
            self.match = temp_model.from_map(m['match'])
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class DeployHttpApiRequestRestApiConfigEnvironment(TeaModel):
    def __init__(
        self,
        backend_scene: str = None,
        custom_domain_ids: List[str] = None,
        environment_id: str = None,
        service_configs: List[DeployHttpApiRequestRestApiConfigEnvironmentServiceConfigs] = None,
    ):
        # API publication scenario.
        self.backend_scene = backend_scene
        # List of user domains.
        self.custom_domain_ids = custom_domain_ids
        # Environment ID.
        self.environment_id = environment_id
        # Existing service configurations. Only one entry is allowed in a single-service scenario, while multiple entries are allowed in scenarios such as by ratio or by content.
        self.service_configs = service_configs

    def validate(self):
        if self.service_configs:
            for k in self.service_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_scene is not None:
            result['backendScene'] = self.backend_scene
        if self.custom_domain_ids is not None:
            result['customDomainIds'] = self.custom_domain_ids
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        result['serviceConfigs'] = []
        if self.service_configs is not None:
            for k in self.service_configs:
                result['serviceConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendScene') is not None:
            self.backend_scene = m.get('backendScene')
        if m.get('customDomainIds') is not None:
            self.custom_domain_ids = m.get('customDomainIds')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        self.service_configs = []
        if m.get('serviceConfigs') is not None:
            for k in m.get('serviceConfigs'):
                temp_model = DeployHttpApiRequestRestApiConfigEnvironmentServiceConfigs()
                self.service_configs.append(temp_model.from_map(k))
        return self


class DeployHttpApiRequestRestApiConfig(TeaModel):
    def __init__(
        self,
        description: str = None,
        environment: DeployHttpApiRequestRestApiConfigEnvironment = None,
        gateway_id: str = None,
        operation_ids: List[str] = None,
        revision_id: str = None,
    ):
        # Publication description.
        self.description = description
        # Publication environment configuration.
        self.environment = environment
        self.gateway_id = gateway_id
        self.operation_ids = operation_ids
        # Historical version number. If this field is specified, the publication information will be based on the historical version information.
        self.revision_id = revision_id

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.environment is not None:
            result['environment'] = self.environment.to_map()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.operation_ids is not None:
            result['operationIds'] = self.operation_ids
        if self.revision_id is not None:
            result['revisionId'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environment') is not None:
            temp_model = DeployHttpApiRequestRestApiConfigEnvironment()
            self.environment = temp_model.from_map(m['environment'])
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('operationIds') is not None:
            self.operation_ids = m.get('operationIds')
        if m.get('revisionId') is not None:
            self.revision_id = m.get('revisionId')
        return self


class DeployHttpApiRequest(TeaModel):
    def __init__(
        self,
        http_api_config: DeployHttpApiRequestHttpApiConfig = None,
        rest_api_config: DeployHttpApiRequestRestApiConfig = None,
        route_id: str = None,
    ):
        self.http_api_config = http_api_config
        # Rest API deployment configuration. Required when deploying an HTTP API as a Rest API.
        self.rest_api_config = rest_api_config
        # Route ID. This must be provided when publishing the route of an HTTP API.
        self.route_id = route_id

    def validate(self):
        if self.http_api_config:
            self.http_api_config.validate()
        if self.rest_api_config:
            self.rest_api_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_api_config is not None:
            result['httpApiConfig'] = self.http_api_config.to_map()
        if self.rest_api_config is not None:
            result['restApiConfig'] = self.rest_api_config.to_map()
        if self.route_id is not None:
            result['routeId'] = self.route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpApiConfig') is not None:
            temp_model = DeployHttpApiRequestHttpApiConfig()
            self.http_api_config = temp_model.from_map(m['httpApiConfig'])
        if m.get('restApiConfig') is not None:
            temp_model = DeployHttpApiRequestRestApiConfig()
            self.rest_api_config = temp_model.from_map(m['restApiConfig'])
        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')
        return self


class DeployHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # 响应消息。
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeployHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeployHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportHttpApiResponseBodyData(TeaModel):
    def __init__(
        self,
        spec_content_base_64: str = None,
    ):
        # Base64编码的API定义。
        self.spec_content_base_64 = spec_content_base_64

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec_content_base_64 is not None:
            result['specContentBase64'] = self.spec_content_base_64
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('specContentBase64') is not None:
            self.spec_content_base_64 = m.get('specContentBase64')
        return self


class ExportHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ExportHttpApiResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # API definition information.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ExportHttpApiResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExportHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ExportHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDashboardRequestFilter(TeaModel):
    def __init__(
        self,
        route_name: str = None,
    ):
        # The route name.
        self.route_name = route_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_name is not None:
            result['routeName'] = self.route_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')
        return self


class GetDashboardRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        api_id: str = None,
        filter: GetDashboardRequestFilter = None,
        name: str = None,
        plugin_class_id: str = None,
        plugin_id: str = None,
        source: str = None,
        upstream_cluster: str = None,
    ):
        # The language. Valid values: zh (Chinese) and en (English).
        self.accept_language = accept_language
        # API ID
        self.api_id = api_id
        # The filter configurations.
        self.filter = filter
        # The dashboard name.
        # 
        # *   LOG: access logs
        # *   PLUGIN: plug-in logs
        self.name = name
        # The plug-in ID.
        self.plugin_class_id = plugin_class_id
        self.plugin_id = plugin_id
        # The dashboard source. Valid values:
        # 
        # *   SLS: Simple Log Service
        self.source = source
        self.upstream_cluster = upstream_cluster

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.filter is not None:
            result['filter'] = self.filter.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id
        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id
        if self.source is not None:
            result['source'] = self.source
        if self.upstream_cluster is not None:
            result['upstreamCluster'] = self.upstream_cluster
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('filter') is not None:
            temp_model = GetDashboardRequestFilter()
            self.filter = temp_model.from_map(m['filter'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')
        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('upstreamCluster') is not None:
            self.upstream_cluster = m.get('upstreamCluster')
        return self


class GetDashboardShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        api_id: str = None,
        filter_shrink: str = None,
        name: str = None,
        plugin_class_id: str = None,
        plugin_id: str = None,
        source: str = None,
        upstream_cluster: str = None,
    ):
        # The language. Valid values: zh (Chinese) and en (English).
        self.accept_language = accept_language
        # API ID
        self.api_id = api_id
        # The filter configurations.
        self.filter_shrink = filter_shrink
        # The dashboard name.
        # 
        # *   LOG: access logs
        # *   PLUGIN: plug-in logs
        self.name = name
        # The plug-in ID.
        self.plugin_class_id = plugin_class_id
        self.plugin_id = plugin_id
        # The dashboard source. Valid values:
        # 
        # *   SLS: Simple Log Service
        self.source = source
        self.upstream_cluster = upstream_cluster

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        if self.api_id is not None:
            result['apiId'] = self.api_id
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink
        if self.name is not None:
            result['name'] = self.name
        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id
        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id
        if self.source is not None:
            result['source'] = self.source
        if self.upstream_cluster is not None:
            result['upstreamCluster'] = self.upstream_cluster
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')
        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('upstreamCluster') is not None:
            self.upstream_cluster = m.get('upstreamCluster')
        return self


class GetDashboardResponseBodyData(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
        title: str = None,
        url: str = None,
    ):
        # The instance ID.
        self.gateway_id = gateway_id
        # The dashboard name.
        self.name = name
        # The dashboard title.
        self.title = title
        # The dashboard URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetDashboardResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetDashboardResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDashboardResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDashboardResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(
        self,
        with_statistics: bool = None,
    ):
        # Specifies whether to return online resource information.
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_statistics is not None:
            result['withStatistics'] = self.with_statistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withStatistics') is not None:
            self.with_statistics = m.get('withStatistics')
        return self


class GetDomainResponseBodyDataStatisticsInfo(TeaModel):
    def __init__(
        self,
        resource_statistics: List[ResourceStatistic] = None,
        total_count: str = None,
    ):
        # The resource statistics.
        self.resource_statistics = resource_statistics
        # The total number of resources.
        self.total_count = total_count

    def validate(self):
        if self.resource_statistics:
            for k in self.resource_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['resourceStatistics'] = []
        if self.resource_statistics is not None:
            for k in self.resource_statistics:
                result['resourceStatistics'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_statistics = []
        if m.get('resourceStatistics') is not None:
            for k in m.get('resourceStatistics'):
                temp_model = ResourceStatistic()
                self.resource_statistics.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        ca_cert_identifier: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        client_cacert: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        default: bool = None,
        domain_id: str = None,
        force_https: bool = None,
        http_2option: str = None,
        issuer: str = None,
        m_tlsenabled: bool = None,
        name: str = None,
        not_after_timstamp: int = None,
        not_before_timestamp: int = None,
        protocol: str = None,
        resource_group_id: str = None,
        sans: str = None,
        statistics_info: GetDomainResponseBodyDataStatisticsInfo = None,
        tls_cipher_suites_config: TlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
        updatetimestamp: int = None,
    ):
        # The encryption algorithm.
        self.algorithm = algorithm
        # The CA certificate ID.
        self.ca_cert_identifier = ca_cert_identifier
        # The certificate ID.
        self.cert_identifier = cert_identifier
        # The certificate name.
        self.cert_name = cert_name
        # The client CA certificate.
        self.client_cacert = client_cacert
        # The creation source.
        # 
        # Valid values:
        # 
        # *   Console
        # *   Ingress
        self.create_from = create_from
        # The creation timestamp.
        self.create_timestamp = create_timestamp
        # Indicates whether the domain name is the default domain name.
        self.default = default
        # The ID of the domain name.
        self.domain_id = domain_id
        # Indicates whether forcible HTTPS redirection is enabled.
        self.force_https = force_https
        # The HTTP/2 configuration.
        # 
        # Valid values:
        # 
        # *   GlobalConfig
        # *   Close
        # *   Open
        self.http_2option = http_2option
        # The certificate issuer.
        self.issuer = issuer
        # Indicates whether mutual authentication is enabled.
        # 
        # Valid values:
        # 
        # *   false
        # *   true
        self.m_tlsenabled = m_tlsenabled
        # The domain name.
        self.name = name
        # The expiration time of the certificate.
        self.not_after_timstamp = not_after_timstamp
        # The time when the certificate started to take effect.
        self.not_before_timestamp = not_before_timestamp
        # The supported protocol. Valid values:
        # 
        # *   HTTP: Only HTTP is supported.
        # *   HTTPS: Only HTTPS is supported.
        self.protocol = protocol
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # All domain names that are bound to the certificate.
        self.sans = sans
        # The information about online resources.
        self.statistics_info = statistics_info
        # The cipher suite configuration.
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum version of the TLS protocol. Up to TLS 1.3 is supported.
        self.tls_max = tls_max
        # The minimum version of the TLS protocol. Down to TLS 1.0 is supported.
        self.tls_min = tls_min
        # The update timestamp.
        self.updatetimestamp = updatetimestamp

    def validate(self):
        if self.statistics_info:
            self.statistics_info.validate()
        if self.tls_cipher_suites_config:
            self.tls_cipher_suites_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.ca_cert_identifier is not None:
            result['caCertIdentifier'] = self.ca_cert_identifier
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['certName'] = self.cert_name
        if self.client_cacert is not None:
            result['clientCACert'] = self.client_cacert
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.default is not None:
            result['default'] = self.default
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.http_2option is not None:
            result['http2Option'] = self.http_2option
        if self.issuer is not None:
            result['issuer'] = self.issuer
        if self.m_tlsenabled is not None:
            result['mTLSEnabled'] = self.m_tlsenabled
        if self.name is not None:
            result['name'] = self.name
        if self.not_after_timstamp is not None:
            result['notAfterTimstamp'] = self.not_after_timstamp
        if self.not_before_timestamp is not None:
            result['notBeforeTimestamp'] = self.not_before_timestamp
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.sans is not None:
            result['sans'] = self.sans
        if self.statistics_info is not None:
            result['statisticsInfo'] = self.statistics_info.to_map()
        if self.tls_cipher_suites_config is not None:
            result['tlsCipherSuitesConfig'] = self.tls_cipher_suites_config.to_map()
        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max
        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min
        if self.updatetimestamp is not None:
            result['updatetimestamp'] = self.updatetimestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('caCertIdentifier') is not None:
            self.ca_cert_identifier = m.get('caCertIdentifier')
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')
        if m.get('clientCACert') is not None:
            self.client_cacert = m.get('clientCACert')
        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')
        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')
        if m.get('mTLSEnabled') is not None:
            self.m_tlsenabled = m.get('mTLSEnabled')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notAfterTimstamp') is not None:
            self.not_after_timstamp = m.get('notAfterTimstamp')
        if m.get('notBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('notBeforeTimestamp')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('sans') is not None:
            self.sans = m.get('sans')
        if m.get('statisticsInfo') is not None:
            temp_model = GetDomainResponseBodyDataStatisticsInfo()
            self.statistics_info = temp_model.from_map(m['statisticsInfo'])
        if m.get('tlsCipherSuitesConfig') is not None:
            temp_model = TlsCipherSuitesConfig()
            self.tls_cipher_suites_config = temp_model.from_map(m['tlsCipherSuitesConfig'])
        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')
        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')
        if m.get('updatetimestamp') is not None:
            self.updatetimestamp = m.get('updatetimestamp')
        return self


class GetDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDomainResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The response message returned.
        self.message = message
        # The request ID, which is used to trace the API call link.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetDomainResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentRequest(TeaModel):
    def __init__(
        self,
        with_statistics: bool = None,
        with_vpc_info: bool = None,
    ):
        # Indicates whether to return online resource info.
        self.with_statistics = with_statistics
        # Option for vpc info.
        self.with_vpc_info = with_vpc_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_statistics is not None:
            result['withStatistics'] = self.with_statistics
        if self.with_vpc_info is not None:
            result['withVpcInfo'] = self.with_vpc_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withStatistics') is not None:
            self.with_statistics = m.get('withStatistics')
        if m.get('withVpcInfo') is not None:
            self.with_vpc_info = m.get('withVpcInfo')
        return self


class GetEnvironmentResponseBodyDataStatisticsInfo(TeaModel):
    def __init__(
        self,
        resource_statistics: List[ResourceStatistic] = None,
        total_count: int = None,
    ):
        # The array of related resource information.
        self.resource_statistics = resource_statistics
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resource_statistics:
            for k in self.resource_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['resourceStatistics'] = []
        if self.resource_statistics is not None:
            for k in self.resource_statistics:
                result['resourceStatistics'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_statistics = []
        if m.get('resourceStatistics') is not None:
            for k in m.get('resourceStatistics'):
                temp_model = ResourceStatistic()
                self.resource_statistics.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(
        self,
        alias: str = None,
        create_timestamp: int = None,
        default: bool = None,
        description: str = None,
        environment_id: str = None,
        gateway_info: GatewayInfo = None,
        name: str = None,
        resource_group_id: str = None,
        statistics_info: GetEnvironmentResponseBodyDataStatisticsInfo = None,
        sub_domain_infos: List[SubDomainInfo] = None,
        update_timestamp: int = None,
    ):
        # Environment alias.
        self.alias = alias
        # Creation timestamp.
        self.create_timestamp = create_timestamp
        # Whether it is the default environment.
        self.default = default
        # Environment description.
        self.description = description
        # Environment ID.
        self.environment_id = environment_id
        # Gateway information
        self.gateway_info = gateway_info
        # Environment name.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Related resource information.
        self.statistics_info = statistics_info
        # List of subdomains.
        self.sub_domain_infos = sub_domain_infos
        # Update timestamp.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.statistics_info:
            self.statistics_info.validate()
        if self.sub_domain_infos:
            for k in self.sub_domain_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.statistics_info is not None:
            result['statisticsInfo'] = self.statistics_info.to_map()
        result['subDomainInfos'] = []
        if self.sub_domain_infos is not None:
            for k in self.sub_domain_infos:
                result['subDomainInfos'].append(k.to_map() if k else None)
        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayInfo') is not None:
            temp_model = GatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('statisticsInfo') is not None:
            temp_model = GetEnvironmentResponseBodyDataStatisticsInfo()
            self.statistics_info = temp_model.from_map(m['statisticsInfo'])
        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k in m.get('subDomainInfos'):
                temp_model = SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k))
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEnvironmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # Request ID, used for tracing the API call chain.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayResponseBodyDataEnvironments(TeaModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        name: str = None,
    ):
        # The environment alias.
        self.alias = alias
        # Environment ID.
        self.environment_id = environment_id
        # The environment name。
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetGatewayResponseBodyDataLoadBalancersPorts(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # Port number.
        self.port = port
        # Protocol:
        # - TCP
        # - UDP
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetGatewayResponseBodyDataLoadBalancers(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        gateway_default: bool = None,
        load_balancer_id: str = None,
        mode: str = None,
        ports: List[GetGatewayResponseBodyDataLoadBalancersPorts] = None,
        status: str = None,
        type: str = None,
    ):
        # The address of the load balancer.
        self.address = address
        # The IP version of the protocol:
        # - ipv4: IPv4 type.
        # - ipv6: IPv6 type.
        self.address_ip_version = address_ip_version
        # Load balancer address type:
        # - Internet: Public.
        # - Intranet: Private.
        self.address_type = address_type
        # Whether it is the default entry address for the gateway.
        self.gateway_default = gateway_default
        # Load balancer ID.
        self.load_balancer_id = load_balancer_id
        # The provision mode of the load balancer for the gateway:
        # - Managed: Managed by the Cloud Native API Gateway.
        self.mode = mode
        # List of listening ports.
        self.ports = ports
        # The status of the load balancer:
        # - Ready: Available.
        # - NotCreate: Not associated with an instance.
        self.status = status
        # The type of load balancer:
        # - NLB: Network Load Balancer.
        # - CLB: Classic Load Balancer.
        self.type = type

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.address_ip_version is not None:
            result['addressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['addressType'] = self.address_type
        if self.gateway_default is not None:
            result['gatewayDefault'] = self.gateway_default
        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id
        if self.mode is not None:
            result['mode'] = self.mode
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
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
        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = GetGatewayResponseBodyDataLoadBalancersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetGatewayResponseBodyDataSecurityGroup(TeaModel):
    def __init__(
        self,
        name: str = None,
        security_group_id: str = None,
    ):
        # Security group name.
        self.name = name
        # Security group ID.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self


class GetGatewayResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        self.key = key
        # The tag value of the resource.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetGatewayResponseBodyDataVSwitch(TeaModel):
    def __init__(
        self,
        name: str = None,
        v_switch_id: str = None,
    ):
        # Virtual switch name.
        self.name = name
        # Virtual switch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        return self


class GetGatewayResponseBodyDataVpc(TeaModel):
    def __init__(
        self,
        name: str = None,
        vpc_id: str = None,
    ):
        # VPC gateway name.
        self.name = name
        # VPC network ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetGatewayResponseBodyDataZonesVSwitch(TeaModel):
    def __init__(
        self,
        name: str = None,
        v_switch_id: str = None,
    ):
        # Virtual switch name.
        self.name = name
        # Virtual switch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        return self


class GetGatewayResponseBodyDataZones(TeaModel):
    def __init__(
        self,
        name: str = None,
        v_switch: GetGatewayResponseBodyDataZonesVSwitch = None,
        zone_id: str = None,
    ):
        # Availability zone name.
        self.name = name
        # Virtual switch.
        self.v_switch = v_switch
        # Availability zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.v_switch:
            self.v_switch.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.v_switch is not None:
            result['vSwitch'] = self.v_switch.to_map()
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vSwitch') is not None:
            temp_model = GetGatewayResponseBodyDataZonesVSwitch()
            self.v_switch = temp_model.from_map(m['vSwitch'])
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class GetGatewayResponseBodyData(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        environments: List[GetGatewayResponseBodyDataEnvironments] = None,
        expire_timestamp: int = None,
        gateway_id: str = None,
        load_balancers: List[GetGatewayResponseBodyDataLoadBalancers] = None,
        name: str = None,
        replicas: str = None,
        resource_group_id: str = None,
        security_group: GetGatewayResponseBodyDataSecurityGroup = None,
        spec: str = None,
        status: str = None,
        tags: List[GetGatewayResponseBodyDataTags] = None,
        target_version: str = None,
        update_timestamp: int = None,
        v_switch: GetGatewayResponseBodyDataVSwitch = None,
        version: str = None,
        vpc: GetGatewayResponseBodyDataVpc = None,
        zones: List[GetGatewayResponseBodyDataZones] = None,
    ):
        # Charge type
        # - POSTPAY: Postpaid (pay-as-you-go)
        # - PREPAY: Prepaid (subscription)
        self.charge_type = charge_type
        # Source of gateway creation:
        # - Console: Console.
        self.create_from = create_from
        # Creation timestamp. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # List of environments associated with the gateway.
        self.environments = environments
        # Expiration timestamp for subscription. Unit: milliseconds.
        self.expire_timestamp = expire_timestamp
        # Gateway ID.
        self.gateway_id = gateway_id
        # List of entry addresses for the gateway.
        self.load_balancers = load_balancers
        # Gateway name.
        self.name = name
        # Number of gateway instance nodes.
        self.replicas = replicas
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security group of the gateway.
        self.security_group = security_group
        # Gateway specification:
        # - apigw.small.x1: Small specification.
        self.spec = spec
        # Gateway status:
        # - Running: Running.
        # - Creating: Creating.
        # - CreateFailed: Creation failed.
        # - Upgrading: Upgrading.
        # - UpgradeFailed: Upgrade failed.
        # - Restarting: Restarting.
        # - RestartFailed: Restart failed.
        # - Deleting: Deleting.
        # - DeleteFailed: Deletion failed.
        self.status = status
        # The resource tags.
        self.tags = tags
        # Target version of the gateway. When it is inconsistent with the current version, an upgrade can be performed.
        self.target_version = target_version
        # Update timestamp. Unit: milliseconds.
        self.update_timestamp = update_timestamp
        # The virtual switch associated with the gateway.
        self.v_switch = v_switch
        # Gateway version.
        self.version = version
        # The VPC (Virtual Private Cloud) associated with the gateway.
        self.vpc = vpc
        # List of availability zones associated with the gateway.
        self.zones = zones

    def validate(self):
        if self.environments:
            for k in self.environments:
                if k:
                    k.validate()
        if self.load_balancers:
            for k in self.load_balancers:
                if k:
                    k.validate()
        if self.security_group:
            self.security_group.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.v_switch:
            self.v_switch.validate()
        if self.vpc:
            self.vpc.validate()
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        result['environments'] = []
        if self.environments is not None:
            for k in self.environments:
                result['environments'].append(k.to_map() if k else None)
        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        result['loadBalancers'] = []
        if self.load_balancers is not None:
            for k in self.load_balancers:
                result['loadBalancers'].append(k.to_map() if k else None)
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
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
            for k in self.zones:
                result['zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        self.environments = []
        if m.get('environments') is not None:
            for k in m.get('environments'):
                temp_model = GetGatewayResponseBodyDataEnvironments()
                self.environments.append(temp_model.from_map(k))
        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        self.load_balancers = []
        if m.get('loadBalancers') is not None:
            for k in m.get('loadBalancers'):
                temp_model = GetGatewayResponseBodyDataLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('securityGroup') is not None:
            temp_model = GetGatewayResponseBodyDataSecurityGroup()
            self.security_group = temp_model.from_map(m['securityGroup'])
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GetGatewayResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        if m.get('vSwitch') is not None:
            temp_model = GetGatewayResponseBodyDataVSwitch()
            self.v_switch = temp_model.from_map(m['vSwitch'])
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('vpc') is not None:
            temp_model = GetGatewayResponseBodyDataVpc()
            self.vpc = temp_model.from_map(m['vpc'])
        self.zones = []
        if m.get('zones') is not None:
            for k in m.get('zones'):
                temp_model = GetGatewayResponseBodyDataZones()
                self.zones.append(temp_model.from_map(k))
        return self


class GetGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetGatewayResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetGatewayResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HttpApiApiInfo = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # API information.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiApiInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HttpApiOperationInfo = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Operation information.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpApiOperationInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHttpApiRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HttpRoute = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The route details.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HttpRoute()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHttpApiRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHttpApiRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetHttpApiRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPluginAttachmentResponseBodyData(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        environment_info: EnvironmentInfo = None,
        gateway_info: GatewayInfo = None,
        parent_resource_info: ParentResourceInfo = None,
        plugin_attachment_id: str = None,
        plugin_class_info: PluginClassInfo = None,
        plugin_config: str = None,
        plugin_id: str = None,
        resource_infos: List[ResourceInfo] = None,
    ):
        self.enable = enable
        self.environment_info = environment_info
        self.gateway_info = gateway_info
        self.parent_resource_info = parent_resource_info
        self.plugin_attachment_id = plugin_attachment_id
        self.plugin_class_info = plugin_class_info
        self.plugin_config = plugin_config
        self.plugin_id = plugin_id
        self.resource_infos = resource_infos

    def validate(self):
        if self.environment_info:
            self.environment_info.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.parent_resource_info:
            self.parent_resource_info.validate()
        if self.plugin_class_info:
            self.plugin_class_info.validate()
        if self.resource_infos:
            for k in self.resource_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.parent_resource_info is not None:
            result['parentResourceInfo'] = self.parent_resource_info.to_map()
        if self.plugin_attachment_id is not None:
            result['pluginAttachmentId'] = self.plugin_attachment_id
        if self.plugin_class_info is not None:
            result['pluginClassInfo'] = self.plugin_class_info.to_map()
        if self.plugin_config is not None:
            result['pluginConfig'] = self.plugin_config
        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id
        result['resourceInfos'] = []
        if self.resource_infos is not None:
            for k in self.resource_infos:
                result['resourceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('environmentInfo') is not None:
            temp_model = EnvironmentInfo()
            self.environment_info = temp_model.from_map(m['environmentInfo'])
        if m.get('gatewayInfo') is not None:
            temp_model = GatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('parentResourceInfo') is not None:
            temp_model = ParentResourceInfo()
            self.parent_resource_info = temp_model.from_map(m['parentResourceInfo'])
        if m.get('pluginAttachmentId') is not None:
            self.plugin_attachment_id = m.get('pluginAttachmentId')
        if m.get('pluginClassInfo') is not None:
            temp_model = PluginClassInfo()
            self.plugin_class_info = temp_model.from_map(m['pluginClassInfo'])
        if m.get('pluginConfig') is not None:
            self.plugin_config = m.get('pluginConfig')
        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')
        self.resource_infos = []
        if m.get('resourceInfos') is not None:
            for k in m.get('resourceInfos'):
                temp_model = ResourceInfo()
                self.resource_infos.append(temp_model.from_map(k))
        return self


class GetPluginAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPluginAttachmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetPluginAttachmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPluginAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPluginAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetPluginAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PolicyDetailInfo = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = PolicyDetailInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyAttachmentResponseBodyData(TeaModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        config: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_attachment_id: str = None,
        policy_id: str = None,
    ):
        # Attached Resource ID
        self.attach_resource_id = attach_resource_id
        # Attached resource type, HttpApi, GatewayRoute, Operation, GatewayService, GatewayServicePort, Gateway, Domain
        self.attach_resource_type = attach_resource_type
        # Policy attachment configuration
        self.config = config
        # Environment ID
        self.environment_id = environment_id
        # Gateway Instance ID
        self.gateway_id = gateway_id
        # Policy Attachment ID
        self.policy_attachment_id = policy_attachment_id
        # Policy ID
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_id is not None:
            result['attachResourceId'] = self.attach_resource_id
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type
        if self.config is not None:
            result['config'] = self.config
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.policy_attachment_id is not None:
            result['policyAttachmentId'] = self.policy_attachment_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class GetPolicyAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPolicyAttachmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response data.
        self.data = data
        # Response message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetPolicyAttachmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPolicyAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetPolicyAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceOverviewRequest(TeaModel):
    def __init__(
        self,
        gateway_type: str = None,
    ):
        self.gateway_type = gateway_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        return self


class GetResourceOverviewResponseBodyDataApi(TeaModel):
    def __init__(
        self,
        published_count: int = None,
        total_count: int = None,
    ):
        # Number of published APIs.
        self.published_count = published_count
        # Number of APIs.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.published_count is not None:
            result['publishedCount'] = self.published_count
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publishedCount') is not None:
            self.published_count = m.get('publishedCount')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetResourceOverviewResponseBodyDataGateway(TeaModel):
    def __init__(
        self,
        running_count: int = None,
        total_count: int = None,
    ):
        # Number of running gateways.
        self.running_count = running_count
        # Number of gateway instances.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.running_count is not None:
            result['runningCount'] = self.running_count
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runningCount') is not None:
            self.running_count = m.get('runningCount')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetResourceOverviewResponseBodyData(TeaModel):
    def __init__(
        self,
        api: GetResourceOverviewResponseBodyDataApi = None,
        gateway: GetResourceOverviewResponseBodyDataGateway = None,
    ):
        # API information.
        self.api = api
        # Gateway information.
        self.gateway = gateway

    def validate(self):
        if self.api:
            self.api.validate()
        if self.gateway:
            self.gateway.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['api'] = self.api.to_map()
        if self.gateway is not None:
            result['gateway'] = self.gateway.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api') is not None:
            temp_model = GetResourceOverviewResponseBodyDataApi()
            self.api = temp_model.from_map(m['api'])
        if m.get('gateway') is not None:
            temp_model = GetResourceOverviewResponseBodyDataGateway()
            self.gateway = temp_model.from_map(m['gateway'])
        return self


class GetResourceOverviewResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetResourceOverviewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Resource information.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetResourceOverviewResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetResourceOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceOverviewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetResourceOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Service = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The service details.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = Service()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceConfigRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # Language Type:
        # zh: Chinese
        # en: English
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        return self


class GetTraceConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        sample_ratio: int = None,
        service_id: str = None,
        service_port: str = None,
        trace_type: str = None,
    ):
        # Whether to Enable Tracing:
        # true: Enabled
        # false: Disabled
        self.enable = enable
        # Sampling Rate
        self.sample_ratio = sample_ratio
        # Service ID, present when the tracing type is SKYWALKING
        self.service_id = service_id
        # 服务端口，链路追踪类型为SKYWALKING时存在该参数
        self.service_port = service_port
        # Tracing Type:
        # - XTRACE
        # - SKYWALKING
        # - OPENTELEMETRY
        # - OTSKYWALKING
        self.trace_type = trace_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.sample_ratio is not None:
            result['sampleRatio'] = self.sample_ratio
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_port is not None:
            result['servicePort'] = self.service_port
        if self.trace_type is not None:
            result['traceType'] = self.trace_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('sampleRatio') is not None:
            self.sample_ratio = m.get('sampleRatio')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('servicePort') is not None:
            self.service_port = m.get('servicePort')
        if m.get('traceType') is not None:
            self.trace_type = m.get('traceType')
        return self


class GetTraceConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTraceConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response Code
        self.code = code
        # Response Data
        self.data = data
        # Error Message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Boolean	Request Result, with the following values:
        # true: Request succeeded.
        # false: Request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetTraceConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTraceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTraceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetTraceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportHttpApiRequestSpecOssConfig(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        object_key: str = None,
        region_id: str = None,
    ):
        # The bucket name.
        self.bucket_name = bucket_name
        # The full path of the file.
        self.object_key = object_key
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.object_key is not None:
            result['objectKey'] = self.object_key
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('objectKey') is not None:
            self.object_key = m.get('objectKey')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ImportHttpApiRequest(TeaModel):
    def __init__(
        self,
        deploy_configs: HttpApiDeployConfig = None,
        description: str = None,
        dry_run: bool = None,
        mcp_route_id: str = None,
        name: str = None,
        resource_group_id: str = None,
        spec_content_base_64: str = None,
        spec_file_url: str = None,
        spec_oss_config: ImportHttpApiRequestSpecOssConfig = None,
        strategy: str = None,
        target_http_api_id: str = None,
        version_config: HttpApiVersionConfig = None,
    ):
        # The deployment configuration.
        self.deploy_configs = deploy_configs
        # The API description, which cannot exceed 255 bytes in length. If you do not specify a description, a description is extracted from the definition file.
        self.description = description
        # Specifies whether to perform a dry run. If this parameter is set to true, a dry run is performed without importing the file.
        self.dry_run = dry_run
        # The MCP route ID.
        self.mcp_route_id = mcp_route_id
        # The API name. If you do not specify a name, a name is extracted from the definition file. If a name and a versioning configuration already exist, the existing API definition is updated based on the strategy field.
        self.name = name
        # [The resource group ID](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The Base64-encoded API definition. OAS 2.0 and OAS 3.0 specifications are supported. YAML and JSON formats are supported. This parameter precedes over the specFileUrl parameter. However, if the file size exceeds 10 MB, use the specFileUrl parameter to pass the definition.
        self.spec_content_base_64 = spec_content_base_64
        # The download URL of the API definition file. You can download the file over the Internet or by using an Object Storage Service (OSS) internal download URL that belongs to the current region. You must obtain the required permissions to download the file. For OSS URLs that are not publicly readable, refer to [Download objects using presigned URLs](https://help.aliyun.com/document_detail/39607.html) to specify URLs that provide download permissions. Currently, only OSS URLs are supported.
        self.spec_file_url = spec_file_url
        # The OSS information.
        self.spec_oss_config = spec_oss_config
        # The update policy when the API to be imported has the same version and name as an existing one. Valid values:
        # 
        # *   SpectOnly: All configurations in the file take effect.
        # *   SpecFirst: The file takes precedence. New APIs are created and existing ones are updated. APIs not included in the file remain unchanged.
        # *   ExistFirst (default): The existing APIs take precedence. New APIs are created but existing ones remain unchanged. If this parameter is not specified, the ExistFirst policy takes effect.
        self.strategy = strategy
        # The API to be updated. If this parameter is specified, this import updates only the specified API. New APIs are not created and unspecified existing APIs are not updated. Only REST APIs can be specified.
        self.target_http_api_id = target_http_api_id
        # The API versioning configuration. If versioning is enabled for an API and the version and name of an API to be imported are the same as those of the existing API, the existing API is updated by this import. If versioning is not enabled for an API and the name of an API to be imported are the same as that of the existing API, the existing API is updated by this import.
        self.version_config = version_config

    def validate(self):
        if self.deploy_configs:
            self.deploy_configs.validate()
        if self.spec_oss_config:
            self.spec_oss_config.validate()
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_configs is not None:
            result['deployConfigs'] = self.deploy_configs.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.mcp_route_id is not None:
            result['mcpRouteId'] = self.mcp_route_id
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.spec_content_base_64 is not None:
            result['specContentBase64'] = self.spec_content_base_64
        if self.spec_file_url is not None:
            result['specFileUrl'] = self.spec_file_url
        if self.spec_oss_config is not None:
            result['specOssConfig'] = self.spec_oss_config.to_map()
        if self.strategy is not None:
            result['strategy'] = self.strategy
        if self.target_http_api_id is not None:
            result['targetHttpApiId'] = self.target_http_api_id
        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployConfigs') is not None:
            temp_model = HttpApiDeployConfig()
            self.deploy_configs = temp_model.from_map(m['deployConfigs'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('mcpRouteId') is not None:
            self.mcp_route_id = m.get('mcpRouteId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('specContentBase64') is not None:
            self.spec_content_base_64 = m.get('specContentBase64')
        if m.get('specFileUrl') is not None:
            self.spec_file_url = m.get('specFileUrl')
        if m.get('specOssConfig') is not None:
            temp_model = ImportHttpApiRequestSpecOssConfig()
            self.spec_oss_config = temp_model.from_map(m['specOssConfig'])
        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')
        if m.get('targetHttpApiId') is not None:
            self.target_http_api_id = m.get('targetHttpApiId')
        if m.get('versionConfig') is not None:
            temp_model = HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m['versionConfig'])
        return self


class ImportHttpApiResponseBodyDataDryRunInfoFailureComponents(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        name: str = None,
    ):
        # The error message.
        self.error_message = error_message
        # The data struct name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ImportHttpApiResponseBodyDataDryRunInfoFailureOperations(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        method: str = None,
        path: str = None,
    ):
        # The error message.
        self.error_message = error_message
        # The HTTP method of the operation.
        self.method = method
        # The operation path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.method is not None:
            result['method'] = self.method
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ImportHttpApiResponseBodyDataDryRunInfoSuccessComponents(TeaModel):
    def __init__(
        self,
        action: str = None,
        name: str = None,
    ):
        # The action that will be performed for the data struct after the dry run.
        # 
        # *   Create: The data struct is created.
        # *   Update: The data struct is updated.
        self.action = action
        # The data struct name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ImportHttpApiResponseBodyDataDryRunInfoSuccessOperations(TeaModel):
    def __init__(
        self,
        action: str = None,
        method: str = None,
        name: str = None,
        path: str = None,
    ):
        # The action that will be performed for the operation after the dry run.
        # 
        # *   Create: The operation is created.
        # *   Update: The operation is updated.
        self.action = action
        # The HTTP method of the operation.
        self.method = method
        # The operation name.
        self.name = name
        # The operation path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ImportHttpApiResponseBodyDataDryRunInfo(TeaModel):
    def __init__(
        self,
        error_messages: List[str] = None,
        exist_http_api_info: HttpApiApiInfo = None,
        failure_components: List[ImportHttpApiResponseBodyDataDryRunInfoFailureComponents] = None,
        failure_operations: List[ImportHttpApiResponseBodyDataDryRunInfoFailureOperations] = None,
        success_components: List[ImportHttpApiResponseBodyDataDryRunInfoSuccessComponents] = None,
        success_operations: List[ImportHttpApiResponseBodyDataDryRunInfoSuccessOperations] = None,
        warning_messages: List[str] = None,
    ):
        # The error messages. If an error message is returned, the API fails to be imported.
        self.error_messages = error_messages
        # The existing APIs. If an existing API is returned, the import updates the existing API.
        self.exist_http_api_info = exist_http_api_info
        # The data structs that fail the dry run.
        self.failure_components = failure_components
        # The operations that fail the dry run.
        self.failure_operations = failure_operations
        # The data structs that pass the dry run.
        self.success_components = success_components
        # The operations that pass the dry run.
        self.success_operations = success_operations
        # The alerts. If an alert is returned, specific operations or structs may fail to be imported.
        self.warning_messages = warning_messages

    def validate(self):
        if self.exist_http_api_info:
            self.exist_http_api_info.validate()
        if self.failure_components:
            for k in self.failure_components:
                if k:
                    k.validate()
        if self.failure_operations:
            for k in self.failure_operations:
                if k:
                    k.validate()
        if self.success_components:
            for k in self.success_components:
                if k:
                    k.validate()
        if self.success_operations:
            for k in self.success_operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_messages is not None:
            result['errorMessages'] = self.error_messages
        if self.exist_http_api_info is not None:
            result['existHttpApiInfo'] = self.exist_http_api_info.to_map()
        result['failureComponents'] = []
        if self.failure_components is not None:
            for k in self.failure_components:
                result['failureComponents'].append(k.to_map() if k else None)
        result['failureOperations'] = []
        if self.failure_operations is not None:
            for k in self.failure_operations:
                result['failureOperations'].append(k.to_map() if k else None)
        result['successComponents'] = []
        if self.success_components is not None:
            for k in self.success_components:
                result['successComponents'].append(k.to_map() if k else None)
        result['successOperations'] = []
        if self.success_operations is not None:
            for k in self.success_operations:
                result['successOperations'].append(k.to_map() if k else None)
        if self.warning_messages is not None:
            result['warningMessages'] = self.warning_messages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessages') is not None:
            self.error_messages = m.get('errorMessages')
        if m.get('existHttpApiInfo') is not None:
            temp_model = HttpApiApiInfo()
            self.exist_http_api_info = temp_model.from_map(m['existHttpApiInfo'])
        self.failure_components = []
        if m.get('failureComponents') is not None:
            for k in m.get('failureComponents'):
                temp_model = ImportHttpApiResponseBodyDataDryRunInfoFailureComponents()
                self.failure_components.append(temp_model.from_map(k))
        self.failure_operations = []
        if m.get('failureOperations') is not None:
            for k in m.get('failureOperations'):
                temp_model = ImportHttpApiResponseBodyDataDryRunInfoFailureOperations()
                self.failure_operations.append(temp_model.from_map(k))
        self.success_components = []
        if m.get('successComponents') is not None:
            for k in m.get('successComponents'):
                temp_model = ImportHttpApiResponseBodyDataDryRunInfoSuccessComponents()
                self.success_components.append(temp_model.from_map(k))
        self.success_operations = []
        if m.get('successOperations') is not None:
            for k in m.get('successOperations'):
                temp_model = ImportHttpApiResponseBodyDataDryRunInfoSuccessOperations()
                self.success_operations.append(temp_model.from_map(k))
        if m.get('warningMessages') is not None:
            self.warning_messages = m.get('warningMessages')
        return self


class ImportHttpApiResponseBodyData(TeaModel):
    def __init__(
        self,
        dry_run_info: ImportHttpApiResponseBodyDataDryRunInfo = None,
        http_api_id: str = None,
        name: str = None,
    ):
        # The dry run result.
        self.dry_run_info = dry_run_info
        # The API ID.
        self.http_api_id = http_api_id
        # The API name.
        self.name = name

    def validate(self):
        if self.dry_run_info:
            self.dry_run_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run_info is not None:
            result['dryRunInfo'] = self.dry_run_info.to_map()
        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRunInfo') is not None:
            temp_model = ImportHttpApiResponseBodyDataDryRunInfo()
            self.dry_run_info = temp_model.from_map(m['dryRunInfo'])
        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ImportHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ImportHttpApiResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The API information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ImportHttpApiResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ImportHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ImportHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_type: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The instance ID.
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        # The domain name keyword for fuzzy search.
        self.name_like = name_like
        # The page number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListDomainsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[DomainInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The information about the domain names.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = DomainInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDomainsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code returned.
        self.code = code
        # The response data.
        self.data = data
        # The message returned.
        self.message = message
        # The request ID, which is used to trace the API call link.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListDomainsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(
        self,
        alias_like: str = None,
        gateway_id: str = None,
        gateway_name_like: str = None,
        gateway_type: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # Environment alias, fuzzy search.
        self.alias_like = alias_like
        # Gateway ID, exact search.
        self.gateway_id = gateway_id
        # Gateway name, fuzzy search.
        self.gateway_name_like = gateway_name_like
        self.gateway_type = gateway_type
        # Environment name, fuzzy search.
        self.name_like = name_like
        # Page number, default is 1.
        self.page_number = page_number
        # Page size, default is 10.
        self.page_size = page_size
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_like is not None:
            result['aliasLike'] = self.alias_like
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_name_like is not None:
            result['gatewayNameLike'] = self.gateway_name_like
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasLike') is not None:
            self.alias_like = m.get('aliasLike')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayNameLike') is not None:
            self.gateway_name_like = m.get('gatewayNameLike')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[EnvironmentInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # List of environment information.
        self.items = items
        # Page number.
        self.page_number = page_number
        # Number of items per page.
        self.page_size = page_size
        # Total number of items.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = EnvironmentInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListEnvironmentsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Paged query environment list response.
        self.data = data
        # Response message.
        self.message = message
        # Request ID, used for tracing the call chain.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnvironmentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewaysRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListGatewaysRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_type: str = None,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tag: List[ListGatewaysRequestTag] = None,
    ):
        # The instance ID. If you specify an ID, an exact search is performed.
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        # The search keyword. A full match is performed. The search is case-insensitive.
        self.keyword = keyword
        # The instance name. If you specify a name, an exact search is performed.
        self.name = name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags that you want to use for the search.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListGatewaysRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListGatewaysShrinkRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_type: str = None,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tag_shrink: str = None,
    ):
        # The instance ID. If you specify an ID, an exact search is performed.
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        # The search keyword. A full match is performed. The search is case-insensitive.
        self.keyword = keyword
        # The instance name. If you specify a name, an exact search is performed.
        self.name = name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags that you want to use for the search.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListGatewaysResponseBodyDataItemsLoadBalancersPorts(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListGatewaysResponseBodyDataItemsLoadBalancers(TeaModel):
    def __init__(
        self,
        address: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        gateway_default: bool = None,
        load_balancer_id: str = None,
        mode: str = None,
        ports: List[ListGatewaysResponseBodyDataItemsLoadBalancersPorts] = None,
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
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.address_ip_version is not None:
            result['addressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['addressType'] = self.address_type
        if self.gateway_default is not None:
            result['gatewayDefault'] = self.gateway_default
        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id
        if self.mode is not None:
            result['mode'] = self.mode
        result['ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['ports'].append(k.to_map() if k else None)
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
        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        self.ports = []
        if m.get('ports') is not None:
            for k in m.get('ports'):
                temp_model = ListGatewaysResponseBodyDataItemsLoadBalancersPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListGatewaysResponseBodyDataItemsSecurityGroup(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
    ):
        # The security group ID.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        return self


class ListGatewaysResponseBodyDataItemsTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListGatewaysResponseBodyDataItemsVSwitch(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        return self


class ListGatewaysResponseBodyDataItemsVpc(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListGatewaysResponseBodyDataItemsZonesVSwitch(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        return self


class ListGatewaysResponseBodyDataItemsZones(TeaModel):
    def __init__(
        self,
        v_switch: ListGatewaysResponseBodyDataItemsZonesVSwitch = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch is not None:
            result['vSwitch'] = self.v_switch.to_map()
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitch') is not None:
            temp_model = ListGatewaysResponseBodyDataItemsZonesVSwitch()
            self.v_switch = temp_model.from_map(m['vSwitch'])
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ListGatewaysResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        expire_timestamp: int = None,
        gateway_id: str = None,
        gateway_type: str = None,
        legacy: bool = None,
        load_balancers: List[ListGatewaysResponseBodyDataItemsLoadBalancers] = None,
        name: str = None,
        replicas: str = None,
        resource_group_id: str = None,
        security_group: ListGatewaysResponseBodyDataItemsSecurityGroup = None,
        spec: str = None,
        status: str = None,
        sub_domain_infos: List[SubDomainInfo] = None,
        tags: List[ListGatewaysResponseBodyDataItemsTags] = None,
        target_version: str = None,
        update_timestamp: int = None,
        v_switch: ListGatewaysResponseBodyDataItemsVSwitch = None,
        version: str = None,
        vpc: ListGatewaysResponseBodyDataItemsVpc = None,
        zones: List[ListGatewaysResponseBodyDataItemsZones] = None,
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
            for k in self.load_balancers:
                if k:
                    k.validate()
        if self.security_group:
            self.security_group.validate()
        if self.sub_domain_infos:
            for k in self.sub_domain_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.v_switch:
            self.v_switch.validate()
        if self.vpc:
            self.vpc.validate()
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.create_from is not None:
            result['createFrom'] = self.create_from
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.legacy is not None:
            result['legacy'] = self.legacy
        result['loadBalancers'] = []
        if self.load_balancers is not None:
            for k in self.load_balancers:
                result['loadBalancers'].append(k.to_map() if k else None)
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
            for k in self.sub_domain_infos:
                result['subDomainInfos'].append(k.to_map() if k else None)
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
            for k in self.zones:
                result['zones'].append(k.to_map() if k else None)
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
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('legacy') is not None:
            self.legacy = m.get('legacy')
        self.load_balancers = []
        if m.get('loadBalancers') is not None:
            for k in m.get('loadBalancers'):
                temp_model = ListGatewaysResponseBodyDataItemsLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('securityGroup') is not None:
            temp_model = ListGatewaysResponseBodyDataItemsSecurityGroup()
            self.security_group = temp_model.from_map(m['securityGroup'])
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k in m.get('subDomainInfos'):
                temp_model = SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k))
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListGatewaysResponseBodyDataItemsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')
        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')
        if m.get('vSwitch') is not None:
            temp_model = ListGatewaysResponseBodyDataItemsVSwitch()
            self.v_switch = temp_model.from_map(m['vSwitch'])
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('vpc') is not None:
            temp_model = ListGatewaysResponseBodyDataItemsVpc()
            self.vpc = temp_model.from_map(m['vpc'])
        self.zones = []
        if m.get('zones') is not None:
            for k in m.get('zones'):
                temp_model = ListGatewaysResponseBodyDataItemsZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListGatewaysResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListGatewaysResponseBodyDataItems] = None,
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
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = ListGatewaysResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListGatewaysResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListGatewaysResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGatewaysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHttpApiOperationsRequest(TeaModel):
    def __init__(
        self,
        consumer_authorization_rule_id: str = None,
        for_deploy: bool = None,
        gateway_id: str = None,
        method: str = None,
        name: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        path_like: str = None,
        with_consumer_in_environment_id: str = None,
        with_consumer_info_by_id: str = None,
        with_plugin_attachment_by_plugin_id: str = None,
    ):
        # Filter the operation list based on a specific consumer authorization rule ID, and the interface list in the response only contains authorized operations.
        self.consumer_authorization_rule_id = consumer_authorization_rule_id
        self.for_deploy = for_deploy
        self.gateway_id = gateway_id
        # List interfaces by Method.
        self.method = method
        # Search operations by exact name.
        self.name = name
        # Search operations by name prefix.
        self.name_like = name_like
        # Page number, starting from 1, default is 1 if not specified.
        self.page_number = page_number
        # Page size, valid range [1, 100], default is 10 if not specified.
        self.page_size = page_size
        # Search operations by path prefix.
        self.path_like = path_like
        # Each operation information in the response carries a list of authorization rules for the specified consumer under the specified environment ID. The withConsumerInEnvironmentId field needs to be additionally specified.
        self.with_consumer_in_environment_id = with_consumer_in_environment_id
        # Each operation information in the response carries a list of authorization rules for the specified consumer under the specified environment ID. The withConsumerInEnvironmentId field needs to be additionally specified.
        self.with_consumer_info_by_id = with_consumer_info_by_id
        # Plugin ID, use this plugin ID to retrieve the plugin release information.
        self.with_plugin_attachment_by_plugin_id = with_plugin_attachment_by_plugin_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_authorization_rule_id is not None:
            result['consumerAuthorizationRuleId'] = self.consumer_authorization_rule_id
        if self.for_deploy is not None:
            result['forDeploy'] = self.for_deploy
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.path_like is not None:
            result['pathLike'] = self.path_like
        if self.with_consumer_in_environment_id is not None:
            result['withConsumerInEnvironmentId'] = self.with_consumer_in_environment_id
        if self.with_consumer_info_by_id is not None:
            result['withConsumerInfoById'] = self.with_consumer_info_by_id
        if self.with_plugin_attachment_by_plugin_id is not None:
            result['withPluginAttachmentByPluginId'] = self.with_plugin_attachment_by_plugin_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerAuthorizationRuleId') is not None:
            self.consumer_authorization_rule_id = m.get('consumerAuthorizationRuleId')
        if m.get('forDeploy') is not None:
            self.for_deploy = m.get('forDeploy')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pathLike') is not None:
            self.path_like = m.get('pathLike')
        if m.get('withConsumerInEnvironmentId') is not None:
            self.with_consumer_in_environment_id = m.get('withConsumerInEnvironmentId')
        if m.get('withConsumerInfoById') is not None:
            self.with_consumer_info_by_id = m.get('withConsumerInfoById')
        if m.get('withPluginAttachmentByPluginId') is not None:
            self.with_plugin_attachment_by_plugin_id = m.get('withPluginAttachmentByPluginId')
        return self


class ListHttpApiOperationsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[HttpApiOperationInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # List of operations.
        self.items = items
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Total count.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = HttpApiOperationInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListHttpApiOperationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListHttpApiOperationsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # List of operations.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListHttpApiOperationsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListHttpApiOperationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHttpApiOperationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHttpApiOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHttpApiRoutesRequest(TeaModel):
    def __init__(
        self,
        consumer_authorization_rule_id: str = None,
        deploy_statuses: str = None,
        domain_id: str = None,
        environment_id: str = None,
        for_deploy: bool = None,
        gateway_id: str = None,
        name: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        path_like: str = None,
        with_auth_policy_info: bool = None,
        with_consumer_info_by_id: str = None,
        with_plugin_attachment_by_plugin_id: str = None,
    ):
        # The string that is used to filter routes based on consumer authentication rules. Only authorized APIs are returned.
        self.consumer_authorization_rule_id = consumer_authorization_rule_id
        # The deployment state of the route.
        # 
        # Enumerated values:
        # 
        # *   Deploying: The route is being deployed.
        # *   DeployedWithChanges: The route is deployed and modified.
        # *   Undeploying: The route is being undeployed.
        # *   NotDeployed: The route is not deployed.
        # *   Deployed: The route is deployed.
        # *   UndeployFailed: The route failed to be undeployed.
        # *   DeployFailed: The route failed to be deployed.
        self.deploy_statuses = deploy_statuses
        # Specifies to filter routes by domain ID.
        self.domain_id = domain_id
        # The environment ID.
        self.environment_id = environment_id
        self.for_deploy = for_deploy
        # The ID of the Cloud-native API Gateway instance.
        self.gateway_id = gateway_id
        # The route name.
        self.name = name
        # The route name keyword for a fuzzy search.
        self.name_like = name_like
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The route path keyword for a fuzzy search.
        self.path_like = path_like
        # The consumer authorization information in the response.
        self.with_auth_policy_info = with_auth_policy_info
        # The authentication rules of the specified consumer in each route returned.
        self.with_consumer_info_by_id = with_consumer_info_by_id
        # The mounting information of the specified plug-in in each route returned.
        self.with_plugin_attachment_by_plugin_id = with_plugin_attachment_by_plugin_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_authorization_rule_id is not None:
            result['consumerAuthorizationRuleId'] = self.consumer_authorization_rule_id
        if self.deploy_statuses is not None:
            result['deployStatuses'] = self.deploy_statuses
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.for_deploy is not None:
            result['forDeploy'] = self.for_deploy
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.name_like is not None:
            result['nameLike'] = self.name_like
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.path_like is not None:
            result['pathLike'] = self.path_like
        if self.with_auth_policy_info is not None:
            result['withAuthPolicyInfo'] = self.with_auth_policy_info
        if self.with_consumer_info_by_id is not None:
            result['withConsumerInfoById'] = self.with_consumer_info_by_id
        if self.with_plugin_attachment_by_plugin_id is not None:
            result['withPluginAttachmentByPluginId'] = self.with_plugin_attachment_by_plugin_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerAuthorizationRuleId') is not None:
            self.consumer_authorization_rule_id = m.get('consumerAuthorizationRuleId')
        if m.get('deployStatuses') is not None:
            self.deploy_statuses = m.get('deployStatuses')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('forDeploy') is not None:
            self.for_deploy = m.get('forDeploy')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pathLike') is not None:
            self.path_like = m.get('pathLike')
        if m.get('withAuthPolicyInfo') is not None:
            self.with_auth_policy_info = m.get('withAuthPolicyInfo')
        if m.get('withConsumerInfoById') is not None:
            self.with_consumer_info_by_id = m.get('withConsumerInfoById')
        if m.get('withPluginAttachmentByPluginId') is not None:
            self.with_plugin_attachment_by_plugin_id = m.get('withPluginAttachmentByPluginId')
        return self


class ListHttpApiRoutesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[HttpRoute] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The routes.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = HttpRoute()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListHttpApiRoutesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListHttpApiRoutesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListHttpApiRoutesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListHttpApiRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHttpApiRoutesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHttpApiRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHttpApisRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_type: str = None,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        types: str = None,
        with_apis_published_to_environment: bool = None,
        with_auth_policy_in_environment_id: str = None,
        with_auth_policy_list: bool = None,
        with_consumer_info_by_id: str = None,
        with_environment_info: bool = None,
        with_environment_info_by_id: str = None,
        with_ingress_info: bool = None,
        with_plugin_attachment_by_plugin_id: str = None,
        with_policy_configs: bool = None,
    ):
        # The ID of the Cloud-native API Gateway instance.
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        # The search keyword. You can fuzzy-search by API name or exact-search by API ID.
        self.keyword = keyword
        # The API name that is used for the search. In this case, exact search is performed.
        self.name = name
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The API type. You can specify multiple types and separate them with a comma (,).
        # 
        # *   Http
        # *   Rest
        # *   WebSocket
        # *   HttpIngress
        self.types = types
        self.with_apis_published_to_environment = with_apis_published_to_environment
        # The consumer authentication policy in the specified environment in each returned API.
        self.with_auth_policy_in_environment_id = with_auth_policy_in_environment_id
        # Specifies whether authentication is enabled.
        self.with_auth_policy_list = with_auth_policy_list
        # The authorization rules of the specified consumer in each returned API.
        self.with_consumer_info_by_id = with_consumer_info_by_id
        # The environment information.
        self.with_environment_info = with_environment_info
        # The environment ID.
        self.with_environment_info_by_id = with_environment_info_by_id
        # The Ingress information.
        self.with_ingress_info = with_ingress_info
        # The plug-in ID. You can use the returned value of this parameter to query the plug-in.
        self.with_plugin_attachment_by_plugin_id = with_plugin_attachment_by_plugin_id
        self.with_policy_configs = with_policy_configs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.types is not None:
            result['types'] = self.types
        if self.with_apis_published_to_environment is not None:
            result['withAPIsPublishedToEnvironment'] = self.with_apis_published_to_environment
        if self.with_auth_policy_in_environment_id is not None:
            result['withAuthPolicyInEnvironmentId'] = self.with_auth_policy_in_environment_id
        if self.with_auth_policy_list is not None:
            result['withAuthPolicyList'] = self.with_auth_policy_list
        if self.with_consumer_info_by_id is not None:
            result['withConsumerInfoById'] = self.with_consumer_info_by_id
        if self.with_environment_info is not None:
            result['withEnvironmentInfo'] = self.with_environment_info
        if self.with_environment_info_by_id is not None:
            result['withEnvironmentInfoById'] = self.with_environment_info_by_id
        if self.with_ingress_info is not None:
            result['withIngressInfo'] = self.with_ingress_info
        if self.with_plugin_attachment_by_plugin_id is not None:
            result['withPluginAttachmentByPluginId'] = self.with_plugin_attachment_by_plugin_id
        if self.with_policy_configs is not None:
            result['withPolicyConfigs'] = self.with_policy_configs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('types') is not None:
            self.types = m.get('types')
        if m.get('withAPIsPublishedToEnvironment') is not None:
            self.with_apis_published_to_environment = m.get('withAPIsPublishedToEnvironment')
        if m.get('withAuthPolicyInEnvironmentId') is not None:
            self.with_auth_policy_in_environment_id = m.get('withAuthPolicyInEnvironmentId')
        if m.get('withAuthPolicyList') is not None:
            self.with_auth_policy_list = m.get('withAuthPolicyList')
        if m.get('withConsumerInfoById') is not None:
            self.with_consumer_info_by_id = m.get('withConsumerInfoById')
        if m.get('withEnvironmentInfo') is not None:
            self.with_environment_info = m.get('withEnvironmentInfo')
        if m.get('withEnvironmentInfoById') is not None:
            self.with_environment_info_by_id = m.get('withEnvironmentInfoById')
        if m.get('withIngressInfo') is not None:
            self.with_ingress_info = m.get('withIngressInfo')
        if m.get('withPluginAttachmentByPluginId') is not None:
            self.with_plugin_attachment_by_plugin_id = m.get('withPluginAttachmentByPluginId')
        if m.get('withPolicyConfigs') is not None:
            self.with_policy_configs = m.get('withPolicyConfigs')
        return self


class ListHttpApisResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[HttpApiInfoByName] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The API information.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = HttpApiInfoByName()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListHttpApisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListHttpApisResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The APIs.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListHttpApisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListHttpApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHttpApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListHttpApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPluginsRequest(TeaModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        gateway_id: str = None,
        gateway_type: str = None,
        include_builtin_ai_gateway: bool = None,
        page_number: int = None,
        page_size: int = None,
        plugin_class_id: str = None,
        plugin_class_name: str = None,
        with_attachment_info: bool = None,
    ):
        self.attach_resource_id = attach_resource_id
        self.attach_resource_type = attach_resource_type
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        self.include_builtin_ai_gateway = include_builtin_ai_gateway
        self.page_number = page_number
        self.page_size = page_size
        self.plugin_class_id = plugin_class_id
        self.plugin_class_name = plugin_class_name
        self.with_attachment_info = with_attachment_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_id is not None:
            result['attachResourceId'] = self.attach_resource_id
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type
        if self.include_builtin_ai_gateway is not None:
            result['includeBuiltinAiGateway'] = self.include_builtin_ai_gateway
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id
        if self.plugin_class_name is not None:
            result['pluginClassName'] = self.plugin_class_name
        if self.with_attachment_info is not None:
            result['withAttachmentInfo'] = self.with_attachment_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')
        if m.get('includeBuiltinAiGateway') is not None:
            self.include_builtin_ai_gateway = m.get('includeBuiltinAiGateway')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')
        if m.get('pluginClassName') is not None:
            self.plugin_class_name = m.get('pluginClassName')
        if m.get('withAttachmentInfo') is not None:
            self.with_attachment_info = m.get('withAttachmentInfo')
        return self


class ListPluginsResponseBodyDataItemsAttachmentInfo(TeaModel):
    def __init__(
        self,
        enable: str = None,
        plugin_attachment_id: str = None,
    ):
        self.enable = enable
        self.plugin_attachment_id = plugin_attachment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.plugin_attachment_id is not None:
            result['pluginAttachmentId'] = self.plugin_attachment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('pluginAttachmentId') is not None:
            self.plugin_attachment_id = m.get('pluginAttachmentId')
        return self


class ListPluginsResponseBodyDataItemsGatewayInfo(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
    ):
        self.gateway_id = gateway_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListPluginsResponseBodyDataItemsPluginClassInfo(TeaModel):
    def __init__(
        self,
        alias: str = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        plugin_class_id: str = None,
        source: str = None,
        version: str = None,
        version_description: str = None,
    ):
        self.alias = alias
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.name = name
        self.plugin_class_id = plugin_class_id
        self.source = source
        self.version = version
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority
        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage
        if self.name is not None:
            result['name'] = self.name
        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id
        if self.source is not None:
            result['source'] = self.source
        if self.version is not None:
            result['version'] = self.version
        if self.version_description is not None:
            result['versionDescription'] = self.version_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')
        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')
        return self


class ListPluginsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        attachment_info: ListPluginsResponseBodyDataItemsAttachmentInfo = None,
        gateway_info: ListPluginsResponseBodyDataItemsGatewayInfo = None,
        plugin_class_info: ListPluginsResponseBodyDataItemsPluginClassInfo = None,
        plugin_id: str = None,
    ):
        self.attachment_info = attachment_info
        self.gateway_info = gateway_info
        self.plugin_class_info = plugin_class_info
        self.plugin_id = plugin_id

    def validate(self):
        if self.attachment_info:
            self.attachment_info.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.plugin_class_info:
            self.plugin_class_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_info is not None:
            result['attachmentInfo'] = self.attachment_info.to_map()
        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()
        if self.plugin_class_info is not None:
            result['pluginClassInfo'] = self.plugin_class_info.to_map()
        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachmentInfo') is not None:
            temp_model = ListPluginsResponseBodyDataItemsAttachmentInfo()
            self.attachment_info = temp_model.from_map(m['attachmentInfo'])
        if m.get('gatewayInfo') is not None:
            temp_model = ListPluginsResponseBodyDataItemsGatewayInfo()
            self.gateway_info = temp_model.from_map(m['gatewayInfo'])
        if m.get('pluginClassInfo') is not None:
            temp_model = ListPluginsResponseBodyDataItemsPluginClassInfo()
            self.plugin_class_info = temp_model.from_map(m['pluginClassInfo'])
        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')
        return self


class ListPluginsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListPluginsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = ListPluginsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListPluginsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListPluginsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListPluginsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListPluginsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPluginsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyClassesRequest(TeaModel):
    def __init__(
        self,
        attach_resource_type: str = None,
        direction: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # Types of attachment points supported by the policy.
        # 
        # - HttpApi: HttpApi.
        # - Operation: Operation of HttpApi.
        # - GatewayRoute: Gateway route.
        # - GatewayService: Gateway service.
        # - GatewayServicePort: Gateway service port.
        # - Domain: Gateway domain.
        # - Gateway: Gateway.
        self.attach_resource_type = attach_resource_type
        # Direction of the policy.
        # - Outbound: OutBound.
        # - Inbound: InBound.
        # - Both directions: Both.
        self.direction = direction
        # Page number, default is 1.
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Type of the policy template.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type
        if self.direction is not None:
            result['direction'] = self.direction
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListPolicyClassesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[PolicyClassInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # List of policy templates
        self.items = items
        # Page number.
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Total number of items.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = PolicyClassInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListPolicyClassesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListPolicyClassesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Policy template information.
        self.data = data
        # ResponseMessage
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListPolicyClassesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListPolicyClassesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyClassesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListPolicyClassesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        source_type: str = None,
        source_types: str = None,
    ):
        # The ID of the Cloud-native API Gateway instance.
        self.gateway_id = gateway_id
        # The service name.
        self.name = name
        # The page number to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The service source. Valid values:
        # 
        # *   MSE_NACOS: a service in an MSE Nacos instance
        # *   K8S: a service in a Kubernetes (K8s) cluster in Container Service for Kubernetes (ACK)
        # *   FC3: a service in Function Compute
        # *   VIP: a fixed address
        # *   DNS: a domain name
        # 
        # Enumerated values:
        # 
        # *   K8S
        # *   FC3
        # *   DNS
        # *   VIP
        # *   MSE_NACOS
        self.source_type = source_type
        self.source_types = source_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.source_types is not None:
            result['sourceTypes'] = self.source_types
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
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('sourceTypes') is not None:
            self.source_types = m.get('sourceTypes')
        return self


class ListServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[Service] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The services.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = Service()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListServicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListServicesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSslCertsRequest(TeaModel):
    def __init__(
        self,
        cert_name_like: str = None,
        domain_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Name matching keyword.
        self.cert_name_like = cert_name_like
        # Domain name.
        self.domain_name = domain_name
        # Page number, default is 1
        self.page_number = page_number
        # Page size, default is 10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name_like is not None:
            result['certNameLike'] = self.cert_name_like
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certNameLike') is not None:
            self.cert_name_like = m.get('certNameLike')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListSslCertsResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[SslCertMetaInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # List of certificate information.
        self.items = items
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size
        # Total count.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
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
            for k in m.get('items'):
                temp_model = SslCertMetaInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListSslCertsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSslCertsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Returned data
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListSslCertsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSslCertsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSslCertsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListSslCertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        # 可用区ID。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ListZonesResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[ListZonesResponseBodyDataItems] = None,
    ):
        # List of availability zones.
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListZonesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListZonesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListZonesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Returned data.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListZonesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RestartGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RestartGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UndeployHttpApiRequest(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
        gateway_id: str = None,
        operation_id: str = None,
        route_id: str = None,
    ):
        # The environment ID.
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.operation_id = operation_id
        # Route ID. This must be provided when publishing the route of an HTTP API.
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        if self.route_id is not None:
            result['routeId'] = self.route_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')
        return self


class UndeployHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UndeployHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UndeployHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UndeployHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDomainRequest(TeaModel):
    def __init__(
        self,
        ca_cert_identifier: str = None,
        cert_identifier: str = None,
        client_cacert: str = None,
        force_https: bool = None,
        http_2option: str = None,
        m_tlsenabled: bool = None,
        protocol: str = None,
        tls_cipher_suites_config: TlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        # The CA certificate ID.
        self.ca_cert_identifier = ca_cert_identifier
        # The certificate ID.
        self.cert_identifier = cert_identifier
        # The client CA certificate.
        self.client_cacert = client_cacert
        # Specifies whether to enable HTTPS redirection. If protocol is set to HTTPS, forceHttps is required.
        self.force_https = force_https
        # The HTTP/2 configuration.
        # 
        # Enumerated values:
        # 
        # *   GlobalConfig
        # *   Close
        # *   Open
        self.http_2option = http_2option
        # Specifies whether to enable mutual TLS (mTLS) authentication.
        self.m_tlsenabled = m_tlsenabled
        # The protocol type to be supported by the domain name. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # 
        # This parameter is required.
        self.protocol = protocol
        # The cipher suite configuration.
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum TLS version. Up to TLS 1.3 is supported.
        self.tls_max = tls_max
        # The minimum TLS version. Down to TLS 1.0 is supported.
        self.tls_min = tls_min

    def validate(self):
        if self.tls_cipher_suites_config:
            self.tls_cipher_suites_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert_identifier is not None:
            result['caCertIdentifier'] = self.ca_cert_identifier
        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier
        if self.client_cacert is not None:
            result['clientCACert'] = self.client_cacert
        if self.force_https is not None:
            result['forceHttps'] = self.force_https
        if self.http_2option is not None:
            result['http2Option'] = self.http_2option
        if self.m_tlsenabled is not None:
            result['mTLSEnabled'] = self.m_tlsenabled
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.tls_cipher_suites_config is not None:
            result['tlsCipherSuitesConfig'] = self.tls_cipher_suites_config.to_map()
        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max
        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caCertIdentifier') is not None:
            self.ca_cert_identifier = m.get('caCertIdentifier')
        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')
        if m.get('clientCACert') is not None:
            self.client_cacert = m.get('clientCACert')
        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')
        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')
        if m.get('mTLSEnabled') is not None:
            self.m_tlsenabled = m.get('mTLSEnabled')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('tlsCipherSuitesConfig') is not None:
            temp_model = TlsCipherSuitesConfig()
            self.tls_cipher_suites_config = temp_model.from_map(m['tlsCipherSuitesConfig'])
        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')
        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')
        return self


class UpdateDomainResponseBodyData(TeaModel):
    def __init__(
        self,
        deploy_revision_id: str = None,
    ):
        # The released version ID.
        self.deploy_revision_id = deploy_revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_revision_id is not None:
            result['deployRevisionId'] = self.deploy_revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployRevisionId') is not None:
            self.deploy_revision_id = m.get('deployRevisionId')
        return self


class UpdateDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateDomainResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID. You can use this value to trace the API call.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateDomainResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
    ):
        # Environment alias.
        # 
        # This parameter is required.
        self.alias = alias
        # Description of the environment, which can include information such as the purpose of the environment and its users.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateEnvironmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID, used for tracing the API call chain.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnvironmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayFeatureRequest(TeaModel):
    def __init__(
        self,
        value: str = None,
    ):
        # Parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateGatewayFeatureResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateGatewayFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayFeatureResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateGatewayFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # Gateway name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateGatewayNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateGatewayNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateGatewayNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpApiRequestIngressConfig(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
        ingress_class: str = None,
        override_ingress_ip: bool = None,
        source_id: str = None,
        watch_namespace: str = None,
    ):
        # The environment ID.
        self.environment_id = environment_id
        # The Ingress class for listening.
        self.ingress_class = ingress_class
        # Specifies whether to update the address in Ingress Status.
        self.override_ingress_ip = override_ingress_ip
        # The source ID.
        self.source_id = source_id
        # The namespace for listening.
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class
        if self.override_ingress_ip is not None:
            result['overrideIngressIp'] = self.override_ingress_ip
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')
        if m.get('overrideIngressIp') is not None:
            self.override_ingress_ip = m.get('overrideIngressIp')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')
        return self


class UpdateHttpApiRequest(TeaModel):
    def __init__(
        self,
        ai_protocols: List[str] = None,
        auth_config: AuthConfig = None,
        base_path: str = None,
        deploy_configs: List[HttpApiDeployConfig] = None,
        description: str = None,
        enable_auth: bool = None,
        ingress_config: UpdateHttpApiRequestIngressConfig = None,
        only_change_config: bool = None,
        protocols: List[str] = None,
        version_config: HttpApiVersionConfig = None,
    ):
        # The AI protocols.
        self.ai_protocols = ai_protocols
        # The authentication configuration.
        self.auth_config = auth_config
        # The API base path, which must start with a forward slash (/).
        # 
        # This parameter is required.
        self.base_path = base_path
        # The deployment configurations.
        self.deploy_configs = deploy_configs
        # The API description.
        self.description = description
        # Specifies whether to enable authentication.
        self.enable_auth = enable_auth
        # The HTTP Ingress API configurations.
        self.ingress_config = ingress_config
        self.only_change_config = only_change_config
        # The protocols that are used to access the API.
        self.protocols = protocols
        # The versioning configurations.
        self.version_config = version_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()
        if self.ingress_config:
            self.ingress_config.validate()
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_protocols is not None:
            result['aiProtocols'] = self.ai_protocols
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.base_path is not None:
            result['basePath'] = self.base_path
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth
        if self.ingress_config is not None:
            result['ingressConfig'] = self.ingress_config.to_map()
        if self.only_change_config is not None:
            result['onlyChangeConfig'] = self.only_change_config
        if self.protocols is not None:
            result['protocols'] = self.protocols
        if self.version_config is not None:
            result['versionConfig'] = self.version_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiProtocols') is not None:
            self.ai_protocols = m.get('aiProtocols')
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')
        if m.get('ingressConfig') is not None:
            temp_model = UpdateHttpApiRequestIngressConfig()
            self.ingress_config = temp_model.from_map(m['ingressConfig'])
        if m.get('onlyChangeConfig') is not None:
            self.only_change_config = m.get('onlyChangeConfig')
        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')
        if m.get('versionConfig') is not None:
            temp_model = HttpApiVersionConfig()
            self.version_config = temp_model.from_map(m['versionConfig'])
        return self


class UpdateHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHttpApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpApiOperationRequest(TeaModel):
    def __init__(
        self,
        operation: HttpApiOperation = None,
    ):
        # operation definition.
        self.operation = operation

    def validate(self):
        if self.operation:
            self.operation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['operation'] = self.operation.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operation') is not None:
            temp_model = HttpApiOperation()
            self.operation = temp_model.from_map(m['operation'])
        return self


class UpdateHttpApiOperationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateHttpApiOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHttpApiOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateHttpApiOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpApiRouteRequestBackendConfigServices(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        # The service port. If you want to use a dynamic port, do not pass this parameter.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.protocol = protocol
        # The service ID.
        self.service_id = service_id
        # The service version.
        self.version = version
        # The percentage value of traffic.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class UpdateHttpApiRouteRequestBackendConfig(TeaModel):
    def __init__(
        self,
        scene: str = None,
        services: List[UpdateHttpApiRouteRequestBackendConfigServices] = None,
    ):
        # The backend service scenario.
        # 
        # Valid values:
        # 
        # *   SingleService
        # *   MultiServiceByRatio
        # *   Redirect
        # *   Mock
        self.scene = scene
        # The backend services.
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = UpdateHttpApiRouteRequestBackendConfigServices()
                self.services.append(temp_model.from_map(k))
        return self


class UpdateHttpApiRouteRequest(TeaModel):
    def __init__(
        self,
        backend_config: UpdateHttpApiRouteRequestBackendConfig = None,
        deploy_configs: List[HttpApiDeployConfig] = None,
        description: str = None,
        domain_ids: List[str] = None,
        environment_id: str = None,
        match: HttpRouteMatch = None,
    ):
        # The backend service configurations of the route.
        self.backend_config = backend_config
        self.deploy_configs = deploy_configs
        # The route description.
        self.description = description
        # The domain IDs.
        self.domain_ids = domain_ids
        # The environment ID.
        self.environment_id = environment_id
        # The rules for matching the route.
        self.match = match

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
        if self.deploy_configs:
            for k in self.deploy_configs:
                if k:
                    k.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_config is not None:
            result['backendConfig'] = self.backend_config.to_map()
        result['deployConfigs'] = []
        if self.deploy_configs is not None:
            for k in self.deploy_configs:
                result['deployConfigs'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.match is not None:
            result['match'] = self.match.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backendConfig') is not None:
            temp_model = UpdateHttpApiRouteRequestBackendConfig()
            self.backend_config = temp_model.from_map(m['backendConfig'])
        self.deploy_configs = []
        if m.get('deployConfigs') is not None:
            for k in m.get('deployConfigs'):
                temp_model = HttpApiDeployConfig()
                self.deploy_configs.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('match') is not None:
            temp_model = HttpRouteMatch()
            self.match = temp_model.from_map(m['match'])
        return self


class UpdateHttpApiRouteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateHttpApiRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateHttpApiRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateHttpApiRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePluginAttachmentRequest(TeaModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        enable: bool = None,
        plugin_config: str = None,
    ):
        self.attach_resource_ids = attach_resource_ids
        self.enable = enable
        self.plugin_config = plugin_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids
        if self.enable is not None:
            result['enable'] = self.enable
        if self.plugin_config is not None:
            result['pluginConfig'] = self.plugin_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('pluginConfig') is not None:
            self.plugin_config = m.get('pluginConfig')
        return self


class UpdatePluginAttachmentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePluginAttachmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePluginAttachmentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdatePluginAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        name: str = None,
    ):
        # Policy configuration
        # 
        # This parameter is required.
        self.config = config
        # Description
        self.description = description
        # Policy name
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeGatewayRequest(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        # Gateway version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpgradeGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpgradeGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


