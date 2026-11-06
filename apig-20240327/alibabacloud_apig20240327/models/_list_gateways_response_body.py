# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewaysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The gateway list query results.
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
            temp_model = main_models.ListGatewaysResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewaysResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListGatewaysResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The gateway list.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total count.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('items'):
                temp_model = main_models.ListGatewaysResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListGatewaysResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        elastic_enabled: bool = None,
        expire_timestamp: int = None,
        gateway_edition: str = None,
        gateway_id: str = None,
        gateway_mode: str = None,
        gateway_type: str = None,
        legacy: bool = None,
        load_balancers: List[main_models.ListGatewaysResponseBodyDataItemsLoadBalancers] = None,
        name: str = None,
        network_access_config: main_models.ListGatewaysResponseBodyDataItemsNetworkAccessConfig = None,
        private_link: main_models.ListGatewaysResponseBodyDataItemsPrivateLink = None,
        replicas: str = None,
        resource_group_id: str = None,
        security_group: main_models.ListGatewaysResponseBodyDataItemsSecurityGroup = None,
        spec: str = None,
        status: str = None,
        sub_domain_infos: List[main_models.SubDomainInfo] = None,
        tags: List[main_models.ListGatewaysResponseBodyDataItemsTags] = None,
        target_version: str = None,
        update_timestamp: int = None,
        v_switch: main_models.ListGatewaysResponseBodyDataItemsVSwitch = None,
        version: str = None,
        vpc: main_models.ListGatewaysResponseBodyDataItemsVpc = None,
        zones: List[main_models.ListGatewaysResponseBodyDataItemsZones] = None,
    ):
        # The billing method. Valid values:
        # - POSTPAY: Pay-as-you-go.
        # - PREPAY: Subscription.
        self.charge_type = charge_type
        # The source from which the gateway was created. Valid values:
        # - Console: The console.
        self.create_from = create_from
        # The creation timestamp. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # Indicates whether elastic scaling is enabled. A value of true indicates that elastic scaling is enabled. A value of false indicates that elastic scaling is disabled. A value of null or an empty value indicates that the status is unknown. This parameter is for query and display purposes only.
        self.elastic_enabled = elastic_enabled
        # The expiration timestamp for subscription instances. Unit: milliseconds.
        self.expire_timestamp = expire_timestamp
        # The edition of the gateway instance. Valid values:
        # - Professional: Regular instance.
        # - Serverless: Serverless instance.
        self.gateway_edition = gateway_edition
        # The gateway ID.
        self.gateway_id = gateway_id
        # The running mode of the AI MultiTenantServerless gateway. Valid values:
        # - ENTERPRISE: Enterprise Edition.
        # - STANDARD: Standard Edition.
        # This parameter is returned only for AI MultiTenantServerless gateways.
        self.gateway_mode = gateway_mode
        # The gateway type.
        self.gateway_type = gateway_type
        # Indicates whether the gateway instance was created before the AI gateway feature was released.
        self.legacy = legacy
        # The list of ingress addresses for the gateway.
        self.load_balancers = load_balancers
        # The gateway name.
        self.name = name
        # The network access configuration of the gateway, including the access ingress type and the security group used by the private endpoint. This parameter is returned only when the gateway is configured with a private ingress.
        self.network_access_config = network_access_config
        # The private connection information of the gateway, including the endpoint ID, access domain name, connection status, and zone information.
        self.private_link = private_link
        # The number of nodes in the gateway instance.
        self.replicas = replicas
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The security group information of the gateway.
        self.security_group = security_group
        # The gateway specification. Valid values:
        # - apigw.small.x1: Small specification.
        self.spec = spec
        # The gateway status. Valid values:
        # - Running: Running.
        # - Creating: Creating.
        # - CreateFailed: Creation failed.
        # - Upgrading: Upgrading.
        # - UpgradeFailed: Upgrade failed.
        # - Restarting: Restarting.
        # - RestartFailed: Restart failed.
        # - Deleting: Releasing.
        # - DeleteFailed: Release failed.
        self.status = status
        # The list of subdomains.
        self.sub_domain_infos = sub_domain_infos
        # The list of tags.
        self.tags = tags
        # The target version of the gateway. If this value differs from the current version, you can upgrade the gateway.
        self.target_version = target_version
        # The update timestamp. Unit: milliseconds.
        self.update_timestamp = update_timestamp
        # The vSwitch information.
        self.v_switch = v_switch
        # The gateway version.
        self.version = version
        # The VPC information of the gateway.
        self.vpc = vpc
        # The zone information of the gateway.
        self.zones = zones

    def validate(self):
        if self.load_balancers:
            for v1 in self.load_balancers:
                 if v1:
                    v1.validate()
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

        if self.legacy is not None:
            result['legacy'] = self.legacy

        result['loadBalancers'] = []
        if self.load_balancers is not None:
            for k1 in self.load_balancers:
                result['loadBalancers'].append(k1.to_map() if k1 else None)

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

        if m.get('legacy') is not None:
            self.legacy = m.get('legacy')

        self.load_balancers = []
        if m.get('loadBalancers') is not None:
            for k1 in m.get('loadBalancers'):
                temp_model = main_models.ListGatewaysResponseBodyDataItemsLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkAccessConfig') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsNetworkAccessConfig()
            self.network_access_config = temp_model.from_map(m.get('networkAccessConfig'))

        if m.get('privateLink') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsPrivateLink()
            self.private_link = temp_model.from_map(m.get('privateLink'))

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('securityGroup') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsSecurityGroup()
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
                temp_model = main_models.ListGatewaysResponseBodyDataItemsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        if m.get('vSwitch') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsVSwitch()
            self.v_switch = temp_model.from_map(m.get('vSwitch'))

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('vpc') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        self.zones = []
        if m.get('zones') is not None:
            for k1 in m.get('zones'):
                temp_model = main_models.ListGatewaysResponseBodyDataItemsZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListGatewaysResponseBodyDataItemsZones(DaraModel):
    def __init__(
        self,
        v_switch: main_models.ListGatewaysResponseBodyDataItemsZonesVSwitch = None,
        zone_id: str = None,
    ):
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
        if self.v_switch is not None:
            result['vSwitch'] = self.v_switch.to_map()

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitch') is not None:
            temp_model = main_models.ListGatewaysResponseBodyDataItemsZonesVSwitch()
            self.v_switch = temp_model.from_map(m.get('vSwitch'))

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class ListGatewaysResponseBodyDataItemsZonesVSwitch(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        return self

class ListGatewaysResponseBodyDataItemsVpc(DaraModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class ListGatewaysResponseBodyDataItemsVSwitch(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        return self

class ListGatewaysResponseBodyDataItemsTags(DaraModel):
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

class ListGatewaysResponseBodyDataItemsSecurityGroup(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
    ):
        # The security group ID.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        return self

class ListGatewaysResponseBodyDataItemsPrivateLink(DaraModel):
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
        zones: List[main_models.ListGatewaysResponseBodyDataItemsPrivateLinkZones] = None,
    ):
        # The connection status between the private endpoint and the endpoint service.
        self.connection_status = connection_status
        # The endpoint domain name used for connection configuration.
        self.endpoint_domain = endpoint_domain
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The ID of the security group configured for the private endpoint.
        self.endpoint_security_group_id = endpoint_security_group_id
        # The status of the private endpoint.
        self.endpoint_status = endpoint_status
        # The error code of the most recent fault that occurred during the private network ingress creation or delete procedure. This parameter is not returned if no error message is available.
        self.last_error_code = last_error_code
        # The description of the most recent fault that occurred during the private network ingress creation or delete procedure. You can use this description along with the error code to troubleshoot the issue. This parameter is not returned if no error message is available.
        self.last_error_message = last_error_message
        # The time when the system last obtained the status of the private endpoint. The time is in RFC 3339 format, such as 2026-11-02T10:00:00Z. This parameter is not returned if the status has not been obtained.
        self.observed_at = observed_at
        # Indicates whether the private endpoint may continue to incur charges. A value of true indicates that the endpoint has been created and its release has not been confirmed. A value of false indicates that there is no charge prompt. Actual charges are subject to the bill.
        self.resource_may_be_charged = resource_may_be_charged
        # The current processing stage of the private ingress. A value of Ready indicates that the private ingress is ready.
        self.stage = stage
        # The zone names.
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
                temp_model = main_models.ListGatewaysResponseBodyDataItemsPrivateLinkZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListGatewaysResponseBodyDataItemsPrivateLinkZones(DaraModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        # The status of the endpoint in the zone.
        self.status = status
        # The zone ID.
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

class ListGatewaysResponseBodyDataItemsNetworkAccessConfig(DaraModel):
    def __init__(
        self,
        endpoint_security_group_id: str = None,
        type: str = None,
    ):
        # The ID of the security group configured for the private endpoint. The security group belongs to the VPC selected by the user and is a non-managed security group.
        self.endpoint_security_group_id = endpoint_security_group_id
        # The gateway access ingress type.
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

class ListGatewaysResponseBodyDataItemsLoadBalancers(DaraModel):
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
        ports: List[main_models.ListGatewaysResponseBodyDataItemsLoadBalancersPorts] = None,
        status: str = None,
        type: str = None,
    ):
        # The load balancing address.
        self.address = address
        # The IP version. Valid values:
        # - ipv4: IPv4.
        # - ipv6: IPv6.
        self.address_ip_version = address_ip_version
        # The load balancing address type. Valid values:
        # - Internet: Internet.
        # - Intranet: Private network.
        self.address_type = address_type
        # Indicates whether the address is the default ingress address of the gateway.
        self.gateway_default = gateway_default
        # The list of IPv4 addresses.
        self.ipv_4addresses = ipv_4addresses
        # The list of IPv6 addresses.
        self.ipv_6addresses = ipv_6addresses
        # The load balancing ID.
        self.load_balancer_id = load_balancer_id
        # The load balancing provisioning pattern of the gateway. Valid values:
        # - Managed: Managed by Cloud-native API Gateway.
        self.mode = mode
        # The list of listened ports.
        self.ports = ports
        # The load balancing status. Valid values:
        # - Ready: Active.
        # - NotCreate: Not associated with an instance.
        self.status = status
        # The load balancing type of the gateway. Valid values:
        # - NLB: Network Load Balancer (NLB) load balancing.
        # - CLB: Classic load balancing.
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
                temp_model = main_models.ListGatewaysResponseBodyDataItemsLoadBalancersPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListGatewaysResponseBodyDataItemsLoadBalancersPorts(DaraModel):
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

