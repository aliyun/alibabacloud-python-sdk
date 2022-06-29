# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nlb20220430 import models as nlb_20220430_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_servers_to_server_group_with_options(
        self,
        request: nlb_20220430_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.AddServersToServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            body['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.AddServersToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_servers_to_server_group_with_options_async(
        self,
        request: nlb_20220430_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.AddServersToServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            body['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.AddServersToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_servers_to_server_group(
        self,
        request: nlb_20220430_models.AddServersToServerGroupRequest,
    ) -> nlb_20220430_models.AddServersToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_servers_to_server_group_with_options(request, runtime)

    async def add_servers_to_server_group_async(
        self,
        request: nlb_20220430_models.AddServersToServerGroupRequest,
    ) -> nlb_20220430_models.AddServersToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_servers_to_server_group_with_options_async(request, runtime)

    def attach_common_bandwidth_package_to_load_balancer_with_options(
        self,
        request: nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachCommonBandwidthPackageToLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_common_bandwidth_package_to_load_balancer_with_options_async(
        self,
        request: nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachCommonBandwidthPackageToLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_common_bandwidth_package_to_load_balancer(
        self,
        request: nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_common_bandwidth_package_to_load_balancer_with_options(request, runtime)

    async def attach_common_bandwidth_package_to_load_balancer_async(
        self,
        request: nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_common_bandwidth_package_to_load_balancer_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        request: nlb_20220430_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not UtilClient.is_unset(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not UtilClient.is_unset(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not UtilClient.is_unset(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cps):
            body['Cps'] = request.cps
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_port):
            body['EndPort'] = request.end_port
        if not UtilClient.is_unset(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_port):
            body['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            body['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.start_port):
            body['StartPort'] = request.start_port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_listener_with_options_async(
        self,
        request: nlb_20220430_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not UtilClient.is_unset(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not UtilClient.is_unset(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not UtilClient.is_unset(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cps):
            body['Cps'] = request.cps
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_port):
            body['EndPort'] = request.end_port
        if not UtilClient.is_unset(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_port):
            body['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            body['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.start_port):
            body['StartPort'] = request.start_port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_listener(
        self,
        request: nlb_20220430_models.CreateListenerRequest,
    ) -> nlb_20220430_models.CreateListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    async def create_listener_async(
        self,
        request: nlb_20220430_models.CreateListenerRequest,
    ) -> nlb_20220430_models.CreateListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_listener_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: nlb_20220430_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        body_flat = {}
        if not UtilClient.is_unset(request.billing_config):
            body_flat['BillingConfig'] = request.billing_config
        if not UtilClient.is_unset(request.biz_flag):
            body['BizFlag'] = request.biz_flag
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.common_bandwidth_package_id):
            body['CommonBandwidthPackageId'] = request.common_bandwidth_package_id
        if not UtilClient.is_unset(request.cross_zone_enabled):
            body['CrossZoneEnabled'] = request.cross_zone_enabled
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_type):
            body['LoadBalancerType'] = request.load_balancer_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_groups):
            body['SecurityGroups'] = request.security_groups
        if not UtilClient.is_unset(request.traffic_affinity_enabled):
            body['TrafficAffinityEnabled'] = request.traffic_affinity_enabled
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: nlb_20220430_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        body_flat = {}
        if not UtilClient.is_unset(request.billing_config):
            body_flat['BillingConfig'] = request.billing_config
        if not UtilClient.is_unset(request.biz_flag):
            body['BizFlag'] = request.biz_flag
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.common_bandwidth_package_id):
            body['CommonBandwidthPackageId'] = request.common_bandwidth_package_id
        if not UtilClient.is_unset(request.cross_zone_enabled):
            body['CrossZoneEnabled'] = request.cross_zone_enabled
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_type):
            body['LoadBalancerType'] = request.load_balancer_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_groups):
            body['SecurityGroups'] = request.security_groups
        if not UtilClient.is_unset(request.traffic_affinity_enabled):
            body['TrafficAffinityEnabled'] = request.traffic_affinity_enabled
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer(
        self,
        request: nlb_20220430_models.CreateLoadBalancerRequest,
    ) -> nlb_20220430_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: nlb_20220430_models.CreateLoadBalancerRequest,
    ) -> nlb_20220430_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_security_policy_with_options(
        self,
        request: nlb_20220430_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateSecurityPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_policy_with_options_async(
        self,
        request: nlb_20220430_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateSecurityPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_policy(
        self,
        request: nlb_20220430_models.CreateSecurityPolicyRequest,
    ) -> nlb_20220430_models.CreateSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_security_policy_with_options(request, runtime)

    async def create_security_policy_async(
        self,
        request: nlb_20220430_models.CreateSecurityPolicyRequest,
    ) -> nlb_20220430_models.CreateSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_security_policy_with_options_async(request, runtime)

    def create_server_group_with_options(
        self,
        request: nlb_20220430_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ipversion):
            body['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not UtilClient.is_unset(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.persistence_enabled):
            body['PersistenceEnabled'] = request.persistence_enabled
        if not UtilClient.is_unset(request.persistence_timeout):
            body['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_group_with_options_async(
        self,
        request: nlb_20220430_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ipversion):
            body['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not UtilClient.is_unset(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.persistence_enabled):
            body['PersistenceEnabled'] = request.persistence_enabled
        if not UtilClient.is_unset(request.persistence_timeout):
            body['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.CreateServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_group(
        self,
        request: nlb_20220430_models.CreateServerGroupRequest,
    ) -> nlb_20220430_models.CreateServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_server_group_with_options(request, runtime)

    async def create_server_group_async(
        self,
        request: nlb_20220430_models.CreateServerGroupRequest,
    ) -> nlb_20220430_models.CreateServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_server_group_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: nlb_20220430_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_listener_with_options_async(
        self,
        request: nlb_20220430_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_listener(
        self,
        request: nlb_20220430_models.DeleteListenerRequest,
    ) -> nlb_20220430_models.DeleteListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    async def delete_listener_async(
        self,
        request: nlb_20220430_models.DeleteListenerRequest,
    ) -> nlb_20220430_models.DeleteListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_listener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: nlb_20220430_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: nlb_20220430_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer(
        self,
        request: nlb_20220430_models.DeleteLoadBalancerRequest,
    ) -> nlb_20220430_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: nlb_20220430_models.DeleteLoadBalancerRequest,
    ) -> nlb_20220430_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_security_policy_with_options(
        self,
        request: nlb_20220430_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteSecurityPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_policy_with_options_async(
        self,
        request: nlb_20220430_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteSecurityPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_policy(
        self,
        request: nlb_20220430_models.DeleteSecurityPolicyRequest,
    ) -> nlb_20220430_models.DeleteSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_policy_with_options(request, runtime)

    async def delete_security_policy_async(
        self,
        request: nlb_20220430_models.DeleteSecurityPolicyRequest,
    ) -> nlb_20220430_models.DeleteSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_policy_with_options_async(request, runtime)

    def delete_server_group_with_options(
        self,
        request: nlb_20220430_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_server_group_with_options_async(
        self,
        request: nlb_20220430_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DeleteServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_server_group(
        self,
        request: nlb_20220430_models.DeleteServerGroupRequest,
    ) -> nlb_20220430_models.DeleteServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_server_group_with_options(request, runtime)

    async def delete_server_group_async(
        self,
        request: nlb_20220430_models.DeleteServerGroupRequest,
    ) -> nlb_20220430_models.DeleteServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_server_group_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: nlb_20220430_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: nlb_20220430_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: nlb_20220430_models.DescribeRegionsRequest,
    ) -> nlb_20220430_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: nlb_20220430_models.DescribeRegionsRequest,
    ) -> nlb_20220430_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: nlb_20220430_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: nlb_20220430_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: nlb_20220430_models.DescribeZonesRequest,
    ) -> nlb_20220430_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: nlb_20220430_models.DescribeZonesRequest,
    ) -> nlb_20220430_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_common_bandwidth_package_from_load_balancer_with_options(
        self,
        request: nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachCommonBandwidthPackageFromLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_common_bandwidth_package_from_load_balancer_with_options_async(
        self,
        request: nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachCommonBandwidthPackageFromLoadBalancer',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_common_bandwidth_package_from_load_balancer(
        self,
        request: nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_common_bandwidth_package_from_load_balancer_with_options(request, runtime)

    async def detach_common_bandwidth_package_from_load_balancer_async(
        self,
        request: nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_common_bandwidth_package_from_load_balancer_with_options_async(request, runtime)

    def disable_load_balancer_ipv_6internet_with_options(
        self,
        request: nlb_20220430_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerIpv6Internet',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_load_balancer_ipv_6internet_with_options_async(
        self,
        request: nlb_20220430_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerIpv6Internet',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_load_balancer_ipv_6internet(
        self,
        request: nlb_20220430_models.DisableLoadBalancerIpv6InternetRequest,
    ) -> nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def disable_load_balancer_ipv_6internet_async(
        self,
        request: nlb_20220430_models.DisableLoadBalancerIpv6InternetRequest,
    ) -> nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def enable_load_balancer_ipv_6internet_with_options(
        self,
        request: nlb_20220430_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerIpv6Internet',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_load_balancer_ipv_6internet_with_options_async(
        self,
        request: nlb_20220430_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerIpv6Internet',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_load_balancer_ipv_6internet(
        self,
        request: nlb_20220430_models.EnableLoadBalancerIpv6InternetRequest,
    ) -> nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def enable_load_balancer_ipv_6internet_async(
        self,
        request: nlb_20220430_models.EnableLoadBalancerIpv6InternetRequest,
    ) -> nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def get_job_status_with_options(
        self,
        request: nlb_20220430_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobStatus',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_status_with_options_async(
        self,
        request: nlb_20220430_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobStatus',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_status(
        self,
        request: nlb_20220430_models.GetJobStatusRequest,
    ) -> nlb_20220430_models.GetJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    async def get_job_status_async(
        self,
        request: nlb_20220430_models.GetJobStatusRequest,
    ) -> nlb_20220430_models.GetJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_status_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: nlb_20220430_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_attribute_with_options_async(
        self,
        request: nlb_20220430_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_attribute(
        self,
        request: nlb_20220430_models.GetListenerAttributeRequest,
    ) -> nlb_20220430_models.GetListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_listener_attribute_with_options(request, runtime)

    async def get_listener_attribute_async(
        self,
        request: nlb_20220430_models.GetListenerAttributeRequest,
    ) -> nlb_20220430_models.GetListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_attribute_with_options_async(request, runtime)

    def get_listener_health_status_with_options(
        self,
        request: nlb_20220430_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetListenerHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetListenerHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_health_status_with_options_async(
        self,
        request: nlb_20220430_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetListenerHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetListenerHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_health_status(
        self,
        request: nlb_20220430_models.GetListenerHealthStatusRequest,
    ) -> nlb_20220430_models.GetListenerHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_listener_health_status_with_options(request, runtime)

    async def get_listener_health_status_async(
        self,
        request: nlb_20220430_models.GetListenerHealthStatusRequest,
    ) -> nlb_20220430_models.GetListenerHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_health_status_with_options_async(request, runtime)

    def get_load_balancer_attribute_with_options(
        self,
        request: nlb_20220430_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_load_balancer_attribute_with_options_async(
        self,
        request: nlb_20220430_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.GetLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_load_balancer_attribute(
        self,
        request: nlb_20220430_models.GetLoadBalancerAttributeRequest,
    ) -> nlb_20220430_models.GetLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_load_balancer_attribute_with_options(request, runtime)

    async def get_load_balancer_attribute_async(
        self,
        request: nlb_20220430_models.GetLoadBalancerAttributeRequest,
    ) -> nlb_20220430_models.GetLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_load_balancer_attribute_with_options_async(request, runtime)

    def list_listener_certificates_with_options(
        self,
        request: nlb_20220430_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListListenerCertificatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListListenerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listener_certificates_with_options_async(
        self,
        request: nlb_20220430_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListListenerCertificatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListListenerCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listener_certificates(
        self,
        request: nlb_20220430_models.ListListenerCertificatesRequest,
    ) -> nlb_20220430_models.ListListenerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    async def list_listener_certificates_async(
        self,
        request: nlb_20220430_models.ListListenerCertificatesRequest,
    ) -> nlb_20220430_models.ListListenerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listener_certificates_with_options_async(request, runtime)

    def list_listeners_with_options(
        self,
        request: nlb_20220430_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListListenersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_with_options_async(
        self,
        request: nlb_20220430_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListListenersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners(
        self,
        request: nlb_20220430_models.ListListenersRequest,
    ) -> nlb_20220430_models.ListListenersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    async def list_listeners_async(
        self,
        request: nlb_20220430_models.ListListenersRequest,
    ) -> nlb_20220430_models.ListListenersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_with_options_async(request, runtime)

    def list_load_balancers_with_options(
        self,
        request: nlb_20220430_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.dnsname):
            query['DNSName'] = request.dnsname
        if not UtilClient.is_unset(request.load_balancer_business_status):
            query['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.load_balancer_type):
            query['LoadBalancerType'] = request.load_balancer_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLoadBalancers',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_load_balancers_with_options_async(
        self,
        request: nlb_20220430_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.dnsname):
            query['DNSName'] = request.dnsname
        if not UtilClient.is_unset(request.load_balancer_business_status):
            query['LoadBalancerBusinessStatus'] = request.load_balancer_business_status
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.load_balancer_type):
            query['LoadBalancerType'] = request.load_balancer_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLoadBalancers',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_load_balancers(
        self,
        request: nlb_20220430_models.ListLoadBalancersRequest,
    ) -> nlb_20220430_models.ListLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_load_balancers_with_options(request, runtime)

    async def list_load_balancers_async(
        self,
        request: nlb_20220430_models.ListLoadBalancersRequest,
    ) -> nlb_20220430_models.ListLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_load_balancers_with_options_async(request, runtime)

    def list_security_policy_with_options(
        self,
        request: nlb_20220430_models.ListSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListSecurityPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_ids):
            body['SecurityPolicyIds'] = request.security_policy_ids
        if not UtilClient.is_unset(request.security_policy_names):
            body['SecurityPolicyNames'] = request.security_policy_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policy_with_options_async(
        self,
        request: nlb_20220430_models.ListSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListSecurityPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_ids):
            body['SecurityPolicyIds'] = request.security_policy_ids
        if not UtilClient.is_unset(request.security_policy_names):
            body['SecurityPolicyNames'] = request.security_policy_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policy(
        self,
        request: nlb_20220430_models.ListSecurityPolicyRequest,
    ) -> nlb_20220430_models.ListSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_security_policy_with_options(request, runtime)

    async def list_security_policy_async(
        self,
        request: nlb_20220430_models.ListSecurityPolicyRequest,
    ) -> nlb_20220430_models.ListSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policy_with_options_async(request, runtime)

    def list_server_group_servers_with_options(
        self,
        request: nlb_20220430_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListServerGroupServersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_ids):
            body['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.server_ips):
            body['ServerIps'] = request.server_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListServerGroupServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_group_servers_with_options_async(
        self,
        request: nlb_20220430_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListServerGroupServersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_ids):
            body['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.server_ips):
            body['ServerIps'] = request.server_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListServerGroupServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_group_servers(
        self,
        request: nlb_20220430_models.ListServerGroupServersRequest,
    ) -> nlb_20220430_models.ListServerGroupServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_server_group_servers_with_options(request, runtime)

    async def list_server_group_servers_async(
        self,
        request: nlb_20220430_models.ListServerGroupServersRequest,
    ) -> nlb_20220430_models.ListServerGroupServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_server_group_servers_with_options_async(request, runtime)

    def list_server_groups_with_options(
        self,
        request: nlb_20220430_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.server_group_ids):
            body['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            body['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_groups_with_options_async(
        self,
        request: nlb_20220430_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.server_group_ids):
            body['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            body['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.server_group_type):
            body['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_groups(
        self,
        request: nlb_20220430_models.ListServerGroupsRequest,
    ) -> nlb_20220430_models.ListServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_server_groups_with_options(request, runtime)

    async def list_server_groups_async(
        self,
        request: nlb_20220430_models.ListServerGroupsRequest,
    ) -> nlb_20220430_models.ListServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_server_groups_with_options_async(request, runtime)

    def list_system_security_policy_with_options(
        self,
        request: nlb_20220430_models.ListSystemSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListSystemSecurityPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSystemSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListSystemSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_security_policy_with_options_async(
        self,
        request: nlb_20220430_models.ListSystemSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListSystemSecurityPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.caller_bid_login_email):
            body['CallerBidLoginEmail'] = request.caller_bid_login_email
        if not UtilClient.is_unset(request.caller_uid_login_email):
            body['CallerUidLoginEmail'] = request.caller_uid_login_email
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id_login_email):
            body['OwnerIdLoginEmail'] = request.owner_id_login_email
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.resource_owner_account):
            body['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSystemSecurityPolicy',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListSystemSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_security_policy(
        self,
        request: nlb_20220430_models.ListSystemSecurityPolicyRequest,
    ) -> nlb_20220430_models.ListSystemSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_system_security_policy_with_options(request, runtime)

    async def list_system_security_policy_async(
        self,
        request: nlb_20220430_models.ListSystemSecurityPolicyRequest,
    ) -> nlb_20220430_models.ListSystemSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_system_security_policy_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: nlb_20220430_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: nlb_20220430_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: nlb_20220430_models.ListTagResourcesRequest,
    ) -> nlb_20220430_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: nlb_20220430_models.ListTagResourcesRequest,
    ) -> nlb_20220430_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def remove_servers_from_server_group_with_options(
        self,
        request: nlb_20220430_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.RemoveServersFromServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            body['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.RemoveServersFromServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_servers_from_server_group_with_options_async(
        self,
        request: nlb_20220430_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.RemoveServersFromServerGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            body['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.RemoveServersFromServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_servers_from_server_group(
        self,
        request: nlb_20220430_models.RemoveServersFromServerGroupRequest,
    ) -> nlb_20220430_models.RemoveServersFromServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_servers_from_server_group_with_options(request, runtime)

    async def remove_servers_from_server_group_async(
        self,
        request: nlb_20220430_models.RemoveServersFromServerGroupRequest,
    ) -> nlb_20220430_models.RemoveServersFromServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_servers_from_server_group_with_options_async(request, runtime)

    def start_listener_with_options(
        self,
        request: nlb_20220430_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StartListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.StartListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_listener_with_options_async(
        self,
        request: nlb_20220430_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StartListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.StartListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_listener(
        self,
        request: nlb_20220430_models.StartListenerRequest,
    ) -> nlb_20220430_models.StartListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_listener_with_options(request, runtime)

    async def start_listener_async(
        self,
        request: nlb_20220430_models.StartListenerRequest,
    ) -> nlb_20220430_models.StartListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_listener_with_options_async(request, runtime)

    def stop_listener_with_options(
        self,
        request: nlb_20220430_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StopListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.StopListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_listener_with_options_async(
        self,
        request: nlb_20220430_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StopListenerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopListener',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.StopListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_listener(
        self,
        request: nlb_20220430_models.StopListenerRequest,
    ) -> nlb_20220430_models.StopListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_listener_with_options(request, runtime)

    async def stop_listener_async(
        self,
        request: nlb_20220430_models.StopListenerRequest,
    ) -> nlb_20220430_models.StopListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: nlb_20220430_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: nlb_20220430_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: nlb_20220430_models.TagResourcesRequest,
    ) -> nlb_20220430_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: nlb_20220430_models.TagResourcesRequest,
    ) -> nlb_20220430_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: nlb_20220430_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: nlb_20220430_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            body_flat['TagKey'] = request.tag_key
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: nlb_20220430_models.UntagResourcesRequest,
    ) -> nlb_20220430_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: nlb_20220430_models.UntagResourcesRequest,
    ) -> nlb_20220430_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_listener_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateListenerAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not UtilClient.is_unset(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not UtilClient.is_unset(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not UtilClient.is_unset(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cps):
            body['Cps'] = request.cps
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_attribute_with_options_async(
        self,
        request: nlb_20220430_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateListenerAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alpn_enabled):
            body['AlpnEnabled'] = request.alpn_enabled
        if not UtilClient.is_unset(request.alpn_policy):
            body['AlpnPolicy'] = request.alpn_policy
        if not UtilClient.is_unset(request.ca_certificate_ids):
            body['CaCertificateIds'] = request.ca_certificate_ids
        if not UtilClient.is_unset(request.ca_enabled):
            body['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificate_ids):
            body['CertificateIds'] = request.certificate_ids
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cps):
            body['Cps'] = request.cps
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.idle_timeout):
            body['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            body['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sec_sensor_enabled):
            body['SecSensorEnabled'] = request.sec_sensor_enabled
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_attribute(
        self,
        request: nlb_20220430_models.UpdateListenerAttributeRequest,
    ) -> nlb_20220430_models.UpdateListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_listener_attribute_with_options(request, runtime)

    async def update_listener_attribute_async(
        self,
        request: nlb_20220430_models.UpdateListenerAttributeRequest,
    ) -> nlb_20220430_models.UpdateListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_attribute_with_options_async(request, runtime)

    def update_load_balancer_address_type_config_with_options(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAddressTypeConfig',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_address_type_config_with_options_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAddressTypeConfig',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_address_type_config(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_address_type_config_with_options(request, runtime)

    async def update_load_balancer_address_type_config_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_address_type_config_with_options_async(request, runtime)

    def update_load_balancer_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cps):
            body['Cps'] = request.cps
        if not UtilClient.is_unset(request.cross_zone_enabled):
            body['CrossZoneEnabled'] = request.cross_zone_enabled
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_groups):
            body['SecurityGroups'] = request.security_groups
        if not UtilClient.is_unset(request.traffic_affinity_enabled):
            body['TrafficAffinityEnabled'] = request.traffic_affinity_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_attribute_with_options_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cps):
            body['Cps'] = request.cps
        if not UtilClient.is_unset(request.cross_zone_enabled):
            body['CrossZoneEnabled'] = request.cross_zone_enabled
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_groups):
            body['SecurityGroups'] = request.security_groups
        if not UtilClient.is_unset(request.traffic_affinity_enabled):
            body['TrafficAffinityEnabled'] = request.traffic_affinity_enabled
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_attribute(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAttributeRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_attribute_with_options(request, runtime)

    async def update_load_balancer_attribute_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAttributeRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_attribute_with_options_async(request, runtime)

    def update_load_balancer_zones_with_options(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerZonesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_zones_with_options_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerZonesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_mappings):
            body['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_zones(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerZonesRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_zones_with_options(request, runtime)

    async def update_load_balancer_zones_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerZonesRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_zones_with_options_async(request, runtime)

    def update_security_policy_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateSecurityPolicyAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSecurityPolicyAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateSecurityPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_policy_attribute_with_options_async(
        self,
        request: nlb_20220430_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateSecurityPolicyAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ciphers):
            body['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_content):
            body['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.security_policy_id):
            body['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.security_policy_name):
            body['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tls_versions):
            body['TlsVersions'] = request.tls_versions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSecurityPolicyAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateSecurityPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_policy_attribute(
        self,
        request: nlb_20220430_models.UpdateSecurityPolicyAttributeRequest,
    ) -> nlb_20220430_models.UpdateSecurityPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_security_policy_attribute_with_options(request, runtime)

    async def update_security_policy_attribute_async(
        self,
        request: nlb_20220430_models.UpdateSecurityPolicyAttributeRequest,
    ) -> nlb_20220430_models.UpdateSecurityPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_security_policy_attribute_with_options_async(request, runtime)

    def update_server_group_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not UtilClient.is_unset(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.persistence_enabled):
            body['PersistenceEnabled'] = request.persistence_enabled
        if not UtilClient.is_unset(request.persistence_timeout):
            body['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_attribute_with_options_async(
        self,
        request: nlb_20220430_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_enabled):
            body['ConnectionDrainEnabled'] = request.connection_drain_enabled
        if not UtilClient.is_unset(request.connection_drain_timeout):
            body['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        body_flat = {}
        if not UtilClient.is_unset(request.health_check_config):
            body_flat['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.persistence_enabled):
            body['PersistenceEnabled'] = request.persistence_enabled
        if not UtilClient.is_unset(request.persistence_timeout):
            body['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.preserve_client_ip_enabled):
            body['PreserveClientIpEnabled'] = request.preserve_client_ip_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scheduler):
            body['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            body['ServerGroupName'] = request.server_group_name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_attribute(
        self,
        request: nlb_20220430_models.UpdateServerGroupAttributeRequest,
    ) -> nlb_20220430_models.UpdateServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_attribute_with_options(request, runtime)

    async def update_server_group_attribute_async(
        self,
        request: nlb_20220430_models.UpdateServerGroupAttributeRequest,
    ) -> nlb_20220430_models.UpdateServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_attribute_with_options_async(request, runtime)

    def update_server_group_servers_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateServerGroupServersAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            body['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupServersAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateServerGroupServersAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_servers_attribute_with_options_async(
        self,
        request: nlb_20220430_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateServerGroupServersAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_group_id):
            body['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            body['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupServersAttribute',
            version='2022-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlb_20220430_models.UpdateServerGroupServersAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_servers_attribute(
        self,
        request: nlb_20220430_models.UpdateServerGroupServersAttributeRequest,
    ) -> nlb_20220430_models.UpdateServerGroupServersAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_servers_attribute_with_options(request, runtime)

    async def update_server_group_servers_attribute_async(
        self,
        request: nlb_20220430_models.UpdateServerGroupServersAttributeRequest,
    ) -> nlb_20220430_models.UpdateServerGroupServersAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_servers_attribute_with_options_async(request, runtime)
