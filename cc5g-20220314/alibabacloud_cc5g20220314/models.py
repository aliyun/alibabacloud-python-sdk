# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddDNSAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        destination_ip: str = None,
        dry_run: bool = None,
        name: str = None,
        source_dnsip: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.destination_ip = destination_ip
        self.dry_run = dry_run
        self.name = name
        self.source_dnsip = source_dnsip
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.source_dnsip is not None:
            result['SourceDNSIp'] = self.source_dnsip
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceDNSIp') is not None:
            self.source_dnsip = m.get('SourceDNSIp')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class AddDNSAuthorizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        request_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        # Id of the request
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


class AddDNSAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDNSAuthorizationRuleResponseBody = None,
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
            temp_model = AddDNSAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachVpcToNetLinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        net_link_id: str = None,
        region_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.net_link_id = net_link_id
        self.region_id = region_id
        self.v_switches = v_switches
        self.vpc_id = vpc_id
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class AttachVpcToNetLinkResponseBody(TeaModel):
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


class AttachVpcToNetLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachVpcToNetLinkResponseBody = None,
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
            temp_model = AttachVpcToNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        destination: str = None,
        destination_type: str = None,
        dry_run: bool = None,
        name: str = None,
        policy: str = None,
        source_cidr: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.destination = destination
        self.destination_type = destination_type
        self.dry_run = dry_run
        self.name = name
        self.policy = policy
        self.source_cidr = source_cidr
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class CreateAuthorizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        request_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        # Id of the request
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


class CreateWirelessCloudConnectorRequestNetLinks(TeaModel):
    def __init__(
        self,
        apn: str = None,
        region_id: str = None,
        v_switchs: List[str] = None,
        vpc_id: str = None,
    ):
        self.apn = apn
        self.region_id = region_id
        self.v_switchs = v_switchs
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switchs is not None:
            result['VSwitchs'] = self.v_switchs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchs') is not None:
            self.v_switchs = m.get('VSwitchs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateWirelessCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        isp: str = None,
        name: str = None,
        net_links: List[CreateWirelessCloudConnectorRequestNetLinks] = None,
        region_id: str = None,
        use_case: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.isp = isp
        self.name = name
        self.net_links = net_links
        self.region_id = region_id
        self.use_case = use_case

    def validate(self):
        if self.net_links:
            for k in self.net_links:
                if k:
                    k.validate()

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
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        result['NetLinks'] = []
        if self.net_links is not None:
            for k in self.net_links:
                result['NetLinks'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.use_case is not None:
            result['UseCase'] = self.use_case
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.net_links = []
        if m.get('NetLinks') is not None:
            for k in m.get('NetLinks'):
                temp_model = CreateWirelessCloudConnectorRequestNetLinks()
                self.net_links.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UseCase') is not None:
            self.use_case = m.get('UseCase')
        return self


class CreateWirelessCloudConnectorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class CreateWirelessCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWirelessCloudConnectorResponseBody = None,
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
            temp_model = CreateWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class DeleteAuthorizationRuleResponseBody(TeaModel):
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


class DeleteWirelessCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class DeleteWirelessCloudConnectorResponseBody(TeaModel):
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


class DeleteWirelessCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWirelessCloudConnectorResponseBody = None,
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
            temp_model = DeleteWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachVpcFromNetLinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        net_link_id: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.net_link_id = net_link_id
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class DetachVpcFromNetLinkResponseBody(TeaModel):
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


class DetachVpcFromNetLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachVpcFromNetLinkResponseBody = None,
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
            temp_model = DetachVpcFromNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesRequest(TeaModel):
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


class ListZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        # 创建时间
        self.local_name = local_name
        # 资源名称
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[ListZonesResponseBodyZones] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 数组，返回示例目录。
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = ListZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListZonesResponseBody = None,
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
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCc5gServiceRequest(TeaModel):
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


class OpenCc5gServiceResponseBody(TeaModel):
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


class OpenCc5gServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenCc5gServiceResponseBody = None,
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
            temp_model = OpenCc5gServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        description: str = None,
        destination: str = None,
        dry_run: bool = None,
        name: str = None,
        policy: str = None,
        source_cidr: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.description = description
        self.destination = destination
        self.dry_run = dry_run
        self.name = name
        self.policy = policy
        self.source_cidr = source_cidr
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateAuthorizationRuleResponseBody(TeaModel):
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


class UpdateAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAuthorizationRuleResponseBody = None,
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
            temp_model = UpdateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCardRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        iccid: str = None,
        name: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.iccid = iccid
        self.name = name
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.name is not None:
            result['Name'] = self.name
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateCardResponseBody(TeaModel):
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


class UpdateCardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCardResponseBody = None,
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
            temp_model = UpdateCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDNSAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        authorization_rule_id: str = None,
        client_token: str = None,
        description: str = None,
        destination_ip: str = None,
        dry_run: bool = None,
        name: str = None,
        source_dnsip: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.description = description
        self.destination_ip = destination_ip
        self.dry_run = dry_run
        self.name = name
        self.source_dnsip = source_dnsip
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.source_dnsip is not None:
            result['SourceDNSIp'] = self.source_dnsip
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceDNSIp') is not None:
            self.source_dnsip = m.get('SourceDNSIp')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateDNSAuthorizationRuleResponseBody(TeaModel):
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


class UpdateDNSAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDNSAuthorizationRuleResponseBody = None,
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
            temp_model = UpdateDNSAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWirelessCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        wireless_cloud_connector_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.name = name
        self.wireless_cloud_connector_id = wireless_cloud_connector_id

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
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
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
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateWirelessCloudConnectorResponseBody(TeaModel):
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


class UpdateWirelessCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateWirelessCloudConnectorResponseBody = None,
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
            temp_model = UpdateWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


