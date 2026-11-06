# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetGatewayResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGatewayResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetGatewayResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGatewayResponseBodyData(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        elastic_enabled: bool = None,
        environments: List[main_models.GetGatewayResponseBodyDataEnvironments] = None,
        expire_timestamp: int = None,
        gateway_edition: str = None,
        gateway_id: str = None,
        gateway_mode: str = None,
        gateway_type: str = None,
        isp: str = None,
        load_balancers: List[main_models.GetGatewayResponseBodyDataLoadBalancers] = None,
        maintenance_period: main_models.GetGatewayResponseBodyDataMaintenancePeriod = None,
        name: str = None,
        network_access_config: main_models.GetGatewayResponseBodyDataNetworkAccessConfig = None,
        private_link: main_models.GetGatewayResponseBodyDataPrivateLink = None,
        replicas: str = None,
        resource_group_id: str = None,
        security_group: main_models.GetGatewayResponseBodyDataSecurityGroup = None,
        spec: str = None,
        status: str = None,
        sub_domain_infos: List[main_models.SubDomainInfo] = None,
        tags: List[main_models.GetGatewayResponseBodyDataTags] = None,
        target_version: str = None,
        tenant_id: str = None,
        update_timestamp: int = None,
        v_switch: main_models.GetGatewayResponseBodyDataVSwitch = None,
        version: str = None,
        vpc: main_models.GetGatewayResponseBodyDataVpc = None,
        zones: List[main_models.GetGatewayResponseBodyDataZones] = None,
    ):
        # The billing method. Valid values:
        # - POSTPAY: Pay-as-you-go.
        # - PREPAY: Subscription.
        self.charge_type = charge_type
        # The creation source of the gateway. Valid values:
        # - Console: The console.
        self.create_from = create_from
        # The creation timestamp. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # Indicates whether elastic scaling is enabled. A value of true indicates that elastic scaling is enabled. A value of false indicates that elastic scaling is disabled. A value of null or a missing value indicates that the status is unknown. This parameter is for query and display purposes only.
        self.elastic_enabled = elastic_enabled
        # The list of environments associated with the gateway.
        self.environments = environments
        # The expiration timestamp for subscription instances. Unit: milliseconds.
        self.expire_timestamp = expire_timestamp
        # The edition of the gateway instance. Valid values:
        # - Professional: Professional instance.
        # - Serverless: Serverless instance.
        self.gateway_edition = gateway_edition
        # The gateway ID.
        self.gateway_id = gateway_id
        # The operation mode for AI multi-tenant V2. The default value is ENTERPRISE. This parameter is applicable only to AI and MultiTenantServerless gateways.
        self.gateway_mode = gateway_mode
        # The gateway type. Valid values:
        # - API: API gateway.
        # - AI: AI gateway.
        self.gateway_type = gateway_type
        # The type of the Internet service provider (ISP).
        self.isp = isp
        # The list of ingress addresses for the gateway.
        self.load_balancers = load_balancers
        # The O&M window.
        self.maintenance_period = maintenance_period
        # The gateway name.
        self.name = name
        # The network access configuration of the gateway, including the access endpoint type and the security group used by the private endpoint. This parameter is returned only when the gateway is configured with a private endpoint.
        self.network_access_config = network_access_config
        # The PrivateLink information of the gateway, including the endpoint ID, access domain name, connection status, and zone information.
        self.private_link = private_link
        # The number of nodes in the gateway instance.
        self.replicas = replicas
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The security group of the gateway.
        self.security_group = security_group
        # The gateway specifications. Valid values:
        # - apigw.small.x1: Small specifications.
        self.spec = spec
        # The gateway status. Valid values:
        # - Running: The gateway is running.
        # - Creating: The gateway is being created.
        # - CreateFailed: The gateway failed to be created.
        # - Upgrading: The gateway is being upgraded.
        # - UpgradeFailed: The gateway failed to be upgraded.
        # - Restarting: The gateway is being restarted.
        # - RestartFailed: The gateway failed to be restarted.
        # - Deleting: The gateway is being released.
        # - DeleteFailed: The gateway failed to be released.
        self.status = status
        # The list of default access domain name information for the gateway. This parameter is not returned if no default domain name information is available.
        self.sub_domain_infos = sub_domain_infos
        # The resource tags.
        self.tags = tags
        # The target version of the gateway. If this value is different from the current version, you can upgrade the gateway.
        self.target_version = target_version
        # The tenant ID returned in STANDARD mode.
        self.tenant_id = tenant_id
        # The update timestamp. Unit: milliseconds.
        self.update_timestamp = update_timestamp
        # The vSwitch associated with the gateway.
        self.v_switch = v_switch
        # The gateway version.
        self.version = version
        # The VPC associated with the gateway.
        self.vpc = vpc
        # The list of zones associated with the gateway.
        self.zones = zones

    def validate(self):
        if self.environments:
            for v1 in self.environments:
                 if v1:
                    v1.validate()
        if self.load_balancers:
            for v1 in self.load_balancers:
                 if v1:
                    v1.validate()
        if self.maintenance_period:
            self.maintenance_period.validate()
        if self.network_access_config:
            self.network_access_config.validate()
        if self.private_link:
            self.private_link.validate()
        if self.security_group:
            self.security_group.validate()
        if self.sub_domain_infos:
            for v1 in self.sub_domain_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switch:
            self.v_switch.validate()
        if self.vpc:
            self.vpc.validate()
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.create_from is not None:
            result['createFrom'] = self.create_from

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.elastic_enabled is not None:
            result['elasticEnabled'] = self.elastic_enabled

        result['environments'] = []
        if self.environments is not None:
            for k1 in self.environments:
                result['environments'].append(k1.to_map() if k1 else None)

        if self.expire_timestamp is not None:
            result['expireTimestamp'] = self.expire_timestamp

        if self.gateway_edition is not None:
            result['gatewayEdition'] = self.gateway_edition

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_mode is not None:
            result['gatewayMode'] = self.gateway_mode

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.isp is not None:
            result['isp'] = self.isp

        result['loadBalancers'] = []
        if self.load_balancers is not None:
            for k1 in self.load_balancers:
                result['loadBalancers'].append(k1.to_map() if k1 else None)

        if self.maintenance_period is not None:
            result['maintenancePeriod'] = self.maintenance_period.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.network_access_config is not None:
            result['networkAccessConfig'] = self.network_access_config.to_map()

        if self.private_link is not None:
            result['privateLink'] = self.private_link.to_map()

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
            for k1 in self.sub_domain_infos:
                result['subDomainInfos'].append(k1.to_map() if k1 else None)

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

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
            for k1 in self.zones:
                result['zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('elasticEnabled') is not None:
            self.elastic_enabled = m.get('elasticEnabled')

        self.environments = []
        if m.get('environments') is not None:
            for k1 in m.get('environments'):
                temp_model = main_models.GetGatewayResponseBodyDataEnvironments()
                self.environments.append(temp_model.from_map(k1))

        if m.get('expireTimestamp') is not None:
            self.expire_timestamp = m.get('expireTimestamp')

        if m.get('gatewayEdition') is not None:
            self.gateway_edition = m.get('gatewayEdition')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayMode') is not None:
            self.gateway_mode = m.get('gatewayMode')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('isp') is not None:
            self.isp = m.get('isp')

        self.load_balancers = []
        if m.get('loadBalancers') is not None:
            for k1 in m.get('loadBalancers'):
                temp_model = main_models.GetGatewayResponseBodyDataLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k1))

        if m.get('maintenancePeriod') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataMaintenancePeriod()
            self.maintenance_period = temp_model.from_map(m.get('maintenancePeriod'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkAccessConfig') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataNetworkAccessConfig()
            self.network_access_config = temp_model.from_map(m.get('networkAccessConfig'))

        if m.get('privateLink') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataPrivateLink()
            self.private_link = temp_model.from_map(m.get('privateLink'))

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('securityGroup') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataSecurityGroup()
            self.security_group = temp_model.from_map(m.get('securityGroup'))

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k1 in m.get('subDomainInfos'):
                temp_model = main_models.SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetGatewayResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        if m.get('vSwitch') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataVSwitch()
            self.v_switch = temp_model.from_map(m.get('vSwitch'))

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('vpc') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        self.zones = []
        if m.get('zones') is not None:
            for k1 in m.get('zones'):
                temp_model = main_models.GetGatewayResponseBodyDataZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class GetGatewayResponseBodyDataZones(DaraModel):
    def __init__(
        self,
        name: str = None,
        v_switch: main_models.GetGatewayResponseBodyDataZonesVSwitch = None,
        zone_id: str = None,
    ):
        # The name of the zone.
        self.name = name
        # The vSwitch.
        self.v_switch = v_switch
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.v_switch:
            self.v_switch.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetGatewayResponseBodyDataZonesVSwitch()
            self.v_switch = temp_model.from_map(m.get('vSwitch'))

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class GetGatewayResponseBodyDataZonesVSwitch(DaraModel):
    def __init__(
        self,
        name: str = None,
        v_switch_id: str = None,
    ):
        # The name of the vSwitch.
        self.name = name
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetGatewayResponseBodyDataVpc(DaraModel):
    def __init__(
        self,
        name: str = None,
        vpc_id: str = None,
    ):
        # The name of the VPC.
        self.name = name
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetGatewayResponseBodyDataVSwitch(DaraModel):
    def __init__(
        self,
        name: str = None,
        v_switch_id: str = None,
    ):
        # The name of the vSwitch.
        self.name = name
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetGatewayResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the resource tag.
        self.key = key
        # The value of the resource tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetGatewayResponseBodyDataSecurityGroup(DaraModel):
    def __init__(
        self,
        name: str = None,
        security_group_id: str = None,
    ):
        # The name of the security group.
        self.name = name
        # The ID of the security group.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetGatewayResponseBodyDataPrivateLink(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_security_group_id: str = None,
        endpoint_status: str = None,
        last_error_code: str = None,
        last_error_message: str = None,
        observed_at: str = None,
        resource_may_be_charged: bool = None,
        stage: str = None,
        zones: List[main_models.GetGatewayResponseBodyDataPrivateLinkZones] = None,
    ):
        # The connection status between the private endpoint and the endpoint service. A value of Connected indicates that the endpoint is connected.
        self.connection_status = connection_status
        # The access domain name of the private endpoint, which can be used to access the gateway from the user VPC.
        self.endpoint_domain = endpoint_domain
        # The ID of the private endpoint.
        self.endpoint_id = endpoint_id
        # The ID of the security group configured for the private endpoint.
        self.endpoint_security_group_id = endpoint_security_group_id
        # The status of the private endpoint. A value of Active indicates that the endpoint is available.
        self.endpoint_status = endpoint_status
        # The error code of the most recent error that occurred during the creation or delete operations of the private endpoint. This parameter is not returned if no error message is available.
        self.last_error_code = last_error_code
        # The description of the most recent error that occurred during the creation or delete operations of the private endpoint. You can use this description along with the error code to troubleshoot the issue. This parameter is not returned if no error message is available.
        self.last_error_message = last_error_message
        # The time when the system last retrieved the status of the private endpoint. The time is in RFC 3339 format. This parameter is not returned if the status has not been retrieved.
        self.observed_at = observed_at
        # Indicates whether the private endpoint may continue to incur fees. A value of true indicates that the endpoint is created and its release is not confirmed. A value of false indicates that no fee prompt is available. The actual fees are subject to the bill.
        self.resource_may_be_charged = resource_may_be_charged
        # The current processing stage of the private endpoint. A value of Ready indicates that the private endpoint is ready.
        self.stage = stage
        # The list of zone information for the private endpoint.
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['connectionStatus'] = self.connection_status

        if self.endpoint_domain is not None:
            result['endpointDomain'] = self.endpoint_domain

        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id

        if self.endpoint_security_group_id is not None:
            result['endpointSecurityGroupId'] = self.endpoint_security_group_id

        if self.endpoint_status is not None:
            result['endpointStatus'] = self.endpoint_status

        if self.last_error_code is not None:
            result['lastErrorCode'] = self.last_error_code

        if self.last_error_message is not None:
            result['lastErrorMessage'] = self.last_error_message

        if self.observed_at is not None:
            result['observedAt'] = self.observed_at

        if self.resource_may_be_charged is not None:
            result['resourceMayBeCharged'] = self.resource_may_be_charged

        if self.stage is not None:
            result['stage'] = self.stage

        result['zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionStatus') is not None:
            self.connection_status = m.get('connectionStatus')

        if m.get('endpointDomain') is not None:
            self.endpoint_domain = m.get('endpointDomain')

        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')

        if m.get('endpointSecurityGroupId') is not None:
            self.endpoint_security_group_id = m.get('endpointSecurityGroupId')

        if m.get('endpointStatus') is not None:
            self.endpoint_status = m.get('endpointStatus')

        if m.get('lastErrorCode') is not None:
            self.last_error_code = m.get('lastErrorCode')

        if m.get('lastErrorMessage') is not None:
            self.last_error_message = m.get('lastErrorMessage')

        if m.get('observedAt') is not None:
            self.observed_at = m.get('observedAt')

        if m.get('resourceMayBeCharged') is not None:
            self.resource_may_be_charged = m.get('resourceMayBeCharged')

        if m.get('stage') is not None:
            self.stage = m.get('stage')

        self.zones = []
        if m.get('zones') is not None:
            for k1 in m.get('zones'):
                temp_model = main_models.GetGatewayResponseBodyDataPrivateLinkZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class GetGatewayResponseBodyDataPrivateLinkZones(DaraModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        # The connection status of the private endpoint in the zone. A value of Connected indicates that the endpoint is connected.
        self.status = status
        # The zone ID of the private endpoint.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class GetGatewayResponseBodyDataNetworkAccessConfig(DaraModel):
    def __init__(
        self,
        endpoint_security_group_id: str = None,
        type: str = None,
    ):
        # The ID of the security group configured for the private endpoint. The security group belongs to the VPC selected by the user and is an unmanaged security group.
        self.endpoint_security_group_id = endpoint_security_group_id
        # The access endpoint type of the gateway. Valid values:
        # - Intranet: Private endpoint only.
        # - InternetAndIntranet: Both Internet and private endpoints.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_security_group_id is not None:
            result['endpointSecurityGroupId'] = self.endpoint_security_group_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointSecurityGroupId') is not None:
            self.endpoint_security_group_id = m.get('endpointSecurityGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetGatewayResponseBodyDataMaintenancePeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The end time of the O&M window in the HH:mm format.
        self.end_time = end_time
        # The start time of the O&M window in the HH:mm format.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class GetGatewayResponseBodyDataLoadBalancers(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ip_version: str = None,
        address_type: str = None,
        gateway_default: bool = None,
        ipv_4addresses: List[str] = None,
        ipv_6addresses: List[str] = None,
        load_balancer_id: str = None,
        mode: str = None,
        ports: List[main_models.GetGatewayResponseBodyDataLoadBalancersPorts] = None,
        status: str = None,
        type: str = None,
    ):
        # The load balancing address.
        self.address = address
        # The IP version. Valid values:
        # - ipv4: IPv4.
        # - ipv6: IPv6.
        self.address_ip_version = address_ip_version
        # The type of the load balancing address. Valid values:
        # - Internet: Internet-facing.
        # - Intranet: Private network.
        self.address_type = address_type
        # Indicates whether the address is the default ingress address for the gateway.
        self.gateway_default = gateway_default
        # The list of IPv4 addresses.
        self.ipv_4addresses = ipv_4addresses
        # The list of IPv6 addresses.
        self.ipv_6addresses = ipv_6addresses
        # The load balancing ID.
        self.load_balancer_id = load_balancer_id
        # The load balancing pattern of the gateway. Valid values:
        # - Managed: Managed by Cloud-native API Gateway.
        self.mode = mode
        # The list of listener ports.
        self.ports = ports
        # The status of the load balancing. Valid values:
        # - Ready: Active.
        # - NotCreate: Not associated with an instance.
        self.status = status
        # The type of the load balancing. Valid values:
        # - NLB: Network Load Balancer (NLB).
        # - CLB: Classic Load Balancer.
        self.type = type

    def validate(self):
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.address_ip_version is not None:
            result['addressIpVersion'] = self.address_ip_version

        if self.address_type is not None:
            result['addressType'] = self.address_type

        if self.gateway_default is not None:
            result['gatewayDefault'] = self.gateway_default

        if self.ipv_4addresses is not None:
            result['ipv4Addresses'] = self.ipv_4addresses

        if self.ipv_6addresses is not None:
            result['ipv6Addresses'] = self.ipv_6addresses

        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id

        if self.mode is not None:
            result['mode'] = self.mode

        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

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

        if m.get('ipv4Addresses') is not None:
            self.ipv_4addresses = m.get('ipv4Addresses')

        if m.get('ipv6Addresses') is not None:
            self.ipv_6addresses = m.get('ipv6Addresses')

        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.GetGatewayResponseBodyDataLoadBalancersPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetGatewayResponseBodyDataLoadBalancersPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number.
        self.port = port
        # The protocol. Valid values:
        # - TCP: TCP.
        # - UDP: UDP.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetGatewayResponseBodyDataEnvironments(DaraModel):
    def __init__(
        self,
        alias: str = None,
        environment_id: str = None,
        name: str = None,
    ):
        # The alias of the environment.
        self.alias = alias
        # The environment ID.
        self.environment_id = environment_id
        # The environment name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

