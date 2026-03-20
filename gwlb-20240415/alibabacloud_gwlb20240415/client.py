# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gwlb20240415 import models as main_models
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
        self._endpoint = self.get_endpoint('gwlb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_servers_to_server_group_with_options(
        self,
        request: main_models.AddServersToServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddServersToServerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddServersToServerGroup',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddServersToServerGroup',
            version = '2024-04-15',
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

    def create_listener_with_options(
        self,
        request: main_models.CreateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateListenerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLoadBalancer',
            version = '2024-04-15',
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

    def create_server_group_with_options(
        self,
        request: main_models.CreateServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not DaraCore.is_null(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerGroup',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not DaraCore.is_null(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerGroup',
            version = '2024-04-15',
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

    def delete_listener_with_options(
        self,
        request: main_models.DeleteListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteListenerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2024-04-15',
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

    def delete_server_group_with_options(
        self,
        request: main_models.DeleteServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerGroup',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerGroup',
            version = '2024-04-15',
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

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2024-04-15',
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

    def get_listener_attribute_with_options(
        self,
        request: main_models.GetListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListenerAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerAttribute',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerAttribute',
            version = '2024-04-15',
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
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.filter):
            body_flat['Filter'] = request.filter
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerHealthStatus',
            version = '2024-04-15',
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
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.filter):
            body_flat['Filter'] = request.filter
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerHealthStatus',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLoadBalancerAttribute',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLoadBalancerAttribute',
            version = '2024-04-15',
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

    def list_listeners_with_options(
        self,
        request: main_models.ListListenersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenersResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.listener_ids):
            body_flat['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2024-04-15',
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
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.listener_ids):
            body_flat['ListenerIds'] = request.listener_ids
        if not DaraCore.is_null(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.load_balancer_business_status):
            body['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        body_flat = {}
        if not DaraCore.is_null(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.load_balancer_names):
            body_flat['LoadBalancerNames'] = request.load_balancer_names
        if not DaraCore.is_null(request.load_balancer_status):
            body['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        if not DaraCore.is_null(request.vpc_ids):
            body_flat['VpcIds'] = request.vpc_ids
        if not DaraCore.is_null(request.zone_ids):
            body_flat['ZoneIds'] = request.zone_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLoadBalancers',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not DaraCore.is_null(request.load_balancer_business_status):
            body['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        body_flat = {}
        if not DaraCore.is_null(request.load_balancer_ids):
            body_flat['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.load_balancer_names):
            body_flat['LoadBalancerNames'] = request.load_balancer_names
        if not DaraCore.is_null(request.load_balancer_status):
            body['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        if not DaraCore.is_null(request.vpc_ids):
            body_flat['VpcIds'] = request.vpc_ids
        if not DaraCore.is_null(request.zone_ids):
            body_flat['ZoneIds'] = request.zone_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLoadBalancers',
            version = '2024-04-15',
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

    def list_server_group_servers_with_options(
        self,
        request: main_models.ListServerGroupServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerGroupServersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.server_ids):
            body_flat['ServerIds'] = request.server_ids
        if not DaraCore.is_null(request.server_ips):
            body_flat['ServerIps'] = request.server_ips
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroupServers',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.server_ids):
            body_flat['ServerIds'] = request.server_ids
        if not DaraCore.is_null(request.server_ips):
            body_flat['ServerIps'] = request.server_ips
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroupServers',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not DaraCore.is_null(request.server_group_ids):
            body_flat['ServerGroupIds'] = request.server_group_ids
        if not DaraCore.is_null(request.server_group_names):
            body_flat['ServerGroupNames'] = request.server_group_names
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroups',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        body_flat = {}
        if not DaraCore.is_null(request.server_group_ids):
            body_flat['ServerGroupIds'] = request.server_group_ids
        if not DaraCore.is_null(request.server_group_names):
            body_flat['ServerGroupNames'] = request.server_group_names
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.skip):
            body['Skip'] = request.skip
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroups',
            version = '2024-04-15',
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

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-04-15',
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

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2024-04-15',
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

    def remove_servers_from_server_group_with_options(
        self,
        request: main_models.RemoveServersFromServerGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveServersFromServerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServersFromServerGroup',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        body_flat = {}
        if not DaraCore.is_null(request.servers):
            body_flat['Servers'] = request.servers
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServersFromServerGroup',
            version = '2024-04-15',
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

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body_flat['Tag'] = request.tag
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2024-04-15',
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

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.all):
            body['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2024-04-15',
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

    def update_listener_attribute_with_options(
        self,
        request: main_models.UpdateListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerAttribute',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.tcp_idle_timeout):
            body['TcpIdleTimeout'] = request.tcp_idle_timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerAttribute',
            version = '2024-04-15',
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

    def update_load_balancer_attribute_with_options(
        self,
        request: main_models.UpdateLoadBalancerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAttribute',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.traffic_mode):
            body['TrafficMode'] = request.traffic_mode
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAttribute',
            version = '2024-04-15',
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

    def update_load_balancer_zones_with_options(
        self,
        request: main_models.UpdateLoadBalancerZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerZonesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        body_flat = {}
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerZones',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        body_flat = {}
        if not DaraCore.is_null(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerZones',
            version = '2024-04-15',
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

    def update_server_group_attribute_with_options(
        self,
        request: main_models.UpdateServerGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServerGroupAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupAttribute',
            version = '2024-04-15',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.connection_drain_config):
            body_flat['ConnectionDrainConfig'] = request.connection_drain_config
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_failover_mode):
            body['ServerFailoverMode'] = request.server_failover_mode
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupAttribute',
            version = '2024-04-15',
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
