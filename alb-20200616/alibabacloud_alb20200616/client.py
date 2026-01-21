# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_alb20200616 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('alb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_entries_to_acl_with_options(
        self,
        request: main_models.AddEntriesToAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEntriesToAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEntriesToAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEntriesToAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_entries_to_acl_with_options_async(
        self,
        request: main_models.AddEntriesToAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEntriesToAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEntriesToAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEntriesToAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_entries_to_acl(
        self,
        request: main_models.AddEntriesToAclRequest,
    ) -> main_models.AddEntriesToAclResponse:
        runtime = RuntimeOptions()
        return self.add_entries_to_acl_with_options(request, runtime)

    async def add_entries_to_acl_async(
        self,
        request: main_models.AddEntriesToAclRequest,
    ) -> main_models.AddEntriesToAclResponse:
        runtime = RuntimeOptions()
        return await self.add_entries_to_acl_with_options_async(request, runtime)

    def add_servers_to_server_group_with_options(
        self,
        request: main_models.AddServersToServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddServersToServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddServersToServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddServersToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_servers_to_server_group_with_options_async(
        self,
        request: main_models.AddServersToServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddServersToServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddServersToServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddServersToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_servers_to_server_group(
        self,
        request: main_models.AddServersToServerGroupRequest,
    ) -> main_models.AddServersToServerGroupResponse:
        runtime = RuntimeOptions()
        return self.add_servers_to_server_group_with_options(request, runtime)

    async def add_servers_to_server_group_async(
        self,
        request: main_models.AddServersToServerGroupRequest,
    ) -> main_models.AddServersToServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_servers_to_server_group_with_options_async(request, runtime)

    def apply_health_check_template_to_server_group_with_options(
        self,
        request: main_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyHealthCheckTemplateToServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyHealthCheckTemplateToServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_health_check_template_to_server_group_with_options_async(
        self,
        request: main_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyHealthCheckTemplateToServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyHealthCheckTemplateToServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_health_check_template_to_server_group(
        self,
        request: main_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> main_models.ApplyHealthCheckTemplateToServerGroupResponse:
        runtime = RuntimeOptions()
        return self.apply_health_check_template_to_server_group_with_options(request, runtime)

    async def apply_health_check_template_to_server_group_async(
        self,
        request: main_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> main_models.ApplyHealthCheckTemplateToServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.apply_health_check_template_to_server_group_with_options_async(request, runtime)

    def associate_acls_with_listener_with_options(
        self,
        request: main_models.AssociateAclsWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateAclsWithListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAclsWithListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateAclsWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_acls_with_listener_with_options_async(
        self,
        request: main_models.AssociateAclsWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateAclsWithListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAclsWithListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateAclsWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_acls_with_listener(
        self,
        request: main_models.AssociateAclsWithListenerRequest,
    ) -> main_models.AssociateAclsWithListenerResponse:
        runtime = RuntimeOptions()
        return self.associate_acls_with_listener_with_options(request, runtime)

    async def associate_acls_with_listener_async(
        self,
        request: main_models.AssociateAclsWithListenerRequest,
    ) -> main_models.AssociateAclsWithListenerResponse:
        runtime = RuntimeOptions()
        return await self.associate_acls_with_listener_with_options_async(request, runtime)

    def associate_additional_certificates_with_listener_with_options(
        self,
        request: main_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateAdditionalCertificatesWithListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAdditionalCertificatesWithListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_additional_certificates_with_listener_with_options_async(
        self,
        request: main_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateAdditionalCertificatesWithListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAdditionalCertificatesWithListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateAdditionalCertificatesWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_additional_certificates_with_listener(
        self,
        request: main_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> main_models.AssociateAdditionalCertificatesWithListenerResponse:
        runtime = RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    async def associate_additional_certificates_with_listener_async(
        self,
        request: main_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> main_models.AssociateAdditionalCertificatesWithListenerResponse:
        runtime = RuntimeOptions()
        return await self.associate_additional_certificates_with_listener_with_options_async(request, runtime)

    def attach_common_bandwidth_package_to_load_balancer_with_options(
        self,
        request: main_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachCommonBandwidthPackageToLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_common_bandwidth_package_to_load_balancer_with_options_async(
        self,
        request: main_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachCommonBandwidthPackageToLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_common_bandwidth_package_to_load_balancer(
        self,
        request: main_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> main_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        runtime = RuntimeOptions()
        return self.attach_common_bandwidth_package_to_load_balancer_with_options(request, runtime)

    async def attach_common_bandwidth_package_to_load_balancer_async(
        self,
        request: main_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> main_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        runtime = RuntimeOptions()
        return await self.attach_common_bandwidth_package_to_load_balancer_with_options_async(request, runtime)

    def cancel_shift_load_balancer_zones_with_options(
        self,
        request: main_models.CancelShiftLoadBalancerZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelShiftLoadBalancerZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelShiftLoadBalancerZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelShiftLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_shift_load_balancer_zones_with_options_async(
        self,
        request: main_models.CancelShiftLoadBalancerZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelShiftLoadBalancerZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelShiftLoadBalancerZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelShiftLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_shift_load_balancer_zones(
        self,
        request: main_models.CancelShiftLoadBalancerZonesRequest,
    ) -> main_models.CancelShiftLoadBalancerZonesResponse:
        runtime = RuntimeOptions()
        return self.cancel_shift_load_balancer_zones_with_options(request, runtime)

    async def cancel_shift_load_balancer_zones_async(
        self,
        request: main_models.CancelShiftLoadBalancerZonesRequest,
    ) -> main_models.CancelShiftLoadBalancerZonesResponse:
        runtime = RuntimeOptions()
        return await self.cancel_shift_load_balancer_zones_with_options_async(request, runtime)

    def create_ascripts_with_options(
        self,
        request: main_models.CreateAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascripts):
            query['AScripts'] = request.ascripts
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ascripts_with_options_async(
        self,
        request: main_models.CreateAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascripts):
            query['AScripts'] = request.ascripts
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ascripts(
        self,
        request: main_models.CreateAScriptsRequest,
    ) -> main_models.CreateAScriptsResponse:
        runtime = RuntimeOptions()
        return self.create_ascripts_with_options(request, runtime)

    async def create_ascripts_async(
        self,
        request: main_models.CreateAScriptsRequest,
    ) -> main_models.CreateAScriptsResponse:
        runtime = RuntimeOptions()
        return await self.create_ascripts_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: main_models.CreateAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_with_options_async(
        self,
        request: main_models.CreateAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl(
        self,
        request: main_models.CreateAclRequest,
    ) -> main_models.CreateAclResponse:
        runtime = RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: main_models.CreateAclRequest,
    ) -> main_models.CreateAclResponse:
        runtime = RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_health_check_template_with_options(
        self,
        request: main_models.CreateHealthCheckTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHealthCheckTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHealthCheckTemplate',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHealthCheckTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_health_check_template_with_options_async(
        self,
        request: main_models.CreateHealthCheckTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHealthCheckTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHealthCheckTemplate',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHealthCheckTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_health_check_template(
        self,
        request: main_models.CreateHealthCheckTemplateRequest,
    ) -> main_models.CreateHealthCheckTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_health_check_template_with_options(request, runtime)

    async def create_health_check_template_async(
        self,
        request: main_models.CreateHealthCheckTemplateRequest,
    ) -> main_models.CreateHealthCheckTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_health_check_template_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        request: main_models.CreateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not DaraCore.is_null(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not DaraCore.is_null(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_listener_with_options_async(
        self,
        request: main_models.CreateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not DaraCore.is_null(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not DaraCore.is_null(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_listener(
        self,
        request: main_models.CreateListenerRequest,
    ) -> main_models.CreateListenerResponse:
        runtime = RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    async def create_listener_async(
        self,
        request: main_models.CreateListenerRequest,
    ) -> main_models.CreateListenerResponse:
        runtime = RuntimeOptions()
        return await self.create_listener_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: main_models.CreateLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_allocated_mode):
            query['AddressAllocatedMode'] = request.address_allocated_mode
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection_enabled):
            query['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_billing_config):
            query['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not DaraCore.is_null(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: main_models.CreateLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_allocated_mode):
            query['AddressAllocatedMode'] = request.address_allocated_mode
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection_enabled):
            query['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_billing_config):
            query['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not DaraCore.is_null(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer(
        self,
        request: main_models.CreateLoadBalancerRequest,
    ) -> main_models.CreateLoadBalancerResponse:
        runtime = RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: main_models.CreateLoadBalancerRequest,
    ) -> main_models.CreateLoadBalancerResponse:
        runtime = RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_rules_with_options(
        self,
        request: main_models.CreateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.rules):
            body_flat['Rules'] = request.rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRules',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        request: main_models.CreateRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.rules):
            body_flat['Rules'] = request.rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRules',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rules(
        self,
        request: main_models.CreateRulesRequest,
    ) -> main_models.CreateRulesResponse:
        runtime = RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    async def create_rules_async(
        self,
        request: main_models.CreateRulesRequest,
    ) -> main_models.CreateRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_rules_with_options_async(request, runtime)

    def create_security_policy_with_options(
        self,
        request: main_models.CreateSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityPolicy',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_policy_with_options_async(
        self,
        request: main_models.CreateSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityPolicy',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_policy(
        self,
        request: main_models.CreateSecurityPolicyRequest,
    ) -> main_models.CreateSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_security_policy_with_options(request, runtime)

    async def create_security_policy_async(
        self,
        request: main_models.CreateSecurityPolicyRequest,
    ) -> main_models.CreateSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_security_policy_with_options_async(request, runtime)

    def create_server_group_with_options(
        self,
        request: main_models.CreateServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.cross_zone_enabled):
            query['CrossZoneEnabled'] = request.cross_zone_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.ipv_6enabled):
            query['Ipv6Enabled'] = request.ipv_6enabled
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not DaraCore.is_null(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not DaraCore.is_null(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_group_with_options_async(
        self,
        request: main_models.CreateServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.cross_zone_enabled):
            query['CrossZoneEnabled'] = request.cross_zone_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.ipv_6enabled):
            query['Ipv6Enabled'] = request.ipv_6enabled
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not DaraCore.is_null(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not DaraCore.is_null(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_group(
        self,
        request: main_models.CreateServerGroupRequest,
    ) -> main_models.CreateServerGroupResponse:
        runtime = RuntimeOptions()
        return self.create_server_group_with_options(request, runtime)

    async def create_server_group_async(
        self,
        request: main_models.CreateServerGroupRequest,
    ) -> main_models.CreateServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_server_group_with_options_async(request, runtime)

    def delete_ascripts_with_options(
        self,
        request: main_models.DeleteAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ascripts_with_options_async(
        self,
        request: main_models.DeleteAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ascripts(
        self,
        request: main_models.DeleteAScriptsRequest,
    ) -> main_models.DeleteAScriptsResponse:
        runtime = RuntimeOptions()
        return self.delete_ascripts_with_options(request, runtime)

    async def delete_ascripts_async(
        self,
        request: main_models.DeleteAScriptsRequest,
    ) -> main_models.DeleteAScriptsResponse:
        runtime = RuntimeOptions()
        return await self.delete_ascripts_with_options_async(request, runtime)

    def delete_acl_with_options(
        self,
        request: main_models.DeleteAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        request: main_models.DeleteAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl(
        self,
        request: main_models.DeleteAclRequest,
    ) -> main_models.DeleteAclResponse:
        runtime = RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: main_models.DeleteAclRequest,
    ) -> main_models.DeleteAclResponse:
        runtime = RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_health_check_templates_with_options(
        self,
        request: main_models.DeleteHealthCheckTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHealthCheckTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHealthCheckTemplates',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHealthCheckTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_health_check_templates_with_options_async(
        self,
        request: main_models.DeleteHealthCheckTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHealthCheckTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHealthCheckTemplates',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHealthCheckTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_health_check_templates(
        self,
        request: main_models.DeleteHealthCheckTemplatesRequest,
    ) -> main_models.DeleteHealthCheckTemplatesResponse:
        runtime = RuntimeOptions()
        return self.delete_health_check_templates_with_options(request, runtime)

    async def delete_health_check_templates_async(
        self,
        request: main_models.DeleteHealthCheckTemplatesRequest,
    ) -> main_models.DeleteHealthCheckTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.delete_health_check_templates_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: main_models.DeleteListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_listener_with_options_async(
        self,
        request: main_models.DeleteListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_listener(
        self,
        request: main_models.DeleteListenerRequest,
    ) -> main_models.DeleteListenerResponse:
        runtime = RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    async def delete_listener_async(
        self,
        request: main_models.DeleteListenerRequest,
    ) -> main_models.DeleteListenerResponse:
        runtime = RuntimeOptions()
        return await self.delete_listener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: main_models.DeleteLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: main_models.DeleteLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer(
        self,
        request: main_models.DeleteLoadBalancerRequest,
    ) -> main_models.DeleteLoadBalancerResponse:
        runtime = RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: main_models.DeleteLoadBalancerRequest,
    ) -> main_models.DeleteLoadBalancerResponse:
        runtime = RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rules_with_options(
        self,
        request: main_models.DeleteRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRules',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rules_with_options_async(
        self,
        request: main_models.DeleteRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRules',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rules(
        self,
        request: main_models.DeleteRulesRequest,
    ) -> main_models.DeleteRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    async def delete_rules_async(
        self,
        request: main_models.DeleteRulesRequest,
    ) -> main_models.DeleteRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_rules_with_options_async(request, runtime)

    def delete_security_policy_with_options(
        self,
        request: main_models.DeleteSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityPolicy',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_policy_with_options_async(
        self,
        request: main_models.DeleteSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityPolicy',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_policy(
        self,
        request: main_models.DeleteSecurityPolicyRequest,
    ) -> main_models.DeleteSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_security_policy_with_options(request, runtime)

    async def delete_security_policy_async(
        self,
        request: main_models.DeleteSecurityPolicyRequest,
    ) -> main_models.DeleteSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_policy_with_options_async(request, runtime)

    def delete_server_group_with_options(
        self,
        request: main_models.DeleteServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_server_group_with_options_async(
        self,
        request: main_models.DeleteServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_server_group(
        self,
        request: main_models.DeleteServerGroupRequest,
    ) -> main_models.DeleteServerGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_server_group_with_options(request, runtime)

    async def delete_server_group_async(
        self,
        request: main_models.DeleteServerGroupRequest,
    ) -> main_models.DeleteServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_server_group_with_options_async(request, runtime)

    def describe_capacity_reservation_with_options(
        self,
        request: main_models.DescribeCapacityReservationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCapacityReservationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCapacityReservation',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_capacity_reservation_with_options_async(
        self,
        request: main_models.DescribeCapacityReservationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCapacityReservationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCapacityReservation',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCapacityReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_capacity_reservation(
        self,
        request: main_models.DescribeCapacityReservationRequest,
    ) -> main_models.DescribeCapacityReservationResponse:
        runtime = RuntimeOptions()
        return self.describe_capacity_reservation_with_options(request, runtime)

    async def describe_capacity_reservation_async(
        self,
        request: main_models.DescribeCapacityReservationRequest,
    ) -> main_models.DescribeCapacityReservationResponse:
        runtime = RuntimeOptions()
        return await self.describe_capacity_reservation_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_common_bandwidth_package_from_load_balancer_with_options(
        self,
        request: main_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachCommonBandwidthPackageFromLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_common_bandwidth_package_from_load_balancer_with_options_async(
        self,
        request: main_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachCommonBandwidthPackageFromLoadBalancer',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_common_bandwidth_package_from_load_balancer(
        self,
        request: main_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> main_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        runtime = RuntimeOptions()
        return self.detach_common_bandwidth_package_from_load_balancer_with_options(request, runtime)

    async def detach_common_bandwidth_package_from_load_balancer_async(
        self,
        request: main_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> main_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        runtime = RuntimeOptions()
        return await self.detach_common_bandwidth_package_from_load_balancer_with_options_async(request, runtime)

    def disable_deletion_protection_with_options(
        self,
        request: main_models.DisableDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDeletionProtection',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_deletion_protection_with_options_async(
        self,
        request: main_models.DisableDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDeletionProtection',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_deletion_protection(
        self,
        request: main_models.DisableDeletionProtectionRequest,
    ) -> main_models.DisableDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return self.disable_deletion_protection_with_options(request, runtime)

    async def disable_deletion_protection_async(
        self,
        request: main_models.DisableDeletionProtectionRequest,
    ) -> main_models.DisableDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return await self.disable_deletion_protection_with_options_async(request, runtime)

    def disable_load_balancer_access_log_with_options(
        self,
        request: main_models.DisableLoadBalancerAccessLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLoadBalancerAccessLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLoadBalancerAccessLog',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLoadBalancerAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_load_balancer_access_log_with_options_async(
        self,
        request: main_models.DisableLoadBalancerAccessLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLoadBalancerAccessLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLoadBalancerAccessLog',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLoadBalancerAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_load_balancer_access_log(
        self,
        request: main_models.DisableLoadBalancerAccessLogRequest,
    ) -> main_models.DisableLoadBalancerAccessLogResponse:
        runtime = RuntimeOptions()
        return self.disable_load_balancer_access_log_with_options(request, runtime)

    async def disable_load_balancer_access_log_async(
        self,
        request: main_models.DisableLoadBalancerAccessLogRequest,
    ) -> main_models.DisableLoadBalancerAccessLogResponse:
        runtime = RuntimeOptions()
        return await self.disable_load_balancer_access_log_with_options_async(request, runtime)

    def disable_load_balancer_ipv_6internet_with_options(
        self,
        request: main_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLoadBalancerIpv6InternetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLoadBalancerIpv6Internet',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLoadBalancerIpv6InternetResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_load_balancer_ipv_6internet_with_options_async(
        self,
        request: main_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLoadBalancerIpv6InternetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableLoadBalancerIpv6Internet',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableLoadBalancerIpv6InternetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_load_balancer_ipv_6internet(
        self,
        request: main_models.DisableLoadBalancerIpv6InternetRequest,
    ) -> main_models.DisableLoadBalancerIpv6InternetResponse:
        runtime = RuntimeOptions()
        return self.disable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def disable_load_balancer_ipv_6internet_async(
        self,
        request: main_models.DisableLoadBalancerIpv6InternetRequest,
    ) -> main_models.DisableLoadBalancerIpv6InternetResponse:
        runtime = RuntimeOptions()
        return await self.disable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def dissociate_acls_from_listener_with_options(
        self,
        request: main_models.DissociateAclsFromListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateAclsFromListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAclsFromListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateAclsFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_acls_from_listener_with_options_async(
        self,
        request: main_models.DissociateAclsFromListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateAclsFromListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAclsFromListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateAclsFromListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_acls_from_listener(
        self,
        request: main_models.DissociateAclsFromListenerRequest,
    ) -> main_models.DissociateAclsFromListenerResponse:
        runtime = RuntimeOptions()
        return self.dissociate_acls_from_listener_with_options(request, runtime)

    async def dissociate_acls_from_listener_async(
        self,
        request: main_models.DissociateAclsFromListenerRequest,
    ) -> main_models.DissociateAclsFromListenerResponse:
        runtime = RuntimeOptions()
        return await self.dissociate_acls_from_listener_with_options_async(request, runtime)

    def dissociate_additional_certificates_from_listener_with_options(
        self,
        request: main_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateAdditionalCertificatesFromListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAdditionalCertificatesFromListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateAdditionalCertificatesFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_additional_certificates_from_listener_with_options_async(
        self,
        request: main_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateAdditionalCertificatesFromListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAdditionalCertificatesFromListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateAdditionalCertificatesFromListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_additional_certificates_from_listener(
        self,
        request: main_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> main_models.DissociateAdditionalCertificatesFromListenerResponse:
        runtime = RuntimeOptions()
        return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)

    async def dissociate_additional_certificates_from_listener_async(
        self,
        request: main_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> main_models.DissociateAdditionalCertificatesFromListenerResponse:
        runtime = RuntimeOptions()
        return await self.dissociate_additional_certificates_from_listener_with_options_async(request, runtime)

    def enable_deletion_protection_with_options(
        self,
        request: main_models.EnableDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDeletionProtection',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_deletion_protection_with_options_async(
        self,
        request: main_models.EnableDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDeletionProtection',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_deletion_protection(
        self,
        request: main_models.EnableDeletionProtectionRequest,
    ) -> main_models.EnableDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return self.enable_deletion_protection_with_options(request, runtime)

    async def enable_deletion_protection_async(
        self,
        request: main_models.EnableDeletionProtectionRequest,
    ) -> main_models.EnableDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return await self.enable_deletion_protection_with_options_async(request, runtime)

    def enable_load_balancer_access_log_with_options(
        self,
        request: main_models.EnableLoadBalancerAccessLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLoadBalancerAccessLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLoadBalancerAccessLog',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLoadBalancerAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_load_balancer_access_log_with_options_async(
        self,
        request: main_models.EnableLoadBalancerAccessLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLoadBalancerAccessLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.log_store):
            query['LogStore'] = request.log_store
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLoadBalancerAccessLog',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLoadBalancerAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_load_balancer_access_log(
        self,
        request: main_models.EnableLoadBalancerAccessLogRequest,
    ) -> main_models.EnableLoadBalancerAccessLogResponse:
        runtime = RuntimeOptions()
        return self.enable_load_balancer_access_log_with_options(request, runtime)

    async def enable_load_balancer_access_log_async(
        self,
        request: main_models.EnableLoadBalancerAccessLogRequest,
    ) -> main_models.EnableLoadBalancerAccessLogResponse:
        runtime = RuntimeOptions()
        return await self.enable_load_balancer_access_log_with_options_async(request, runtime)

    def enable_load_balancer_ipv_6internet_with_options(
        self,
        request: main_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLoadBalancerIpv6InternetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLoadBalancerIpv6Internet',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLoadBalancerIpv6InternetResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_load_balancer_ipv_6internet_with_options_async(
        self,
        request: main_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLoadBalancerIpv6InternetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableLoadBalancerIpv6Internet',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableLoadBalancerIpv6InternetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_load_balancer_ipv_6internet(
        self,
        request: main_models.EnableLoadBalancerIpv6InternetRequest,
    ) -> main_models.EnableLoadBalancerIpv6InternetResponse:
        runtime = RuntimeOptions()
        return self.enable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def enable_load_balancer_ipv_6internet_async(
        self,
        request: main_models.EnableLoadBalancerIpv6InternetRequest,
    ) -> main_models.EnableLoadBalancerIpv6InternetResponse:
        runtime = RuntimeOptions()
        return await self.enable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def get_health_check_template_attribute_with_options(
        self,
        request: main_models.GetHealthCheckTemplateAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHealthCheckTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHealthCheckTemplateAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHealthCheckTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_health_check_template_attribute_with_options_async(
        self,
        request: main_models.GetHealthCheckTemplateAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHealthCheckTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHealthCheckTemplateAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHealthCheckTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_health_check_template_attribute(
        self,
        request: main_models.GetHealthCheckTemplateAttributeRequest,
    ) -> main_models.GetHealthCheckTemplateAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_health_check_template_attribute_with_options(request, runtime)

    async def get_health_check_template_attribute_async(
        self,
        request: main_models.GetHealthCheckTemplateAttributeRequest,
    ) -> main_models.GetHealthCheckTemplateAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_health_check_template_attribute_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: main_models.GetListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_attribute_with_options_async(
        self,
        request: main_models.GetListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_attribute(
        self,
        request: main_models.GetListenerAttributeRequest,
    ) -> main_models.GetListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_listener_attribute_with_options(request, runtime)

    async def get_listener_attribute_async(
        self,
        request: main_models.GetListenerAttributeRequest,
    ) -> main_models.GetListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_listener_attribute_with_options_async(request, runtime)

    def get_listener_health_status_with_options(
        self,
        request: main_models.GetListenerHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListenerHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerHealthStatus',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListenerHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_health_status_with_options_async(
        self,
        request: main_models.GetListenerHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListenerHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerHealthStatus',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListenerHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_health_status(
        self,
        request: main_models.GetListenerHealthStatusRequest,
    ) -> main_models.GetListenerHealthStatusResponse:
        runtime = RuntimeOptions()
        return self.get_listener_health_status_with_options(request, runtime)

    async def get_listener_health_status_async(
        self,
        request: main_models.GetListenerHealthStatusRequest,
    ) -> main_models.GetListenerHealthStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_listener_health_status_with_options_async(request, runtime)

    def get_load_balancer_attribute_with_options(
        self,
        request: main_models.GetLoadBalancerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoadBalancerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoadBalancerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_load_balancer_attribute_with_options_async(
        self,
        request: main_models.GetLoadBalancerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoadBalancerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoadBalancerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_load_balancer_attribute(
        self,
        request: main_models.GetLoadBalancerAttributeRequest,
    ) -> main_models.GetLoadBalancerAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_load_balancer_attribute_with_options(request, runtime)

    async def get_load_balancer_attribute_async(
        self,
        request: main_models.GetLoadBalancerAttributeRequest,
    ) -> main_models.GetLoadBalancerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_load_balancer_attribute_with_options_async(request, runtime)

    def list_ascripts_with_options(
        self,
        request: main_models.ListAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not DaraCore.is_null(request.ascript_names):
            query['AScriptNames'] = request.ascript_names
        if not DaraCore.is_null(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ascripts_with_options_async(
        self,
        request: main_models.ListAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not DaraCore.is_null(request.ascript_names):
            query['AScriptNames'] = request.ascript_names
        if not DaraCore.is_null(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ascripts(
        self,
        request: main_models.ListAScriptsRequest,
    ) -> main_models.ListAScriptsResponse:
        runtime = RuntimeOptions()
        return self.list_ascripts_with_options(request, runtime)

    async def list_ascripts_async(
        self,
        request: main_models.ListAScriptsRequest,
    ) -> main_models.ListAScriptsResponse:
        runtime = RuntimeOptions()
        return await self.list_ascripts_with_options_async(request, runtime)

    def list_acl_entries_with_options(
        self,
        request: main_models.ListAclEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAclEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAclEntries',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_entries_with_options_async(
        self,
        request: main_models.ListAclEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAclEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAclEntries',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_entries(
        self,
        request: main_models.ListAclEntriesRequest,
    ) -> main_models.ListAclEntriesResponse:
        runtime = RuntimeOptions()
        return self.list_acl_entries_with_options(request, runtime)

    async def list_acl_entries_async(
        self,
        request: main_models.ListAclEntriesRequest,
    ) -> main_models.ListAclEntriesResponse:
        runtime = RuntimeOptions()
        return await self.list_acl_entries_with_options_async(request, runtime)

    def list_acl_relations_with_options(
        self,
        request: main_models.ListAclRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAclRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAclRelations',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_relations_with_options_async(
        self,
        request: main_models.ListAclRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAclRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAclRelations',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_relations(
        self,
        request: main_models.ListAclRelationsRequest,
    ) -> main_models.ListAclRelationsResponse:
        runtime = RuntimeOptions()
        return self.list_acl_relations_with_options(request, runtime)

    async def list_acl_relations_async(
        self,
        request: main_models.ListAclRelationsRequest,
    ) -> main_models.ListAclRelationsResponse:
        runtime = RuntimeOptions()
        return await self.list_acl_relations_with_options_async(request, runtime)

    def list_acls_with_options(
        self,
        request: main_models.ListAclsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAclsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.acl_names):
            query['AclNames'] = request.acl_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcls',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acls_with_options_async(
        self,
        request: main_models.ListAclsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAclsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.acl_names):
            query['AclNames'] = request.acl_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcls',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAclsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acls(
        self,
        request: main_models.ListAclsRequest,
    ) -> main_models.ListAclsResponse:
        runtime = RuntimeOptions()
        return self.list_acls_with_options(request, runtime)

    async def list_acls_async(
        self,
        request: main_models.ListAclsRequest,
    ) -> main_models.ListAclsResponse:
        runtime = RuntimeOptions()
        return await self.list_acls_with_options_async(request, runtime)

    def list_asyn_jobs_with_options(
        self,
        request: main_models.ListAsynJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsynJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsynJobs',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsynJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asyn_jobs_with_options_async(
        self,
        request: main_models.ListAsynJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsynJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsynJobs',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsynJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_asyn_jobs(
        self,
        request: main_models.ListAsynJobsRequest,
    ) -> main_models.ListAsynJobsResponse:
        runtime = RuntimeOptions()
        return self.list_asyn_jobs_with_options(request, runtime)

    async def list_asyn_jobs_async(
        self,
        request: main_models.ListAsynJobsRequest,
    ) -> main_models.ListAsynJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_asyn_jobs_with_options_async(request, runtime)

    def list_health_check_templates_with_options(
        self,
        request: main_models.ListHealthCheckTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHealthCheckTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        if not DaraCore.is_null(request.health_check_template_names):
            query['HealthCheckTemplateNames'] = request.health_check_template_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHealthCheckTemplates',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHealthCheckTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_health_check_templates_with_options_async(
        self,
        request: main_models.ListHealthCheckTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHealthCheckTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        if not DaraCore.is_null(request.health_check_template_names):
            query['HealthCheckTemplateNames'] = request.health_check_template_names
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHealthCheckTemplates',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHealthCheckTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_health_check_templates(
        self,
        request: main_models.ListHealthCheckTemplatesRequest,
    ) -> main_models.ListHealthCheckTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_health_check_templates_with_options(request, runtime)

    async def list_health_check_templates_async(
        self,
        request: main_models.ListHealthCheckTemplatesRequest,
    ) -> main_models.ListHealthCheckTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_health_check_templates_with_options_async(request, runtime)

    def list_listener_certificates_with_options(
        self,
        request: main_models.ListListenerCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenerCertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_ids):
            query['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenerCertificates',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listener_certificates_with_options_async(
        self,
        request: main_models.ListListenerCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenerCertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_ids):
            query['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenerCertificates',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenerCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listener_certificates(
        self,
        request: main_models.ListListenerCertificatesRequest,
    ) -> main_models.ListListenerCertificatesResponse:
        runtime = RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    async def list_listener_certificates_async(
        self,
        request: main_models.ListListenerCertificatesRequest,
    ) -> main_models.ListListenerCertificatesResponse:
        runtime = RuntimeOptions()
        return await self.list_listener_certificates_with_options_async(request, runtime)

    def list_listeners_with_options(
        self,
        request: main_models.ListListenersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_with_options_async(
        self,
        request: main_models.ListListenersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners(
        self,
        request: main_models.ListListenersRequest,
    ) -> main_models.ListListenersResponse:
        runtime = RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    async def list_listeners_async(
        self,
        request: main_models.ListListenersRequest,
    ) -> main_models.ListListenersResponse:
        runtime = RuntimeOptions()
        return await self.list_listeners_with_options_async(request, runtime)

    def list_load_balancers_with_options(
        self,
        request: main_models.ListLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.dnsname):
            query['DNSName'] = request.dnsname
        if not DaraCore.is_null(request.ipv_6address_type):
            query['Ipv6AddressType'] = request.ipv_6address_type
        if not DaraCore.is_null(request.load_balancer_bussiness_status):
            query['LoadBalancerBussinessStatus'] = request.load_balancer_bussiness_status
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLoadBalancers',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_load_balancers_with_options_async(
        self,
        request: main_models.ListLoadBalancersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.dnsname):
            query['DNSName'] = request.dnsname
        if not DaraCore.is_null(request.ipv_6address_type):
            query['Ipv6AddressType'] = request.ipv_6address_type
        if not DaraCore.is_null(request.load_balancer_bussiness_status):
            query['LoadBalancerBussinessStatus'] = request.load_balancer_bussiness_status
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLoadBalancers',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_load_balancers(
        self,
        request: main_models.ListLoadBalancersRequest,
    ) -> main_models.ListLoadBalancersResponse:
        runtime = RuntimeOptions()
        return self.list_load_balancers_with_options(request, runtime)

    async def list_load_balancers_async(
        self,
        request: main_models.ListLoadBalancersRequest,
    ) -> main_models.ListLoadBalancersResponse:
        runtime = RuntimeOptions()
        return await self.list_load_balancers_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_security_policies_with_options(
        self,
        request: main_models.ListSecurityPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        if not DaraCore.is_null(request.security_policy_names):
            query['SecurityPolicyNames'] = request.security_policy_names
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityPolicies',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policies_with_options_async(
        self,
        request: main_models.ListSecurityPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        if not DaraCore.is_null(request.security_policy_names):
            query['SecurityPolicyNames'] = request.security_policy_names
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityPolicies',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policies(
        self,
        request: main_models.ListSecurityPoliciesRequest,
    ) -> main_models.ListSecurityPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_security_policies_with_options(request, runtime)

    async def list_security_policies_async(
        self,
        request: main_models.ListSecurityPoliciesRequest,
    ) -> main_models.ListSecurityPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_security_policies_with_options_async(request, runtime)

    def list_security_policy_relations_with_options(
        self,
        request: main_models.ListSecurityPolicyRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityPolicyRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityPolicyRelations',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityPolicyRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policy_relations_with_options_async(
        self,
        request: main_models.ListSecurityPolicyRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityPolicyRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityPolicyRelations',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityPolicyRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policy_relations(
        self,
        request: main_models.ListSecurityPolicyRelationsRequest,
    ) -> main_models.ListSecurityPolicyRelationsResponse:
        runtime = RuntimeOptions()
        return self.list_security_policy_relations_with_options(request, runtime)

    async def list_security_policy_relations_async(
        self,
        request: main_models.ListSecurityPolicyRelationsRequest,
    ) -> main_models.ListSecurityPolicyRelationsResponse:
        runtime = RuntimeOptions()
        return await self.list_security_policy_relations_with_options_async(request, runtime)

    def list_server_group_servers_with_options(
        self,
        request: main_models.ListServerGroupServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerGroupServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_ids):
            query['ServerIds'] = request.server_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroupServers',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerGroupServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_group_servers_with_options_async(
        self,
        request: main_models.ListServerGroupServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerGroupServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_ids):
            query['ServerIds'] = request.server_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroupServers',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerGroupServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_group_servers(
        self,
        request: main_models.ListServerGroupServersRequest,
    ) -> main_models.ListServerGroupServersResponse:
        runtime = RuntimeOptions()
        return self.list_server_group_servers_with_options(request, runtime)

    async def list_server_group_servers_async(
        self,
        request: main_models.ListServerGroupServersRequest,
    ) -> main_models.ListServerGroupServersResponse:
        runtime = RuntimeOptions()
        return await self.list_server_group_servers_with_options_async(request, runtime)

    def list_server_groups_with_options(
        self,
        request: main_models.ListServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.server_group_ids):
            query['ServerGroupIds'] = request.server_group_ids
        if not DaraCore.is_null(request.server_group_names):
            query['ServerGroupNames'] = request.server_group_names
        if not DaraCore.is_null(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroups',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_groups_with_options_async(
        self,
        request: main_models.ListServerGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.server_group_ids):
            query['ServerGroupIds'] = request.server_group_ids
        if not DaraCore.is_null(request.server_group_names):
            query['ServerGroupNames'] = request.server_group_names
        if not DaraCore.is_null(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroups',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_groups(
        self,
        request: main_models.ListServerGroupsRequest,
    ) -> main_models.ListServerGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_server_groups_with_options(request, runtime)

    async def list_server_groups_async(
        self,
        request: main_models.ListServerGroupsRequest,
    ) -> main_models.ListServerGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_server_groups_with_options_async(request, runtime)

    def list_system_security_policies_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemSecurityPoliciesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListSystemSecurityPolicies',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_security_policies_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemSecurityPoliciesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListSystemSecurityPolicies',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemSecurityPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_security_policies(self) -> main_models.ListSystemSecurityPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_system_security_policies_with_options(runtime)

    async def list_system_security_policies_async(self) -> main_models.ListSystemSecurityPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_system_security_policies_with_options_async(runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-06-16',
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
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-06-16',
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

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def load_balancer_join_security_group_with_options(
        self,
        request: main_models.LoadBalancerJoinSecurityGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadBalancerJoinSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerJoinSecurityGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadBalancerJoinSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_balancer_join_security_group_with_options_async(
        self,
        request: main_models.LoadBalancerJoinSecurityGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadBalancerJoinSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerJoinSecurityGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadBalancerJoinSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_balancer_join_security_group(
        self,
        request: main_models.LoadBalancerJoinSecurityGroupRequest,
    ) -> main_models.LoadBalancerJoinSecurityGroupResponse:
        runtime = RuntimeOptions()
        return self.load_balancer_join_security_group_with_options(request, runtime)

    async def load_balancer_join_security_group_async(
        self,
        request: main_models.LoadBalancerJoinSecurityGroupRequest,
    ) -> main_models.LoadBalancerJoinSecurityGroupResponse:
        runtime = RuntimeOptions()
        return await self.load_balancer_join_security_group_with_options_async(request, runtime)

    def load_balancer_leave_security_group_with_options(
        self,
        request: main_models.LoadBalancerLeaveSecurityGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadBalancerLeaveSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerLeaveSecurityGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadBalancerLeaveSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_balancer_leave_security_group_with_options_async(
        self,
        request: main_models.LoadBalancerLeaveSecurityGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadBalancerLeaveSecurityGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerLeaveSecurityGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LoadBalancerLeaveSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_balancer_leave_security_group(
        self,
        request: main_models.LoadBalancerLeaveSecurityGroupRequest,
    ) -> main_models.LoadBalancerLeaveSecurityGroupResponse:
        runtime = RuntimeOptions()
        return self.load_balancer_leave_security_group_with_options(request, runtime)

    async def load_balancer_leave_security_group_async(
        self,
        request: main_models.LoadBalancerLeaveSecurityGroupRequest,
    ) -> main_models.LoadBalancerLeaveSecurityGroupResponse:
        runtime = RuntimeOptions()
        return await self.load_balancer_leave_security_group_with_options_async(request, runtime)

    def modify_capacity_reservation_with_options(
        self,
        request: main_models.ModifyCapacityReservationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCapacityReservationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.minimum_load_balancer_capacity):
            query['MinimumLoadBalancerCapacity'] = request.minimum_load_balancer_capacity
        if not DaraCore.is_null(request.reset_capacity_reservation):
            query['ResetCapacityReservation'] = request.reset_capacity_reservation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCapacityReservation',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_capacity_reservation_with_options_async(
        self,
        request: main_models.ModifyCapacityReservationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCapacityReservationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.minimum_load_balancer_capacity):
            query['MinimumLoadBalancerCapacity'] = request.minimum_load_balancer_capacity
        if not DaraCore.is_null(request.reset_capacity_reservation):
            query['ResetCapacityReservation'] = request.reset_capacity_reservation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCapacityReservation',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCapacityReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_capacity_reservation(
        self,
        request: main_models.ModifyCapacityReservationRequest,
    ) -> main_models.ModifyCapacityReservationResponse:
        runtime = RuntimeOptions()
        return self.modify_capacity_reservation_with_options(request, runtime)

    async def modify_capacity_reservation_async(
        self,
        request: main_models.ModifyCapacityReservationRequest,
    ) -> main_models.ModifyCapacityReservationResponse:
        runtime = RuntimeOptions()
        return await self.modify_capacity_reservation_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2020-06-16',
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
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2020-06-16',
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

    def remove_entries_from_acl_with_options(
        self,
        request: main_models.RemoveEntriesFromAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveEntriesFromAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.entries):
            query['Entries'] = request.entries
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEntriesFromAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveEntriesFromAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_entries_from_acl_with_options_async(
        self,
        request: main_models.RemoveEntriesFromAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveEntriesFromAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.entries):
            query['Entries'] = request.entries
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEntriesFromAcl',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveEntriesFromAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_entries_from_acl(
        self,
        request: main_models.RemoveEntriesFromAclRequest,
    ) -> main_models.RemoveEntriesFromAclResponse:
        runtime = RuntimeOptions()
        return self.remove_entries_from_acl_with_options(request, runtime)

    async def remove_entries_from_acl_async(
        self,
        request: main_models.RemoveEntriesFromAclRequest,
    ) -> main_models.RemoveEntriesFromAclResponse:
        runtime = RuntimeOptions()
        return await self.remove_entries_from_acl_with_options_async(request, runtime)

    def remove_servers_from_server_group_with_options(
        self,
        request: main_models.RemoveServersFromServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveServersFromServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.servers):
            query['Servers'] = request.servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServersFromServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveServersFromServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_servers_from_server_group_with_options_async(
        self,
        request: main_models.RemoveServersFromServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveServersFromServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.servers):
            query['Servers'] = request.servers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServersFromServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveServersFromServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_servers_from_server_group(
        self,
        request: main_models.RemoveServersFromServerGroupRequest,
    ) -> main_models.RemoveServersFromServerGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_servers_from_server_group_with_options(request, runtime)

    async def remove_servers_from_server_group_async(
        self,
        request: main_models.RemoveServersFromServerGroupRequest,
    ) -> main_models.RemoveServersFromServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_servers_from_server_group_with_options_async(request, runtime)

    def replace_servers_in_server_group_with_options(
        self,
        request: main_models.ReplaceServersInServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceServersInServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.removed_servers):
            query['RemovedServers'] = request.removed_servers
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.added_servers):
            body_flat['AddedServers'] = request.added_servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceServersInServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceServersInServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_servers_in_server_group_with_options_async(
        self,
        request: main_models.ReplaceServersInServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceServersInServerGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.removed_servers):
            query['RemovedServers'] = request.removed_servers
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.added_servers):
            body_flat['AddedServers'] = request.added_servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceServersInServerGroup',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceServersInServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_servers_in_server_group(
        self,
        request: main_models.ReplaceServersInServerGroupRequest,
    ) -> main_models.ReplaceServersInServerGroupResponse:
        runtime = RuntimeOptions()
        return self.replace_servers_in_server_group_with_options(request, runtime)

    async def replace_servers_in_server_group_async(
        self,
        request: main_models.ReplaceServersInServerGroupRequest,
    ) -> main_models.ReplaceServersInServerGroupResponse:
        runtime = RuntimeOptions()
        return await self.replace_servers_in_server_group_with_options_async(request, runtime)

    def start_listener_with_options(
        self,
        request: main_models.StartListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_listener_with_options_async(
        self,
        request: main_models.StartListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_listener(
        self,
        request: main_models.StartListenerRequest,
    ) -> main_models.StartListenerResponse:
        runtime = RuntimeOptions()
        return self.start_listener_with_options(request, runtime)

    async def start_listener_async(
        self,
        request: main_models.StartListenerRequest,
    ) -> main_models.StartListenerResponse:
        runtime = RuntimeOptions()
        return await self.start_listener_with_options_async(request, runtime)

    def start_shift_load_balancer_zones_with_options(
        self,
        request: main_models.StartShiftLoadBalancerZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartShiftLoadBalancerZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartShiftLoadBalancerZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartShiftLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_shift_load_balancer_zones_with_options_async(
        self,
        request: main_models.StartShiftLoadBalancerZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartShiftLoadBalancerZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartShiftLoadBalancerZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartShiftLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_shift_load_balancer_zones(
        self,
        request: main_models.StartShiftLoadBalancerZonesRequest,
    ) -> main_models.StartShiftLoadBalancerZonesResponse:
        runtime = RuntimeOptions()
        return self.start_shift_load_balancer_zones_with_options(request, runtime)

    async def start_shift_load_balancer_zones_async(
        self,
        request: main_models.StartShiftLoadBalancerZonesRequest,
    ) -> main_models.StartShiftLoadBalancerZonesResponse:
        runtime = RuntimeOptions()
        return await self.start_shift_load_balancer_zones_with_options_async(request, runtime)

    def stop_listener_with_options(
        self,
        request: main_models.StopListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_listener_with_options_async(
        self,
        request: main_models.StopListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopListener',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_listener(
        self,
        request: main_models.StopListenerRequest,
    ) -> main_models.StopListenerResponse:
        runtime = RuntimeOptions()
        return self.stop_listener_with_options(request, runtime)

    async def stop_listener_async(
        self,
        request: main_models.StopListenerRequest,
    ) -> main_models.StopListenerResponse:
        runtime = RuntimeOptions()
        return await self.stop_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-06-16',
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
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-06-16',
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

    def un_tag_resources_with_options(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_ascripts_with_options(
        self,
        request: main_models.UpdateAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascripts):
            query['AScripts'] = request.ascripts
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ascripts_with_options_async(
        self,
        request: main_models.UpdateAScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascripts):
            query['AScripts'] = request.ascripts
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAScripts',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ascripts(
        self,
        request: main_models.UpdateAScriptsRequest,
    ) -> main_models.UpdateAScriptsResponse:
        runtime = RuntimeOptions()
        return self.update_ascripts_with_options(request, runtime)

    async def update_ascripts_async(
        self,
        request: main_models.UpdateAScriptsRequest,
    ) -> main_models.UpdateAScriptsResponse:
        runtime = RuntimeOptions()
        return await self.update_ascripts_with_options_async(request, runtime)

    def update_acl_attribute_with_options(
        self,
        request: main_models.UpdateAclAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAclAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAclAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAclAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_acl_attribute_with_options_async(
        self,
        request: main_models.UpdateAclAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAclAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAclAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAclAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_acl_attribute(
        self,
        request: main_models.UpdateAclAttributeRequest,
    ) -> main_models.UpdateAclAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_acl_attribute_with_options(request, runtime)

    async def update_acl_attribute_async(
        self,
        request: main_models.UpdateAclAttributeRequest,
    ) -> main_models.UpdateAclAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_acl_attribute_with_options_async(request, runtime)

    def update_health_check_template_attribute_with_options(
        self,
        request: main_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHealthCheckTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not DaraCore.is_null(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHealthCheckTemplateAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHealthCheckTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_health_check_template_attribute_with_options_async(
        self,
        request: main_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHealthCheckTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not DaraCore.is_null(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not DaraCore.is_null(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not DaraCore.is_null(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not DaraCore.is_null(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not DaraCore.is_null(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not DaraCore.is_null(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not DaraCore.is_null(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHealthCheckTemplateAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHealthCheckTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_health_check_template_attribute(
        self,
        request: main_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> main_models.UpdateHealthCheckTemplateAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_health_check_template_attribute_with_options(request, runtime)

    async def update_health_check_template_attribute_async(
        self,
        request: main_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> main_models.UpdateHealthCheckTemplateAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_health_check_template_attribute_with_options_async(request, runtime)

    def update_listener_attribute_with_options(
        self,
        request: main_models.UpdateListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not DaraCore.is_null(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not DaraCore.is_null(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_attribute_with_options_async(
        self,
        request: main_models.UpdateListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not DaraCore.is_null(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not DaraCore.is_null(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_attribute(
        self,
        request: main_models.UpdateListenerAttributeRequest,
    ) -> main_models.UpdateListenerAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_listener_attribute_with_options(request, runtime)

    async def update_listener_attribute_async(
        self,
        request: main_models.UpdateListenerAttributeRequest,
    ) -> main_models.UpdateListenerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_listener_attribute_with_options_async(request, runtime)

    def update_listener_log_config_with_options(
        self,
        request: main_models.UpdateListenerLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not DaraCore.is_null(request.access_log_tracing_config):
            query['AccessLogTracingConfig'] = request.access_log_tracing_config
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerLogConfig',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateListenerLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_log_config_with_options_async(
        self,
        request: main_models.UpdateListenerLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not DaraCore.is_null(request.access_log_tracing_config):
            query['AccessLogTracingConfig'] = request.access_log_tracing_config
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerLogConfig',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateListenerLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_log_config(
        self,
        request: main_models.UpdateListenerLogConfigRequest,
    ) -> main_models.UpdateListenerLogConfigResponse:
        runtime = RuntimeOptions()
        return self.update_listener_log_config_with_options(request, runtime)

    async def update_listener_log_config_async(
        self,
        request: main_models.UpdateListenerLogConfigRequest,
    ) -> main_models.UpdateListenerLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_listener_log_config_with_options_async(request, runtime)

    def update_load_balancer_address_type_config_with_options(
        self,
        request: main_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerAddressTypeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAddressTypeConfig',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_address_type_config_with_options_async(
        self,
        request: main_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerAddressTypeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAddressTypeConfig',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_address_type_config(
        self,
        request: main_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> main_models.UpdateLoadBalancerAddressTypeConfigResponse:
        runtime = RuntimeOptions()
        return self.update_load_balancer_address_type_config_with_options(request, runtime)

    async def update_load_balancer_address_type_config_async(
        self,
        request: main_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> main_models.UpdateLoadBalancerAddressTypeConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_load_balancer_address_type_config_with_options_async(request, runtime)

    def update_load_balancer_attribute_with_options(
        self,
        request: main_models.UpdateLoadBalancerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_attribute_with_options_async(
        self,
        request: main_models.UpdateLoadBalancerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_attribute(
        self,
        request: main_models.UpdateLoadBalancerAttributeRequest,
    ) -> main_models.UpdateLoadBalancerAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_load_balancer_attribute_with_options(request, runtime)

    async def update_load_balancer_attribute_async(
        self,
        request: main_models.UpdateLoadBalancerAttributeRequest,
    ) -> main_models.UpdateLoadBalancerAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_load_balancer_attribute_with_options_async(request, runtime)

    def update_load_balancer_edition_with_options(
        self,
        request: main_models.UpdateLoadBalancerEditionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerEditionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerEdition',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerEditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_edition_with_options_async(
        self,
        request: main_models.UpdateLoadBalancerEditionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerEditionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerEdition',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerEditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_edition(
        self,
        request: main_models.UpdateLoadBalancerEditionRequest,
    ) -> main_models.UpdateLoadBalancerEditionResponse:
        runtime = RuntimeOptions()
        return self.update_load_balancer_edition_with_options(request, runtime)

    async def update_load_balancer_edition_async(
        self,
        request: main_models.UpdateLoadBalancerEditionRequest,
    ) -> main_models.UpdateLoadBalancerEditionResponse:
        runtime = RuntimeOptions()
        return await self.update_load_balancer_edition_with_options_async(request, runtime)

    def update_load_balancer_zones_with_options(
        self,
        request: main_models.UpdateLoadBalancerZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_zones_with_options_async(
        self,
        request: main_models.UpdateLoadBalancerZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerZones',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_zones(
        self,
        request: main_models.UpdateLoadBalancerZonesRequest,
    ) -> main_models.UpdateLoadBalancerZonesResponse:
        runtime = RuntimeOptions()
        return self.update_load_balancer_zones_with_options(request, runtime)

    async def update_load_balancer_zones_async(
        self,
        request: main_models.UpdateLoadBalancerZonesRequest,
    ) -> main_models.UpdateLoadBalancerZonesResponse:
        runtime = RuntimeOptions()
        return await self.update_load_balancer_zones_with_options_async(request, runtime)

    def update_rule_attribute_with_options(
        self,
        request: main_models.UpdateRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_attribute_with_options_async(
        self,
        request: main_models.UpdateRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not DaraCore.is_null(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_attribute(
        self,
        request: main_models.UpdateRuleAttributeRequest,
    ) -> main_models.UpdateRuleAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_rule_attribute_with_options(request, runtime)

    async def update_rule_attribute_async(
        self,
        request: main_models.UpdateRuleAttributeRequest,
    ) -> main_models.UpdateRuleAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_rule_attribute_with_options_async(request, runtime)

    def update_rules_attribute_with_options(
        self,
        request: main_models.UpdateRulesAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRulesAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.rules):
            body_flat['Rules'] = request.rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRulesAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRulesAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rules_attribute_with_options_async(
        self,
        request: main_models.UpdateRulesAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRulesAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.rules):
            body_flat['Rules'] = request.rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRulesAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRulesAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rules_attribute(
        self,
        request: main_models.UpdateRulesAttributeRequest,
    ) -> main_models.UpdateRulesAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_rules_attribute_with_options(request, runtime)

    async def update_rules_attribute_async(
        self,
        request: main_models.UpdateRulesAttributeRequest,
    ) -> main_models.UpdateRulesAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_rules_attribute_with_options_async(request, runtime)

    def update_security_policy_attribute_with_options(
        self,
        request: main_models.UpdateSecurityPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityPolicyAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_policy_attribute_with_options_async(
        self,
        request: main_models.UpdateSecurityPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityPolicyAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityPolicyAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_policy_attribute(
        self,
        request: main_models.UpdateSecurityPolicyAttributeRequest,
    ) -> main_models.UpdateSecurityPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_security_policy_attribute_with_options(request, runtime)

    async def update_security_policy_attribute_async(
        self,
        request: main_models.UpdateSecurityPolicyAttributeRequest,
    ) -> main_models.UpdateSecurityPolicyAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_security_policy_attribute_with_options_async(request, runtime)

    def update_server_group_attribute_with_options(
        self,
        request: main_models.UpdateServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServerGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.cross_zone_enabled):
            query['CrossZoneEnabled'] = request.cross_zone_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not DaraCore.is_null(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not DaraCore.is_null(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not DaraCore.is_null(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_attribute_with_options_async(
        self,
        request: main_models.UpdateServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServerGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.cross_zone_enabled):
            query['CrossZoneEnabled'] = request.cross_zone_enabled
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not DaraCore.is_null(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not DaraCore.is_null(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not DaraCore.is_null(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_attribute(
        self,
        request: main_models.UpdateServerGroupAttributeRequest,
    ) -> main_models.UpdateServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_server_group_attribute_with_options(request, runtime)

    async def update_server_group_attribute_async(
        self,
        request: main_models.UpdateServerGroupAttributeRequest,
    ) -> main_models.UpdateServerGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_server_group_attribute_with_options_async(request, runtime)

    def update_server_group_servers_attribute_with_options(
        self,
        request: main_models.UpdateServerGroupServersAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServerGroupServersAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupServersAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServerGroupServersAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_servers_attribute_with_options_async(
        self,
        request: main_models.UpdateServerGroupServersAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServerGroupServersAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupServersAttribute',
            version = '2020-06-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServerGroupServersAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_servers_attribute(
        self,
        request: main_models.UpdateServerGroupServersAttributeRequest,
    ) -> main_models.UpdateServerGroupServersAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_server_group_servers_attribute_with_options(request, runtime)

    async def update_server_group_servers_attribute_async(
        self,
        request: main_models.UpdateServerGroupServersAttributeRequest,
    ) -> main_models.UpdateServerGroupServersAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_server_group_servers_attribute_with_options_async(request, runtime)
