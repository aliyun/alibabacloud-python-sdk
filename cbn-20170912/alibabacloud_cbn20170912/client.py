# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cbn20170912 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cbn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def active_flow_log_with_options(
        self,
        request: main_models.ActiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveFlowLog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_flow_log_with_options_async(
        self,
        request: main_models.ActiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveFlowLog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_flow_log(
        self,
        request: main_models.ActiveFlowLogRequest,
    ) -> main_models.ActiveFlowLogResponse:
        runtime = RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    async def active_flow_log_async(
        self,
        request: main_models.ActiveFlowLogRequest,
    ) -> main_models.ActiveFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.active_flow_log_with_options_async(request, runtime)

    def add_traffic_match_rule_to_traffic_marking_policy_with_options(
        self,
        request: main_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTrafficMatchRuleToTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_traffic_match_rule_to_traffic_marking_policy_with_options_async(
        self,
        request: main_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTrafficMatchRuleToTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_traffic_match_rule_to_traffic_marking_policy(
        self,
        request: main_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> main_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return self.add_traffic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    async def add_traffic_match_rule_to_traffic_marking_policy_async(
        self,
        request: main_models.AddTrafficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> main_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.add_traffic_match_rule_to_traffic_marking_policy_with_options_async(request, runtime)

    def add_trafic_match_rule_to_traffic_marking_policy_with_options(
        self,
        request: main_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTraficMatchRuleToTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_trafic_match_rule_to_traffic_marking_policy_with_options_async(
        self,
        request: main_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTraficMatchRuleToTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_trafic_match_rule_to_traffic_marking_policy(
        self,
        request: main_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> main_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return self.add_trafic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    async def add_trafic_match_rule_to_traffic_marking_policy_async(
        self,
        request: main_models.AddTraficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> main_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.add_trafic_match_rule_to_traffic_marking_policy_with_options_async(request, runtime)

    def associate_cen_bandwidth_package_with_options(
        self,
        request: main_models.AssociateCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_cen_bandwidth_package_with_options_async(
        self,
        request: main_models.AssociateCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_cen_bandwidth_package(
        self,
        request: main_models.AssociateCenBandwidthPackageRequest,
    ) -> main_models.AssociateCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.associate_cen_bandwidth_package_with_options(request, runtime)

    async def associate_cen_bandwidth_package_async(
        self,
        request: main_models.AssociateCenBandwidthPackageRequest,
    ) -> main_models.AssociateCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.associate_cen_bandwidth_package_with_options_async(request, runtime)

    def associate_transit_router_attachment_with_route_table_with_options(
        self,
        request: main_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateTransitRouterAttachmentWithRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateTransitRouterAttachmentWithRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_transit_router_attachment_with_route_table_with_options_async(
        self,
        request: main_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateTransitRouterAttachmentWithRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateTransitRouterAttachmentWithRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_transit_router_attachment_with_route_table(
        self,
        request: main_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
    ) -> main_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        runtime = RuntimeOptions()
        return self.associate_transit_router_attachment_with_route_table_with_options(request, runtime)

    async def associate_transit_router_attachment_with_route_table_async(
        self,
        request: main_models.AssociateTransitRouterAttachmentWithRouteTableRequest,
    ) -> main_models.AssociateTransitRouterAttachmentWithRouteTableResponse:
        runtime = RuntimeOptions()
        return await self.associate_transit_router_attachment_with_route_table_with_options_async(request, runtime)

    def associate_transit_router_multicast_domain_with_options(
        self,
        request: main_models.AssociateTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_transit_router_multicast_domain_with_options_async(
        self,
        request: main_models.AssociateTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_transit_router_multicast_domain(
        self,
        request: main_models.AssociateTransitRouterMulticastDomainRequest,
    ) -> main_models.AssociateTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return self.associate_transit_router_multicast_domain_with_options(request, runtime)

    async def associate_transit_router_multicast_domain_async(
        self,
        request: main_models.AssociateTransitRouterMulticastDomainRequest,
    ) -> main_models.AssociateTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return await self.associate_transit_router_multicast_domain_with_options_async(request, runtime)

    def attach_cen_child_instance_with_options(
        self,
        request: main_models.AttachCenChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachCenChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachCenChildInstance',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachCenChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_cen_child_instance_with_options_async(
        self,
        request: main_models.AttachCenChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachCenChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachCenChildInstance',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachCenChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_cen_child_instance(
        self,
        request: main_models.AttachCenChildInstanceRequest,
    ) -> main_models.AttachCenChildInstanceResponse:
        runtime = RuntimeOptions()
        return self.attach_cen_child_instance_with_options(request, runtime)

    async def attach_cen_child_instance_async(
        self,
        request: main_models.AttachCenChildInstanceRequest,
    ) -> main_models.AttachCenChildInstanceResponse:
        runtime = RuntimeOptions()
        return await self.attach_cen_child_instance_with_options_async(request, runtime)

    def check_transit_router_service_with_options(
        self,
        request: main_models.CheckTransitRouterServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckTransitRouterServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckTransitRouterService',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTransitRouterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_transit_router_service_with_options_async(
        self,
        request: main_models.CheckTransitRouterServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckTransitRouterServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckTransitRouterService',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckTransitRouterServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_transit_router_service(
        self,
        request: main_models.CheckTransitRouterServiceRequest,
    ) -> main_models.CheckTransitRouterServiceResponse:
        runtime = RuntimeOptions()
        return self.check_transit_router_service_with_options(request, runtime)

    async def check_transit_router_service_async(
        self,
        request: main_models.CheckTransitRouterServiceRequest,
    ) -> main_models.CheckTransitRouterServiceResponse:
        runtime = RuntimeOptions()
        return await self.check_transit_router_service_with_options_async(request, runtime)

    def create_cen_with_options(
        self,
        request: main_models.CreateCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_with_options_async(
        self,
        request: main_models.CreateCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen(
        self,
        request: main_models.CreateCenRequest,
    ) -> main_models.CreateCenResponse:
        runtime = RuntimeOptions()
        return self.create_cen_with_options(request, runtime)

    async def create_cen_async(
        self,
        request: main_models.CreateCenRequest,
    ) -> main_models.CreateCenResponse:
        runtime = RuntimeOptions()
        return await self.create_cen_with_options_async(request, runtime)

    def create_cen_bandwidth_package_with_options(
        self,
        request: main_models.CreateCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_package_charge_type):
            query['BandwidthPackageChargeType'] = request.bandwidth_package_charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not DaraCore.is_null(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_bandwidth_package_with_options_async(
        self,
        request: main_models.CreateCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_package_charge_type):
            query['BandwidthPackageChargeType'] = request.bandwidth_package_charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not DaraCore.is_null(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_bandwidth_package(
        self,
        request: main_models.CreateCenBandwidthPackageRequest,
    ) -> main_models.CreateCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.create_cen_bandwidth_package_with_options(request, runtime)

    async def create_cen_bandwidth_package_async(
        self,
        request: main_models.CreateCenBandwidthPackageRequest,
    ) -> main_models.CreateCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.create_cen_bandwidth_package_with_options_async(request, runtime)

    def create_cen_child_instance_route_entry_to_attachment_with_options(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenChildInstanceRouteEntryToAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenChildInstanceRouteEntryToAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_child_instance_route_entry_to_attachment_with_options_async(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenChildInstanceRouteEntryToAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenChildInstanceRouteEntryToAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_child_instance_route_entry_to_attachment(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> main_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    async def create_cen_child_instance_route_entry_to_attachment_async(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> main_models.CreateCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.create_cen_child_instance_route_entry_to_attachment_with_options_async(request, runtime)

    def create_cen_child_instance_route_entry_to_cen_with_options(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenChildInstanceRouteEntryToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenChildInstanceRouteEntryToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenChildInstanceRouteEntryToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_child_instance_route_entry_to_cen_with_options_async(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenChildInstanceRouteEntryToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenChildInstanceRouteEntryToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenChildInstanceRouteEntryToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_child_instance_route_entry_to_cen(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToCenRequest,
    ) -> main_models.CreateCenChildInstanceRouteEntryToCenResponse:
        runtime = RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    async def create_cen_child_instance_route_entry_to_cen_async(
        self,
        request: main_models.CreateCenChildInstanceRouteEntryToCenRequest,
    ) -> main_models.CreateCenChildInstanceRouteEntryToCenResponse:
        runtime = RuntimeOptions()
        return await self.create_cen_child_instance_route_entry_to_cen_with_options_async(request, runtime)

    def create_cen_inter_region_traffic_qos_policy_with_options(
        self,
        request: main_models.CreateCenInterRegionTrafficQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenInterRegionTrafficQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_guarantee_mode):
            query['BandwidthGuaranteeMode'] = request.bandwidth_guarantee_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_dry_run):
            query['ConsoleDryRun'] = request.console_dry_run
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not DaraCore.is_null(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not DaraCore.is_null(request.traffic_qos_queues):
            query['TrafficQosQueues'] = request.traffic_qos_queues
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenInterRegionTrafficQosPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenInterRegionTrafficQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_inter_region_traffic_qos_policy_with_options_async(
        self,
        request: main_models.CreateCenInterRegionTrafficQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenInterRegionTrafficQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_guarantee_mode):
            query['BandwidthGuaranteeMode'] = request.bandwidth_guarantee_mode
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.console_dry_run):
            query['ConsoleDryRun'] = request.console_dry_run
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not DaraCore.is_null(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not DaraCore.is_null(request.traffic_qos_queues):
            query['TrafficQosQueues'] = request.traffic_qos_queues
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenInterRegionTrafficQosPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenInterRegionTrafficQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_inter_region_traffic_qos_policy(
        self,
        request: main_models.CreateCenInterRegionTrafficQosPolicyRequest,
    ) -> main_models.CreateCenInterRegionTrafficQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    async def create_cen_inter_region_traffic_qos_policy_async(
        self,
        request: main_models.CreateCenInterRegionTrafficQosPolicyRequest,
    ) -> main_models.CreateCenInterRegionTrafficQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_cen_inter_region_traffic_qos_policy_with_options_async(request, runtime)

    def create_cen_inter_region_traffic_qos_queue_with_options(
        self,
        request: main_models.CreateCenInterRegionTrafficQosQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenInterRegionTrafficQosQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dscps):
            query['Dscps'] = request.dscps
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not DaraCore.is_null(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not DaraCore.is_null(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenInterRegionTrafficQosQueue',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenInterRegionTrafficQosQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_inter_region_traffic_qos_queue_with_options_async(
        self,
        request: main_models.CreateCenInterRegionTrafficQosQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenInterRegionTrafficQosQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dscps):
            query['Dscps'] = request.dscps
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not DaraCore.is_null(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not DaraCore.is_null(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenInterRegionTrafficQosQueue',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenInterRegionTrafficQosQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_inter_region_traffic_qos_queue(
        self,
        request: main_models.CreateCenInterRegionTrafficQosQueueRequest,
    ) -> main_models.CreateCenInterRegionTrafficQosQueueResponse:
        runtime = RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    async def create_cen_inter_region_traffic_qos_queue_async(
        self,
        request: main_models.CreateCenInterRegionTrafficQosQueueRequest,
    ) -> main_models.CreateCenInterRegionTrafficQosQueueResponse:
        runtime = RuntimeOptions()
        return await self.create_cen_inter_region_traffic_qos_queue_with_options_async(request, runtime)

    def create_cen_route_map_with_options(
        self,
        request: main_models.CreateCenRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenRouteMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not DaraCore.is_null(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not DaraCore.is_null(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not DaraCore.is_null(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not DaraCore.is_null(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not DaraCore.is_null(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not DaraCore.is_null(request.destination_region_ids):
            query['DestinationRegionIds'] = request.destination_region_ids
        if not DaraCore.is_null(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not DaraCore.is_null(request.map_result):
            query['MapResult'] = request.map_result
        if not DaraCore.is_null(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not DaraCore.is_null(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not DaraCore.is_null(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not DaraCore.is_null(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not DaraCore.is_null(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preference):
            query['Preference'] = request.preference
        if not DaraCore.is_null(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_types):
            query['RouteTypes'] = request.route_types
        if not DaraCore.is_null(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not DaraCore.is_null(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not DaraCore.is_null(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not DaraCore.is_null(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not DaraCore.is_null(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not DaraCore.is_null(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenRouteMap',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cen_route_map_with_options_async(
        self,
        request: main_models.CreateCenRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCenRouteMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not DaraCore.is_null(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not DaraCore.is_null(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not DaraCore.is_null(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not DaraCore.is_null(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not DaraCore.is_null(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not DaraCore.is_null(request.destination_region_ids):
            query['DestinationRegionIds'] = request.destination_region_ids
        if not DaraCore.is_null(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not DaraCore.is_null(request.map_result):
            query['MapResult'] = request.map_result
        if not DaraCore.is_null(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not DaraCore.is_null(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not DaraCore.is_null(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not DaraCore.is_null(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not DaraCore.is_null(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preference):
            query['Preference'] = request.preference
        if not DaraCore.is_null(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_types):
            query['RouteTypes'] = request.route_types
        if not DaraCore.is_null(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not DaraCore.is_null(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not DaraCore.is_null(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not DaraCore.is_null(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not DaraCore.is_null(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not DaraCore.is_null(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCenRouteMap',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCenRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cen_route_map(
        self,
        request: main_models.CreateCenRouteMapRequest,
    ) -> main_models.CreateCenRouteMapResponse:
        runtime = RuntimeOptions()
        return self.create_cen_route_map_with_options(request, runtime)

    async def create_cen_route_map_async(
        self,
        request: main_models.CreateCenRouteMapRequest,
    ) -> main_models.CreateCenRouteMapResponse:
        runtime = RuntimeOptions()
        return await self.create_cen_route_map_with_options_async(request, runtime)

    def create_flowlog_with_options(
        self,
        request: main_models.CreateFlowlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowlogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_format_string):
            query['LogFormatString'] = request.log_format_string
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowlog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowlogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flowlog_with_options_async(
        self,
        request: main_models.CreateFlowlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFlowlogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_format_string):
            query['LogFormatString'] = request.log_format_string
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFlowlog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFlowlogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_flowlog(
        self,
        request: main_models.CreateFlowlogRequest,
    ) -> main_models.CreateFlowlogResponse:
        runtime = RuntimeOptions()
        return self.create_flowlog_with_options(request, runtime)

    async def create_flowlog_async(
        self,
        request: main_models.CreateFlowlogRequest,
    ) -> main_models.CreateFlowlogResponse:
        runtime = RuntimeOptions()
        return await self.create_flowlog_with_options_async(request, runtime)

    def create_traffic_marking_policy_with_options(
        self,
        request: main_models.CreateTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.marking_dscp):
            query['MarkingDscp'] = request.marking_dscp
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not DaraCore.is_null(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not DaraCore.is_null(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_marking_policy_with_options_async(
        self,
        request: main_models.CreateTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.marking_dscp):
            query['MarkingDscp'] = request.marking_dscp
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not DaraCore.is_null(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not DaraCore.is_null(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_marking_policy(
        self,
        request: main_models.CreateTrafficMarkingPolicyRequest,
    ) -> main_models.CreateTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_traffic_marking_policy_with_options(request, runtime)

    async def create_traffic_marking_policy_async(
        self,
        request: main_models.CreateTrafficMarkingPolicyRequest,
    ) -> main_models.CreateTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_traffic_marking_policy_with_options_async(request, runtime)

    def create_transit_route_table_aggregation_with_options(
        self,
        tmp_req: main_models.CreateTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouteTableAggregationResponse:
        tmp_req.validate()
        request = main_models.CreateTransitRouteTableAggregationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_route_table_aggregation_scope_list):
            request.transit_route_table_aggregation_scope_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_route_table_aggregation_scope_list, 'TransitRouteTableAggregationScopeList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_aggregation_description):
            query['TransitRouteTableAggregationDescription'] = request.transit_route_table_aggregation_description
        if not DaraCore.is_null(request.transit_route_table_aggregation_name):
            query['TransitRouteTableAggregationName'] = request.transit_route_table_aggregation_name
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope):
            query['TransitRouteTableAggregationScope'] = request.transit_route_table_aggregation_scope
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope_list_shrink):
            query['TransitRouteTableAggregationScopeList'] = request.transit_route_table_aggregation_scope_list_shrink
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_route_table_aggregation_with_options_async(
        self,
        tmp_req: main_models.CreateTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouteTableAggregationResponse:
        tmp_req.validate()
        request = main_models.CreateTransitRouteTableAggregationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_route_table_aggregation_scope_list):
            request.transit_route_table_aggregation_scope_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_route_table_aggregation_scope_list, 'TransitRouteTableAggregationScopeList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_aggregation_description):
            query['TransitRouteTableAggregationDescription'] = request.transit_route_table_aggregation_description
        if not DaraCore.is_null(request.transit_route_table_aggregation_name):
            query['TransitRouteTableAggregationName'] = request.transit_route_table_aggregation_name
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope):
            query['TransitRouteTableAggregationScope'] = request.transit_route_table_aggregation_scope
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope_list_shrink):
            query['TransitRouteTableAggregationScopeList'] = request.transit_route_table_aggregation_scope_list_shrink
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouteTableAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_route_table_aggregation(
        self,
        request: main_models.CreateTransitRouteTableAggregationRequest,
    ) -> main_models.CreateTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return self.create_transit_route_table_aggregation_with_options(request, runtime)

    async def create_transit_route_table_aggregation_async(
        self,
        request: main_models.CreateTransitRouteTableAggregationRequest,
    ) -> main_models.CreateTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_route_table_aggregation_with_options_async(request, runtime)

    def create_transit_router_with_options(
        self,
        tmp_req: main_models.CreateTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterResponse:
        tmp_req.validate()
        request = main_models.CreateTransitRouterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_router_cidr_list):
            request.transit_router_cidr_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_router_cidr_list, 'TransitRouterCidrList', 'json')
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_cidr_list_shrink):
            query['TransitRouterCidrList'] = request.transit_router_cidr_list_shrink
        if not DaraCore.is_null(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not DaraCore.is_null(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_with_options_async(
        self,
        tmp_req: main_models.CreateTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterResponse:
        tmp_req.validate()
        request = main_models.CreateTransitRouterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_router_cidr_list):
            request.transit_router_cidr_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_router_cidr_list, 'TransitRouterCidrList', 'json')
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_cidr_list_shrink):
            query['TransitRouterCidrList'] = request.transit_router_cidr_list_shrink
        if not DaraCore.is_null(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not DaraCore.is_null(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router(
        self,
        request: main_models.CreateTransitRouterRequest,
    ) -> main_models.CreateTransitRouterResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_with_options(request, runtime)

    async def create_transit_router_async(
        self,
        request: main_models.CreateTransitRouterRequest,
    ) -> main_models.CreateTransitRouterResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_with_options_async(request, runtime)

    def create_transit_router_cidr_with_options(
        self,
        request: main_models.CreateTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_cidr_with_options_async(
        self,
        request: main_models.CreateTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_cidr(
        self,
        request: main_models.CreateTransitRouterCidrRequest,
    ) -> main_models.CreateTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_cidr_with_options(request, runtime)

    async def create_transit_router_cidr_async(
        self,
        request: main_models.CreateTransitRouterCidrRequest,
    ) -> main_models.CreateTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_cidr_with_options_async(request, runtime)

    def create_transit_router_ecr_attachment_with_options(
        self,
        request: main_models.CreateTransitRouterEcrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterEcrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            query['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.ecr_owner_id):
            query['EcrOwnerId'] = request.ecr_owner_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterEcrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterEcrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_ecr_attachment_with_options_async(
        self,
        request: main_models.CreateTransitRouterEcrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterEcrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ecr_id):
            query['EcrId'] = request.ecr_id
        if not DaraCore.is_null(request.ecr_owner_id):
            query['EcrOwnerId'] = request.ecr_owner_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterEcrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterEcrAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_ecr_attachment(
        self,
        request: main_models.CreateTransitRouterEcrAttachmentRequest,
    ) -> main_models.CreateTransitRouterEcrAttachmentResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_ecr_attachment_with_options(request, runtime)

    async def create_transit_router_ecr_attachment_async(
        self,
        request: main_models.CreateTransitRouterEcrAttachmentRequest,
    ) -> main_models.CreateTransitRouterEcrAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_ecr_attachment_with_options_async(request, runtime)

    def create_transit_router_multicast_domain_with_options(
        self,
        request: main_models.CreateTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not DaraCore.is_null(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_multicast_domain_with_options_async(
        self,
        request: main_models.CreateTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not DaraCore.is_null(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_multicast_domain(
        self,
        request: main_models.CreateTransitRouterMulticastDomainRequest,
    ) -> main_models.CreateTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_multicast_domain_with_options(request, runtime)

    async def create_transit_router_multicast_domain_async(
        self,
        request: main_models.CreateTransitRouterMulticastDomainRequest,
    ) -> main_models.CreateTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_multicast_domain_with_options_async(request, runtime)

    def create_transit_router_peer_attachment_with_options(
        self,
        request: main_models.CreateTransitRouterPeerAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterPeerAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_link_type):
            query['DefaultLinkType'] = request.default_link_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_id):
            query['PeerTransitRouterId'] = request.peer_transit_router_id
        if not DaraCore.is_null(request.peer_transit_router_region_id):
            query['PeerTransitRouterRegionId'] = request.peer_transit_router_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterPeerAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterPeerAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_peer_attachment_with_options_async(
        self,
        request: main_models.CreateTransitRouterPeerAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterPeerAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_link_type):
            query['DefaultLinkType'] = request.default_link_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_id):
            query['PeerTransitRouterId'] = request.peer_transit_router_id
        if not DaraCore.is_null(request.peer_transit_router_region_id):
            query['PeerTransitRouterRegionId'] = request.peer_transit_router_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterPeerAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterPeerAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_peer_attachment(
        self,
        request: main_models.CreateTransitRouterPeerAttachmentRequest,
    ) -> main_models.CreateTransitRouterPeerAttachmentResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_peer_attachment_with_options(request, runtime)

    async def create_transit_router_peer_attachment_async(
        self,
        request: main_models.CreateTransitRouterPeerAttachmentRequest,
    ) -> main_models.CreateTransitRouterPeerAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_peer_attachment_with_options_async(request, runtime)

    def create_transit_router_prefix_list_association_with_options(
        self,
        request: main_models.CreateTransitRouterPrefixListAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterPrefixListAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterPrefixListAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_prefix_list_association_with_options_async(
        self,
        request: main_models.CreateTransitRouterPrefixListAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterPrefixListAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterPrefixListAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterPrefixListAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_prefix_list_association(
        self,
        request: main_models.CreateTransitRouterPrefixListAssociationRequest,
    ) -> main_models.CreateTransitRouterPrefixListAssociationResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_prefix_list_association_with_options(request, runtime)

    async def create_transit_router_prefix_list_association_async(
        self,
        request: main_models.CreateTransitRouterPrefixListAssociationRequest,
    ) -> main_models.CreateTransitRouterPrefixListAssociationResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_prefix_list_association_with_options_async(request, runtime)

    def create_transit_router_route_entry_with_options(
        self,
        request: main_models.CreateTransitRouterRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterRouteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not DaraCore.is_null(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not DaraCore.is_null(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterRouteEntry',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_route_entry_with_options_async(
        self,
        request: main_models.CreateTransitRouterRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterRouteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not DaraCore.is_null(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not DaraCore.is_null(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterRouteEntry',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_route_entry(
        self,
        request: main_models.CreateTransitRouterRouteEntryRequest,
    ) -> main_models.CreateTransitRouterRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_route_entry_with_options(request, runtime)

    async def create_transit_router_route_entry_async(
        self,
        request: main_models.CreateTransitRouterRouteEntryRequest,
    ) -> main_models.CreateTransitRouterRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_route_entry_with_options_async(request, runtime)

    def create_transit_router_route_table_with_options(
        self,
        request: main_models.CreateTransitRouterRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not DaraCore.is_null(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_route_table_with_options_async(
        self,
        request: main_models.CreateTransitRouterRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not DaraCore.is_null(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_route_table(
        self,
        request: main_models.CreateTransitRouterRouteTableRequest,
    ) -> main_models.CreateTransitRouterRouteTableResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_route_table_with_options(request, runtime)

    async def create_transit_router_route_table_async(
        self,
        request: main_models.CreateTransitRouterRouteTableRequest,
    ) -> main_models.CreateTransitRouterRouteTableResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_route_table_with_options_async(request, runtime)

    def create_transit_router_vbr_attachment_with_options(
        self,
        request: main_models.CreateTransitRouterVbrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterVbrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not DaraCore.is_null(request.vbr_owner_id):
            query['VbrOwnerId'] = request.vbr_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterVbrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterVbrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_vbr_attachment_with_options_async(
        self,
        request: main_models.CreateTransitRouterVbrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterVbrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not DaraCore.is_null(request.vbr_owner_id):
            query['VbrOwnerId'] = request.vbr_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterVbrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterVbrAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_vbr_attachment(
        self,
        request: main_models.CreateTransitRouterVbrAttachmentRequest,
    ) -> main_models.CreateTransitRouterVbrAttachmentResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_vbr_attachment_with_options(request, runtime)

    async def create_transit_router_vbr_attachment_async(
        self,
        request: main_models.CreateTransitRouterVbrAttachmentRequest,
    ) -> main_models.CreateTransitRouterVbrAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_vbr_attachment_with_options_async(request, runtime)

    def create_transit_router_vpc_attachment_with_options(
        self,
        tmp_req: main_models.CreateTransitRouterVpcAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterVpcAttachmentResponse:
        tmp_req.validate()
        request = main_models.CreateTransitRouterVpcAttachmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_router_vpcattachment_options):
            request.transit_router_vpcattachment_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_router_vpcattachment_options, 'TransitRouterVPCAttachmentOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_vpcattachment_options_shrink):
            query['TransitRouterVPCAttachmentOptions'] = request.transit_router_vpcattachment_options_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            query['VpcOwnerId'] = request.vpc_owner_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterVpcAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterVpcAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_vpc_attachment_with_options_async(
        self,
        tmp_req: main_models.CreateTransitRouterVpcAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterVpcAttachmentResponse:
        tmp_req.validate()
        request = main_models.CreateTransitRouterVpcAttachmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_router_vpcattachment_options):
            request.transit_router_vpcattachment_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_router_vpcattachment_options, 'TransitRouterVPCAttachmentOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_vpcattachment_options_shrink):
            query['TransitRouterVPCAttachmentOptions'] = request.transit_router_vpcattachment_options_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            query['VpcOwnerId'] = request.vpc_owner_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterVpcAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterVpcAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_vpc_attachment(
        self,
        request: main_models.CreateTransitRouterVpcAttachmentRequest,
    ) -> main_models.CreateTransitRouterVpcAttachmentResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_vpc_attachment_with_options(request, runtime)

    async def create_transit_router_vpc_attachment_async(
        self,
        request: main_models.CreateTransitRouterVpcAttachmentRequest,
    ) -> main_models.CreateTransitRouterVpcAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_vpc_attachment_with_options_async(request, runtime)

    def create_transit_router_vpn_attachment_with_options(
        self,
        request: main_models.CreateTransitRouterVpnAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterVpnAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpn_id):
            query['VpnId'] = request.vpn_id
        if not DaraCore.is_null(request.vpn_owner_id):
            query['VpnOwnerId'] = request.vpn_owner_id
        if not DaraCore.is_null(request.zone):
            query['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterVpnAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterVpnAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transit_router_vpn_attachment_with_options_async(
        self,
        request: main_models.CreateTransitRouterVpnAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransitRouterVpnAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpn_id):
            query['VpnId'] = request.vpn_id
        if not DaraCore.is_null(request.vpn_owner_id):
            query['VpnOwnerId'] = request.vpn_owner_id
        if not DaraCore.is_null(request.zone):
            query['Zone'] = request.zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransitRouterVpnAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransitRouterVpnAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transit_router_vpn_attachment(
        self,
        request: main_models.CreateTransitRouterVpnAttachmentRequest,
    ) -> main_models.CreateTransitRouterVpnAttachmentResponse:
        runtime = RuntimeOptions()
        return self.create_transit_router_vpn_attachment_with_options(request, runtime)

    async def create_transit_router_vpn_attachment_async(
        self,
        request: main_models.CreateTransitRouterVpnAttachmentRequest,
    ) -> main_models.CreateTransitRouterVpnAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.create_transit_router_vpn_attachment_with_options_async(request, runtime)

    def deactive_flow_log_with_options(
        self,
        request: main_models.DeactiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveFlowLog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactive_flow_log_with_options_async(
        self,
        request: main_models.DeactiveFlowLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactiveFlowLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactiveFlowLog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactiveFlowLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactive_flow_log(
        self,
        request: main_models.DeactiveFlowLogRequest,
    ) -> main_models.DeactiveFlowLogResponse:
        runtime = RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    async def deactive_flow_log_async(
        self,
        request: main_models.DeactiveFlowLogRequest,
    ) -> main_models.DeactiveFlowLogResponse:
        runtime = RuntimeOptions()
        return await self.deactive_flow_log_with_options_async(request, runtime)

    def delete_cen_with_options(
        self,
        request: main_models.DeleteCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_with_options_async(
        self,
        request: main_models.DeleteCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen(
        self,
        request: main_models.DeleteCenRequest,
    ) -> main_models.DeleteCenResponse:
        runtime = RuntimeOptions()
        return self.delete_cen_with_options(request, runtime)

    async def delete_cen_async(
        self,
        request: main_models.DeleteCenRequest,
    ) -> main_models.DeleteCenResponse:
        runtime = RuntimeOptions()
        return await self.delete_cen_with_options_async(request, runtime)

    def delete_cen_bandwidth_package_with_options(
        self,
        request: main_models.DeleteCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_bandwidth_package_with_options_async(
        self,
        request: main_models.DeleteCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_bandwidth_package(
        self,
        request: main_models.DeleteCenBandwidthPackageRequest,
    ) -> main_models.DeleteCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.delete_cen_bandwidth_package_with_options(request, runtime)

    async def delete_cen_bandwidth_package_async(
        self,
        request: main_models.DeleteCenBandwidthPackageRequest,
    ) -> main_models.DeleteCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.delete_cen_bandwidth_package_with_options_async(request, runtime)

    def delete_cen_child_instance_route_entry_to_attachment_with_options(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenChildInstanceRouteEntryToAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_child_instance_route_entry_to_attachment_with_options_async(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenChildInstanceRouteEntryToAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_child_instance_route_entry_to_attachment(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    async def delete_cen_child_instance_route_entry_to_attachment_async(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToAttachmentRequest,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_cen_child_instance_route_entry_to_attachment_with_options_async(request, runtime)

    def delete_cen_child_instance_route_entry_to_cen_with_options(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenChildInstanceRouteEntryToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenChildInstanceRouteEntryToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_child_instance_route_entry_to_cen_with_options_async(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenChildInstanceRouteEntryToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenChildInstanceRouteEntryToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_child_instance_route_entry_to_cen(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToCenRequest,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        runtime = RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    async def delete_cen_child_instance_route_entry_to_cen_async(
        self,
        request: main_models.DeleteCenChildInstanceRouteEntryToCenRequest,
    ) -> main_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        runtime = RuntimeOptions()
        return await self.delete_cen_child_instance_route_entry_to_cen_with_options_async(request, runtime)

    def delete_cen_inter_region_traffic_qos_policy_with_options(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenInterRegionTrafficQosPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenInterRegionTrafficQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_inter_region_traffic_qos_policy_with_options_async(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenInterRegionTrafficQosPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenInterRegionTrafficQosPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_inter_region_traffic_qos_policy(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosPolicyRequest,
    ) -> main_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    async def delete_cen_inter_region_traffic_qos_policy_async(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosPolicyRequest,
    ) -> main_models.DeleteCenInterRegionTrafficQosPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_cen_inter_region_traffic_qos_policy_with_options_async(request, runtime)

    def delete_cen_inter_region_traffic_qos_queue_with_options(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenInterRegionTrafficQosQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenInterRegionTrafficQosQueue',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenInterRegionTrafficQosQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_inter_region_traffic_qos_queue_with_options_async(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenInterRegionTrafficQosQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenInterRegionTrafficQosQueue',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenInterRegionTrafficQosQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_inter_region_traffic_qos_queue(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosQueueRequest,
    ) -> main_models.DeleteCenInterRegionTrafficQosQueueResponse:
        runtime = RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    async def delete_cen_inter_region_traffic_qos_queue_async(
        self,
        request: main_models.DeleteCenInterRegionTrafficQosQueueRequest,
    ) -> main_models.DeleteCenInterRegionTrafficQosQueueResponse:
        runtime = RuntimeOptions()
        return await self.delete_cen_inter_region_traffic_qos_queue_with_options_async(request, runtime)

    def delete_cen_route_map_with_options(
        self,
        request: main_models.DeleteCenRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenRouteMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenRouteMap',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cen_route_map_with_options_async(
        self,
        request: main_models.DeleteCenRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCenRouteMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCenRouteMap',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCenRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cen_route_map(
        self,
        request: main_models.DeleteCenRouteMapRequest,
    ) -> main_models.DeleteCenRouteMapResponse:
        runtime = RuntimeOptions()
        return self.delete_cen_route_map_with_options(request, runtime)

    async def delete_cen_route_map_async(
        self,
        request: main_models.DeleteCenRouteMapRequest,
    ) -> main_models.DeleteCenRouteMapResponse:
        runtime = RuntimeOptions()
        return await self.delete_cen_route_map_with_options_async(request, runtime)

    def delete_flowlog_with_options(
        self,
        request: main_models.DeleteFlowlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowlogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowlog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowlogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flowlog_with_options_async(
        self,
        request: main_models.DeleteFlowlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFlowlogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFlowlog',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFlowlogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_flowlog(
        self,
        request: main_models.DeleteFlowlogRequest,
    ) -> main_models.DeleteFlowlogResponse:
        runtime = RuntimeOptions()
        return self.delete_flowlog_with_options(request, runtime)

    async def delete_flowlog_async(
        self,
        request: main_models.DeleteFlowlogRequest,
    ) -> main_models.DeleteFlowlogResponse:
        runtime = RuntimeOptions()
        return await self.delete_flowlog_with_options_async(request, runtime)

    def delete_route_service_in_cen_with_options(
        self,
        request: main_models.DeleteRouteServiceInCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteServiceInCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRouteServiceInCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteServiceInCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_service_in_cen_with_options_async(
        self,
        request: main_models.DeleteRouteServiceInCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRouteServiceInCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRouteServiceInCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRouteServiceInCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route_service_in_cen(
        self,
        request: main_models.DeleteRouteServiceInCenRequest,
    ) -> main_models.DeleteRouteServiceInCenResponse:
        runtime = RuntimeOptions()
        return self.delete_route_service_in_cen_with_options(request, runtime)

    async def delete_route_service_in_cen_async(
        self,
        request: main_models.DeleteRouteServiceInCenRequest,
    ) -> main_models.DeleteRouteServiceInCenResponse:
        runtime = RuntimeOptions()
        return await self.delete_route_service_in_cen_with_options_async(request, runtime)

    def delete_traffic_marking_policy_with_options(
        self,
        request: main_models.DeleteTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_marking_policy_with_options_async(
        self,
        request: main_models.DeleteTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_marking_policy(
        self,
        request: main_models.DeleteTrafficMarkingPolicyRequest,
    ) -> main_models.DeleteTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_traffic_marking_policy_with_options(request, runtime)

    async def delete_traffic_marking_policy_async(
        self,
        request: main_models.DeleteTrafficMarkingPolicyRequest,
    ) -> main_models.DeleteTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_traffic_marking_policy_with_options_async(request, runtime)

    def delete_transit_route_table_aggregation_with_options(
        self,
        request: main_models.DeleteTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouteTableAggregationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_route_table_aggregation_with_options_async(
        self,
        request: main_models.DeleteTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouteTableAggregationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouteTableAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_route_table_aggregation(
        self,
        request: main_models.DeleteTransitRouteTableAggregationRequest,
    ) -> main_models.DeleteTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_route_table_aggregation_with_options(request, runtime)

    async def delete_transit_route_table_aggregation_async(
        self,
        request: main_models.DeleteTransitRouteTableAggregationRequest,
    ) -> main_models.DeleteTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_route_table_aggregation_with_options_async(request, runtime)

    def delete_transit_router_with_options(
        self,
        request: main_models.DeleteTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_with_options_async(
        self,
        request: main_models.DeleteTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router(
        self,
        request: main_models.DeleteTransitRouterRequest,
    ) -> main_models.DeleteTransitRouterResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_with_options(request, runtime)

    async def delete_transit_router_async(
        self,
        request: main_models.DeleteTransitRouterRequest,
    ) -> main_models.DeleteTransitRouterResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_with_options_async(request, runtime)

    def delete_transit_router_cidr_with_options(
        self,
        request: main_models.DeleteTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_cidr_with_options_async(
        self,
        request: main_models.DeleteTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_cidr(
        self,
        request: main_models.DeleteTransitRouterCidrRequest,
    ) -> main_models.DeleteTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_cidr_with_options(request, runtime)

    async def delete_transit_router_cidr_async(
        self,
        request: main_models.DeleteTransitRouterCidrRequest,
    ) -> main_models.DeleteTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_cidr_with_options_async(request, runtime)

    def delete_transit_router_ecr_attachment_with_options(
        self,
        request: main_models.DeleteTransitRouterEcrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterEcrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterEcrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterEcrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_ecr_attachment_with_options_async(
        self,
        request: main_models.DeleteTransitRouterEcrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterEcrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterEcrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterEcrAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_ecr_attachment(
        self,
        request: main_models.DeleteTransitRouterEcrAttachmentRequest,
    ) -> main_models.DeleteTransitRouterEcrAttachmentResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_ecr_attachment_with_options(request, runtime)

    async def delete_transit_router_ecr_attachment_async(
        self,
        request: main_models.DeleteTransitRouterEcrAttachmentRequest,
    ) -> main_models.DeleteTransitRouterEcrAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_ecr_attachment_with_options_async(request, runtime)

    def delete_transit_router_multicast_domain_with_options(
        self,
        request: main_models.DeleteTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_multicast_domain_with_options_async(
        self,
        request: main_models.DeleteTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_multicast_domain(
        self,
        request: main_models.DeleteTransitRouterMulticastDomainRequest,
    ) -> main_models.DeleteTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_multicast_domain_with_options(request, runtime)

    async def delete_transit_router_multicast_domain_async(
        self,
        request: main_models.DeleteTransitRouterMulticastDomainRequest,
    ) -> main_models.DeleteTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_multicast_domain_with_options_async(request, runtime)

    def delete_transit_router_peer_attachment_with_options(
        self,
        request: main_models.DeleteTransitRouterPeerAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterPeerAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterPeerAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterPeerAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_peer_attachment_with_options_async(
        self,
        request: main_models.DeleteTransitRouterPeerAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterPeerAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterPeerAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterPeerAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_peer_attachment(
        self,
        request: main_models.DeleteTransitRouterPeerAttachmentRequest,
    ) -> main_models.DeleteTransitRouterPeerAttachmentResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_peer_attachment_with_options(request, runtime)

    async def delete_transit_router_peer_attachment_async(
        self,
        request: main_models.DeleteTransitRouterPeerAttachmentRequest,
    ) -> main_models.DeleteTransitRouterPeerAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_peer_attachment_with_options_async(request, runtime)

    def delete_transit_router_prefix_list_association_with_options(
        self,
        request: main_models.DeleteTransitRouterPrefixListAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterPrefixListAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterPrefixListAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_prefix_list_association_with_options_async(
        self,
        request: main_models.DeleteTransitRouterPrefixListAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterPrefixListAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterPrefixListAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterPrefixListAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_prefix_list_association(
        self,
        request: main_models.DeleteTransitRouterPrefixListAssociationRequest,
    ) -> main_models.DeleteTransitRouterPrefixListAssociationResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_prefix_list_association_with_options(request, runtime)

    async def delete_transit_router_prefix_list_association_async(
        self,
        request: main_models.DeleteTransitRouterPrefixListAssociationRequest,
    ) -> main_models.DeleteTransitRouterPrefixListAssociationResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_prefix_list_association_with_options_async(request, runtime)

    def delete_transit_router_route_entry_with_options(
        self,
        request: main_models.DeleteTransitRouterRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterRouteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not DaraCore.is_null(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterRouteEntry',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_route_entry_with_options_async(
        self,
        request: main_models.DeleteTransitRouterRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterRouteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not DaraCore.is_null(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterRouteEntry',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_route_entry(
        self,
        request: main_models.DeleteTransitRouterRouteEntryRequest,
    ) -> main_models.DeleteTransitRouterRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_route_entry_with_options(request, runtime)

    async def delete_transit_router_route_entry_async(
        self,
        request: main_models.DeleteTransitRouterRouteEntryRequest,
    ) -> main_models.DeleteTransitRouterRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_route_entry_with_options_async(request, runtime)

    def delete_transit_router_route_table_with_options(
        self,
        request: main_models.DeleteTransitRouterRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_route_table_with_options_async(
        self,
        request: main_models.DeleteTransitRouterRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_route_table(
        self,
        request: main_models.DeleteTransitRouterRouteTableRequest,
    ) -> main_models.DeleteTransitRouterRouteTableResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_route_table_with_options(request, runtime)

    async def delete_transit_router_route_table_async(
        self,
        request: main_models.DeleteTransitRouterRouteTableRequest,
    ) -> main_models.DeleteTransitRouterRouteTableResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_route_table_with_options_async(request, runtime)

    def delete_transit_router_vbr_attachment_with_options(
        self,
        request: main_models.DeleteTransitRouterVbrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterVbrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterVbrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterVbrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_vbr_attachment_with_options_async(
        self,
        request: main_models.DeleteTransitRouterVbrAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterVbrAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterVbrAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterVbrAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_vbr_attachment(
        self,
        request: main_models.DeleteTransitRouterVbrAttachmentRequest,
    ) -> main_models.DeleteTransitRouterVbrAttachmentResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_vbr_attachment_with_options(request, runtime)

    async def delete_transit_router_vbr_attachment_async(
        self,
        request: main_models.DeleteTransitRouterVbrAttachmentRequest,
    ) -> main_models.DeleteTransitRouterVbrAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_vbr_attachment_with_options_async(request, runtime)

    def delete_transit_router_vpc_attachment_with_options(
        self,
        request: main_models.DeleteTransitRouterVpcAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterVpcAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterVpcAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterVpcAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_vpc_attachment_with_options_async(
        self,
        request: main_models.DeleteTransitRouterVpcAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterVpcAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterVpcAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterVpcAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_vpc_attachment(
        self,
        request: main_models.DeleteTransitRouterVpcAttachmentRequest,
    ) -> main_models.DeleteTransitRouterVpcAttachmentResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_vpc_attachment_with_options(request, runtime)

    async def delete_transit_router_vpc_attachment_async(
        self,
        request: main_models.DeleteTransitRouterVpcAttachmentRequest,
    ) -> main_models.DeleteTransitRouterVpcAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_vpc_attachment_with_options_async(request, runtime)

    def delete_transit_router_vpn_attachment_with_options(
        self,
        request: main_models.DeleteTransitRouterVpnAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterVpnAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterVpnAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterVpnAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transit_router_vpn_attachment_with_options_async(
        self,
        request: main_models.DeleteTransitRouterVpnAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTransitRouterVpnAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTransitRouterVpnAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTransitRouterVpnAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transit_router_vpn_attachment(
        self,
        request: main_models.DeleteTransitRouterVpnAttachmentRequest,
    ) -> main_models.DeleteTransitRouterVpnAttachmentResponse:
        runtime = RuntimeOptions()
        return self.delete_transit_router_vpn_attachment_with_options(request, runtime)

    async def delete_transit_router_vpn_attachment_async(
        self,
        request: main_models.DeleteTransitRouterVpnAttachmentRequest,
    ) -> main_models.DeleteTransitRouterVpnAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_transit_router_vpn_attachment_with_options_async(request, runtime)

    def deregister_transit_router_multicast_group_members_with_options(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterTransitRouterMulticastGroupMembers',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterTransitRouterMulticastGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_transit_router_multicast_group_members_with_options_async(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterTransitRouterMulticastGroupMembers',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterTransitRouterMulticastGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_transit_router_multicast_group_members(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupMembersRequest,
    ) -> main_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        runtime = RuntimeOptions()
        return self.deregister_transit_router_multicast_group_members_with_options(request, runtime)

    async def deregister_transit_router_multicast_group_members_async(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupMembersRequest,
    ) -> main_models.DeregisterTransitRouterMulticastGroupMembersResponse:
        runtime = RuntimeOptions()
        return await self.deregister_transit_router_multicast_group_members_with_options_async(request, runtime)

    def deregister_transit_router_multicast_group_sources_with_options(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterTransitRouterMulticastGroupSources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterTransitRouterMulticastGroupSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_transit_router_multicast_group_sources_with_options_async(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterTransitRouterMulticastGroupSources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterTransitRouterMulticastGroupSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_transit_router_multicast_group_sources(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
    ) -> main_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        runtime = RuntimeOptions()
        return self.deregister_transit_router_multicast_group_sources_with_options(request, runtime)

    async def deregister_transit_router_multicast_group_sources_async(
        self,
        request: main_models.DeregisterTransitRouterMulticastGroupSourcesRequest,
    ) -> main_models.DeregisterTransitRouterMulticastGroupSourcesResponse:
        runtime = RuntimeOptions()
        return await self.deregister_transit_router_multicast_group_sources_with_options_async(request, runtime)

    def describe_cen_attached_child_instance_attribute_with_options(
        self,
        request: main_models.DescribeCenAttachedChildInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenAttachedChildInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenAttachedChildInstanceAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenAttachedChildInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_attached_child_instance_attribute_with_options_async(
        self,
        request: main_models.DescribeCenAttachedChildInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenAttachedChildInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenAttachedChildInstanceAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenAttachedChildInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_attached_child_instance_attribute(
        self,
        request: main_models.DescribeCenAttachedChildInstanceAttributeRequest,
    ) -> main_models.DescribeCenAttachedChildInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_attached_child_instance_attribute_with_options(request, runtime)

    async def describe_cen_attached_child_instance_attribute_async(
        self,
        request: main_models.DescribeCenAttachedChildInstanceAttributeRequest,
    ) -> main_models.DescribeCenAttachedChildInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_attached_child_instance_attribute_with_options_async(request, runtime)

    def describe_cen_attached_child_instances_with_options(
        self,
        request: main_models.DescribeCenAttachedChildInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenAttachedChildInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenAttachedChildInstances',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenAttachedChildInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_attached_child_instances_with_options_async(
        self,
        request: main_models.DescribeCenAttachedChildInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenAttachedChildInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenAttachedChildInstances',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenAttachedChildInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_attached_child_instances(
        self,
        request: main_models.DescribeCenAttachedChildInstancesRequest,
    ) -> main_models.DescribeCenAttachedChildInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_attached_child_instances_with_options(request, runtime)

    async def describe_cen_attached_child_instances_async(
        self,
        request: main_models.DescribeCenAttachedChildInstancesRequest,
    ) -> main_models.DescribeCenAttachedChildInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_attached_child_instances_with_options_async(request, runtime)

    def describe_cen_bandwidth_packages_with_options(
        self,
        request: main_models.DescribeCenBandwidthPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenBandwidthPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.include_reservation_data):
            query['IncludeReservationData'] = request.include_reservation_data
        if not DaraCore.is_null(request.is_or_key):
            query['IsOrKey'] = request.is_or_key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenBandwidthPackages',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenBandwidthPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_bandwidth_packages_with_options_async(
        self,
        request: main_models.DescribeCenBandwidthPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenBandwidthPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.include_reservation_data):
            query['IncludeReservationData'] = request.include_reservation_data
        if not DaraCore.is_null(request.is_or_key):
            query['IsOrKey'] = request.is_or_key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenBandwidthPackages',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenBandwidthPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_bandwidth_packages(
        self,
        request: main_models.DescribeCenBandwidthPackagesRequest,
    ) -> main_models.DescribeCenBandwidthPackagesResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_bandwidth_packages_with_options(request, runtime)

    async def describe_cen_bandwidth_packages_async(
        self,
        request: main_models.DescribeCenBandwidthPackagesRequest,
    ) -> main_models.DescribeCenBandwidthPackagesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_bandwidth_packages_with_options_async(request, runtime)

    def describe_cen_child_instance_route_entries_with_options(
        self,
        request: main_models.DescribeCenChildInstanceRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenChildInstanceRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenChildInstanceRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenChildInstanceRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_child_instance_route_entries_with_options_async(
        self,
        request: main_models.DescribeCenChildInstanceRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenChildInstanceRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenChildInstanceRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenChildInstanceRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_child_instance_route_entries(
        self,
        request: main_models.DescribeCenChildInstanceRouteEntriesRequest,
    ) -> main_models.DescribeCenChildInstanceRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_child_instance_route_entries_with_options(request, runtime)

    async def describe_cen_child_instance_route_entries_async(
        self,
        request: main_models.DescribeCenChildInstanceRouteEntriesRequest,
    ) -> main_models.DescribeCenChildInstanceRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_child_instance_route_entries_with_options_async(request, runtime)

    def describe_cen_geographic_span_remaining_bandwidth_with_options(
        self,
        request: main_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not DaraCore.is_null(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenGeographicSpanRemainingBandwidth',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenGeographicSpanRemainingBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_geographic_span_remaining_bandwidth_with_options_async(
        self,
        request: main_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not DaraCore.is_null(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenGeographicSpanRemainingBandwidth',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenGeographicSpanRemainingBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_geographic_span_remaining_bandwidth(
        self,
        request: main_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
    ) -> main_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_geographic_span_remaining_bandwidth_with_options(request, runtime)

    async def describe_cen_geographic_span_remaining_bandwidth_async(
        self,
        request: main_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
    ) -> main_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_geographic_span_remaining_bandwidth_with_options_async(request, runtime)

    def describe_cen_geographic_spans_with_options(
        self,
        request: main_models.DescribeCenGeographicSpansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenGeographicSpansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.geographic_span_id):
            query['GeographicSpanId'] = request.geographic_span_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenGeographicSpans',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenGeographicSpansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_geographic_spans_with_options_async(
        self,
        request: main_models.DescribeCenGeographicSpansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenGeographicSpansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.geographic_span_id):
            query['GeographicSpanId'] = request.geographic_span_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenGeographicSpans',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenGeographicSpansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_geographic_spans(
        self,
        request: main_models.DescribeCenGeographicSpansRequest,
    ) -> main_models.DescribeCenGeographicSpansResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_geographic_spans_with_options(request, runtime)

    async def describe_cen_geographic_spans_async(
        self,
        request: main_models.DescribeCenGeographicSpansRequest,
    ) -> main_models.DescribeCenGeographicSpansResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_geographic_spans_with_options_async(request, runtime)

    def describe_cen_inter_region_bandwidth_limits_with_options(
        self,
        request: main_models.DescribeCenInterRegionBandwidthLimitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenInterRegionBandwidthLimitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tr_region_id):
            query['TrRegionId'] = request.tr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenInterRegionBandwidthLimits',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenInterRegionBandwidthLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_inter_region_bandwidth_limits_with_options_async(
        self,
        request: main_models.DescribeCenInterRegionBandwidthLimitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenInterRegionBandwidthLimitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tr_region_id):
            query['TrRegionId'] = request.tr_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenInterRegionBandwidthLimits',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenInterRegionBandwidthLimitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_inter_region_bandwidth_limits(
        self,
        request: main_models.DescribeCenInterRegionBandwidthLimitsRequest,
    ) -> main_models.DescribeCenInterRegionBandwidthLimitsResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_inter_region_bandwidth_limits_with_options(request, runtime)

    async def describe_cen_inter_region_bandwidth_limits_async(
        self,
        request: main_models.DescribeCenInterRegionBandwidthLimitsRequest,
    ) -> main_models.DescribeCenInterRegionBandwidthLimitsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_inter_region_bandwidth_limits_with_options_async(request, runtime)

    def describe_cen_private_zone_routes_with_options(
        self,
        request: main_models.DescribeCenPrivateZoneRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenPrivateZoneRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenPrivateZoneRoutes',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenPrivateZoneRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_private_zone_routes_with_options_async(
        self,
        request: main_models.DescribeCenPrivateZoneRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenPrivateZoneRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenPrivateZoneRoutes',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenPrivateZoneRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_private_zone_routes(
        self,
        request: main_models.DescribeCenPrivateZoneRoutesRequest,
    ) -> main_models.DescribeCenPrivateZoneRoutesResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_private_zone_routes_with_options(request, runtime)

    async def describe_cen_private_zone_routes_async(
        self,
        request: main_models.DescribeCenPrivateZoneRoutesRequest,
    ) -> main_models.DescribeCenPrivateZoneRoutesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_private_zone_routes_with_options_async(request, runtime)

    def describe_cen_region_domain_route_entries_with_options(
        self,
        request: main_models.DescribeCenRegionDomainRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenRegionDomainRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenRegionDomainRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenRegionDomainRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_region_domain_route_entries_with_options_async(
        self,
        request: main_models.DescribeCenRegionDomainRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenRegionDomainRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenRegionDomainRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenRegionDomainRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_region_domain_route_entries(
        self,
        request: main_models.DescribeCenRegionDomainRouteEntriesRequest,
    ) -> main_models.DescribeCenRegionDomainRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_region_domain_route_entries_with_options(request, runtime)

    async def describe_cen_region_domain_route_entries_async(
        self,
        request: main_models.DescribeCenRegionDomainRouteEntriesRequest,
    ) -> main_models.DescribeCenRegionDomainRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_region_domain_route_entries_with_options_async(request, runtime)

    def describe_cen_route_maps_with_options(
        self,
        request: main_models.DescribeCenRouteMapsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenRouteMapsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not DaraCore.is_null(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenRouteMaps',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenRouteMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_route_maps_with_options_async(
        self,
        request: main_models.DescribeCenRouteMapsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenRouteMapsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not DaraCore.is_null(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenRouteMaps',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenRouteMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_route_maps(
        self,
        request: main_models.DescribeCenRouteMapsRequest,
    ) -> main_models.DescribeCenRouteMapsResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_route_maps_with_options(request, runtime)

    async def describe_cen_route_maps_async(
        self,
        request: main_models.DescribeCenRouteMapsRequest,
    ) -> main_models.DescribeCenRouteMapsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_route_maps_with_options_async(request, runtime)

    def describe_cen_vbr_health_check_with_options(
        self,
        request: main_models.DescribeCenVbrHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenVbrHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not DaraCore.is_null(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenVbrHealthCheck',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cen_vbr_health_check_with_options_async(
        self,
        request: main_models.DescribeCenVbrHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCenVbrHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not DaraCore.is_null(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCenVbrHealthCheck',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCenVbrHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cen_vbr_health_check(
        self,
        request: main_models.DescribeCenVbrHealthCheckRequest,
    ) -> main_models.DescribeCenVbrHealthCheckResponse:
        runtime = RuntimeOptions()
        return self.describe_cen_vbr_health_check_with_options(request, runtime)

    async def describe_cen_vbr_health_check_async(
        self,
        request: main_models.DescribeCenVbrHealthCheckRequest,
    ) -> main_models.DescribeCenVbrHealthCheckResponse:
        runtime = RuntimeOptions()
        return await self.describe_cen_vbr_health_check_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: main_models.DescribeCensRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCens',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: main_models.DescribeCensRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCens',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cens(
        self,
        request: main_models.DescribeCensRequest,
    ) -> main_models.DescribeCensResponse:
        runtime = RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: main_models.DescribeCensRequest,
    ) -> main_models.DescribeCensResponse:
        runtime = RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_child_instance_regions_with_options(
        self,
        request: main_models.DescribeChildInstanceRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChildInstanceRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChildInstanceRegions',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChildInstanceRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_child_instance_regions_with_options_async(
        self,
        request: main_models.DescribeChildInstanceRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeChildInstanceRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeChildInstanceRegions',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeChildInstanceRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_child_instance_regions(
        self,
        request: main_models.DescribeChildInstanceRegionsRequest,
    ) -> main_models.DescribeChildInstanceRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_child_instance_regions_with_options(request, runtime)

    async def describe_child_instance_regions_async(
        self,
        request: main_models.DescribeChildInstanceRegionsRequest,
    ) -> main_models.DescribeChildInstanceRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_child_instance_regions_with_options_async(request, runtime)

    def describe_flowlogs_with_options(
        self,
        request: main_models.DescribeFlowlogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowlogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.flow_log_version):
            query['FlowLogVersion'] = request.flow_log_version
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowlogs',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowlogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flowlogs_with_options_async(
        self,
        request: main_models.DescribeFlowlogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFlowlogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.flow_log_version):
            query['FlowLogVersion'] = request.flow_log_version
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFlowlogs',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFlowlogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flowlogs(
        self,
        request: main_models.DescribeFlowlogsRequest,
    ) -> main_models.DescribeFlowlogsResponse:
        runtime = RuntimeOptions()
        return self.describe_flowlogs_with_options(request, runtime)

    async def describe_flowlogs_async(
        self,
        request: main_models.DescribeFlowlogsRequest,
    ) -> main_models.DescribeFlowlogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_flowlogs_with_options_async(request, runtime)

    def describe_geographic_region_membership_with_options(
        self,
        request: main_models.DescribeGeographicRegionMembershipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGeographicRegionMembershipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.geographic_region_id):
            query['GeographicRegionId'] = request.geographic_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGeographicRegionMembership',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGeographicRegionMembershipResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_geographic_region_membership_with_options_async(
        self,
        request: main_models.DescribeGeographicRegionMembershipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGeographicRegionMembershipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.geographic_region_id):
            query['GeographicRegionId'] = request.geographic_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGeographicRegionMembership',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGeographicRegionMembershipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_geographic_region_membership(
        self,
        request: main_models.DescribeGeographicRegionMembershipRequest,
    ) -> main_models.DescribeGeographicRegionMembershipResponse:
        runtime = RuntimeOptions()
        return self.describe_geographic_region_membership_with_options(request, runtime)

    async def describe_geographic_region_membership_async(
        self,
        request: main_models.DescribeGeographicRegionMembershipRequest,
    ) -> main_models.DescribeGeographicRegionMembershipResponse:
        runtime = RuntimeOptions()
        return await self.describe_geographic_region_membership_with_options_async(request, runtime)

    def describe_grant_rules_to_cen_with_options(
        self,
        request: main_models.DescribeGrantRulesToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantRulesToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.enabled_ipv_6):
            query['EnabledIpv6'] = request.enabled_ipv_6
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantRulesToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantRulesToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_rules_to_cen_with_options_async(
        self,
        request: main_models.DescribeGrantRulesToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantRulesToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.enabled_ipv_6):
            query['EnabledIpv6'] = request.enabled_ipv_6
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantRulesToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantRulesToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grant_rules_to_cen(
        self,
        request: main_models.DescribeGrantRulesToCenRequest,
    ) -> main_models.DescribeGrantRulesToCenResponse:
        runtime = RuntimeOptions()
        return self.describe_grant_rules_to_cen_with_options(request, runtime)

    async def describe_grant_rules_to_cen_async(
        self,
        request: main_models.DescribeGrantRulesToCenRequest,
    ) -> main_models.DescribeGrantRulesToCenResponse:
        runtime = RuntimeOptions()
        return await self.describe_grant_rules_to_cen_with_options_async(request, runtime)

    def describe_grant_rules_to_resource_with_options(
        self,
        request: main_models.DescribeGrantRulesToResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantRulesToResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantRulesToResource',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantRulesToResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grant_rules_to_resource_with_options_async(
        self,
        request: main_models.DescribeGrantRulesToResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGrantRulesToResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGrantRulesToResource',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGrantRulesToResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grant_rules_to_resource(
        self,
        request: main_models.DescribeGrantRulesToResourceRequest,
    ) -> main_models.DescribeGrantRulesToResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_grant_rules_to_resource_with_options(request, runtime)

    async def describe_grant_rules_to_resource_async(
        self,
        request: main_models.DescribeGrantRulesToResourceRequest,
    ) -> main_models.DescribeGrantRulesToResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_grant_rules_to_resource_with_options_async(request, runtime)

    def describe_published_route_entries_with_options(
        self,
        request: main_models.DescribePublishedRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePublishedRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePublishedRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePublishedRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_published_route_entries_with_options_async(
        self,
        request: main_models.DescribePublishedRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePublishedRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePublishedRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePublishedRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_published_route_entries(
        self,
        request: main_models.DescribePublishedRouteEntriesRequest,
    ) -> main_models.DescribePublishedRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.describe_published_route_entries_with_options(request, runtime)

    async def describe_published_route_entries_async(
        self,
        request: main_models.DescribePublishedRouteEntriesRequest,
    ) -> main_models.DescribePublishedRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_published_route_entries_with_options_async(request, runtime)

    def describe_route_conflict_with_options(
        self,
        request: main_models.DescribeRouteConflictRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRouteConflictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRouteConflict',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRouteConflictResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_route_conflict_with_options_async(
        self,
        request: main_models.DescribeRouteConflictRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRouteConflictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRouteConflict',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRouteConflictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_route_conflict(
        self,
        request: main_models.DescribeRouteConflictRequest,
    ) -> main_models.DescribeRouteConflictResponse:
        runtime = RuntimeOptions()
        return self.describe_route_conflict_with_options(request, runtime)

    async def describe_route_conflict_async(
        self,
        request: main_models.DescribeRouteConflictRequest,
    ) -> main_models.DescribeRouteConflictResponse:
        runtime = RuntimeOptions()
        return await self.describe_route_conflict_with_options_async(request, runtime)

    def describe_route_services_in_cen_with_options(
        self,
        request: main_models.DescribeRouteServicesInCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRouteServicesInCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRouteServicesInCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRouteServicesInCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_route_services_in_cen_with_options_async(
        self,
        request: main_models.DescribeRouteServicesInCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRouteServicesInCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRouteServicesInCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRouteServicesInCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_route_services_in_cen(
        self,
        request: main_models.DescribeRouteServicesInCenRequest,
    ) -> main_models.DescribeRouteServicesInCenResponse:
        runtime = RuntimeOptions()
        return self.describe_route_services_in_cen_with_options(request, runtime)

    async def describe_route_services_in_cen_async(
        self,
        request: main_models.DescribeRouteServicesInCenRequest,
    ) -> main_models.DescribeRouteServicesInCenResponse:
        runtime = RuntimeOptions()
        return await self.describe_route_services_in_cen_with_options_async(request, runtime)

    def describe_transit_route_table_aggregation_with_options(
        self,
        request: main_models.DescribeTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransitRouteTableAggregationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transit_route_table_aggregation_with_options_async(
        self,
        request: main_models.DescribeTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransitRouteTableAggregationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransitRouteTableAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transit_route_table_aggregation(
        self,
        request: main_models.DescribeTransitRouteTableAggregationRequest,
    ) -> main_models.DescribeTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return self.describe_transit_route_table_aggregation_with_options(request, runtime)

    async def describe_transit_route_table_aggregation_async(
        self,
        request: main_models.DescribeTransitRouteTableAggregationRequest,
    ) -> main_models.DescribeTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return await self.describe_transit_route_table_aggregation_with_options_async(request, runtime)

    def describe_transit_route_table_aggregation_detail_with_options(
        self,
        request: main_models.DescribeTransitRouteTableAggregationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransitRouteTableAggregationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransitRouteTableAggregationDetail',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransitRouteTableAggregationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transit_route_table_aggregation_detail_with_options_async(
        self,
        request: main_models.DescribeTransitRouteTableAggregationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransitRouteTableAggregationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransitRouteTableAggregationDetail',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransitRouteTableAggregationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transit_route_table_aggregation_detail(
        self,
        request: main_models.DescribeTransitRouteTableAggregationDetailRequest,
    ) -> main_models.DescribeTransitRouteTableAggregationDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_transit_route_table_aggregation_detail_with_options(request, runtime)

    async def describe_transit_route_table_aggregation_detail_async(
        self,
        request: main_models.DescribeTransitRouteTableAggregationDetailRequest,
    ) -> main_models.DescribeTransitRouteTableAggregationDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_transit_route_table_aggregation_detail_with_options_async(request, runtime)

    def detach_cen_child_instance_with_options(
        self,
        request: main_models.DetachCenChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachCenChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachCenChildInstance',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachCenChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_cen_child_instance_with_options_async(
        self,
        request: main_models.DetachCenChildInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachCenChildInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachCenChildInstance',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachCenChildInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_cen_child_instance(
        self,
        request: main_models.DetachCenChildInstanceRequest,
    ) -> main_models.DetachCenChildInstanceResponse:
        runtime = RuntimeOptions()
        return self.detach_cen_child_instance_with_options(request, runtime)

    async def detach_cen_child_instance_async(
        self,
        request: main_models.DetachCenChildInstanceRequest,
    ) -> main_models.DetachCenChildInstanceResponse:
        runtime = RuntimeOptions()
        return await self.detach_cen_child_instance_with_options_async(request, runtime)

    def disable_cen_vbr_health_check_with_options(
        self,
        request: main_models.DisableCenVbrHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableCenVbrHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not DaraCore.is_null(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableCenVbrHealthCheck',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_cen_vbr_health_check_with_options_async(
        self,
        request: main_models.DisableCenVbrHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableCenVbrHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not DaraCore.is_null(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableCenVbrHealthCheck',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCenVbrHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_cen_vbr_health_check(
        self,
        request: main_models.DisableCenVbrHealthCheckRequest,
    ) -> main_models.DisableCenVbrHealthCheckResponse:
        runtime = RuntimeOptions()
        return self.disable_cen_vbr_health_check_with_options(request, runtime)

    async def disable_cen_vbr_health_check_async(
        self,
        request: main_models.DisableCenVbrHealthCheckRequest,
    ) -> main_models.DisableCenVbrHealthCheckResponse:
        runtime = RuntimeOptions()
        return await self.disable_cen_vbr_health_check_with_options_async(request, runtime)

    def disable_transit_router_route_table_propagation_with_options(
        self,
        request: main_models.DisableTransitRouterRouteTablePropagationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableTransitRouterRouteTablePropagationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableTransitRouterRouteTablePropagation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableTransitRouterRouteTablePropagationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_transit_router_route_table_propagation_with_options_async(
        self,
        request: main_models.DisableTransitRouterRouteTablePropagationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableTransitRouterRouteTablePropagationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableTransitRouterRouteTablePropagation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableTransitRouterRouteTablePropagationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_transit_router_route_table_propagation(
        self,
        request: main_models.DisableTransitRouterRouteTablePropagationRequest,
    ) -> main_models.DisableTransitRouterRouteTablePropagationResponse:
        runtime = RuntimeOptions()
        return self.disable_transit_router_route_table_propagation_with_options(request, runtime)

    async def disable_transit_router_route_table_propagation_async(
        self,
        request: main_models.DisableTransitRouterRouteTablePropagationRequest,
    ) -> main_models.DisableTransitRouterRouteTablePropagationResponse:
        runtime = RuntimeOptions()
        return await self.disable_transit_router_route_table_propagation_with_options_async(request, runtime)

    def disassociate_transit_router_multicast_domain_with_options(
        self,
        request: main_models.DisassociateTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_transit_router_multicast_domain_with_options_async(
        self,
        request: main_models.DisassociateTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_transit_router_multicast_domain(
        self,
        request: main_models.DisassociateTransitRouterMulticastDomainRequest,
    ) -> main_models.DisassociateTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return self.disassociate_transit_router_multicast_domain_with_options(request, runtime)

    async def disassociate_transit_router_multicast_domain_async(
        self,
        request: main_models.DisassociateTransitRouterMulticastDomainRequest,
    ) -> main_models.DisassociateTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_transit_router_multicast_domain_with_options_async(request, runtime)

    def dissociate_transit_router_attachment_from_route_table_with_options(
        self,
        request: main_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateTransitRouterAttachmentFromRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateTransitRouterAttachmentFromRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_transit_router_attachment_from_route_table_with_options_async(
        self,
        request: main_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateTransitRouterAttachmentFromRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateTransitRouterAttachmentFromRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_transit_router_attachment_from_route_table(
        self,
        request: main_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
    ) -> main_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        runtime = RuntimeOptions()
        return self.dissociate_transit_router_attachment_from_route_table_with_options(request, runtime)

    async def dissociate_transit_router_attachment_from_route_table_async(
        self,
        request: main_models.DissociateTransitRouterAttachmentFromRouteTableRequest,
    ) -> main_models.DissociateTransitRouterAttachmentFromRouteTableResponse:
        runtime = RuntimeOptions()
        return await self.dissociate_transit_router_attachment_from_route_table_with_options_async(request, runtime)

    def enable_cen_vbr_health_check_with_options(
        self,
        request: main_models.EnableCenVbrHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCenVbrHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_only):
            query['HealthCheckOnly'] = request.health_check_only
        if not DaraCore.is_null(request.health_check_source_ip):
            query['HealthCheckSourceIp'] = request.health_check_source_ip
        if not DaraCore.is_null(request.health_check_target_ip):
            query['HealthCheckTargetIp'] = request.health_check_target_ip
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not DaraCore.is_null(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCenVbrHealthCheck',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_cen_vbr_health_check_with_options_async(
        self,
        request: main_models.EnableCenVbrHealthCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCenVbrHealthCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_only):
            query['HealthCheckOnly'] = request.health_check_only
        if not DaraCore.is_null(request.health_check_source_ip):
            query['HealthCheckSourceIp'] = request.health_check_source_ip
        if not DaraCore.is_null(request.health_check_target_ip):
            query['HealthCheckTargetIp'] = request.health_check_target_ip
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not DaraCore.is_null(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not DaraCore.is_null(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCenVbrHealthCheck',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCenVbrHealthCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_cen_vbr_health_check(
        self,
        request: main_models.EnableCenVbrHealthCheckRequest,
    ) -> main_models.EnableCenVbrHealthCheckResponse:
        runtime = RuntimeOptions()
        return self.enable_cen_vbr_health_check_with_options(request, runtime)

    async def enable_cen_vbr_health_check_async(
        self,
        request: main_models.EnableCenVbrHealthCheckRequest,
    ) -> main_models.EnableCenVbrHealthCheckResponse:
        runtime = RuntimeOptions()
        return await self.enable_cen_vbr_health_check_with_options_async(request, runtime)

    def enable_transit_router_route_table_propagation_with_options(
        self,
        request: main_models.EnableTransitRouterRouteTablePropagationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableTransitRouterRouteTablePropagationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableTransitRouterRouteTablePropagation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableTransitRouterRouteTablePropagationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_transit_router_route_table_propagation_with_options_async(
        self,
        request: main_models.EnableTransitRouterRouteTablePropagationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableTransitRouterRouteTablePropagationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableTransitRouterRouteTablePropagation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableTransitRouterRouteTablePropagationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_transit_router_route_table_propagation(
        self,
        request: main_models.EnableTransitRouterRouteTablePropagationRequest,
    ) -> main_models.EnableTransitRouterRouteTablePropagationResponse:
        runtime = RuntimeOptions()
        return self.enable_transit_router_route_table_propagation_with_options(request, runtime)

    async def enable_transit_router_route_table_propagation_async(
        self,
        request: main_models.EnableTransitRouterRouteTablePropagationRequest,
    ) -> main_models.EnableTransitRouterRouteTablePropagationResponse:
        runtime = RuntimeOptions()
        return await self.enable_transit_router_route_table_propagation_with_options_async(request, runtime)

    def grant_instance_to_transit_router_with_options(
        self,
        request: main_models.GrantInstanceToTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantInstanceToTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantInstanceToTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantInstanceToTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_instance_to_transit_router_with_options_async(
        self,
        request: main_models.GrantInstanceToTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantInstanceToTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantInstanceToTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantInstanceToTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_instance_to_transit_router(
        self,
        request: main_models.GrantInstanceToTransitRouterRequest,
    ) -> main_models.GrantInstanceToTransitRouterResponse:
        runtime = RuntimeOptions()
        return self.grant_instance_to_transit_router_with_options(request, runtime)

    async def grant_instance_to_transit_router_async(
        self,
        request: main_models.GrantInstanceToTransitRouterRequest,
    ) -> main_models.GrantInstanceToTransitRouterResponse:
        runtime = RuntimeOptions()
        return await self.grant_instance_to_transit_router_with_options_async(request, runtime)

    def list_cen_child_instance_route_entries_to_attachment_with_options(
        self,
        request: main_models.ListCenChildInstanceRouteEntriesToAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCenChildInstanceRouteEntriesToAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_filter):
            query['RouteFilter'] = request.route_filter
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCenChildInstanceRouteEntriesToAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCenChildInstanceRouteEntriesToAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cen_child_instance_route_entries_to_attachment_with_options_async(
        self,
        request: main_models.ListCenChildInstanceRouteEntriesToAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCenChildInstanceRouteEntriesToAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_filter):
            query['RouteFilter'] = request.route_filter
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCenChildInstanceRouteEntriesToAttachment',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCenChildInstanceRouteEntriesToAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cen_child_instance_route_entries_to_attachment(
        self,
        request: main_models.ListCenChildInstanceRouteEntriesToAttachmentRequest,
    ) -> main_models.ListCenChildInstanceRouteEntriesToAttachmentResponse:
        runtime = RuntimeOptions()
        return self.list_cen_child_instance_route_entries_to_attachment_with_options(request, runtime)

    async def list_cen_child_instance_route_entries_to_attachment_async(
        self,
        request: main_models.ListCenChildInstanceRouteEntriesToAttachmentRequest,
    ) -> main_models.ListCenChildInstanceRouteEntriesToAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.list_cen_child_instance_route_entries_to_attachment_with_options_async(request, runtime)

    def list_cen_inter_region_traffic_qos_policies_with_options(
        self,
        request: main_models.ListCenInterRegionTrafficQosPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCenInterRegionTrafficQosPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not DaraCore.is_null(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCenInterRegionTrafficQosPolicies',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCenInterRegionTrafficQosPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cen_inter_region_traffic_qos_policies_with_options_async(
        self,
        request: main_models.ListCenInterRegionTrafficQosPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCenInterRegionTrafficQosPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not DaraCore.is_null(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCenInterRegionTrafficQosPolicies',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCenInterRegionTrafficQosPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cen_inter_region_traffic_qos_policies(
        self,
        request: main_models.ListCenInterRegionTrafficQosPoliciesRequest,
    ) -> main_models.ListCenInterRegionTrafficQosPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_cen_inter_region_traffic_qos_policies_with_options(request, runtime)

    async def list_cen_inter_region_traffic_qos_policies_async(
        self,
        request: main_models.ListCenInterRegionTrafficQosPoliciesRequest,
    ) -> main_models.ListCenInterRegionTrafficQosPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_cen_inter_region_traffic_qos_policies_with_options_async(request, runtime)

    def list_cen_inter_region_traffic_qos_queues_with_options(
        self,
        request: main_models.ListCenInterRegionTrafficQosQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCenInterRegionTrafficQosQueuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_bandwidth_filter):
            query['EffectiveBandwidthFilter'] = request.effective_bandwidth_filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not DaraCore.is_null(request.traffic_qos_queue_description):
            query['TrafficQosQueueDescription'] = request.traffic_qos_queue_description
        if not DaraCore.is_null(request.traffic_qos_queue_id):
            query['TrafficQosQueueId'] = request.traffic_qos_queue_id
        if not DaraCore.is_null(request.traffic_qos_queue_name):
            query['TrafficQosQueueName'] = request.traffic_qos_queue_name
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCenInterRegionTrafficQosQueues',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCenInterRegionTrafficQosQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cen_inter_region_traffic_qos_queues_with_options_async(
        self,
        request: main_models.ListCenInterRegionTrafficQosQueuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCenInterRegionTrafficQosQueuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_bandwidth_filter):
            query['EffectiveBandwidthFilter'] = request.effective_bandwidth_filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not DaraCore.is_null(request.traffic_qos_queue_description):
            query['TrafficQosQueueDescription'] = request.traffic_qos_queue_description
        if not DaraCore.is_null(request.traffic_qos_queue_id):
            query['TrafficQosQueueId'] = request.traffic_qos_queue_id
        if not DaraCore.is_null(request.traffic_qos_queue_name):
            query['TrafficQosQueueName'] = request.traffic_qos_queue_name
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCenInterRegionTrafficQosQueues',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCenInterRegionTrafficQosQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cen_inter_region_traffic_qos_queues(
        self,
        request: main_models.ListCenInterRegionTrafficQosQueuesRequest,
    ) -> main_models.ListCenInterRegionTrafficQosQueuesResponse:
        runtime = RuntimeOptions()
        return self.list_cen_inter_region_traffic_qos_queues_with_options(request, runtime)

    async def list_cen_inter_region_traffic_qos_queues_async(
        self,
        request: main_models.ListCenInterRegionTrafficQosQueuesRequest,
    ) -> main_models.ListCenInterRegionTrafficQosQueuesResponse:
        runtime = RuntimeOptions()
        return await self.list_cen_inter_region_traffic_qos_queues_with_options_async(request, runtime)

    def list_grant_vswitch_enis_with_options(
        self,
        request: main_models.ListGrantVSwitchEnisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGrantVSwitchEnisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.network_interface_name):
            query['NetworkInterfaceName'] = request.network_interface_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.primary_ip_address):
            query['PrimaryIpAddress'] = request.primary_ip_address
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrantVSwitchEnis',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrantVSwitchEnisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grant_vswitch_enis_with_options_async(
        self,
        request: main_models.ListGrantVSwitchEnisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGrantVSwitchEnisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not DaraCore.is_null(request.network_interface_name):
            query['NetworkInterfaceName'] = request.network_interface_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.primary_ip_address):
            query['PrimaryIpAddress'] = request.primary_ip_address
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrantVSwitchEnis',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrantVSwitchEnisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grant_vswitch_enis(
        self,
        request: main_models.ListGrantVSwitchEnisRequest,
    ) -> main_models.ListGrantVSwitchEnisResponse:
        runtime = RuntimeOptions()
        return self.list_grant_vswitch_enis_with_options(request, runtime)

    async def list_grant_vswitch_enis_async(
        self,
        request: main_models.ListGrantVSwitchEnisRequest,
    ) -> main_models.ListGrantVSwitchEnisResponse:
        runtime = RuntimeOptions()
        return await self.list_grant_vswitch_enis_with_options_async(request, runtime)

    def list_grant_vswitches_to_cen_with_options(
        self,
        request: main_models.ListGrantVSwitchesToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGrantVSwitchesToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.enabled_ipv_6):
            query['EnabledIpv6'] = request.enabled_ipv_6
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrantVSwitchesToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrantVSwitchesToCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grant_vswitches_to_cen_with_options_async(
        self,
        request: main_models.ListGrantVSwitchesToCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGrantVSwitchesToCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.enabled_ipv_6):
            query['EnabledIpv6'] = request.enabled_ipv_6
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrantVSwitchesToCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrantVSwitchesToCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grant_vswitches_to_cen(
        self,
        request: main_models.ListGrantVSwitchesToCenRequest,
    ) -> main_models.ListGrantVSwitchesToCenResponse:
        runtime = RuntimeOptions()
        return self.list_grant_vswitches_to_cen_with_options(request, runtime)

    async def list_grant_vswitches_to_cen_async(
        self,
        request: main_models.ListGrantVSwitchesToCenRequest,
    ) -> main_models.ListGrantVSwitchesToCenResponse:
        runtime = RuntimeOptions()
        return await self.list_grant_vswitches_to_cen_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_traffic_marking_policies_with_options(
        self,
        request: main_models.ListTrafficMarkingPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficMarkingPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficMarkingPolicies',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficMarkingPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_marking_policies_with_options_async(
        self,
        request: main_models.ListTrafficMarkingPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficMarkingPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficMarkingPolicies',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficMarkingPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_marking_policies(
        self,
        request: main_models.ListTrafficMarkingPoliciesRequest,
    ) -> main_models.ListTrafficMarkingPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_traffic_marking_policies_with_options(request, runtime)

    async def list_traffic_marking_policies_async(
        self,
        request: main_models.ListTrafficMarkingPoliciesRequest,
    ) -> main_models.ListTrafficMarkingPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_traffic_marking_policies_with_options_async(request, runtime)

    def list_transit_router_available_resource_with_options(
        self,
        request: main_models.ListTransitRouterAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterAvailableResource',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_available_resource_with_options_async(
        self,
        request: main_models.ListTransitRouterAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterAvailableResource',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_available_resource(
        self,
        request: main_models.ListTransitRouterAvailableResourceRequest,
    ) -> main_models.ListTransitRouterAvailableResourceResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_available_resource_with_options(request, runtime)

    async def list_transit_router_available_resource_async(
        self,
        request: main_models.ListTransitRouterAvailableResourceRequest,
    ) -> main_models.ListTransitRouterAvailableResourceResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_available_resource_with_options_async(request, runtime)

    def list_transit_router_cidr_with_options(
        self,
        request: main_models.ListTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_cidr_with_options_async(
        self,
        request: main_models.ListTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_cidr(
        self,
        request: main_models.ListTransitRouterCidrRequest,
    ) -> main_models.ListTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_cidr_with_options(request, runtime)

    async def list_transit_router_cidr_async(
        self,
        request: main_models.ListTransitRouterCidrRequest,
    ) -> main_models.ListTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_cidr_with_options_async(request, runtime)

    def list_transit_router_cidr_allocation_with_options(
        self,
        request: main_models.ListTransitRouterCidrAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterCidrAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not DaraCore.is_null(request.attachment_name):
            query['AttachmentName'] = request.attachment_name
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_owner_id):
            query['DedicatedOwnerId'] = request.dedicated_owner_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterCidrAllocation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterCidrAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_cidr_allocation_with_options_async(
        self,
        request: main_models.ListTransitRouterCidrAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterCidrAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not DaraCore.is_null(request.attachment_name):
            query['AttachmentName'] = request.attachment_name
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedicated_owner_id):
            query['DedicatedOwnerId'] = request.dedicated_owner_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterCidrAllocation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterCidrAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_cidr_allocation(
        self,
        request: main_models.ListTransitRouterCidrAllocationRequest,
    ) -> main_models.ListTransitRouterCidrAllocationResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_cidr_allocation_with_options(request, runtime)

    async def list_transit_router_cidr_allocation_async(
        self,
        request: main_models.ListTransitRouterCidrAllocationRequest,
    ) -> main_models.ListTransitRouterCidrAllocationResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_cidr_allocation_with_options_async(request, runtime)

    def list_transit_router_ecr_attachments_with_options(
        self,
        request: main_models.ListTransitRouterEcrAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterEcrAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterEcrAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterEcrAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_ecr_attachments_with_options_async(
        self,
        request: main_models.ListTransitRouterEcrAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterEcrAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterEcrAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterEcrAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_ecr_attachments(
        self,
        request: main_models.ListTransitRouterEcrAttachmentsRequest,
    ) -> main_models.ListTransitRouterEcrAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_ecr_attachments_with_options(request, runtime)

    async def list_transit_router_ecr_attachments_async(
        self,
        request: main_models.ListTransitRouterEcrAttachmentsRequest,
    ) -> main_models.ListTransitRouterEcrAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_ecr_attachments_with_options_async(request, runtime)

    def list_transit_router_multicast_domain_associations_with_options(
        self,
        request: main_models.ListTransitRouterMulticastDomainAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastDomainAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastDomainAssociations',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastDomainAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_domain_associations_with_options_async(
        self,
        request: main_models.ListTransitRouterMulticastDomainAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastDomainAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastDomainAssociations',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastDomainAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_domain_associations(
        self,
        request: main_models.ListTransitRouterMulticastDomainAssociationsRequest,
    ) -> main_models.ListTransitRouterMulticastDomainAssociationsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_multicast_domain_associations_with_options(request, runtime)

    async def list_transit_router_multicast_domain_associations_async(
        self,
        request: main_models.ListTransitRouterMulticastDomainAssociationsRequest,
    ) -> main_models.ListTransitRouterMulticastDomainAssociationsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_multicast_domain_associations_with_options_async(request, runtime)

    def list_transit_router_multicast_domain_vswitches_with_options(
        self,
        request: main_models.ListTransitRouterMulticastDomainVSwitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastDomainVSwitches',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastDomainVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_domain_vswitches_with_options_async(
        self,
        request: main_models.ListTransitRouterMulticastDomainVSwitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastDomainVSwitches',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastDomainVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_domain_vswitches(
        self,
        request: main_models.ListTransitRouterMulticastDomainVSwitchesRequest,
    ) -> main_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_multicast_domain_vswitches_with_options(request, runtime)

    async def list_transit_router_multicast_domain_vswitches_async(
        self,
        request: main_models.ListTransitRouterMulticastDomainVSwitchesRequest,
    ) -> main_models.ListTransitRouterMulticastDomainVSwitchesResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_multicast_domain_vswitches_with_options_async(request, runtime)

    def list_transit_router_multicast_domains_with_options(
        self,
        request: main_models.ListTransitRouterMulticastDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastDomains',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_domains_with_options_async(
        self,
        request: main_models.ListTransitRouterMulticastDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastDomains',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_domains(
        self,
        request: main_models.ListTransitRouterMulticastDomainsRequest,
    ) -> main_models.ListTransitRouterMulticastDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_multicast_domains_with_options(request, runtime)

    async def list_transit_router_multicast_domains_async(
        self,
        request: main_models.ListTransitRouterMulticastDomainsRequest,
    ) -> main_models.ListTransitRouterMulticastDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_multicast_domains_with_options_async(request, runtime)

    def list_transit_router_multicast_groups_with_options(
        self,
        request: main_models.ListTransitRouterMulticastGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.is_group_member):
            query['IsGroupMember'] = request.is_group_member
        if not DaraCore.is_null(request.is_group_source):
            query['IsGroupSource'] = request.is_group_source
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastGroups',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_multicast_groups_with_options_async(
        self,
        request: main_models.ListTransitRouterMulticastGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterMulticastGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.is_group_member):
            query['IsGroupMember'] = request.is_group_member
        if not DaraCore.is_null(request.is_group_source):
            query['IsGroupSource'] = request.is_group_source
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterMulticastGroups',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterMulticastGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_multicast_groups(
        self,
        request: main_models.ListTransitRouterMulticastGroupsRequest,
    ) -> main_models.ListTransitRouterMulticastGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_multicast_groups_with_options(request, runtime)

    async def list_transit_router_multicast_groups_async(
        self,
        request: main_models.ListTransitRouterMulticastGroupsRequest,
    ) -> main_models.ListTransitRouterMulticastGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_multicast_groups_with_options_async(request, runtime)

    def list_transit_router_peer_attachments_with_options(
        self,
        request: main_models.ListTransitRouterPeerAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterPeerAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterPeerAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterPeerAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_peer_attachments_with_options_async(
        self,
        request: main_models.ListTransitRouterPeerAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterPeerAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterPeerAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterPeerAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_peer_attachments(
        self,
        request: main_models.ListTransitRouterPeerAttachmentsRequest,
    ) -> main_models.ListTransitRouterPeerAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_peer_attachments_with_options(request, runtime)

    async def list_transit_router_peer_attachments_async(
        self,
        request: main_models.ListTransitRouterPeerAttachmentsRequest,
    ) -> main_models.ListTransitRouterPeerAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_peer_attachments_with_options_async(request, runtime)

    def list_transit_router_prefix_list_association_with_options(
        self,
        request: main_models.ListTransitRouterPrefixListAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterPrefixListAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.next_hop_instance_id):
            query['NextHopInstanceId'] = request.next_hop_instance_id
        if not DaraCore.is_null(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterPrefixListAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_prefix_list_association_with_options_async(
        self,
        request: main_models.ListTransitRouterPrefixListAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterPrefixListAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_hop):
            query['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.next_hop_instance_id):
            query['NextHopInstanceId'] = request.next_hop_instance_id
        if not DaraCore.is_null(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterPrefixListAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterPrefixListAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_prefix_list_association(
        self,
        request: main_models.ListTransitRouterPrefixListAssociationRequest,
    ) -> main_models.ListTransitRouterPrefixListAssociationResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_prefix_list_association_with_options(request, runtime)

    async def list_transit_router_prefix_list_association_async(
        self,
        request: main_models.ListTransitRouterPrefixListAssociationRequest,
    ) -> main_models.ListTransitRouterPrefixListAssociationResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_prefix_list_association_with_options_async(request, runtime)

    def list_transit_router_route_entries_with_options(
        self,
        request: main_models.ListTransitRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_filter):
            query['RouteFilter'] = request.route_filter
        if not DaraCore.is_null(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not DaraCore.is_null(request.transit_router_route_entry_ids):
            query['TransitRouterRouteEntryIds'] = request.transit_router_route_entry_ids
        if not DaraCore.is_null(request.transit_router_route_entry_names):
            query['TransitRouterRouteEntryNames'] = request.transit_router_route_entry_names
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_resource_id):
            query['TransitRouterRouteEntryNextHopResourceId'] = request.transit_router_route_entry_next_hop_resource_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_resource_type):
            query['TransitRouterRouteEntryNextHopResourceType'] = request.transit_router_route_entry_next_hop_resource_type
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not DaraCore.is_null(request.transit_router_route_entry_origin_resource_id):
            query['TransitRouterRouteEntryOriginResourceId'] = request.transit_router_route_entry_origin_resource_id
        if not DaraCore.is_null(request.transit_router_route_entry_origin_resource_type):
            query['TransitRouterRouteEntryOriginResourceType'] = request.transit_router_route_entry_origin_resource_type
        if not DaraCore.is_null(request.transit_router_route_entry_status):
            query['TransitRouterRouteEntryStatus'] = request.transit_router_route_entry_status
        if not DaraCore.is_null(request.transit_router_route_entry_type):
            query['TransitRouterRouteEntryType'] = request.transit_router_route_entry_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_entries_with_options_async(
        self,
        request: main_models.ListTransitRouterRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_filter):
            query['RouteFilter'] = request.route_filter
        if not DaraCore.is_null(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not DaraCore.is_null(request.transit_router_route_entry_ids):
            query['TransitRouterRouteEntryIds'] = request.transit_router_route_entry_ids
        if not DaraCore.is_null(request.transit_router_route_entry_names):
            query['TransitRouterRouteEntryNames'] = request.transit_router_route_entry_names
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_resource_id):
            query['TransitRouterRouteEntryNextHopResourceId'] = request.transit_router_route_entry_next_hop_resource_id
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_resource_type):
            query['TransitRouterRouteEntryNextHopResourceType'] = request.transit_router_route_entry_next_hop_resource_type
        if not DaraCore.is_null(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not DaraCore.is_null(request.transit_router_route_entry_origin_resource_id):
            query['TransitRouterRouteEntryOriginResourceId'] = request.transit_router_route_entry_origin_resource_id
        if not DaraCore.is_null(request.transit_router_route_entry_origin_resource_type):
            query['TransitRouterRouteEntryOriginResourceType'] = request.transit_router_route_entry_origin_resource_type
        if not DaraCore.is_null(request.transit_router_route_entry_status):
            query['TransitRouterRouteEntryStatus'] = request.transit_router_route_entry_status
        if not DaraCore.is_null(request.transit_router_route_entry_type):
            query['TransitRouterRouteEntryType'] = request.transit_router_route_entry_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_entries(
        self,
        request: main_models.ListTransitRouterRouteEntriesRequest,
    ) -> main_models.ListTransitRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_route_entries_with_options(request, runtime)

    async def list_transit_router_route_entries_async(
        self,
        request: main_models.ListTransitRouterRouteEntriesRequest,
    ) -> main_models.ListTransitRouterRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_route_entries_with_options_async(request, runtime)

    def list_transit_router_route_table_associations_with_options(
        self,
        request: main_models.ListTransitRouterRouteTableAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteTableAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_id):
            query['TransitRouterAttachmentResourceId'] = request.transit_router_attachment_resource_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_type):
            query['TransitRouterAttachmentResourceType'] = request.transit_router_attachment_resource_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteTableAssociations',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteTableAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_table_associations_with_options_async(
        self,
        request: main_models.ListTransitRouterRouteTableAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteTableAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_id):
            query['TransitRouterAttachmentResourceId'] = request.transit_router_attachment_resource_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_type):
            query['TransitRouterAttachmentResourceType'] = request.transit_router_attachment_resource_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteTableAssociations',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteTableAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_table_associations(
        self,
        request: main_models.ListTransitRouterRouteTableAssociationsRequest,
    ) -> main_models.ListTransitRouterRouteTableAssociationsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_route_table_associations_with_options(request, runtime)

    async def list_transit_router_route_table_associations_async(
        self,
        request: main_models.ListTransitRouterRouteTableAssociationsRequest,
    ) -> main_models.ListTransitRouterRouteTableAssociationsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_route_table_associations_with_options_async(request, runtime)

    def list_transit_router_route_table_propagations_with_options(
        self,
        request: main_models.ListTransitRouterRouteTablePropagationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteTablePropagationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_id):
            query['TransitRouterAttachmentResourceId'] = request.transit_router_attachment_resource_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_type):
            query['TransitRouterAttachmentResourceType'] = request.transit_router_attachment_resource_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteTablePropagations',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteTablePropagationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_table_propagations_with_options_async(
        self,
        request: main_models.ListTransitRouterRouteTablePropagationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteTablePropagationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_id):
            query['TransitRouterAttachmentResourceId'] = request.transit_router_attachment_resource_id
        if not DaraCore.is_null(request.transit_router_attachment_resource_type):
            query['TransitRouterAttachmentResourceType'] = request.transit_router_attachment_resource_type
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteTablePropagations',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteTablePropagationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_table_propagations(
        self,
        request: main_models.ListTransitRouterRouteTablePropagationsRequest,
    ) -> main_models.ListTransitRouterRouteTablePropagationsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_route_table_propagations_with_options(request, runtime)

    async def list_transit_router_route_table_propagations_async(
        self,
        request: main_models.ListTransitRouterRouteTablePropagationsRequest,
    ) -> main_models.ListTransitRouterRouteTablePropagationsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_route_table_propagations_with_options_async(request, runtime)

    def list_transit_router_route_tables_with_options(
        self,
        request: main_models.ListTransitRouterRouteTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_route_table_ids):
            query['TransitRouterRouteTableIds'] = request.transit_router_route_table_ids
        if not DaraCore.is_null(request.transit_router_route_table_names):
            query['TransitRouterRouteTableNames'] = request.transit_router_route_table_names
        if not DaraCore.is_null(request.transit_router_route_table_status):
            query['TransitRouterRouteTableStatus'] = request.transit_router_route_table_status
        if not DaraCore.is_null(request.transit_router_route_table_type):
            query['TransitRouterRouteTableType'] = request.transit_router_route_table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteTables',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_route_tables_with_options_async(
        self,
        request: main_models.ListTransitRouterRouteTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterRouteTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_route_table_ids):
            query['TransitRouterRouteTableIds'] = request.transit_router_route_table_ids
        if not DaraCore.is_null(request.transit_router_route_table_names):
            query['TransitRouterRouteTableNames'] = request.transit_router_route_table_names
        if not DaraCore.is_null(request.transit_router_route_table_status):
            query['TransitRouterRouteTableStatus'] = request.transit_router_route_table_status
        if not DaraCore.is_null(request.transit_router_route_table_type):
            query['TransitRouterRouteTableType'] = request.transit_router_route_table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterRouteTables',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterRouteTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_route_tables(
        self,
        request: main_models.ListTransitRouterRouteTablesRequest,
    ) -> main_models.ListTransitRouterRouteTablesResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_route_tables_with_options(request, runtime)

    async def list_transit_router_route_tables_async(
        self,
        request: main_models.ListTransitRouterRouteTablesRequest,
    ) -> main_models.ListTransitRouterRouteTablesResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_route_tables_with_options_async(request, runtime)

    def list_transit_router_vbr_attachments_with_options(
        self,
        request: main_models.ListTransitRouterVbrAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterVbrAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterVbrAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterVbrAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_vbr_attachments_with_options_async(
        self,
        request: main_models.ListTransitRouterVbrAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterVbrAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterVbrAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterVbrAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_vbr_attachments(
        self,
        request: main_models.ListTransitRouterVbrAttachmentsRequest,
    ) -> main_models.ListTransitRouterVbrAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_vbr_attachments_with_options(request, runtime)

    async def list_transit_router_vbr_attachments_async(
        self,
        request: main_models.ListTransitRouterVbrAttachmentsRequest,
    ) -> main_models.ListTransitRouterVbrAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_vbr_attachments_with_options_async(request, runtime)

    def list_transit_router_vpc_attachments_with_options(
        self,
        request: main_models.ListTransitRouterVpcAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterVpcAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterVpcAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterVpcAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_vpc_attachments_with_options_async(
        self,
        request: main_models.ListTransitRouterVpcAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterVpcAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterVpcAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterVpcAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_vpc_attachments(
        self,
        request: main_models.ListTransitRouterVpcAttachmentsRequest,
    ) -> main_models.ListTransitRouterVpcAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_vpc_attachments_with_options(request, runtime)

    async def list_transit_router_vpc_attachments_async(
        self,
        request: main_models.ListTransitRouterVpcAttachmentsRequest,
    ) -> main_models.ListTransitRouterVpcAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_vpc_attachments_with_options_async(request, runtime)

    def list_transit_router_vpn_attachments_with_options(
        self,
        request: main_models.ListTransitRouterVpnAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterVpnAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterVpnAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterVpnAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_router_vpn_attachments_with_options_async(
        self,
        request: main_models.ListTransitRouterVpnAttachmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRouterVpnAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouterVpnAttachments',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRouterVpnAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_router_vpn_attachments(
        self,
        request: main_models.ListTransitRouterVpnAttachmentsRequest,
    ) -> main_models.ListTransitRouterVpnAttachmentsResponse:
        runtime = RuntimeOptions()
        return self.list_transit_router_vpn_attachments_with_options(request, runtime)

    async def list_transit_router_vpn_attachments_async(
        self,
        request: main_models.ListTransitRouterVpnAttachmentsRequest,
    ) -> main_models.ListTransitRouterVpnAttachmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_router_vpn_attachments_with_options_async(request, runtime)

    def list_transit_routers_with_options(
        self,
        request: main_models.ListTransitRoutersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRoutersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.feature_filter):
            query['FeatureFilter'] = request.feature_filter
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouters',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRoutersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transit_routers_with_options_async(
        self,
        request: main_models.ListTransitRoutersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTransitRoutersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.feature_filter):
            query['FeatureFilter'] = request.feature_filter
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTransitRouters',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTransitRoutersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transit_routers(
        self,
        request: main_models.ListTransitRoutersRequest,
    ) -> main_models.ListTransitRoutersResponse:
        runtime = RuntimeOptions()
        return self.list_transit_routers_with_options(request, runtime)

    async def list_transit_routers_async(
        self,
        request: main_models.ListTransitRoutersRequest,
    ) -> main_models.ListTransitRoutersResponse:
        runtime = RuntimeOptions()
        return await self.list_transit_routers_with_options_async(request, runtime)

    def modify_cen_attribute_with_options(
        self,
        request: main_models.ModifyCenAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_attribute_with_options_async(
        self,
        request: main_models.ModifyCenAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_attribute(
        self,
        request: main_models.ModifyCenAttributeRequest,
    ) -> main_models.ModifyCenAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_cen_attribute_with_options(request, runtime)

    async def modify_cen_attribute_async(
        self,
        request: main_models.ModifyCenAttributeRequest,
    ) -> main_models.ModifyCenAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_cen_attribute_with_options_async(request, runtime)

    def modify_cen_bandwidth_package_attribute_with_options(
        self,
        request: main_models.ModifyCenBandwidthPackageAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenBandwidthPackageAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenBandwidthPackageAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenBandwidthPackageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_bandwidth_package_attribute_with_options_async(
        self,
        request: main_models.ModifyCenBandwidthPackageAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenBandwidthPackageAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenBandwidthPackageAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenBandwidthPackageAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_bandwidth_package_attribute(
        self,
        request: main_models.ModifyCenBandwidthPackageAttributeRequest,
    ) -> main_models.ModifyCenBandwidthPackageAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_cen_bandwidth_package_attribute_with_options(request, runtime)

    async def modify_cen_bandwidth_package_attribute_async(
        self,
        request: main_models.ModifyCenBandwidthPackageAttributeRequest,
    ) -> main_models.ModifyCenBandwidthPackageAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_cen_bandwidth_package_attribute_with_options_async(request, runtime)

    def modify_cen_bandwidth_package_spec_with_options(
        self,
        request: main_models.ModifyCenBandwidthPackageSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenBandwidthPackageSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenBandwidthPackageSpec',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenBandwidthPackageSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_bandwidth_package_spec_with_options_async(
        self,
        request: main_models.ModifyCenBandwidthPackageSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenBandwidthPackageSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenBandwidthPackageSpec',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenBandwidthPackageSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_bandwidth_package_spec(
        self,
        request: main_models.ModifyCenBandwidthPackageSpecRequest,
    ) -> main_models.ModifyCenBandwidthPackageSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_cen_bandwidth_package_spec_with_options(request, runtime)

    async def modify_cen_bandwidth_package_spec_async(
        self,
        request: main_models.ModifyCenBandwidthPackageSpecRequest,
    ) -> main_models.ModifyCenBandwidthPackageSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_cen_bandwidth_package_spec_with_options_async(request, runtime)

    def modify_cen_route_map_with_options(
        self,
        request: main_models.ModifyCenRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenRouteMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not DaraCore.is_null(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not DaraCore.is_null(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not DaraCore.is_null(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not DaraCore.is_null(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not DaraCore.is_null(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not DaraCore.is_null(request.destination_region_ids):
            query['DestinationRegionIds'] = request.destination_region_ids
        if not DaraCore.is_null(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not DaraCore.is_null(request.map_result):
            query['MapResult'] = request.map_result
        if not DaraCore.is_null(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not DaraCore.is_null(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not DaraCore.is_null(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not DaraCore.is_null(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not DaraCore.is_null(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preference):
            query['Preference'] = request.preference
        if not DaraCore.is_null(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not DaraCore.is_null(request.route_types):
            query['RouteTypes'] = request.route_types
        if not DaraCore.is_null(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not DaraCore.is_null(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not DaraCore.is_null(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not DaraCore.is_null(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not DaraCore.is_null(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenRouteMap',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cen_route_map_with_options_async(
        self,
        request: main_models.ModifyCenRouteMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCenRouteMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not DaraCore.is_null(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not DaraCore.is_null(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not DaraCore.is_null(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not DaraCore.is_null(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not DaraCore.is_null(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not DaraCore.is_null(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not DaraCore.is_null(request.destination_region_ids):
            query['DestinationRegionIds'] = request.destination_region_ids
        if not DaraCore.is_null(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not DaraCore.is_null(request.map_result):
            query['MapResult'] = request.map_result
        if not DaraCore.is_null(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not DaraCore.is_null(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not DaraCore.is_null(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not DaraCore.is_null(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not DaraCore.is_null(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preference):
            query['Preference'] = request.preference
        if not DaraCore.is_null(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not DaraCore.is_null(request.route_types):
            query['RouteTypes'] = request.route_types
        if not DaraCore.is_null(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not DaraCore.is_null(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not DaraCore.is_null(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not DaraCore.is_null(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not DaraCore.is_null(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCenRouteMap',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCenRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cen_route_map(
        self,
        request: main_models.ModifyCenRouteMapRequest,
    ) -> main_models.ModifyCenRouteMapResponse:
        runtime = RuntimeOptions()
        return self.modify_cen_route_map_with_options(request, runtime)

    async def modify_cen_route_map_async(
        self,
        request: main_models.ModifyCenRouteMapRequest,
    ) -> main_models.ModifyCenRouteMapResponse:
        runtime = RuntimeOptions()
        return await self.modify_cen_route_map_with_options_async(request, runtime)

    def modify_flow_log_attribute_with_options(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlowLogAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowLogAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not DaraCore.is_null(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFlowLogAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFlowLogAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow_log_attribute(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    async def modify_flow_log_attribute_async(
        self,
        request: main_models.ModifyFlowLogAttributeRequest,
    ) -> main_models.ModifyFlowLogAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_flow_log_attribute_with_options_async(request, runtime)

    def modify_grant_instance_to_transit_router_with_options(
        self,
        request: main_models.ModifyGrantInstanceToTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGrantInstanceToTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGrantInstanceToTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGrantInstanceToTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_grant_instance_to_transit_router_with_options_async(
        self,
        request: main_models.ModifyGrantInstanceToTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGrantInstanceToTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGrantInstanceToTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGrantInstanceToTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_grant_instance_to_transit_router(
        self,
        request: main_models.ModifyGrantInstanceToTransitRouterRequest,
    ) -> main_models.ModifyGrantInstanceToTransitRouterResponse:
        runtime = RuntimeOptions()
        return self.modify_grant_instance_to_transit_router_with_options(request, runtime)

    async def modify_grant_instance_to_transit_router_async(
        self,
        request: main_models.ModifyGrantInstanceToTransitRouterRequest,
    ) -> main_models.ModifyGrantInstanceToTransitRouterResponse:
        runtime = RuntimeOptions()
        return await self.modify_grant_instance_to_transit_router_with_options_async(request, runtime)

    def modify_traffic_match_rule_to_traffic_marking_policy_with_options(
        self,
        request: main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_match_rule_description):
            query['TrafficMatchRuleDescription'] = request.traffic_match_rule_description
        if not DaraCore.is_null(request.traffic_match_rule_id):
            query['TrafficMatchRuleId'] = request.traffic_match_rule_id
        if not DaraCore.is_null(request.traffic_match_rule_name):
            query['TrafficMatchRuleName'] = request.traffic_match_rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrafficMatchRuleToTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_traffic_match_rule_to_traffic_marking_policy_with_options_async(
        self,
        request: main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_match_rule_description):
            query['TrafficMatchRuleDescription'] = request.traffic_match_rule_description
        if not DaraCore.is_null(request.traffic_match_rule_id):
            query['TrafficMatchRuleId'] = request.traffic_match_rule_id
        if not DaraCore.is_null(request.traffic_match_rule_name):
            query['TrafficMatchRuleName'] = request.traffic_match_rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrafficMatchRuleToTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_traffic_match_rule_to_traffic_marking_policy(
        self,
        request: main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_traffic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    async def modify_traffic_match_rule_to_traffic_marking_policy_async(
        self,
        request: main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyRequest,
    ) -> main_models.ModifyTrafficMatchRuleToTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_traffic_match_rule_to_traffic_marking_policy_with_options_async(request, runtime)

    def modify_transit_route_table_aggregation_with_options(
        self,
        tmp_req: main_models.ModifyTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTransitRouteTableAggregationResponse:
        tmp_req.validate()
        request = main_models.ModifyTransitRouteTableAggregationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_route_table_aggregation_scope_list):
            request.transit_route_table_aggregation_scope_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_route_table_aggregation_scope_list, 'TransitRouteTableAggregationScopeList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_aggregation_description):
            query['TransitRouteTableAggregationDescription'] = request.transit_route_table_aggregation_description
        if not DaraCore.is_null(request.transit_route_table_aggregation_name):
            query['TransitRouteTableAggregationName'] = request.transit_route_table_aggregation_name
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope):
            query['TransitRouteTableAggregationScope'] = request.transit_route_table_aggregation_scope
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope_list_shrink):
            query['TransitRouteTableAggregationScopeList'] = request.transit_route_table_aggregation_scope_list_shrink
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_transit_route_table_aggregation_with_options_async(
        self,
        tmp_req: main_models.ModifyTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTransitRouteTableAggregationResponse:
        tmp_req.validate()
        request = main_models.ModifyTransitRouteTableAggregationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_route_table_aggregation_scope_list):
            request.transit_route_table_aggregation_scope_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_route_table_aggregation_scope_list, 'TransitRouteTableAggregationScopeList', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_aggregation_description):
            query['TransitRouteTableAggregationDescription'] = request.transit_route_table_aggregation_description
        if not DaraCore.is_null(request.transit_route_table_aggregation_name):
            query['TransitRouteTableAggregationName'] = request.transit_route_table_aggregation_name
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope):
            query['TransitRouteTableAggregationScope'] = request.transit_route_table_aggregation_scope
        if not DaraCore.is_null(request.transit_route_table_aggregation_scope_list_shrink):
            query['TransitRouteTableAggregationScopeList'] = request.transit_route_table_aggregation_scope_list_shrink
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTransitRouteTableAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_transit_route_table_aggregation(
        self,
        request: main_models.ModifyTransitRouteTableAggregationRequest,
    ) -> main_models.ModifyTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return self.modify_transit_route_table_aggregation_with_options(request, runtime)

    async def modify_transit_route_table_aggregation_async(
        self,
        request: main_models.ModifyTransitRouteTableAggregationRequest,
    ) -> main_models.ModifyTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return await self.modify_transit_route_table_aggregation_with_options_async(request, runtime)

    def modify_transit_router_cidr_with_options(
        self,
        request: main_models.ModifyTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_transit_router_cidr_with_options_async(
        self,
        request: main_models.ModifyTransitRouterCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTransitRouterCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTransitRouterCidr',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTransitRouterCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_transit_router_cidr(
        self,
        request: main_models.ModifyTransitRouterCidrRequest,
    ) -> main_models.ModifyTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return self.modify_transit_router_cidr_with_options(request, runtime)

    async def modify_transit_router_cidr_async(
        self,
        request: main_models.ModifyTransitRouterCidrRequest,
    ) -> main_models.ModifyTransitRouterCidrResponse:
        runtime = RuntimeOptions()
        return await self.modify_transit_router_cidr_with_options_async(request, runtime)

    def modify_transit_router_multicast_domain_with_options(
        self,
        request: main_models.ModifyTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_transit_router_multicast_domain_with_options_async(
        self,
        request: main_models.ModifyTransitRouterMulticastDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTransitRouterMulticastDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTransitRouterMulticastDomain',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTransitRouterMulticastDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_transit_router_multicast_domain(
        self,
        request: main_models.ModifyTransitRouterMulticastDomainRequest,
    ) -> main_models.ModifyTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return self.modify_transit_router_multicast_domain_with_options(request, runtime)

    async def modify_transit_router_multicast_domain_async(
        self,
        request: main_models.ModifyTransitRouterMulticastDomainRequest,
    ) -> main_models.ModifyTransitRouterMulticastDomainResponse:
        runtime = RuntimeOptions()
        return await self.modify_transit_router_multicast_domain_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def open_transit_router_service_with_options(
        self,
        request: main_models.OpenTransitRouterServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenTransitRouterServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenTransitRouterService',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenTransitRouterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_transit_router_service_with_options_async(
        self,
        request: main_models.OpenTransitRouterServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenTransitRouterServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenTransitRouterService',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenTransitRouterServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_transit_router_service(
        self,
        request: main_models.OpenTransitRouterServiceRequest,
    ) -> main_models.OpenTransitRouterServiceResponse:
        runtime = RuntimeOptions()
        return self.open_transit_router_service_with_options(request, runtime)

    async def open_transit_router_service_async(
        self,
        request: main_models.OpenTransitRouterServiceRequest,
    ) -> main_models.OpenTransitRouterServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_transit_router_service_with_options_async(request, runtime)

    def publish_route_entries_with_options(
        self,
        request: main_models.PublishRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_route_entries_with_options_async(
        self,
        request: main_models.PublishRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_route_entries(
        self,
        request: main_models.PublishRouteEntriesRequest,
    ) -> main_models.PublishRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.publish_route_entries_with_options(request, runtime)

    async def publish_route_entries_async(
        self,
        request: main_models.PublishRouteEntriesRequest,
    ) -> main_models.PublishRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.publish_route_entries_with_options_async(request, runtime)

    def refresh_transit_route_table_aggregation_with_options(
        self,
        request: main_models.RefreshTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshTransitRouteTableAggregationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_transit_route_table_aggregation_with_options_async(
        self,
        request: main_models.RefreshTransitRouteTableAggregationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshTransitRouteTableAggregationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not DaraCore.is_null(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshTransitRouteTableAggregation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshTransitRouteTableAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_transit_route_table_aggregation(
        self,
        request: main_models.RefreshTransitRouteTableAggregationRequest,
    ) -> main_models.RefreshTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return self.refresh_transit_route_table_aggregation_with_options(request, runtime)

    async def refresh_transit_route_table_aggregation_async(
        self,
        request: main_models.RefreshTransitRouteTableAggregationRequest,
    ) -> main_models.RefreshTransitRouteTableAggregationResponse:
        runtime = RuntimeOptions()
        return await self.refresh_transit_route_table_aggregation_with_options_async(request, runtime)

    def register_transit_router_multicast_group_members_with_options(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterTransitRouterMulticastGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterTransitRouterMulticastGroupMembers',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterTransitRouterMulticastGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_transit_router_multicast_group_members_with_options_async(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterTransitRouterMulticastGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterTransitRouterMulticastGroupMembers',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterTransitRouterMulticastGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_transit_router_multicast_group_members(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupMembersRequest,
    ) -> main_models.RegisterTransitRouterMulticastGroupMembersResponse:
        runtime = RuntimeOptions()
        return self.register_transit_router_multicast_group_members_with_options(request, runtime)

    async def register_transit_router_multicast_group_members_async(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupMembersRequest,
    ) -> main_models.RegisterTransitRouterMulticastGroupMembersResponse:
        runtime = RuntimeOptions()
        return await self.register_transit_router_multicast_group_members_with_options_async(request, runtime)

    def register_transit_router_multicast_group_sources_with_options(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterTransitRouterMulticastGroupSources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterTransitRouterMulticastGroupSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_transit_router_multicast_group_sources_with_options_async(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not DaraCore.is_null(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterTransitRouterMulticastGroupSources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterTransitRouterMulticastGroupSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_transit_router_multicast_group_sources(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupSourcesRequest,
    ) -> main_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        runtime = RuntimeOptions()
        return self.register_transit_router_multicast_group_sources_with_options(request, runtime)

    async def register_transit_router_multicast_group_sources_async(
        self,
        request: main_models.RegisterTransitRouterMulticastGroupSourcesRequest,
    ) -> main_models.RegisterTransitRouterMulticastGroupSourcesResponse:
        runtime = RuntimeOptions()
        return await self.register_transit_router_multicast_group_sources_with_options_async(request, runtime)

    def remove_traffic_match_rule_from_traffic_marking_policy_with_options(
        self,
        request: main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTrafficMatchRuleFromTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_traffic_match_rule_from_traffic_marking_policy_with_options_async(
        self,
        request: main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTrafficMatchRuleFromTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_traffic_match_rule_from_traffic_marking_policy(
        self,
        request: main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return self.remove_traffic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    async def remove_traffic_match_rule_from_traffic_marking_policy_async(
        self,
        request: main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> main_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.remove_traffic_match_rule_from_traffic_marking_policy_with_options_async(request, runtime)

    def remove_trafic_match_rule_from_traffic_marking_policy_with_options(
        self,
        request: main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTraficMatchRuleFromTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_trafic_match_rule_from_traffic_marking_policy_with_options_async(
        self,
        request: main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTraficMatchRuleFromTrafficMarkingPolicy',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_trafic_match_rule_from_traffic_marking_policy(
        self,
        request: main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return self.remove_trafic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    async def remove_trafic_match_rule_from_traffic_marking_policy_async(
        self,
        request: main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest,
    ) -> main_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.remove_trafic_match_rule_from_traffic_marking_policy_with_options_async(request, runtime)

    def replace_transit_router_route_table_association_with_options(
        self,
        request: main_models.ReplaceTransitRouterRouteTableAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceTransitRouterRouteTableAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceTransitRouterRouteTableAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceTransitRouterRouteTableAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_transit_router_route_table_association_with_options_async(
        self,
        request: main_models.ReplaceTransitRouterRouteTableAssociationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceTransitRouterRouteTableAssociationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceTransitRouterRouteTableAssociation',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceTransitRouterRouteTableAssociationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_transit_router_route_table_association(
        self,
        request: main_models.ReplaceTransitRouterRouteTableAssociationRequest,
    ) -> main_models.ReplaceTransitRouterRouteTableAssociationResponse:
        runtime = RuntimeOptions()
        return self.replace_transit_router_route_table_association_with_options(request, runtime)

    async def replace_transit_router_route_table_association_async(
        self,
        request: main_models.ReplaceTransitRouterRouteTableAssociationRequest,
    ) -> main_models.ReplaceTransitRouterRouteTableAssociationResponse:
        runtime = RuntimeOptions()
        return await self.replace_transit_router_route_table_association_with_options_async(request, runtime)

    def resolve_and_route_service_in_cen_with_options(
        self,
        request: main_models.ResolveAndRouteServiceInCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResolveAndRouteServiceInCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_ids):
            query['AccessRegionIds'] = request.access_region_ids
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResolveAndRouteServiceInCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResolveAndRouteServiceInCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def resolve_and_route_service_in_cen_with_options_async(
        self,
        request: main_models.ResolveAndRouteServiceInCenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResolveAndRouteServiceInCenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_ids):
            query['AccessRegionIds'] = request.access_region_ids
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResolveAndRouteServiceInCen',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResolveAndRouteServiceInCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resolve_and_route_service_in_cen(
        self,
        request: main_models.ResolveAndRouteServiceInCenRequest,
    ) -> main_models.ResolveAndRouteServiceInCenResponse:
        runtime = RuntimeOptions()
        return self.resolve_and_route_service_in_cen_with_options(request, runtime)

    async def resolve_and_route_service_in_cen_async(
        self,
        request: main_models.ResolveAndRouteServiceInCenRequest,
    ) -> main_models.ResolveAndRouteServiceInCenResponse:
        runtime = RuntimeOptions()
        return await self.resolve_and_route_service_in_cen_with_options_async(request, runtime)

    def revoke_instance_from_transit_router_with_options(
        self,
        request: main_models.RevokeInstanceFromTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_instance_from_transit_router_with_options_async(
        self,
        request: main_models.RevokeInstanceFromTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeInstanceFromTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeInstanceFromTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeInstanceFromTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_instance_from_transit_router(
        self,
        request: main_models.RevokeInstanceFromTransitRouterRequest,
    ) -> main_models.RevokeInstanceFromTransitRouterResponse:
        runtime = RuntimeOptions()
        return self.revoke_instance_from_transit_router_with_options(request, runtime)

    async def revoke_instance_from_transit_router_async(
        self,
        request: main_models.RevokeInstanceFromTransitRouterRequest,
    ) -> main_models.RevokeInstanceFromTransitRouterResponse:
        runtime = RuntimeOptions()
        return await self.revoke_instance_from_transit_router_with_options_async(request, runtime)

    def route_private_zone_in_cen_to_vpc_with_options(
        self,
        request: main_models.RoutePrivateZoneInCenToVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RoutePrivateZoneInCenToVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RoutePrivateZoneInCenToVpc',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RoutePrivateZoneInCenToVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def route_private_zone_in_cen_to_vpc_with_options_async(
        self,
        request: main_models.RoutePrivateZoneInCenToVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RoutePrivateZoneInCenToVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not DaraCore.is_null(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RoutePrivateZoneInCenToVpc',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RoutePrivateZoneInCenToVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def route_private_zone_in_cen_to_vpc(
        self,
        request: main_models.RoutePrivateZoneInCenToVpcRequest,
    ) -> main_models.RoutePrivateZoneInCenToVpcResponse:
        runtime = RuntimeOptions()
        return self.route_private_zone_in_cen_to_vpc_with_options(request, runtime)

    async def route_private_zone_in_cen_to_vpc_async(
        self,
        request: main_models.RoutePrivateZoneInCenToVpcRequest,
    ) -> main_models.RoutePrivateZoneInCenToVpcResponse:
        runtime = RuntimeOptions()
        return await self.route_private_zone_in_cen_to_vpc_with_options_async(request, runtime)

    def set_cen_inter_region_bandwidth_limit_with_options(
        self,
        request: main_models.SetCenInterRegionBandwidthLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCenInterRegionBandwidthLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_limit):
            query['BandwidthLimit'] = request.bandwidth_limit
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.local_region_id):
            query['LocalRegionId'] = request.local_region_id
        if not DaraCore.is_null(request.opposite_region_id):
            query['OppositeRegionId'] = request.opposite_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCenInterRegionBandwidthLimit',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCenInterRegionBandwidthLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_cen_inter_region_bandwidth_limit_with_options_async(
        self,
        request: main_models.SetCenInterRegionBandwidthLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCenInterRegionBandwidthLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_limit):
            query['BandwidthLimit'] = request.bandwidth_limit
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.local_region_id):
            query['LocalRegionId'] = request.local_region_id
        if not DaraCore.is_null(request.opposite_region_id):
            query['OppositeRegionId'] = request.opposite_region_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCenInterRegionBandwidthLimit',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCenInterRegionBandwidthLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_cen_inter_region_bandwidth_limit(
        self,
        request: main_models.SetCenInterRegionBandwidthLimitRequest,
    ) -> main_models.SetCenInterRegionBandwidthLimitResponse:
        runtime = RuntimeOptions()
        return self.set_cen_inter_region_bandwidth_limit_with_options(request, runtime)

    async def set_cen_inter_region_bandwidth_limit_async(
        self,
        request: main_models.SetCenInterRegionBandwidthLimitRequest,
    ) -> main_models.SetCenInterRegionBandwidthLimitResponse:
        runtime = RuntimeOptions()
        return await self.set_cen_inter_region_bandwidth_limit_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def temp_upgrade_cen_bandwidth_package_spec_with_options(
        self,
        request: main_models.TempUpgradeCenBandwidthPackageSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempUpgradeCenBandwidthPackageSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TempUpgradeCenBandwidthPackageSpec',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempUpgradeCenBandwidthPackageSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_upgrade_cen_bandwidth_package_spec_with_options_async(
        self,
        request: main_models.TempUpgradeCenBandwidthPackageSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TempUpgradeCenBandwidthPackageSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TempUpgradeCenBandwidthPackageSpec',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TempUpgradeCenBandwidthPackageSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_upgrade_cen_bandwidth_package_spec(
        self,
        request: main_models.TempUpgradeCenBandwidthPackageSpecRequest,
    ) -> main_models.TempUpgradeCenBandwidthPackageSpecResponse:
        runtime = RuntimeOptions()
        return self.temp_upgrade_cen_bandwidth_package_spec_with_options(request, runtime)

    async def temp_upgrade_cen_bandwidth_package_spec_async(
        self,
        request: main_models.TempUpgradeCenBandwidthPackageSpecRequest,
    ) -> main_models.TempUpgradeCenBandwidthPackageSpecResponse:
        runtime = RuntimeOptions()
        return await self.temp_upgrade_cen_bandwidth_package_spec_with_options_async(request, runtime)

    def unassociate_cen_bandwidth_package_with_options(
        self,
        request: main_models.UnassociateCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnassociateCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnassociateCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnassociateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassociate_cen_bandwidth_package_with_options_async(
        self,
        request: main_models.UnassociateCenBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnassociateCenBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnassociateCenBandwidthPackage',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnassociateCenBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassociate_cen_bandwidth_package(
        self,
        request: main_models.UnassociateCenBandwidthPackageRequest,
    ) -> main_models.UnassociateCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.unassociate_cen_bandwidth_package_with_options(request, runtime)

    async def unassociate_cen_bandwidth_package_async(
        self,
        request: main_models.UnassociateCenBandwidthPackageRequest,
    ) -> main_models.UnassociateCenBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.unassociate_cen_bandwidth_package_with_options_async(request, runtime)

    def unroute_private_zone_in_cen_to_vpc_with_options(
        self,
        request: main_models.UnroutePrivateZoneInCenToVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnroutePrivateZoneInCenToVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnroutePrivateZoneInCenToVpc',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnroutePrivateZoneInCenToVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def unroute_private_zone_in_cen_to_vpc_with_options_async(
        self,
        request: main_models.UnroutePrivateZoneInCenToVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnroutePrivateZoneInCenToVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnroutePrivateZoneInCenToVpc',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnroutePrivateZoneInCenToVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unroute_private_zone_in_cen_to_vpc(
        self,
        request: main_models.UnroutePrivateZoneInCenToVpcRequest,
    ) -> main_models.UnroutePrivateZoneInCenToVpcResponse:
        runtime = RuntimeOptions()
        return self.unroute_private_zone_in_cen_to_vpc_with_options(request, runtime)

    async def unroute_private_zone_in_cen_to_vpc_async(
        self,
        request: main_models.UnroutePrivateZoneInCenToVpcRequest,
    ) -> main_models.UnroutePrivateZoneInCenToVpcResponse:
        runtime = RuntimeOptions()
        return await self.unroute_private_zone_in_cen_to_vpc_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_cen_inter_region_traffic_qos_policy_attribute_with_options(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not DaraCore.is_null(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCenInterRegionTrafficQosPolicyAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cen_inter_region_traffic_qos_policy_attribute_with_options_async(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not DaraCore.is_null(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not DaraCore.is_null(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCenInterRegionTrafficQosPolicyAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cen_inter_region_traffic_qos_policy_attribute(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
    ) -> main_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_cen_inter_region_traffic_qos_policy_attribute_with_options(request, runtime)

    async def update_cen_inter_region_traffic_qos_policy_attribute_async(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosPolicyAttributeRequest,
    ) -> main_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_cen_inter_region_traffic_qos_policy_attribute_with_options_async(request, runtime)

    def update_cen_inter_region_traffic_qos_queue_attribute_with_options(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dscps):
            query['Dscps'] = request.dscps
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not DaraCore.is_null(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not DaraCore.is_null(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not DaraCore.is_null(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCenInterRegionTrafficQosQueueAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cen_inter_region_traffic_qos_queue_attribute_with_options_async(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dscps):
            query['Dscps'] = request.dscps
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not DaraCore.is_null(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not DaraCore.is_null(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not DaraCore.is_null(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCenInterRegionTrafficQosQueueAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cen_inter_region_traffic_qos_queue_attribute(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
    ) -> main_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_cen_inter_region_traffic_qos_queue_attribute_with_options(request, runtime)

    async def update_cen_inter_region_traffic_qos_queue_attribute_async(
        self,
        request: main_models.UpdateCenInterRegionTrafficQosQueueAttributeRequest,
    ) -> main_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_cen_inter_region_traffic_qos_queue_attribute_with_options_async(request, runtime)

    def update_traffic_marking_policy_attribute_with_options(
        self,
        request: main_models.UpdateTrafficMarkingPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficMarkingPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_traffic_match_rules):
            query['AddTrafficMatchRules'] = request.add_traffic_match_rules
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_traffic_match_rules):
            query['DeleteTrafficMatchRules'] = request.delete_traffic_match_rules
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficMarkingPolicyAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficMarkingPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_traffic_marking_policy_attribute_with_options_async(
        self,
        request: main_models.UpdateTrafficMarkingPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTrafficMarkingPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_traffic_match_rules):
            query['AddTrafficMatchRules'] = request.add_traffic_match_rules
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delete_traffic_match_rules):
            query['DeleteTrafficMatchRules'] = request.delete_traffic_match_rules
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not DaraCore.is_null(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not DaraCore.is_null(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrafficMarkingPolicyAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTrafficMarkingPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_traffic_marking_policy_attribute(
        self,
        request: main_models.UpdateTrafficMarkingPolicyAttributeRequest,
    ) -> main_models.UpdateTrafficMarkingPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_traffic_marking_policy_attribute_with_options(request, runtime)

    async def update_traffic_marking_policy_attribute_async(
        self,
        request: main_models.UpdateTrafficMarkingPolicyAttributeRequest,
    ) -> main_models.UpdateTrafficMarkingPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_traffic_marking_policy_attribute_with_options_async(request, runtime)

    def update_transit_router_with_options(
        self,
        request: main_models.UpdateTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_with_options_async(
        self,
        request: main_models.UpdateTransitRouterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouter',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router(
        self,
        request: main_models.UpdateTransitRouterRequest,
    ) -> main_models.UpdateTransitRouterResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_with_options(request, runtime)

    async def update_transit_router_async(
        self,
        request: main_models.UpdateTransitRouterRequest,
    ) -> main_models.UpdateTransitRouterResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_with_options_async(request, runtime)

    def update_transit_router_ecr_attachment_attribute_with_options(
        self,
        request: main_models.UpdateTransitRouterEcrAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterEcrAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterEcrAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterEcrAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_ecr_attachment_attribute_with_options_async(
        self,
        request: main_models.UpdateTransitRouterEcrAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterEcrAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterEcrAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterEcrAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_ecr_attachment_attribute(
        self,
        request: main_models.UpdateTransitRouterEcrAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterEcrAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_ecr_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_ecr_attachment_attribute_async(
        self,
        request: main_models.UpdateTransitRouterEcrAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterEcrAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_ecr_attachment_attribute_with_options_async(request, runtime)

    def update_transit_router_peer_attachment_attribute_with_options(
        self,
        request: main_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_link_type):
            query['DefaultLinkType'] = request.default_link_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterPeerAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterPeerAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_peer_attachment_attribute_with_options_async(
        self,
        request: main_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_link_type):
            query['DefaultLinkType'] = request.default_link_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterPeerAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterPeerAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_peer_attachment_attribute(
        self,
        request: main_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_peer_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_peer_attachment_attribute_async(
        self,
        request: main_models.UpdateTransitRouterPeerAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterPeerAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_peer_attachment_attribute_with_options_async(request, runtime)

    def update_transit_router_route_entry_with_options(
        self,
        request: main_models.UpdateTransitRouterRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterRouteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not DaraCore.is_null(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not DaraCore.is_null(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterRouteEntry',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_route_entry_with_options_async(
        self,
        request: main_models.UpdateTransitRouterRouteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterRouteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not DaraCore.is_null(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not DaraCore.is_null(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterRouteEntry',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_route_entry(
        self,
        request: main_models.UpdateTransitRouterRouteEntryRequest,
    ) -> main_models.UpdateTransitRouterRouteEntryResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_route_entry_with_options(request, runtime)

    async def update_transit_router_route_entry_async(
        self,
        request: main_models.UpdateTransitRouterRouteEntryRequest,
    ) -> main_models.UpdateTransitRouterRouteEntryResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_route_entry_with_options_async(request, runtime)

    def update_transit_router_route_table_with_options(
        self,
        request: main_models.UpdateTransitRouterRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not DaraCore.is_null(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not DaraCore.is_null(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_route_table_with_options_async(
        self,
        request: main_models.UpdateTransitRouterRouteTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterRouteTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not DaraCore.is_null(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not DaraCore.is_null(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not DaraCore.is_null(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterRouteTable',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterRouteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_route_table(
        self,
        request: main_models.UpdateTransitRouterRouteTableRequest,
    ) -> main_models.UpdateTransitRouterRouteTableResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_route_table_with_options(request, runtime)

    async def update_transit_router_route_table_async(
        self,
        request: main_models.UpdateTransitRouterRouteTableRequest,
    ) -> main_models.UpdateTransitRouterRouteTableResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_route_table_with_options_async(request, runtime)

    def update_transit_router_vbr_attachment_attribute_with_options(
        self,
        request: main_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVbrAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVbrAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vbr_attachment_attribute_with_options_async(
        self,
        request: main_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVbrAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVbrAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vbr_attachment_attribute(
        self,
        request: main_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_vbr_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_vbr_attachment_attribute_async(
        self,
        request: main_models.UpdateTransitRouterVbrAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterVbrAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_vbr_attachment_attribute_with_options_async(request, runtime)

    def update_transit_router_vpc_attachment_attribute_with_options(
        self,
        tmp_req: main_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        tmp_req.validate()
        request = main_models.UpdateTransitRouterVpcAttachmentAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_router_vpcattachment_options):
            request.transit_router_vpcattachment_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_router_vpcattachment_options, 'TransitRouterVPCAttachmentOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_vpcattachment_options_shrink):
            query['TransitRouterVPCAttachmentOptions'] = request.transit_router_vpcattachment_options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVpcAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVpcAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vpc_attachment_attribute_with_options_async(
        self,
        tmp_req: main_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        tmp_req.validate()
        request = main_models.UpdateTransitRouterVpcAttachmentAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transit_router_vpcattachment_options):
            request.transit_router_vpcattachment_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.transit_router_vpcattachment_options, 'TransitRouterVPCAttachmentOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not DaraCore.is_null(request.transit_router_vpcattachment_options_shrink):
            query['TransitRouterVPCAttachmentOptions'] = request.transit_router_vpcattachment_options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVpcAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVpcAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vpc_attachment_attribute(
        self,
        request: main_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_vpc_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_vpc_attachment_attribute_async(
        self,
        request: main_models.UpdateTransitRouterVpcAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterVpcAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_vpc_attachment_attribute_with_options_async(request, runtime)

    def update_transit_router_vpc_attachment_zones_with_options(
        self,
        request: main_models.UpdateTransitRouterVpcAttachmentZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_zone_mappings):
            query['AddZoneMappings'] = request.add_zone_mappings
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remove_zone_mappings):
            query['RemoveZoneMappings'] = request.remove_zone_mappings
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVpcAttachmentZones',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVpcAttachmentZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vpc_attachment_zones_with_options_async(
        self,
        request: main_models.UpdateTransitRouterVpcAttachmentZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_zone_mappings):
            query['AddZoneMappings'] = request.add_zone_mappings
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remove_zone_mappings):
            query['RemoveZoneMappings'] = request.remove_zone_mappings
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVpcAttachmentZones',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVpcAttachmentZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vpc_attachment_zones(
        self,
        request: main_models.UpdateTransitRouterVpcAttachmentZonesRequest,
    ) -> main_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_vpc_attachment_zones_with_options(request, runtime)

    async def update_transit_router_vpc_attachment_zones_async(
        self,
        request: main_models.UpdateTransitRouterVpcAttachmentZonesRequest,
    ) -> main_models.UpdateTransitRouterVpcAttachmentZonesResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_vpc_attachment_zones_with_options_async(request, runtime)

    def update_transit_router_vpn_attachment_attribute_with_options(
        self,
        request: main_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVpnAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVpnAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transit_router_vpn_attachment_attribute_with_options_async(
        self,
        request: main_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not DaraCore.is_null(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not DaraCore.is_null(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTransitRouterVpnAttachmentAttribute',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTransitRouterVpnAttachmentAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transit_router_vpn_attachment_attribute(
        self,
        request: main_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_transit_router_vpn_attachment_attribute_with_options(request, runtime)

    async def update_transit_router_vpn_attachment_attribute_async(
        self,
        request: main_models.UpdateTransitRouterVpnAttachmentAttributeRequest,
    ) -> main_models.UpdateTransitRouterVpnAttachmentAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_transit_router_vpn_attachment_attribute_with_options_async(request, runtime)

    def withdraw_published_route_entries_with_options(
        self,
        request: main_models.WithdrawPublishedRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawPublishedRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawPublishedRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawPublishedRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_published_route_entries_with_options_async(
        self,
        request: main_models.WithdrawPublishedRouteEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawPublishedRouteEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not DaraCore.is_null(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not DaraCore.is_null(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not DaraCore.is_null(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawPublishedRouteEntries',
            version = '2017-09-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawPublishedRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_published_route_entries(
        self,
        request: main_models.WithdrawPublishedRouteEntriesRequest,
    ) -> main_models.WithdrawPublishedRouteEntriesResponse:
        runtime = RuntimeOptions()
        return self.withdraw_published_route_entries_with_options(request, runtime)

    async def withdraw_published_route_entries_async(
        self,
        request: main_models.WithdrawPublishedRouteEntriesRequest,
    ) -> main_models.WithdrawPublishedRouteEntriesResponse:
        runtime = RuntimeOptions()
        return await self.withdraw_published_route_entries_with_options_async(request, runtime)
