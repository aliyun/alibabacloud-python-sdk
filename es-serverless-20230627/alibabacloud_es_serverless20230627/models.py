# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreateAppRequestAuthenticationBasicAuth(TeaModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class CreateAppRequestAuthentication(TeaModel):
    def __init__(
        self,
        basic_auth: List[CreateAppRequestAuthenticationBasicAuth] = None,
    ):
        self.basic_auth = basic_auth

    def validate(self):
        if self.basic_auth:
            for k in self.basic_auth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['basicAuth'] = []
        if self.basic_auth is not None:
            for k in self.basic_auth:
                result['basicAuth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.basic_auth = []
        if m.get('basicAuth') is not None:
            for k in m.get('basicAuth'):
                temp_model = CreateAppRequestAuthenticationBasicAuth()
                self.basic_auth.append(temp_model.from_map(k))
        return self


class CreateAppRequestNetworkWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        self.group_name = group_name
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class CreateAppRequestNetwork(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        port: int = None,
        type: str = None,
        white_ip_group: List[CreateAppRequestNetworkWhiteIpGroup] = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.port = port
        self.type = type
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for k in self.white_ip_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.port is not None:
            result['port'] = self.port
        if self.type is not None:
            result['type'] = self.type
        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k in self.white_ip_group:
                result['whiteIpGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('type') is not None:
            self.type = m.get('type')
        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k in m.get('whiteIpGroup'):
                temp_model = CreateAppRequestNetworkWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k))
        return self


class CreateAppRequestPrivateNetworkWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        self.group_name = group_name
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class CreateAppRequestPrivateNetwork(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        pvl_endpoint_id: str = None,
        type: str = None,
        vpc_id: str = None,
        white_ip_group: List[CreateAppRequestPrivateNetworkWhiteIpGroup] = None,
    ):
        self.enabled = enabled
        self.pvl_endpoint_id = pvl_endpoint_id
        self.type = type
        self.vpc_id = vpc_id
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for k in self.white_ip_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.pvl_endpoint_id is not None:
            result['pvlEndpointId'] = self.pvl_endpoint_id
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k in self.white_ip_group:
                result['whiteIpGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('pvlEndpointId') is not None:
            self.pvl_endpoint_id = m.get('pvlEndpointId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k in m.get('whiteIpGroup'):
                temp_model = CreateAppRequestPrivateNetworkWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k))
        return self


class CreateAppRequestQuotaInfo(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        cu: int = None,
        storage: int = None,
    ):
        self.app_type = app_type
        self.cu = cu
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.cu is not None:
            result['cu'] = self.cu
        if self.storage is not None:
            result['storage'] = self.storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        authentication: CreateAppRequestAuthentication = None,
        charge_type: str = None,
        description: str = None,
        network: List[CreateAppRequestNetwork] = None,
        private_network: List[CreateAppRequestPrivateNetwork] = None,
        quota_info: CreateAppRequestQuotaInfo = None,
        region_id: str = None,
        scenario: str = None,
        version: str = None,
        dry_run: bool = None,
    ):
        # 应用名
        # 
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.authentication = authentication
        # This parameter is required.
        self.charge_type = charge_type
        # 应用备注
        self.description = description
        self.network = network
        self.private_network = private_network
        self.quota_info = quota_info
        self.region_id = region_id
        self.scenario = scenario
        self.version = version
        self.dry_run = dry_run

    def validate(self):
        if self.authentication:
            self.authentication.validate()
        if self.network:
            for k in self.network:
                if k:
                    k.validate()
        if self.private_network:
            for k in self.private_network:
                if k:
                    k.validate()
        if self.quota_info:
            self.quota_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.description is not None:
            result['description'] = self.description
        result['network'] = []
        if self.network is not None:
            for k in self.network:
                result['network'].append(k.to_map() if k else None)
        result['privateNetwork'] = []
        if self.private_network is not None:
            for k in self.private_network:
                result['privateNetwork'].append(k.to_map() if k else None)
        if self.quota_info is not None:
            result['quotaInfo'] = self.quota_info.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.version is not None:
            result['version'] = self.version
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('authentication') is not None:
            temp_model = CreateAppRequestAuthentication()
            self.authentication = temp_model.from_map(m['authentication'])
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.network = []
        if m.get('network') is not None:
            for k in m.get('network'):
                temp_model = CreateAppRequestNetwork()
                self.network.append(temp_model.from_map(k))
        self.private_network = []
        if m.get('privateNetwork') is not None:
            for k in m.get('privateNetwork'):
                temp_model = CreateAppRequestPrivateNetwork()
                self.private_network.append(temp_model.from_map(k))
        if m.get('quotaInfo') is not None:
            temp_model = CreateAppRequestQuotaInfo()
            self.quota_info = temp_model.from_map(m['quotaInfo'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        instane_id: str = None,
    ):
        self.instane_id = instane_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instane_id is not None:
            result['instaneId'] = self.instane_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instaneId') is not None:
            self.instane_id = m.get('instaneId')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAppResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointRequestEndpointZones(TeaModel):
    def __init__(
        self,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class CreateEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_zones: List[CreateEndpointRequestEndpointZones] = None,
        name: str = None,
        vpc_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.endpoint_zones = endpoint_zones
        self.name = name
        # This parameter is required.
        self.vpc_id = vpc_id
        self.type = type

    def validate(self):
        if self.endpoint_zones:
            for k in self.endpoint_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['endpointZones'] = []
        if self.endpoint_zones is not None:
            for k in self.endpoint_zones:
                result['endpointZones'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_zones = []
        if m.get('endpointZones') is not None:
            for k in m.get('endpointZones'):
                temp_model = CreateEndpointRequestEndpointZones()
                self.endpoint_zones.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateEndpointResponseBodyResult(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
    ):
        self.endpoint_id = endpoint_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        return self


class CreateEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateEndpointResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateEndpointResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEndpointResponseBody = None,
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
            temp_model = CreateEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteAppResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        detailed: bool = None,
    ):
        self.detailed = detailed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detailed is not None:
            result['detailed'] = self.detailed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detailed') is not None:
            self.detailed = m.get('detailed')
        return self


class GetAppResponseBodyResultNetworkWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        self.group_name = group_name
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class GetAppResponseBodyResultNetwork(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        port: int = None,
        type: str = None,
        white_ip_group: List[GetAppResponseBodyResultNetworkWhiteIpGroup] = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.port = port
        self.type = type
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for k in self.white_ip_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.port is not None:
            result['port'] = self.port
        if self.type is not None:
            result['type'] = self.type
        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k in self.white_ip_group:
                result['whiteIpGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('type') is not None:
            self.type = m.get('type')
        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k in m.get('whiteIpGroup'):
                temp_model = GetAppResponseBodyResultNetworkWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k))
        return self


class GetAppResponseBodyResultPrivateNetworkWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        self.group_name = group_name
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class GetAppResponseBodyResultPrivateNetwork(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        port: int = None,
        pvl_endpoint_id: str = None,
        type: str = None,
        vpc_id: str = None,
        white_ip_group: List[GetAppResponseBodyResultPrivateNetworkWhiteIpGroup] = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.port = port
        self.pvl_endpoint_id = pvl_endpoint_id
        self.type = type
        self.vpc_id = vpc_id
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for k in self.white_ip_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.port is not None:
            result['port'] = self.port
        if self.pvl_endpoint_id is not None:
            result['pvlEndpointId'] = self.pvl_endpoint_id
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k in self.white_ip_group:
                result['whiteIpGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('pvlEndpointId') is not None:
            self.pvl_endpoint_id = m.get('pvlEndpointId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k in m.get('whiteIpGroup'):
                temp_model = GetAppResponseBodyResultPrivateNetworkWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k))
        return self


class GetAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        create_time: str = None,
        description: str = None,
        instance_id: str = None,
        modified_time: str = None,
        network: List[GetAppResponseBodyResultNetwork] = None,
        owner_id: str = None,
        private_network: List[GetAppResponseBodyResultPrivateNetwork] = None,
        region_id: str = None,
        status: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.description = description
        self.instance_id = instance_id
        self.modified_time = modified_time
        self.network = network
        self.owner_id = owner_id
        self.private_network = private_network
        self.region_id = region_id
        self.status = status
        self.version = version

    def validate(self):
        if self.network:
            for k in self.network:
                if k:
                    k.validate()
        if self.private_network:
            for k in self.private_network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        result['network'] = []
        if self.network is not None:
            for k in self.network:
                result['network'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        result['privateNetwork'] = []
        if self.private_network is not None:
            for k in self.private_network:
                result['privateNetwork'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        self.network = []
        if m.get('network') is not None:
            for k in m.get('network'):
                temp_model = GetAppResponseBodyResultNetwork()
                self.network.append(temp_model.from_map(k))
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        self.private_network = []
        if m.get('privateNetwork') is not None:
            for k in m.get('privateNetwork'):
                temp_model = GetAppResponseBodyResultPrivateNetwork()
                self.private_network.append(temp_model.from_map(k))
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAppResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppResponseBody = None,
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppQuotaResponseBodyResultLimiterInfoLimiters(TeaModel):
    def __init__(
        self,
        immutable: bool = None,
        max_value: int = None,
        min_value: int = None,
        type: str = None,
    ):
        self.immutable = immutable
        self.max_value = max_value
        self.min_value = min_value
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.immutable is not None:
            result['immutable'] = self.immutable
        if self.max_value is not None:
            result['maxValue'] = self.max_value
        if self.min_value is not None:
            result['minValue'] = self.min_value
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('immutable') is not None:
            self.immutable = m.get('immutable')
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')
        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetAppQuotaResponseBodyResultLimiterInfo(TeaModel):
    def __init__(
        self,
        limiters: List[GetAppQuotaResponseBodyResultLimiterInfoLimiters] = None,
    ):
        self.limiters = limiters

    def validate(self):
        if self.limiters:
            for k in self.limiters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['limiters'] = []
        if self.limiters is not None:
            for k in self.limiters:
                result['limiters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.limiters = []
        if m.get('limiters') is not None:
            for k in m.get('limiters'):
                temp_model = GetAppQuotaResponseBodyResultLimiterInfoLimiters()
                self.limiters.append(temp_model.from_map(k))
        return self


class GetAppQuotaResponseBodyResult(TeaModel):
    def __init__(
        self,
        limiter_info: GetAppQuotaResponseBodyResultLimiterInfo = None,
        quota_info: Dict[str, Any] = None,
    ):
        self.limiter_info = limiter_info
        self.quota_info = quota_info

    def validate(self):
        if self.limiter_info:
            self.limiter_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limiter_info is not None:
            result['limiterInfo'] = self.limiter_info.to_map()
        if self.quota_info is not None:
            result['quotaInfo'] = self.quota_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limiterInfo') is not None:
            temp_model = GetAppQuotaResponseBodyResultLimiterInfo()
            self.limiter_info = temp_model.from_map(m['limiterInfo'])
        if m.get('quotaInfo') is not None:
            self.quota_info = m.get('quotaInfo')
        return self


class GetAppQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAppQuotaResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetAppQuotaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetAppQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppQuotaResponseBody = None,
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
            temp_model = GetAppQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonitorDataRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetMonitorDataResponseBodyResult(TeaModel):
    def __init__(
        self,
        dps: Dict[str, Any] = None,
        integrity: float = None,
        message_watermark: int = None,
        metric: str = None,
        summary: float = None,
        tags: Dict[str, Any] = None,
    ):
        self.dps = dps
        self.integrity = integrity
        self.message_watermark = message_watermark
        self.metric = metric
        self.summary = summary
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dps is not None:
            result['dps'] = self.dps
        if self.integrity is not None:
            result['integrity'] = self.integrity
        if self.message_watermark is not None:
            result['messageWatermark'] = self.message_watermark
        if self.metric is not None:
            result['metric'] = self.metric
        if self.summary is not None:
            result['summary'] = self.summary
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dps') is not None:
            self.dps = m.get('dps')
        if m.get('integrity') is not None:
            self.integrity = m.get('integrity')
        if m.get('messageWatermark') is not None:
            self.message_watermark = m.get('messageWatermark')
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class GetMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[GetMonitorDataResponseBodyResult] = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetMonitorDataResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMonitorDataResponseBody = None,
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
            temp_model = GetMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        description: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.app_name = app_name
        self.create_time = create_time
        self.description = description
        self.order_type = order_type
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAppsResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        create_time: str = None,
        description: str = None,
        instance_id: str = None,
        modified_time: str = None,
        owner_id: str = None,
        region_id: str = None,
        status: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        # 代表资源名称的资源属性字段
        self.app_name = app_name
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 应用备注
        self.description = description
        self.instance_id = instance_id
        self.modified_time = modified_time
        # OwnerID账号ID
        self.owner_id = owner_id
        # 代表region的资源属性字段
        self.region_id = region_id
        # 代表资源状态的资源属性字段
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAppsResponseBodyResult] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.result = result
        # This parameter is required.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAppsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppsResponseBody = None,
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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequestAuthenticationBasicAuth(TeaModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class UpdateAppRequestAuthentication(TeaModel):
    def __init__(
        self,
        basic_auth: List[UpdateAppRequestAuthenticationBasicAuth] = None,
    ):
        self.basic_auth = basic_auth

    def validate(self):
        if self.basic_auth:
            for k in self.basic_auth:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['basicAuth'] = []
        if self.basic_auth is not None:
            for k in self.basic_auth:
                result['basicAuth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.basic_auth = []
        if m.get('basicAuth') is not None:
            for k in m.get('basicAuth'):
                temp_model = UpdateAppRequestAuthenticationBasicAuth()
                self.basic_auth.append(temp_model.from_map(k))
        return self


class UpdateAppRequestLimiterInfoLimiters(TeaModel):
    def __init__(
        self,
        max_value: int = None,
        min_value: int = None,
        type: str = None,
        values: List[str] = None,
    ):
        self.max_value = max_value
        self.min_value = min_value
        self.type = type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_value is not None:
            result['maxValue'] = self.max_value
        if self.min_value is not None:
            result['minValue'] = self.min_value
        if self.type is not None:
            result['type'] = self.type
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')
        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateAppRequestLimiterInfo(TeaModel):
    def __init__(
        self,
        limiters: List[UpdateAppRequestLimiterInfoLimiters] = None,
    ):
        self.limiters = limiters

    def validate(self):
        if self.limiters:
            for k in self.limiters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['limiters'] = []
        if self.limiters is not None:
            for k in self.limiters:
                result['limiters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.limiters = []
        if m.get('limiters') is not None:
            for k in m.get('limiters'):
                temp_model = UpdateAppRequestLimiterInfoLimiters()
                self.limiters.append(temp_model.from_map(k))
        return self


class UpdateAppRequestNetworkWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        self.group_name = group_name
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class UpdateAppRequestNetwork(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        port: int = None,
        type: str = None,
        white_ip_group: List[UpdateAppRequestNetworkWhiteIpGroup] = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.port = port
        self.type = type
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for k in self.white_ip_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.port is not None:
            result['port'] = self.port
        if self.type is not None:
            result['type'] = self.type
        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k in self.white_ip_group:
                result['whiteIpGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('type') is not None:
            self.type = m.get('type')
        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k in m.get('whiteIpGroup'):
                temp_model = UpdateAppRequestNetworkWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k))
        return self


class UpdateAppRequestPrivateNetworkWhiteIpGroup(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
    ):
        self.group_name = group_name
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class UpdateAppRequestPrivateNetwork(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        pvl_endpoint_id: str = None,
        type: str = None,
        vpc_id: str = None,
        white_ip_group: List[UpdateAppRequestPrivateNetworkWhiteIpGroup] = None,
    ):
        self.enabled = enabled
        self.pvl_endpoint_id = pvl_endpoint_id
        self.type = type
        self.vpc_id = vpc_id
        self.white_ip_group = white_ip_group

    def validate(self):
        if self.white_ip_group:
            for k in self.white_ip_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.pvl_endpoint_id is not None:
            result['pvlEndpointId'] = self.pvl_endpoint_id
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        result['whiteIpGroup'] = []
        if self.white_ip_group is not None:
            for k in self.white_ip_group:
                result['whiteIpGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('pvlEndpointId') is not None:
            self.pvl_endpoint_id = m.get('pvlEndpointId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        self.white_ip_group = []
        if m.get('whiteIpGroup') is not None:
            for k in m.get('whiteIpGroup'):
                temp_model = UpdateAppRequestPrivateNetworkWhiteIpGroup()
                self.white_ip_group.append(temp_model.from_map(k))
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        apply_reason: str = None,
        authentication: UpdateAppRequestAuthentication = None,
        contact_info: str = None,
        description: str = None,
        limiter_info: UpdateAppRequestLimiterInfo = None,
        network: List[UpdateAppRequestNetwork] = None,
        private_network: List[UpdateAppRequestPrivateNetwork] = None,
    ):
        self.apply_reason = apply_reason
        self.authentication = authentication
        self.contact_info = contact_info
        # 应用备注
        self.description = description
        self.limiter_info = limiter_info
        self.network = network
        self.private_network = private_network

    def validate(self):
        if self.authentication:
            self.authentication.validate()
        if self.limiter_info:
            self.limiter_info.validate()
        if self.network:
            for k in self.network:
                if k:
                    k.validate()
        if self.private_network:
            for k in self.private_network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason is not None:
            result['applyReason'] = self.apply_reason
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()
        if self.contact_info is not None:
            result['contactInfo'] = self.contact_info
        if self.description is not None:
            result['description'] = self.description
        if self.limiter_info is not None:
            result['limiterInfo'] = self.limiter_info.to_map()
        result['network'] = []
        if self.network is not None:
            for k in self.network:
                result['network'].append(k.to_map() if k else None)
        result['privateNetwork'] = []
        if self.private_network is not None:
            for k in self.private_network:
                result['privateNetwork'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyReason') is not None:
            self.apply_reason = m.get('applyReason')
        if m.get('authentication') is not None:
            temp_model = UpdateAppRequestAuthentication()
            self.authentication = temp_model.from_map(m['authentication'])
        if m.get('contactInfo') is not None:
            self.contact_info = m.get('contactInfo')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('limiterInfo') is not None:
            temp_model = UpdateAppRequestLimiterInfo()
            self.limiter_info = temp_model.from_map(m['limiterInfo'])
        self.network = []
        if m.get('network') is not None:
            for k in m.get('network'):
                temp_model = UpdateAppRequestNetwork()
                self.network.append(temp_model.from_map(k))
        self.private_network = []
        if m.get('privateNetwork') is not None:
            for k in m.get('privateNetwork'):
                temp_model = UpdateAppRequestPrivateNetwork()
                self.private_network.append(temp_model.from_map(k))
        return self


class UpdateAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateAppResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppResponseBody = None,
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
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


