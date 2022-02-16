# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddCidrToConnectionPoolRequest(TeaModel):
    def __init__(
        self,
        cidrs: List[str] = None,
        client_token: str = None,
        connection_pool_id: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.cidrs = cidrs
        self.client_token = client_token
        self.connection_pool_id = connection_pool_id
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

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
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddCidrToConnectionPoolResponseBody(TeaModel):
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


class AddCidrToConnectionPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddCidrToConnectionPoolResponseBody = None,
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
            temp_model = AddCidrToConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIoTCloudConnectorToGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        io_tcloud_connector_id: List[str] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddIoTCloudConnectorToGroupResponseBody(TeaModel):
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


class AddIoTCloudConnectorToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddIoTCloudConnectorToGroupResponseBody = None,
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
            temp_model = AddIoTCloudConnectorToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateIpWithConnectionPoolRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        connection_pool_id: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        ips: List[str] = None,
        ips_file_path: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.connection_pool_id = connection_pool_id
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.ips = ips
        self.ips_file_path = ips_file_path
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.ips_file_path is not None:
            result['IpsFilePath'] = self.ips_file_path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('IpsFilePath') is not None:
            self.ips_file_path = m.get('IpsFilePath')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateIpWithConnectionPoolResponseBody(TeaModel):
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


class AssociateIpWithConnectionPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateIpWithConnectionPoolResponseBody = None,
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
            temp_model = AssociateIpWithConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateVSwitchWithIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        v_switch_list: List[str] = None,
        vpc_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.v_switch_list = v_switch_list
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_list is not None:
            result['VSwitchList'] = self.v_switch_list
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchList') is not None:
            self.v_switch_list = m.get('VSwitchList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class AssociateVSwitchWithIoTCloudConnectorResponseBody(TeaModel):
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


class AssociateVSwitchWithIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateVSwitchWithIoTCloudConnectorResponseBody = None,
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
            temp_model = AssociateVSwitchWithIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        destination: str = None,
        destination_type: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        policy: str = None,
        region_id: str = None,
        source_cidrs: List[str] = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_name = authorization_rule_name
        self.client_token = client_token
        self.destination = destination
        self.destination_type = destination_type
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.policy = policy
        self.region_id = region_id
        self.source_cidrs = source_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class CreateAuthorizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        request_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAuthorizationRuleResponseBody = None,
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
            temp_model = CreateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionPoolRequest(TeaModel):
    def __init__(
        self,
        cidrs: List[str] = None,
        client_token: str = None,
        connection_pool_description: str = None,
        connection_pool_name: str = None,
        count: int = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.cidrs = cidrs
        self.client_token = client_token
        self.connection_pool_description = connection_pool_description
        self.connection_pool_name = connection_pool_name
        self.count = count
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

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
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.count is not None:
            result['Count'] = self.count
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateConnectionPoolResponseBody(TeaModel):
    def __init__(
        self,
        connection_pool_id: str = None,
        request_id: str = None,
    ):
        self.connection_pool_id = connection_pool_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConnectionPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConnectionPoolResponseBody = None,
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
            temp_model = CreateConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDNSServiceRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        destination: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_type: str = None,
        source: str = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_name = authorization_rule_name
        self.client_token = client_token
        self.destination = destination
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateDNSServiceRuleResponseBody(TeaModel):
    def __init__(
        self,
        dnsservice_rule_id: str = None,
        request_id: str = None,
    ):
        self.dnsservice_rule_id = dnsservice_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDNSServiceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDNSServiceRuleResponseBody = None,
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
            temp_model = CreateDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        destination: str = None,
        destination_type: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        policy: str = None,
        region_id: str = None,
        source_cidrs: List[str] = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_name = authorization_rule_name
        self.client_token = client_token
        self.destination = destination
        self.destination_type = destination_type
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.policy = policy
        self.region_id = region_id
        self.source_cidrs = source_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class CreateGroupAuthorizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        io_tcloud_connector_group_id: str = None,
        request_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupAuthorizationRuleResponseBody = None,
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
            temp_model = CreateGroupAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupDNSServiceRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dnsservice_rule_description: str = None,
        dnsservice_rule_name: str = None,
        destination: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        region_id: str = None,
        service_type: str = None,
        source: str = None,
    ):
        self.client_token = client_token
        self.dnsservice_rule_description = dnsservice_rule_description
        self.dnsservice_rule_name = dnsservice_rule_name
        self.destination = destination
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.region_id = region_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateGroupDNSServiceRuleResponseBody(TeaModel):
    def __init__(
        self,
        dnsservice_rule_id: str = None,
        io_tcloud_connector_group_id: str = None,
        request_id: str = None,
    ):
        self.dnsservice_rule_id = dnsservice_rule_id
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupDNSServiceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupDNSServiceRuleResponseBody = None,
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
            temp_model = CreateGroupDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        apn: str = None,
        client_token: str = None,
        dry_run: bool = None,
        isp: str = None,
        io_tcloud_connector_description: str = None,
        io_tcloud_connector_name: str = None,
        region_id: str = None,
        resource_uid: int = None,
        wildcard_domain_enabled: bool = None,
    ):
        self.apn = apn
        self.client_token = client_token
        self.dry_run = dry_run
        self.isp = isp
        self.io_tcloud_connector_description = io_tcloud_connector_description
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.region_id = region_id
        self.resource_uid = resource_uid
        self.wildcard_domain_enabled = wildcard_domain_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class CreateIoTCloudConnectorResponseBody(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        request_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIoTCloudConnectorResponseBody = None,
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
            temp_model = CreateIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIoTCloudConnectorGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.name = name
        self.region_id = region_id

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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateIoTCloudConnectorGroupResponseBody(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_group_id: str = None,
        request_id: str = None,
    ):
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIoTCloudConnectorGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIoTCloudConnectorGroupResponseBody = None,
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
            temp_model = CreateIoTCloudConnectorGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_description: str = None,
        service_name: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_description = service_description
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_id: str = None,
    ):
        self.request_id = request_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceEntryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_entry_description: str = None,
        service_entry_name: str = None,
        service_id: str = None,
        target: str = None,
        target_type: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_entry_description = service_entry_description
        self.service_entry_name = service_entry_name
        self.service_id = service_id
        self.target = target
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateServiceEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_entry_id: str = None,
    ):
        self.request_id = request_id
        self.service_entry_id = service_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        return self


class CreateServiceEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceEntryResponseBody = None,
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
            temp_model = CreateServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAuthorizationRuleResponseBody(TeaModel):
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


class DeleteAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAuthorizationRuleResponseBody = None,
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
            temp_model = DeleteAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionPoolRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        connection_pool_id: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.connection_pool_id = connection_pool_id
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteConnectionPoolResponseBody(TeaModel):
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


class DeleteConnectionPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConnectionPoolResponseBody = None,
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
            temp_model = DeleteConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDNSServiceRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dnsservice_rule_id: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dnsservice_rule_id = dnsservice_rule_id
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDNSServiceRuleResponseBody(TeaModel):
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


class DeleteDNSServiceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDNSServiceRuleResponseBody = None,
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
            temp_model = DeleteDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        region_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteGroupAuthorizationRuleResponseBody(TeaModel):
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


class DeleteGroupAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupAuthorizationRuleResponseBody = None,
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
            temp_model = DeleteGroupAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupDNSServiceRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dnsservice_rule_id: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dnsservice_rule_id = dnsservice_rule_id
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteGroupDNSServiceRuleResponseBody(TeaModel):
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


class DeleteGroupDNSServiceRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupDNSServiceRuleResponseBody = None,
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
            temp_model = DeleteGroupDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIoTCloudConnectorResponseBody(TeaModel):
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


class DeleteIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIoTCloudConnectorResponseBody = None,
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
            temp_model = DeleteIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIoTCloudConnectorGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIoTCloudConnectorGroupResponseBody(TeaModel):
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


class DeleteIoTCloudConnectorGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIoTCloudConnectorGroupResponseBody = None,
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
            temp_model = DeleteIoTCloudConnectorGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceResponseBody(TeaModel):
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceEntryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_entry_id: str = None,
        service_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_entry_id = service_entry_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceEntryResponseBody(TeaModel):
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


class DeleteServiceEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceEntryResponseBody = None,
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
            temp_model = DeleteServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableIoTCloudConnectorAccessLogResponseBody(TeaModel):
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


class DisableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableIoTCloudConnectorAccessLogResponseBody = None,
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
            temp_model = DisableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateIpFromConnectionPoolRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        connection_pool_id: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        ips: List[str] = None,
        ips_file_path: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.connection_pool_id = connection_pool_id
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.ips = ips
        self.ips_file_path = ips_file_path
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.ips_file_path is not None:
            result['IpsFilePath'] = self.ips_file_path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('IpsFilePath') is not None:
            self.ips_file_path = m.get('IpsFilePath')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateIpFromConnectionPoolResponseBody(TeaModel):
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


class DissociateIpFromConnectionPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociateIpFromConnectionPoolResponseBody = None,
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
            temp_model = DissociateIpFromConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateVSwitchFromIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateVSwitchFromIoTCloudConnectorResponseBody(TeaModel):
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


class DissociateVSwitchFromIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociateVSwitchFromIoTCloudConnectorResponseBody = None,
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
            temp_model = DissociateVSwitchFromIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(
        self,
        access_log_sls_log_store: str = None,
        access_log_sls_project: str = None,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.access_log_sls_log_store = access_log_sls_log_store
        self.access_log_sls_project = access_log_sls_project
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableIoTCloudConnectorAccessLogResponseBody(TeaModel):
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


class EnableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableIoTCloudConnectorAccessLogResponseBody = None,
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
            temp_model = EnableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionPoolIpOperationResultRequest(TeaModel):
    def __init__(
        self,
        connection_pool_id: str = None,
        io_tcloud_connector_id: str = None,
        query_request_id: str = None,
        region_id: str = None,
    ):
        self.connection_pool_id = connection_pool_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.query_request_id = query_request_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.query_request_id is not None:
            result['QueryRequestId'] = self.query_request_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('QueryRequestId') is not None:
            self.query_request_id = m.get('QueryRequestId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetConnectionPoolIpOperationResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_file_paths: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # OssPath
        self.result_file_paths = result_file_paths

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_file_paths is not None:
            result['ResultFilePaths'] = self.result_file_paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultFilePaths') is not None:
            self.result_file_paths = m.get('ResultFilePaths')
        return self


class GetConnectionPoolIpOperationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConnectionPoolIpOperationResultResponseBody = None,
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
            temp_model = GetConnectionPoolIpOperationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnoseResultForSingleCardRequest(TeaModel):
    def __init__(
        self,
        diagnose_task_id: str = None,
        region_id: str = None,
    ):
        self.diagnose_task_id = diagnose_task_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnose_task_id is not None:
            result['DiagnoseTaskId'] = self.diagnose_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseTaskId') is not None:
            self.diagnose_task_id = m.get('DiagnoseTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem(TeaModel):
    def __init__(
        self,
        part: str = None,
        status: str = None,
    ):
        self.part = part
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.part is not None:
            result['Part'] = self.part
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Part') is not None:
            self.part = m.get('Part')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDiagnoseResultForSingleCardResponseBodyErrorResult(TeaModel):
    def __init__(
        self,
        error_desc: str = None,
        error_level: str = None,
        error_part: str = None,
        error_suggestion: str = None,
    ):
        self.error_desc = error_desc
        self.error_level = error_level
        self.error_part = error_part
        self.error_suggestion = error_suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_desc is not None:
            result['ErrorDesc'] = self.error_desc
        if self.error_level is not None:
            result['ErrorLevel'] = self.error_level
        if self.error_part is not None:
            result['ErrorPart'] = self.error_part
        if self.error_suggestion is not None:
            result['ErrorSuggestion'] = self.error_suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDesc') is not None:
            self.error_desc = m.get('ErrorDesc')
        if m.get('ErrorLevel') is not None:
            self.error_level = m.get('ErrorLevel')
        if m.get('ErrorPart') is not None:
            self.error_part = m.get('ErrorPart')
        if m.get('ErrorSuggestion') is not None:
            self.error_suggestion = m.get('ErrorSuggestion')
        return self


class GetDiagnoseResultForSingleCardResponseBody(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        card_ip: str = None,
        destination: str = None,
        diagnose_item: List[GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem] = None,
        end_time: int = None,
        error_result: List[GetDiagnoseResultForSingleCardResponseBodyErrorResult] = None,
        icc_id: str = None,
        io_tcloud_connector_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.begin_time = begin_time
        self.card_ip = card_ip
        self.destination = destination
        self.diagnose_item = diagnose_item
        self.end_time = end_time
        self.error_result = error_result
        self.icc_id = icc_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.diagnose_item:
            for k in self.diagnose_item:
                if k:
                    k.validate()
        if self.error_result:
            for k in self.error_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.card_ip is not None:
            result['CardIp'] = self.card_ip
        if self.destination is not None:
            result['Destination'] = self.destination
        result['DiagnoseItem'] = []
        if self.diagnose_item is not None:
            for k in self.diagnose_item:
                result['DiagnoseItem'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ErrorResult'] = []
        if self.error_result is not None:
            for k in self.error_result:
                result['ErrorResult'].append(k.to_map() if k else None)
        if self.icc_id is not None:
            result['IccId'] = self.icc_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CardIp') is not None:
            self.card_ip = m.get('CardIp')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        self.diagnose_item = []
        if m.get('DiagnoseItem') is not None:
            for k in m.get('DiagnoseItem'):
                temp_model = GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem()
                self.diagnose_item.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.error_result = []
        if m.get('ErrorResult') is not None:
            for k in m.get('ErrorResult'):
                temp_model = GetDiagnoseResultForSingleCardResponseBodyErrorResult()
                self.error_result.append(temp_model.from_map(k))
        if m.get('IccId') is not None:
            self.icc_id = m.get('IccId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDiagnoseResultForSingleCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDiagnoseResultForSingleCardResponseBody = None,
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
            temp_model = GetDiagnoseResultForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(
        self,
        access_log_sls_log_store: str = None,
        access_log_sls_project: str = None,
        access_log_status: str = None,
        request_id: str = None,
    ):
        self.access_log_sls_log_store = access_log_sls_log_store
        self.access_log_sls_project = access_log_sls_project
        self.access_log_status = access_log_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.access_log_status is not None:
            result['AccessLogStatus'] = self.access_log_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('AccessLogStatus') is not None:
            self.access_log_status = m.get('AccessLogStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIoTCloudConnectorAccessLogResponseBody = None,
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
            temp_model = GetIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStsInfoAndOssPathRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        connection_pool_id: str = None,
        dry_run: bool = None,
        file_name: str = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.connection_pool_id = connection_pool_id
        self.dry_run = dry_run
        self.file_name = file_name
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStsInfoAndOssPathResponseBody(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        expiration: str = None,
        oss_path: str = None,
        request_id: str = None,
        security_token: str = None,
    ):
        # Sts info of accessKeyId
        self.access_key_id = access_key_id
        # Sts info of accessKeySecret
        self.access_key_secret = access_key_secret
        # Sts info expiration time
        self.expiration = expiration
        # OssPath
        self.oss_path = oss_path
        # Id of the request
        self.request_id = request_id
        # Sts info of securityToken
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetStsInfoAndOssPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStsInfoAndOssPathResponseBody = None,
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
            temp_model = GetStsInfoAndOssPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantVirtualBorderRouterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        virtual_border_router_id: str = None,
    ):
        self.region_id = region_id
        self.virtual_border_router_id = virtual_border_router_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_border_router_id is not None:
            result['VirtualBorderRouterId'] = self.virtual_border_router_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualBorderRouterId') is not None:
            self.virtual_border_router_id = m.get('VirtualBorderRouterId')
        return self


class GrantVirtualBorderRouterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class GrantVirtualBorderRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantVirtualBorderRouterResponseBody = None,
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
            temp_model = GrantVirtualBorderRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAPNsRequest(TeaModel):
    def __init__(
        self,
        apn: str = None,
        isp: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.apn = apn
        self.isp = isp
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAPNsResponseBodyAPNs(TeaModel):
    def __init__(
        self,
        apn: str = None,
        description: str = None,
        feature_list: List[str] = None,
        isp: str = None,
        name: str = None,
        zone_list: List[str] = None,
    ):
        self.apn = apn
        self.description = description
        self.feature_list = feature_list
        self.isp = isp
        self.name = name
        self.zone_list = zone_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ZoneList') is not None:
            self.zone_list = m.get('ZoneList')
        return self


class ListAPNsResponseBody(TeaModel):
    def __init__(
        self,
        apns: List[ListAPNsResponseBodyAPNs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.apns = apns
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.apns:
            for k in self.apns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['APNs'] = []
        if self.apns is not None:
            for k in self.apns:
                result['APNs'].append(k.to_map() if k else None)
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
        self.apns = []
        if m.get('APNs') is not None:
            for k in m.get('APNs'):
                temp_model = ListAPNsResponseBodyAPNs()
                self.apns.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAPNsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAPNsResponseBody = None,
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
            temp_model = ListAPNsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationRulesRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_ids: List[str] = None,
        authorization_rule_name: List[str] = None,
        authorization_rule_status: List[str] = None,
        destination: List[str] = None,
        destination_type: List[str] = None,
        io_tcloud_connector_id: str = None,
        max_results: int = None,
        next_token: str = None,
        policy: List[str] = None,
        region_id: str = None,
    ):
        self.authorization_rule_ids = authorization_rule_ids
        self.authorization_rule_name = authorization_rule_name
        self.authorization_rule_status = authorization_rule_status
        self.destination = destination
        self.destination_type = destination_type
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.max_results = max_results
        self.next_token = next_token
        self.policy = policy
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_ids is not None:
            result['AuthorizationRuleIds'] = self.authorization_rule_ids
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleIds') is not None:
            self.authorization_rule_ids = m.get('AuthorizationRuleIds')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAuthorizationRulesResponseBodyAuthorizationRules(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_id: str = None,
        authorization_rule_name: str = None,
        authorization_rule_status: str = None,
        destination: str = None,
        destination_type: str = None,
        io_tcloud_connector_id: str = None,
        policy: str = None,
        source_cidrs: List[str] = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_id = authorization_rule_id
        self.authorization_rule_name = authorization_rule_name
        self.authorization_rule_status = authorization_rule_status
        self.destination = destination
        self.destination_type = destination_type
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.policy = policy
        self.source_cidrs = source_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class ListAuthorizationRulesResponseBody(TeaModel):
    def __init__(
        self,
        authorization_rules: List[ListAuthorizationRulesResponseBodyAuthorizationRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorization_rules = authorization_rules
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorization_rules:
            for k in self.authorization_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizationRules'] = []
        if self.authorization_rules is not None:
            for k in self.authorization_rules:
                result['AuthorizationRules'].append(k.to_map() if k else None)
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
        self.authorization_rules = []
        if m.get('AuthorizationRules') is not None:
            for k in m.get('AuthorizationRules'):
                temp_model = ListAuthorizationRulesResponseBodyAuthorizationRules()
                self.authorization_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthorizationRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAuthorizationRulesResponseBody = None,
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
            temp_model = ListAuthorizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolAllIpsRequest(TeaModel):
    def __init__(
        self,
        connection_pool_id: str = None,
        io_tcloud_connector_id: str = None,
        ip: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.connection_pool_id = connection_pool_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.ip = ip
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListConnectionPoolAllIpsResponseBodyConnectionPoolIps(TeaModel):
    def __init__(
        self,
        connection_pool_id: str = None,
        ip: str = None,
        ip_num: int = None,
        status: str = None,
        type: str = None,
    ):
        self.connection_pool_id = connection_pool_id
        self.ip = ip
        self.ip_num = ip_num
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_num is not None:
            result['IpNum'] = self.ip_num
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpNum') is not None:
            self.ip_num = m.get('IpNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListConnectionPoolAllIpsResponseBody(TeaModel):
    def __init__(
        self,
        connection_pool_ips: List[ListConnectionPoolAllIpsResponseBodyConnectionPoolIps] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_ips_count: int = None,
    ):
        self.connection_pool_ips = connection_pool_ips
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_ips_count = total_ips_count

    def validate(self):
        if self.connection_pool_ips:
            for k in self.connection_pool_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionPoolIps'] = []
        if self.connection_pool_ips is not None:
            for k in self.connection_pool_ips:
                result['ConnectionPoolIps'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_ips_count is not None:
            result['TotalIpsCount'] = self.total_ips_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_pool_ips = []
        if m.get('ConnectionPoolIps') is not None:
            for k in m.get('ConnectionPoolIps'):
                temp_model = ListConnectionPoolAllIpsResponseBodyConnectionPoolIps()
                self.connection_pool_ips.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalIpsCount') is not None:
            self.total_ips_count = m.get('TotalIpsCount')
        return self


class ListConnectionPoolAllIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectionPoolAllIpsResponseBody = None,
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
            temp_model = ListConnectionPoolAllIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolIpsRequest(TeaModel):
    def __init__(
        self,
        connection_pool_id: str = None,
        io_tcloud_connector_id: str = None,
        ip: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.connection_pool_id = connection_pool_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.ip = ip
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListConnectionPoolIpsResponseBodyConnectionPoolIps(TeaModel):
    def __init__(
        self,
        connection_pool_id: str = None,
        ip: str = None,
        status: str = None,
    ):
        self.connection_pool_id = connection_pool_id
        self.ip = ip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListConnectionPoolIpsResponseBody(TeaModel):
    def __init__(
        self,
        connection_pool_ips: List[ListConnectionPoolIpsResponseBodyConnectionPoolIps] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.connection_pool_ips = connection_pool_ips
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.connection_pool_ips:
            for k in self.connection_pool_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionPoolIps'] = []
        if self.connection_pool_ips is not None:
            for k in self.connection_pool_ips:
                result['ConnectionPoolIps'].append(k.to_map() if k else None)
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
        self.connection_pool_ips = []
        if m.get('ConnectionPoolIps') is not None:
            for k in m.get('ConnectionPoolIps'):
                temp_model = ListConnectionPoolIpsResponseBodyConnectionPoolIps()
                self.connection_pool_ips.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConnectionPoolIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectionPoolIpsResponseBody = None,
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
            temp_model = ListConnectionPoolIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolsRequest(TeaModel):
    def __init__(
        self,
        connection_pool_ids: List[str] = None,
        connection_pool_name: List[str] = None,
        connection_pool_status: List[str] = None,
        io_tcloud_connector_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.connection_pool_ids = connection_pool_ids
        self.connection_pool_name = connection_pool_name
        self.connection_pool_status = connection_pool_status
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_ids is not None:
            result['ConnectionPoolIds'] = self.connection_pool_ids
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolIds') is not None:
            self.connection_pool_ids = m.get('ConnectionPoolIds')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListConnectionPoolsResponseBodyConnectionPools(TeaModel):
    def __init__(
        self,
        cidrs: List[str] = None,
        connection_pool_description: str = None,
        connection_pool_id: str = None,
        connection_pool_name: str = None,
        connection_pool_status: str = None,
        operate_result_request_id: str = None,
    ):
        self.cidrs = cidrs
        self.connection_pool_description = connection_pool_description
        self.connection_pool_id = connection_pool_id
        self.connection_pool_name = connection_pool_name
        self.connection_pool_status = connection_pool_status
        self.operate_result_request_id = operate_result_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.operate_result_request_id is not None:
            result['OperateResultRequestID'] = self.operate_result_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('OperateResultRequestID') is not None:
            self.operate_result_request_id = m.get('OperateResultRequestID')
        return self


class ListConnectionPoolsResponseBody(TeaModel):
    def __init__(
        self,
        connection_pools: List[ListConnectionPoolsResponseBodyConnectionPools] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.connection_pools = connection_pools
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.connection_pools:
            for k in self.connection_pools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionPools'] = []
        if self.connection_pools is not None:
            for k in self.connection_pools:
                result['ConnectionPools'].append(k.to_map() if k else None)
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
        self.connection_pools = []
        if m.get('ConnectionPools') is not None:
            for k in m.get('ConnectionPools'):
                temp_model = ListConnectionPoolsResponseBodyConnectionPools()
                self.connection_pools.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConnectionPoolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectionPoolsResponseBody = None,
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
            temp_model = ListConnectionPoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDNSServiceRulesRequest(TeaModel):
    def __init__(
        self,
        dnsservice_rule_ids: List[str] = None,
        dnsservice_rule_name: List[str] = None,
        dnsservice_rule_status: List[str] = None,
        destination: List[str] = None,
        io_tcloud_connector_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_type: str = None,
        source: List[str] = None,
    ):
        self.dnsservice_rule_ids = dnsservice_rule_ids
        self.dnsservice_rule_name = dnsservice_rule_name
        self.dnsservice_rule_status = dnsservice_rule_status
        self.destination = destination
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_ids is not None:
            result['DNSServiceRuleIds'] = self.dnsservice_rule_ids
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSServiceRuleIds') is not None:
            self.dnsservice_rule_ids = m.get('DNSServiceRuleIds')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDNSServiceRulesResponseBodyDNSServiceRules(TeaModel):
    def __init__(
        self,
        dnsservice_rule_description: str = None,
        dnsservice_rule_id: str = None,
        dnsservice_rule_name: str = None,
        dnsservice_rule_status: str = None,
        destination: str = None,
        io_tcloud_connector_id: str = None,
        service_type: str = None,
        source: str = None,
    ):
        self.dnsservice_rule_description = dnsservice_rule_description
        self.dnsservice_rule_id = dnsservice_rule_id
        self.dnsservice_rule_name = dnsservice_rule_name
        self.dnsservice_rule_status = dnsservice_rule_status
        self.destination = destination
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDNSServiceRulesResponseBody(TeaModel):
    def __init__(
        self,
        dnsservice_rules: List[ListDNSServiceRulesResponseBodyDNSServiceRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dnsservice_rules = dnsservice_rules
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dnsservice_rules:
            for k in self.dnsservice_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DNSServiceRules'] = []
        if self.dnsservice_rules is not None:
            for k in self.dnsservice_rules:
                result['DNSServiceRules'].append(k.to_map() if k else None)
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
        self.dnsservice_rules = []
        if m.get('DNSServiceRules') is not None:
            for k in m.get('DNSServiceRules'):
                temp_model = ListDNSServiceRulesResponseBodyDNSServiceRules()
                self.dnsservice_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDNSServiceRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDNSServiceRulesResponseBody = None,
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
            temp_model = ListDNSServiceRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseInfoForSingleCardRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        source: str = None,
        source_type: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.source = source
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        card_ip: str = None,
        destination: str = None,
        destination_type: str = None,
        diagnose_time: int = None,
        end_time: int = None,
        icc_id: str = None,
        io_tcloud_connector_id: str = None,
        source: str = None,
        source_type: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.begin_time = begin_time
        self.card_ip = card_ip
        self.destination = destination
        self.destination_type = destination_type
        self.diagnose_time = diagnose_time
        self.end_time = end_time
        self.icc_id = icc_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.source = source
        self.source_type = source_type
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.card_ip is not None:
            result['CardIp'] = self.card_ip
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.diagnose_time is not None:
            result['DiagnoseTime'] = self.diagnose_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.icc_id is not None:
            result['IccId'] = self.icc_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CardIp') is not None:
            self.card_ip = m.get('CardIp')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DiagnoseTime') is not None:
            self.diagnose_time = m.get('DiagnoseTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IccId') is not None:
            self.icc_id = m.get('IccId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListDiagnoseInfoForSingleCardResponseBody(TeaModel):
    def __init__(
        self,
        diagnose_info: List[ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.diagnose_info = diagnose_info
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.diagnose_info:
            for k in self.diagnose_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiagnoseInfo'] = []
        if self.diagnose_info is not None:
            for k in self.diagnose_info:
                result['DiagnoseInfo'].append(k.to_map() if k else None)
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
        self.diagnose_info = []
        if m.get('DiagnoseInfo') is not None:
            for k in m.get('DiagnoseInfo'):
                temp_model = ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo()
                self.diagnose_info.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDiagnoseInfoForSingleCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDiagnoseInfoForSingleCardResponseBody = None,
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
            temp_model = ListDiagnoseInfoForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupAuthorizationRulesRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_ids: List[str] = None,
        authorization_rule_name: List[str] = None,
        authorization_rule_status: List[str] = None,
        destination: List[str] = None,
        destination_type: List[str] = None,
        io_tcloud_connector_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        policy: List[str] = None,
        region_id: str = None,
    ):
        self.authorization_rule_ids = authorization_rule_ids
        self.authorization_rule_name = authorization_rule_name
        self.authorization_rule_status = authorization_rule_status
        self.destination = destination
        self.destination_type = destination_type
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.max_results = max_results
        self.next_token = next_token
        self.policy = policy
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_ids is not None:
            result['AuthorizationRuleIds'] = self.authorization_rule_ids
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleIds') is not None:
            self.authorization_rule_ids = m.get('AuthorizationRuleIds')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListGroupAuthorizationRulesResponseBodyGroupAuthorizationRules(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_id: str = None,
        authorization_rule_name: str = None,
        authorization_rule_status: str = None,
        destination: str = None,
        destination_type: str = None,
        io_tcloud_connector_group_id: str = None,
        policy: str = None,
        source_cidrs: List[str] = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_id = authorization_rule_id
        self.authorization_rule_name = authorization_rule_name
        self.authorization_rule_status = authorization_rule_status
        self.destination = destination
        self.destination_type = destination_type
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.policy = policy
        self.source_cidrs = source_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class ListGroupAuthorizationRulesResponseBody(TeaModel):
    def __init__(
        self,
        group_authorization_rules: List[ListGroupAuthorizationRulesResponseBodyGroupAuthorizationRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.group_authorization_rules = group_authorization_rules
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.group_authorization_rules:
            for k in self.group_authorization_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupAuthorizationRules'] = []
        if self.group_authorization_rules is not None:
            for k in self.group_authorization_rules:
                result['GroupAuthorizationRules'].append(k.to_map() if k else None)
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
        self.group_authorization_rules = []
        if m.get('GroupAuthorizationRules') is not None:
            for k in m.get('GroupAuthorizationRules'):
                temp_model = ListGroupAuthorizationRulesResponseBodyGroupAuthorizationRules()
                self.group_authorization_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupAuthorizationRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupAuthorizationRulesResponseBody = None,
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
            temp_model = ListGroupAuthorizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupDNSServiceRulesRequest(TeaModel):
    def __init__(
        self,
        dnsservice_rule_ids: List[str] = None,
        dnsservice_rule_name: List[str] = None,
        dnsservice_rule_status: List[str] = None,
        destination: List[str] = None,
        io_tcloud_connector_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_type: str = None,
        source: List[str] = None,
    ):
        self.dnsservice_rule_ids = dnsservice_rule_ids
        self.dnsservice_rule_name = dnsservice_rule_name
        self.dnsservice_rule_status = dnsservice_rule_status
        self.destination = destination
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_ids is not None:
            result['DNSServiceRuleIds'] = self.dnsservice_rule_ids
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSServiceRuleIds') is not None:
            self.dnsservice_rule_ids = m.get('DNSServiceRuleIds')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListGroupDNSServiceRulesResponseBodyDNSServiceRules(TeaModel):
    def __init__(
        self,
        dnsservice_rule_description: str = None,
        dnsservice_rule_id: str = None,
        dnsservice_rule_name: str = None,
        dnsservice_rule_status: str = None,
        destination: str = None,
        io_tcloud_connector_group_id: str = None,
        service_type: str = None,
        source: str = None,
    ):
        self.dnsservice_rule_description = dnsservice_rule_description
        self.dnsservice_rule_id = dnsservice_rule_id
        self.dnsservice_rule_name = dnsservice_rule_name
        self.dnsservice_rule_status = dnsservice_rule_status
        self.destination = destination
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListGroupDNSServiceRulesResponseBody(TeaModel):
    def __init__(
        self,
        dnsservice_rules: List[ListGroupDNSServiceRulesResponseBodyDNSServiceRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dnsservice_rules = dnsservice_rules
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dnsservice_rules:
            for k in self.dnsservice_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DNSServiceRules'] = []
        if self.dnsservice_rules is not None:
            for k in self.dnsservice_rules:
                result['DNSServiceRules'].append(k.to_map() if k else None)
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
        self.dnsservice_rules = []
        if m.get('DNSServiceRules') is not None:
            for k in m.get('DNSServiceRules'):
                temp_model = ListGroupDNSServiceRulesResponseBodyDNSServiceRules()
                self.dnsservice_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupDNSServiceRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupDNSServiceRulesResponseBody = None,
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
            temp_model = ListGroupDNSServiceRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorAvailableZonesRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIoTCloudConnectorAvailableZonesResponseBody(TeaModel):
    def __init__(
        self,
        available_zone_list: List[str] = None,
        io_tcloud_connector_id: str = None,
        request_id: str = None,
    ):
        self.available_zone_list = available_zone_list
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zone_list is not None:
            result['AvailableZoneList'] = self.available_zone_list
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableZoneList') is not None:
            self.available_zone_list = m.get('AvailableZoneList')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListIoTCloudConnectorAvailableZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIoTCloudConnectorAvailableZonesResponseBody = None,
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
            temp_model = ListIoTCloudConnectorAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorGroupsRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_group_ids: List[str] = None,
        io_tcloud_connector_group_name: List[str] = None,
        io_tcloud_connector_group_status: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_group_ids = io_tcloud_connector_group_ids
        self.io_tcloud_connector_group_name = io_tcloud_connector_group_name
        self.io_tcloud_connector_group_status = io_tcloud_connector_group_status
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_group_ids is not None:
            result['IoTCloudConnectorGroupIds'] = self.io_tcloud_connector_group_ids
        if self.io_tcloud_connector_group_name is not None:
            result['IoTCloudConnectorGroupName'] = self.io_tcloud_connector_group_name
        if self.io_tcloud_connector_group_status is not None:
            result['IoTCloudConnectorGroupStatus'] = self.io_tcloud_connector_group_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorGroupIds') is not None:
            self.io_tcloud_connector_group_ids = m.get('IoTCloudConnectorGroupIds')
        if m.get('IoTCloudConnectorGroupName') is not None:
            self.io_tcloud_connector_group_name = m.get('IoTCloudConnectorGroupName')
        if m.get('IoTCloudConnectorGroupStatus') is not None:
            self.io_tcloud_connector_group_status = m.get('IoTCloudConnectorGroupStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroupsIoTCloudConnectors(TeaModel):
    def __init__(
        self,
        apn: str = None,
        create_time: int = None,
        isp: str = None,
        io_tcloud_connector_description: str = None,
        io_tcloud_connector_id: str = None,
        io_tcloud_connector_name: str = None,
        io_tcloud_connector_status: str = None,
    ):
        self.apn = apn
        self.create_time = create_time
        self.isp = isp
        self.io_tcloud_connector_description = io_tcloud_connector_description
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.io_tcloud_connector_status = io_tcloud_connector_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        return self


class ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroups(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        io_tcloud_connector_group_id: str = None,
        io_tcloud_connector_group_status: str = None,
        io_tcloud_connectors: List[ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroupsIoTCloudConnectors] = None,
        name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.io_tcloud_connector_group_status = io_tcloud_connector_group_status
        self.io_tcloud_connectors = io_tcloud_connectors
        self.name = name

    def validate(self):
        if self.io_tcloud_connectors:
            for k in self.io_tcloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_group_status is not None:
            result['IoTCloudConnectorGroupStatus'] = self.io_tcloud_connector_group_status
        result['IoTCloudConnectors'] = []
        if self.io_tcloud_connectors is not None:
            for k in self.io_tcloud_connectors:
                result['IoTCloudConnectors'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorGroupStatus') is not None:
            self.io_tcloud_connector_group_status = m.get('IoTCloudConnectorGroupStatus')
        self.io_tcloud_connectors = []
        if m.get('IoTCloudConnectors') is not None:
            for k in m.get('IoTCloudConnectors'):
                temp_model = ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroupsIoTCloudConnectors()
                self.io_tcloud_connectors.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListIoTCloudConnectorGroupsResponseBody(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_groups: List[ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.io_tcloud_connector_groups = io_tcloud_connector_groups
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.io_tcloud_connector_groups:
            for k in self.io_tcloud_connector_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IoTCloudConnectorGroups'] = []
        if self.io_tcloud_connector_groups is not None:
            for k in self.io_tcloud_connector_groups:
                result['IoTCloudConnectorGroups'].append(k.to_map() if k else None)
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
        self.io_tcloud_connector_groups = []
        if m.get('IoTCloudConnectorGroups') is not None:
            for k in m.get('IoTCloudConnectorGroups'):
                temp_model = ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroups()
                self.io_tcloud_connector_groups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIoTCloudConnectorGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIoTCloudConnectorGroupsResponseBody = None,
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
            temp_model = ListIoTCloudConnectorGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorsRequest(TeaModel):
    def __init__(
        self,
        apn: List[str] = None,
        isp: List[str] = None,
        io_tcloud_connector_group_id: str = None,
        io_tcloud_connector_ids: List[str] = None,
        io_tcloud_connector_name: List[str] = None,
        io_tcloud_connector_status: List[str] = None,
        is_in_group: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        vpc_id: List[str] = None,
    ):
        self.apn = apn
        self.isp = isp
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.io_tcloud_connector_ids = io_tcloud_connector_ids
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.io_tcloud_connector_status = io_tcloud_connector_status
        self.is_in_group = is_in_group
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_ids is not None:
            result['IoTCloudConnectorIds'] = self.io_tcloud_connector_ids
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.is_in_group is not None:
            result['IsInGroup'] = self.is_in_group
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorIds') is not None:
            self.io_tcloud_connector_ids = m.get('IoTCloudConnectorIds')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('IsInGroup') is not None:
            self.is_in_group = m.get('IsInGroup')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListIoTCloudConnectorsResponseBodyIoTCloudConnectors(TeaModel):
    def __init__(
        self,
        apn: str = None,
        create_time: int = None,
        isp: str = None,
        io_tcloud_connector_business_status: str = None,
        io_tcloud_connector_description: str = None,
        io_tcloud_connector_group_id: str = None,
        io_tcloud_connector_id: str = None,
        io_tcloud_connector_name: str = None,
        io_tcloud_connector_status: str = None,
        modify_time: int = None,
        rate_limit: int = None,
        v_switch_list: List[str] = None,
        vpc_id: str = None,
        wildcard_domain_enabled: bool = None,
    ):
        self.apn = apn
        self.create_time = create_time
        self.isp = isp
        self.io_tcloud_connector_business_status = io_tcloud_connector_business_status
        self.io_tcloud_connector_description = io_tcloud_connector_description
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.io_tcloud_connector_status = io_tcloud_connector_status
        self.modify_time = modify_time
        self.rate_limit = rate_limit
        self.v_switch_list = v_switch_list
        self.vpc_id = vpc_id
        self.wildcard_domain_enabled = wildcard_domain_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_business_status is not None:
            result['IoTCloudConnectorBusinessStatus'] = self.io_tcloud_connector_business_status
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit
        if self.v_switch_list is not None:
            result['VSwitchList'] = self.v_switch_list
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorBusinessStatus') is not None:
            self.io_tcloud_connector_business_status = m.get('IoTCloudConnectorBusinessStatus')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RateLimit') is not None:
            self.rate_limit = m.get('RateLimit')
        if m.get('VSwitchList') is not None:
            self.v_switch_list = m.get('VSwitchList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class ListIoTCloudConnectorsResponseBody(TeaModel):
    def __init__(
        self,
        io_tcloud_connectors: List[ListIoTCloudConnectorsResponseBodyIoTCloudConnectors] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.io_tcloud_connectors = io_tcloud_connectors
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.io_tcloud_connectors:
            for k in self.io_tcloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IoTCloudConnectors'] = []
        if self.io_tcloud_connectors is not None:
            for k in self.io_tcloud_connectors:
                result['IoTCloudConnectors'].append(k.to_map() if k else None)
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
        self.io_tcloud_connectors = []
        if m.get('IoTCloudConnectors') is not None:
            for k in m.get('IoTCloudConnectors'):
                temp_model = ListIoTCloudConnectorsResponseBodyIoTCloudConnectors()
                self.io_tcloud_connectors.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIoTCloudConnectorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIoTCloudConnectorsResponseBody = None,
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
            temp_model = ListIoTCloudConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBodyRegions(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[ListRegionsResponseBodyRegions] = None,
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
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_statuses: List[str] = None,
        service_ids: List[str] = None,
        service_names: List[str] = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_statuses = resource_statuses
        self.service_ids = service_ids
        self.service_names = service_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_statuses is not None:
            result['ResourceStatuses'] = self.resource_statuses
        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids
        if self.service_names is not None:
            result['ServiceNames'] = self.service_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceStatuses') is not None:
            self.resource_statuses = m.get('ResourceStatuses')
        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')
        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')
        return self


class ListServiceResponseBodyServices(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        service_description: str = None,
        service_id: str = None,
        service_name: str = None,
        service_status: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_description = service_description
        self.service_id = service_id
        self.service_name = service_name
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class ListServiceResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[ListServiceResponseBodyServices] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.services = services
        self.total_count = total_count

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServiceResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceResponseBody = None,
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
            temp_model = ListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceEntriesRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_entry_ids: List[str] = None,
        service_entry_name: List[str] = None,
        service_entry_status: List[str] = None,
        service_id: str = None,
        target: List[str] = None,
        target_type: List[str] = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_entry_ids = service_entry_ids
        self.service_entry_name = service_entry_name
        self.service_entry_status = service_entry_status
        self.service_id = service_id
        self.target = target
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_ids is not None:
            result['ServiceEntryIds'] = self.service_entry_ids
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryIds') is not None:
            self.service_entry_ids = m.get('ServiceEntryIds')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListServiceEntriesResponseBodyServiceEntries(TeaModel):
    def __init__(
        self,
        service_entry_description: str = None,
        service_entry_id: str = None,
        service_entry_name: str = None,
        service_entry_status: str = None,
        service_id: str = None,
        target: str = None,
        target_type: str = None,
    ):
        self.service_entry_description = service_entry_description
        self.service_entry_id = service_entry_id
        self.service_entry_name = service_entry_name
        self.service_entry_status = service_entry_status
        self.service_id = service_id
        self.target = target
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListServiceEntriesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_entries: List[ListServiceEntriesResponseBodyServiceEntries] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.service_entries = service_entries
        self.total_count = total_count

    def validate(self):
        if self.service_entries:
            for k in self.service_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceEntries'] = []
        if self.service_entries is not None:
            for k in self.service_entries:
                result['ServiceEntries'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_entries = []
        if m.get('ServiceEntries') is not None:
            for k in m.get('ServiceEntries'):
                temp_model = ListServiceEntriesResponseBodyServiceEntries()
                self.service_entries.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceEntriesResponseBody = None,
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
            temp_model = ListServiceEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAuthorizationRuleToDNSServiceRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveAuthorizationRuleToDNSServiceResponseBody(TeaModel):
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


class MoveAuthorizationRuleToDNSServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveAuthorizationRuleToDNSServiceResponseBody = None,
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
            temp_model = MoveAuthorizationRuleToDNSServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveGroupAuthorizationRuleToDNSServiceRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        region_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveGroupAuthorizationRuleToDNSServiceResponseBody(TeaModel):
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


class MoveGroupAuthorizationRuleToDNSServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveGroupAuthorizationRuleToDNSServiceResponseBody = None,
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
            temp_model = MoveGroupAuthorizationRuleToDNSServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenIoTCloudConnectorServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenIoTCloudConnectorServiceResponseBody(TeaModel):
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


class OpenIoTCloudConnectorServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenIoTCloudConnectorServiceResponseBody = None,
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
            temp_model = OpenIoTCloudConnectorServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveIoTCloudConnectorFromGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        io_tcloud_connector_id: List[str] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveIoTCloudConnectorFromGroupResponseBody(TeaModel):
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


class RemoveIoTCloudConnectorFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveIoTCloudConnectorFromGroupResponseBody = None,
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
            temp_model = RemoveIoTCloudConnectorFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDiagnoseTaskForSingleCardRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        destination: str = None,
        destination_type: str = None,
        end_time: int = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        resource_uid: int = None,
        source: str = None,
        source_type: str = None,
    ):
        self.begin_time = begin_time
        self.destination = destination
        self.destination_type = destination_type
        self.end_time = end_time
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.resource_uid = resource_uid
        self.source = source
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SubmitDiagnoseTaskForSingleCardResponseBody(TeaModel):
    def __init__(
        self,
        diagnose_task_id: str = None,
        request_id: str = None,
    ):
        self.diagnose_task_id = diagnose_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnose_task_id is not None:
            result['DiagnoseTaskId'] = self.diagnose_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseTaskId') is not None:
            self.diagnose_task_id = m.get('DiagnoseTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDiagnoseTaskForSingleCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitDiagnoseTaskForSingleCardResponseBody = None,
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
            temp_model = SubmitDiagnoseTaskForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_id: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        destination: str = None,
        destination_type: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        policy: str = None,
        region_id: str = None,
        source_cidrs: List[str] = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_id = authorization_rule_id
        self.authorization_rule_name = authorization_rule_name
        self.client_token = client_token
        self.destination = destination
        self.destination_type = destination_type
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.policy = policy
        self.region_id = region_id
        self.source_cidrs = source_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class UpdateAuthorizationRuleAttributeResponseBody(TeaModel):
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


class UpdateAuthorizationRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAuthorizationRuleAttributeResponseBody = None,
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
            temp_model = UpdateAuthorizationRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionPoolAttributeRequest(TeaModel):
    def __init__(
        self,
        cidrs: List[str] = None,
        client_token: str = None,
        connection_pool_description: str = None,
        connection_pool_id: str = None,
        connection_pool_name: str = None,
        count: int = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
    ):
        self.cidrs = cidrs
        self.client_token = client_token
        self.connection_pool_description = connection_pool_description
        self.connection_pool_id = connection_pool_id
        self.connection_pool_name = connection_pool_name
        self.count = count
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id

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
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.count is not None:
            result['Count'] = self.count
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateConnectionPoolAttributeResponseBody(TeaModel):
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


class UpdateConnectionPoolAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConnectionPoolAttributeResponseBody = None,
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
            temp_model = UpdateConnectionPoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDNSServiceRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        dnsservice_rule_id: str = None,
        destination: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_type: str = None,
        source: str = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_name = authorization_rule_name
        self.client_token = client_token
        self.dnsservice_rule_id = dnsservice_rule_id
        self.destination = destination
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateDNSServiceRuleAttributeResponseBody(TeaModel):
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


class UpdateDNSServiceRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDNSServiceRuleAttributeResponseBody = None,
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
            temp_model = UpdateDNSServiceRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupAuthorizationRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_description: str = None,
        authorization_rule_id: str = None,
        authorization_rule_name: str = None,
        client_token: str = None,
        destination: str = None,
        destination_type: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        policy: str = None,
        region_id: str = None,
        source_cidrs: List[str] = None,
    ):
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_id = authorization_rule_id
        self.authorization_rule_name = authorization_rule_name
        self.client_token = client_token
        self.destination = destination
        self.destination_type = destination_type
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.policy = policy
        self.region_id = region_id
        self.source_cidrs = source_cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class UpdateGroupAuthorizationRuleAttributeResponseBody(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        io_tcloud_connector_group_id: str = None,
        request_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupAuthorizationRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupAuthorizationRuleAttributeResponseBody = None,
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
            temp_model = UpdateGroupAuthorizationRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupDNSServiceRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dnsservice_rule_description: str = None,
        dnsservice_rule_id: str = None,
        dnsservice_rule_name: str = None,
        destination: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        region_id: str = None,
        service_type: str = None,
        source: str = None,
    ):
        self.client_token = client_token
        self.dnsservice_rule_description = dnsservice_rule_description
        self.dnsservice_rule_id = dnsservice_rule_id
        self.dnsservice_rule_name = dnsservice_rule_name
        self.destination = destination
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.region_id = region_id
        self.service_type = service_type
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateGroupDNSServiceRuleAttributeResponseBody(TeaModel):
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


class UpdateGroupDNSServiceRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupDNSServiceRuleAttributeResponseBody = None,
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
            temp_model = UpdateGroupDNSServiceRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIoTCloudConnectorAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_description: str = None,
        io_tcloud_connector_id: str = None,
        io_tcloud_connector_name: str = None,
        region_id: str = None,
        wildcard_domain_enabled: bool = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_description = io_tcloud_connector_description
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.region_id = region_id
        self.wildcard_domain_enabled = wildcard_domain_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class UpdateIoTCloudConnectorAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class UpdateIoTCloudConnectorAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIoTCloudConnectorAttributeResponseBody = None,
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
            temp_model = UpdateIoTCloudConnectorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIoTCloudConnectorGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        io_tcloud_connector_group_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id
        self.name = name
        self.region_id = region_id

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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIoTCloudConnectorGroupAttributeResponseBody(TeaModel):
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


class UpdateIoTCloudConnectorGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIoTCloudConnectorGroupAttributeResponseBody = None,
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
            temp_model = UpdateIoTCloudConnectorGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_description: str = None,
        service_id: str = None,
        service_name: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_description = service_description
        self.service_id = service_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class UpdateServiceAttributeResponseBody(TeaModel):
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


class UpdateServiceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceAttributeResponseBody = None,
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
            temp_model = UpdateServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceEntryAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        io_tcloud_connector_id: str = None,
        region_id: str = None,
        service_entry_description: str = None,
        service_entry_id: str = None,
        service_entry_name: str = None,
        service_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.region_id = region_id
        self.service_entry_description = service_entry_description
        self.service_entry_id = service_entry_id
        self.service_entry_name = service_entry_name
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateServiceEntryAttributeResponseBody(TeaModel):
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


class UpdateServiceEntryAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceEntryAttributeResponseBody = None,
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
            temp_model = UpdateServiceEntryAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


