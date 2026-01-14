# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_nlb20220430 import models as main_models
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
        self._endpoint = self.get_endpoint('nlb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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

    def associate_additional_certificates_with_listener_with_options(
        self,
        request: main_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateAdditionalCertificatesWithListenerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAdditionalCertificatesWithListener',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAdditionalCertificatesWithListener',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachCommonBandwidthPackageToLoadBalancer',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachCommonBandwidthPackageToLoadBalancer',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelShiftLoadBalancerZones',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelShiftLoadBalancerZones',
            version = '2022-04-30',
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

    def create_listener_with_options(
        self,
        tmp_req: main_models.CreateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateListenerResponse:
        tmp_req.validate()
        request = main_models.CreateListenerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = Utils.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
        body = {}
        if not DaraCore.is_null(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not DaraCore.is_null(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not DaraCore.is_null(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not DaraCore.is_null(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cps):
            body['Cps'] = request.cps
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.end_port):
            body['EndPort'] = request.end_port
        if not DaraCore.is_null(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_port):
            body['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            body['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.mss):
            body['Mss'] = request.mss
        if not DaraCore.is_null(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not DaraCore.is_null(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.start_port):
            body['StartPort'] = request.start_port
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2022-04-30',
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
        tmp_req: main_models.CreateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateListenerResponse:
        tmp_req.validate()
        request = main_models.CreateListenerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = Utils.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
        body = {}
        if not DaraCore.is_null(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not DaraCore.is_null(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not DaraCore.is_null(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not DaraCore.is_null(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cps):
            body['Cps'] = request.cps
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.end_port):
            body['EndPort'] = request.end_port
        if not DaraCore.is_null(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_port):
            body['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            body['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.mss):
            body['Mss'] = request.mss
        if not DaraCore.is_null(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not DaraCore.is_null(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.start_port):
            body['StartPort'] = request.start_port
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.deletion_protection_config):
            body_flat['DeletionProtectionConfig'] = request.deletion_protection_config
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_billing_config):
            body_flat['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.load_balancer_type):
            body['LoadBalancerType'] = request.load_balancer_type
        if not DaraCore.is_null(request.modification_protection_config):
            body_flat['ModificationProtectionConfig'] = request.modification_protection_config
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not DaraCore.is_null(request.deletion_protection_config):
            body_flat['DeletionProtectionConfig'] = request.deletion_protection_config
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_billing_config):
            body_flat['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.load_balancer_type):
            body['LoadBalancerType'] = request.load_balancer_type
        if not DaraCore.is_null(request.modification_protection_config):
            body_flat['ModificationProtectionConfig'] = request.modification_protection_config
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
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
            version = '2022-04-30',
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

    def create_security_policy_with_options(
        self,
        request: main_models.CreateSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityPolicy',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityPolicy',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.address_ipversion):
            body['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.any_port_enabled):
            body['AnyPortEnabled'] = request.any_port_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not DaraCore.is_null(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.ip_version_affinity_mode):
            body['IpVersionAffinityMode'] = request.ip_version_affinity_mode
        if not DaraCore.is_null(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerGroup',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.address_ipversion):
            body['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.any_port_enabled):
            body['AnyPortEnabled'] = request.any_port_enabled
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not DaraCore.is_null(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.ip_version_affinity_mode):
            body['IpVersionAffinityMode'] = request.ip_version_affinity_mode
        if not DaraCore.is_null(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerGroup',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLoadBalancer',
            version = '2022-04-30',
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

    def delete_security_policy_with_options(
        self,
        request: main_models.DeleteSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityPolicy',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityPolicy',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerGroup',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerGroup',
            version = '2022-04-30',
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

    def describe_hd_monitor_region_config_with_options(
        self,
        request: main_models.DescribeHdMonitorRegionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHdMonitorRegionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHdMonitorRegionConfig',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHdMonitorRegionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hd_monitor_region_config_with_options_async(
        self,
        request: main_models.DescribeHdMonitorRegionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHdMonitorRegionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHdMonitorRegionConfig',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHdMonitorRegionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hd_monitor_region_config(
        self,
        request: main_models.DescribeHdMonitorRegionConfigRequest,
    ) -> main_models.DescribeHdMonitorRegionConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_hd_monitor_region_config_with_options(request, runtime)

    async def describe_hd_monitor_region_config_async(
        self,
        request: main_models.DescribeHdMonitorRegionConfigRequest,
    ) -> main_models.DescribeHdMonitorRegionConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_hd_monitor_region_config_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachCommonBandwidthPackageFromLoadBalancer',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachCommonBandwidthPackageFromLoadBalancer',
            version = '2022-04-30',
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

    def disable_load_balancer_ipv_6internet_with_options(
        self,
        request: main_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableLoadBalancerIpv6InternetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableLoadBalancerIpv6Internet',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableLoadBalancerIpv6Internet',
            version = '2022-04-30',
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

    def disassociate_additional_certificates_with_listener_with_options(
        self,
        request: main_models.DisassociateAdditionalCertificatesWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateAdditionalCertificatesWithListenerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateAdditionalCertificatesWithListener',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_additional_certificates_with_listener_with_options_async(
        self,
        request: main_models.DisassociateAdditionalCertificatesWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateAdditionalCertificatesWithListenerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateAdditionalCertificatesWithListener',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateAdditionalCertificatesWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_additional_certificates_with_listener(
        self,
        request: main_models.DisassociateAdditionalCertificatesWithListenerRequest,
    ) -> main_models.DisassociateAdditionalCertificatesWithListenerResponse:
        runtime = RuntimeOptions()
        return self.disassociate_additional_certificates_with_listener_with_options(request, runtime)

    async def disassociate_additional_certificates_with_listener_async(
        self,
        request: main_models.DisassociateAdditionalCertificatesWithListenerRequest,
    ) -> main_models.DisassociateAdditionalCertificatesWithListenerResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_additional_certificates_with_listener_with_options_async(request, runtime)

    def enable_load_balancer_ipv_6internet_with_options(
        self,
        request: main_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableLoadBalancerIpv6InternetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableLoadBalancerIpv6Internet',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableLoadBalancerIpv6Internet',
            version = '2022-04-30',
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

    def get_job_status_with_options(
        self,
        request: main_models.GetJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobStatus',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_status_with_options_async(
        self,
        request: main_models.GetJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobStatus',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_status(
        self,
        request: main_models.GetJobStatusRequest,
    ) -> main_models.GetJobStatusResponse:
        runtime = RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    async def get_job_status_async(
        self,
        request: main_models.GetJobStatusRequest,
    ) -> main_models.GetJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_job_status_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: main_models.GetListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListenerAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerAttribute',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerAttribute',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerHealthStatus',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListenerHealthStatus',
            version = '2022-04-30',
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
            action = 'GetLoadBalancerAttribute',
            version = '2022-04-30',
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
            action = 'GetLoadBalancerAttribute',
            version = '2022-04-30',
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

    def list_asyn_jobs_with_options(
        self,
        request: main_models.ListAsynJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsynJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsynJobs',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsynJobs',
            version = '2022-04-30',
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

    def list_listener_certificates_with_options(
        self,
        request: main_models.ListListenerCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenerCertificatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cert_type):
            body['CertType'] = request.cert_type
        if not DaraCore.is_null(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListListenerCertificates',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.cert_type):
            body['CertType'] = request.cert_type
        if not DaraCore.is_null(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListListenerCertificates',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sec_sensor_enabled):
            query['SecSensorEnabled'] = request.sec_sensor_enabled
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sec_sensor_enabled):
            query['SecSensorEnabled'] = request.sec_sensor_enabled
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.load_balancer_business_status):
            query['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.load_balancer_type):
            query['LoadBalancerType'] = request.load_balancer_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.load_balancer_business_status):
            query['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        if not DaraCore.is_null(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not DaraCore.is_null(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not DaraCore.is_null(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not DaraCore.is_null(request.load_balancer_type):
            query['LoadBalancerType'] = request.load_balancer_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2022-04-30',
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

    def list_security_policy_with_options(
        self,
        request: main_models.ListSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_ids):
            body['SecurityPolicyIds'] = request.security_policy_ids
        if not DaraCore.is_null(request.security_policy_names):
            body['SecurityPolicyNames'] = request.security_policy_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityPolicy',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policy_with_options_async(
        self,
        request: main_models.ListSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_policy_ids):
            body['SecurityPolicyIds'] = request.security_policy_ids
        if not DaraCore.is_null(request.security_policy_names):
            body['SecurityPolicyNames'] = request.security_policy_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityPolicy',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policy(
        self,
        request: main_models.ListSecurityPolicyRequest,
    ) -> main_models.ListSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_security_policy_with_options(request, runtime)

    async def list_security_policy_async(
        self,
        request: main_models.ListSecurityPolicyRequest,
    ) -> main_models.ListSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_security_policy_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_ids):
            body['ServerIds'] = request.server_ids
        if not DaraCore.is_null(request.server_ips):
            body['ServerIps'] = request.server_ips
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroupServers',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.server_ids):
            body['ServerIds'] = request.server_ids
        if not DaraCore.is_null(request.server_ips):
            body['ServerIps'] = request.server_ips
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroupServers',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.server_group_ids):
            body['ServerGroupIds'] = request.server_group_ids
        if not DaraCore.is_null(request.server_group_names):
            body['ServerGroupNames'] = request.server_group_names
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroups',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.server_group_ids):
            body['ServerGroupIds'] = request.server_group_ids
        if not DaraCore.is_null(request.server_group_names):
            body['ServerGroupNames'] = request.server_group_names
        if not DaraCore.is_null(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServerGroups',
            version = '2022-04-30',
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

    def list_system_security_policy_with_options(
        self,
        request: main_models.ListSystemSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemSecurityPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemSecurityPolicy',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_security_policy_with_options_async(
        self,
        request: main_models.ListSystemSecurityPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemSecurityPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemSecurityPolicy',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_security_policy(
        self,
        request: main_models.ListSystemSecurityPolicyRequest,
    ) -> main_models.ListSystemSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_system_security_policy_with_options(request, runtime)

    async def list_system_security_policy_async(
        self,
        request: main_models.ListSystemSecurityPolicyRequest,
    ) -> main_models.ListSystemSecurityPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_system_security_policy_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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

    def load_balancer_join_security_group_with_options(
        self,
        request: main_models.LoadBalancerJoinSecurityGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LoadBalancerJoinSecurityGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerJoinSecurityGroup',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerJoinSecurityGroup',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerLeaveSecurityGroup',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LoadBalancerLeaveSecurityGroup',
            version = '2022-04-30',
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

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.servers):
            body['Servers'] = request.servers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServersFromServerGroup',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.servers):
            body['Servers'] = request.servers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServersFromServerGroup',
            version = '2022-04-30',
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

    def set_hd_monitor_region_config_with_options(
        self,
        request: main_models.SetHdMonitorRegionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetHdMonitorRegionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.metric_store):
            query['MetricStore'] = request.metric_store
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetHdMonitorRegionConfig',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetHdMonitorRegionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_hd_monitor_region_config_with_options_async(
        self,
        request: main_models.SetHdMonitorRegionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetHdMonitorRegionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_project):
            query['LogProject'] = request.log_project
        if not DaraCore.is_null(request.metric_store):
            query['MetricStore'] = request.metric_store
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetHdMonitorRegionConfig',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetHdMonitorRegionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_hd_monitor_region_config(
        self,
        request: main_models.SetHdMonitorRegionConfigRequest,
    ) -> main_models.SetHdMonitorRegionConfigResponse:
        runtime = RuntimeOptions()
        return self.set_hd_monitor_region_config_with_options(request, runtime)

    async def set_hd_monitor_region_config_async(
        self,
        request: main_models.SetHdMonitorRegionConfigRequest,
    ) -> main_models.SetHdMonitorRegionConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_hd_monitor_region_config_with_options_async(request, runtime)

    def start_listener_with_options(
        self,
        request: main_models.StartListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartListenerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartListener',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartListener',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartShiftLoadBalancerZones',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartShiftLoadBalancerZones',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopListener',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopListener',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
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
            version = '2022-04-30',
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
        tmp_req: main_models.UpdateListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerAttributeResponse:
        tmp_req.validate()
        request = main_models.UpdateListenerAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = Utils.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
        body = {}
        if not DaraCore.is_null(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not DaraCore.is_null(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not DaraCore.is_null(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not DaraCore.is_null(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cps):
            body['Cps'] = request.cps
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.mss):
            body['Mss'] = request.mss
        if not DaraCore.is_null(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not DaraCore.is_null(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerAttribute',
            version = '2022-04-30',
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
        tmp_req: main_models.UpdateListenerAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerAttributeResponse:
        tmp_req.validate()
        request = main_models.UpdateListenerAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = Utils.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
        body = {}
        if not DaraCore.is_null(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not DaraCore.is_null(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not DaraCore.is_null(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not DaraCore.is_null(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not DaraCore.is_null(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cps):
            body['Cps'] = request.cps
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not DaraCore.is_null(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.mss):
            body['Mss'] = request.mss
        if not DaraCore.is_null(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not DaraCore.is_null(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateListenerAttribute',
            version = '2022-04-30',
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

    def update_load_balancer_address_type_config_with_options(
        self,
        request: main_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerAddressTypeConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAddressTypeConfig',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.address_type):
            body['AddressType'] = request.address_type
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAddressTypeConfig',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cps):
            body['Cps'] = request.cps
        if not DaraCore.is_null(request.cross_zone_enabled):
            body['CrossZoneEnabled'] = request.cross_zone_enabled
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAttribute',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.cps):
            body['Cps'] = request.cps
        if not DaraCore.is_null(request.cross_zone_enabled):
            body['CrossZoneEnabled'] = request.cross_zone_enabled
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerAttribute',
            version = '2022-04-30',
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

    def update_load_balancer_protection_with_options(
        self,
        request: main_models.UpdateLoadBalancerProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerProtectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection_enabled):
            body['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not DaraCore.is_null(request.deletion_protection_reason):
            body['DeletionProtectionReason'] = request.deletion_protection_reason
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.modification_protection_reason):
            body['ModificationProtectionReason'] = request.modification_protection_reason
        if not DaraCore.is_null(request.modification_protection_status):
            body['ModificationProtectionStatus'] = request.modification_protection_status
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerProtection',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_protection_with_options_async(
        self,
        request: main_models.UpdateLoadBalancerProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLoadBalancerProtectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection_enabled):
            body['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not DaraCore.is_null(request.deletion_protection_reason):
            body['DeletionProtectionReason'] = request.deletion_protection_reason
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.modification_protection_reason):
            body['ModificationProtectionReason'] = request.modification_protection_reason
        if not DaraCore.is_null(request.modification_protection_status):
            body['ModificationProtectionStatus'] = request.modification_protection_status
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerProtection',
            version = '2022-04-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLoadBalancerProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_protection(
        self,
        request: main_models.UpdateLoadBalancerProtectionRequest,
    ) -> main_models.UpdateLoadBalancerProtectionResponse:
        runtime = RuntimeOptions()
        return self.update_load_balancer_protection_with_options(request, runtime)

    async def update_load_balancer_protection_async(
        self,
        request: main_models.UpdateLoadBalancerProtectionRequest,
    ) -> main_models.UpdateLoadBalancerProtectionResponse:
        runtime = RuntimeOptions()
        return await self.update_load_balancer_protection_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerZones',
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLoadBalancerZones',
            version = '2022-04-30',
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

    def update_security_policy_attribute_with_options(
        self,
        request: main_models.UpdateSecurityPolicyAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityPolicyAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityPolicyAttribute',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not DaraCore.is_null(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityPolicyAttribute',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not DaraCore.is_null(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.ip_version_affinity_mode):
            body['IpVersionAffinityMode'] = request.ip_version_affinity_mode
        if not DaraCore.is_null(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
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
            version = '2022-04-30',
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
        if not DaraCore.is_null(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not DaraCore.is_null(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not DaraCore.is_null(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.ip_version_affinity_mode):
            body['IpVersionAffinityMode'] = request.ip_version_affinity_mode
        if not DaraCore.is_null(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scheduler):
            body['Scheduler'] = request.scheduler
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
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.servers):
            body['Servers'] = request.servers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupServersAttribute',
            version = '2022-04-30',
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
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            body['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not DaraCore.is_null(request.servers):
            body['Servers'] = request.servers
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServerGroupServersAttribute',
            version = '2022-04-30',
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
