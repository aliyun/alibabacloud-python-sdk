# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelSpecReviewTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CancelSpecReviewTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelSpecReviewTaskResponseBody = None,
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
            temp_model = CancelSpecReviewTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        indices: str = None,
        snapshot: str = None,
        dry_run: bool = None,
    ):
        # This parameter is required.
        self.indices = indices
        # This parameter is required.
        self.snapshot = snapshot
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.indices is not None:
            result['indices'] = self.indices
        if self.snapshot is not None:
            result['snapshot'] = self.snapshot
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('indices') is not None:
            self.indices = m.get('indices')
        if m.get('snapshot') is not None:
            self.snapshot = m.get('snapshot')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSnapshotResponseBody = None,
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
            temp_model = CreateSnapshotResponseBody()
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


class DeleteDictRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DeleteDictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteDictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDictResponseBody = None,
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
            temp_model = DeleteDictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEndpointResponseBody = None,
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
            temp_model = DeleteEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSnapshotResponseBody = None,
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
            temp_model = DeleteSnapshotResponseBody()
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
        app_type: str = None,
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
        self.app_type = app_type
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
        if self.app_type is not None:
            result['appType'] = self.app_type
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
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
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


class GetSnapshotSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        quartz_regex: str = None,
    ):
        self.enable = enable
        self.quartz_regex = quartz_regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.quartz_regex is not None:
            result['quartzRegex'] = self.quartz_regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('quartzRegex') is not None:
            self.quartz_regex = m.get('quartzRegex')
        return self


class GetSnapshotSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetSnapshotSettingResponseBodyResult = None,
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
            temp_model = GetSnapshotSettingResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSnapshotSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSnapshotSettingResponseBody = None,
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
            temp_model = GetSnapshotSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpecReviewTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        id: str = None,
        app_name: str = None,
        apply_limiter: Dict[str, Any] = None,
        apply_quota: Dict[str, Any] = None,
        apply_reason: str = None,
        effective_limiter: Dict[str, Any] = None,
        effective_quota: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        old_limiter: Dict[str, Any] = None,
        old_quota: Dict[str, Any] = None,
        source: str = None,
        status: str = None,
        type: str = None,
    ):
        # 代表资源一级ID的资源属性字段
        self.id = id
        self.app_name = app_name
        self.apply_limiter = apply_limiter
        self.apply_quota = apply_quota
        self.apply_reason = apply_reason
        self.effective_limiter = effective_limiter
        self.effective_quota = effective_quota
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.old_limiter = old_limiter
        self.old_quota = old_quota
        self.source = source
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.apply_limiter is not None:
            result['applyLimiter'] = self.apply_limiter
        if self.apply_quota is not None:
            result['applyQuota'] = self.apply_quota
        if self.apply_reason is not None:
            result['applyReason'] = self.apply_reason
        if self.effective_limiter is not None:
            result['effectiveLimiter'] = self.effective_limiter
        if self.effective_quota is not None:
            result['effectiveQuota'] = self.effective_quota
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.old_limiter is not None:
            result['oldLimiter'] = self.old_limiter
        if self.old_quota is not None:
            result['oldQuota'] = self.old_quota
        if self.source is not None:
            result['source'] = self.source
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('applyLimiter') is not None:
            self.apply_limiter = m.get('applyLimiter')
        if m.get('applyQuota') is not None:
            self.apply_quota = m.get('applyQuota')
        if m.get('applyReason') is not None:
            self.apply_reason = m.get('applyReason')
        if m.get('effectiveLimiter') is not None:
            self.effective_limiter = m.get('effectiveLimiter')
        if m.get('effectiveQuota') is not None:
            self.effective_quota = m.get('effectiveQuota')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('oldLimiter') is not None:
            self.old_limiter = m.get('oldLimiter')
        if m.get('oldQuota') is not None:
            self.old_quota = m.get('oldQuota')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetSpecReviewTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetSpecReviewTaskResponseBodyResult = None,
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
            temp_model = GetSpecReviewTaskResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSpecReviewTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSpecReviewTaskResponseBody = None,
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
            temp_model = GetSpecReviewTaskResponseBody()
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
        app_type: str = None,
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
        self.app_type = app_type
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
        if self.app_type is not None:
            result['appType'] = self.app_type
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
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
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


class ListDictsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDictsResponseBodyResult(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.download_url = download_url
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDictsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDictsResponseBodyResult] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.result = result
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
                temp_model = ListDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDictsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDictsResponseBody = None,
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
            temp_model = ListDictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEndpointsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_id: str = None,
        type: str = None,
        vpc_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.resource_id = resource_id
        # This parameter is required.
        self.type = type
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListEndpointsResponseBodyResultEndpointZones(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class ListEndpointsResponseBodyResult(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        created: int = None,
        domain: str = None,
        endpoint_id: str = None,
        endpoint_zones: List[ListEndpointsResponseBodyResultEndpointZones] = None,
        name: str = None,
        resource_id: str = None,
        security_group_ids: List[str] = None,
        status: str = None,
        type: str = None,
        updated: int = None,
        vpc_id: str = None,
    ):
        self.connection_status = connection_status
        self.created = created
        self.domain = domain
        self.endpoint_id = endpoint_id
        self.endpoint_zones = endpoint_zones
        self.name = name
        self.resource_id = resource_id
        self.security_group_ids = security_group_ids
        self.status = status
        self.type = type
        self.updated = updated
        self.vpc_id = vpc_id

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
        if self.connection_status is not None:
            result['connectionStatus'] = self.connection_status
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        result['endpointZones'] = []
        if self.endpoint_zones is not None:
            for k in self.endpoint_zones:
                result['endpointZones'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionStatus') is not None:
            self.connection_status = m.get('connectionStatus')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        self.endpoint_zones = []
        if m.get('endpointZones') is not None:
            for k in m.get('endpointZones'):
                temp_model = ListEndpointsResponseBodyResultEndpointZones()
                self.endpoint_zones.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListEndpointsResponseBodyResult] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.result = result
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
                temp_model = ListEndpointsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEndpointsResponseBody = None,
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
            temp_model = ListEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Any] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListIndicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIndicesResponseBody = None,
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
            temp_model = ListIndicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotRepositoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListSnapshotRepositoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSnapshotRepositoriesResponseBody = None,
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
            temp_model = ListSnapshotRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        repository: str = None,
        snapshot: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.repository = repository
        self.snapshot = snapshot

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.repository is not None:
            result['repository'] = self.repository
        if self.snapshot is not None:
            result['snapshot'] = self.snapshot
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('repository') is not None:
            self.repository = m.get('repository')
        if m.get('snapshot') is not None:
            self.snapshot = m.get('snapshot')
        return self


class ListSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.result = result
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSnapshotsResponseBody = None,
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
            temp_model = ListSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpecReviewTasksRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        type: str = None,
    ):
        self.page = page
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSpecReviewTasksResponseBodyResult(TeaModel):
    def __init__(
        self,
        id: str = None,
        app_name: str = None,
        apply_reason: str = None,
        gmt_create: str = None,
        source: str = None,
        status: str = None,
        type: str = None,
    ):
        # 代表资源一级ID的资源属性字段
        self.id = id
        self.app_name = app_name
        self.apply_reason = apply_reason
        self.gmt_create = gmt_create
        self.source = source
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.apply_reason is not None:
            result['applyReason'] = self.apply_reason
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.source is not None:
            result['source'] = self.source
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('applyReason') is not None:
            self.apply_reason = m.get('applyReason')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSpecReviewTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListSpecReviewTasksResponseBodyResult] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result
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
                temp_model = ListSpecReviewTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSpecReviewTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSpecReviewTasksResponseBody = None,
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
            temp_model = ListSpecReviewTasksResponseBody()
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


class UpdateDictRequestFilesOssObject(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        key: str = None,
    ):
        self.bucket_name = bucket_name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class UpdateDictRequestFiles(TeaModel):
    def __init__(
        self,
        name: str = None,
        oss_object: UpdateDictRequestFilesOssObject = None,
    ):
        self.name = name
        self.oss_object = oss_object

    def validate(self):
        if self.oss_object:
            self.oss_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.oss_object is not None:
            result['ossObject'] = self.oss_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ossObject') is not None:
            temp_model = UpdateDictRequestFilesOssObject()
            self.oss_object = temp_model.from_map(m['ossObject'])
        return self


class UpdateDictRequest(TeaModel):
    def __init__(
        self,
        allow_cover: bool = None,
        files: List[UpdateDictRequestFiles] = None,
        source_type: str = None,
        type: str = None,
        dry_run: bool = None,
    ):
        self.allow_cover = allow_cover
        # This parameter is required.
        self.files = files
        self.source_type = source_type
        self.type = type
        self.dry_run = dry_run

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_cover is not None:
            result['allowCover'] = self.allow_cover
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowCover') is not None:
            self.allow_cover = m.get('allowCover')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = UpdateDictRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateDictResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateDictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDictResponseBody = None,
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
            temp_model = UpdateDictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointRequestEndpointZones(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class UpdateEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_zones: List[UpdateEndpointRequestEndpointZones] = None,
        name: str = None,
    ):
        # This parameter is required.
        self.endpoint_zones = endpoint_zones
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_zones = []
        if m.get('endpointZones') is not None:
            for k in m.get('endpointZones'):
                temp_model = UpdateEndpointRequestEndpointZones()
                self.endpoint_zones.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateEndpointResponseBodyResult(TeaModel):
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


class UpdateEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateEndpointResponseBodyResult = None,
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
            temp_model = UpdateEndpointResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEndpointResponseBody = None,
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
            temp_model = UpdateEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotSettingRequest(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        quartz_regex: str = None,
    ):
        # This parameter is required.
        self.enable = enable
        # This parameter is required.
        self.quartz_regex = quartz_regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.quartz_regex is not None:
            result['quartzRegex'] = self.quartz_regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('quartzRegex') is not None:
            self.quartz_regex = m.get('quartzRegex')
        return self


class UpdateSnapshotSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateSnapshotSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSnapshotSettingResponseBody = None,
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
            temp_model = UpdateSnapshotSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


