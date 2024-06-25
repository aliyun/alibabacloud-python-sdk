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
        """
        @summary Adds backend servers to a specified server group.
        
        @param request: AddServersToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServersToServerGroupResponse
        """
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
        body_flat = {}
        if not UtilClient.is_unset(request.servers):
            body_flat['Servers'] = request.servers
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Adds backend servers to a specified server group.
        
        @param request: AddServersToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServersToServerGroupResponse
        """
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
        body_flat = {}
        if not UtilClient.is_unset(request.servers):
            body_flat['Servers'] = request.servers
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
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
        """
        @summary Adds backend servers to a specified server group.
        
        @param request: AddServersToServerGroupRequest
        @return: AddServersToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_servers_to_server_group_with_options(request, runtime)

    async def add_servers_to_server_group_async(
        self,
        request: nlb_20220430_models.AddServersToServerGroupRequest,
    ) -> nlb_20220430_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to a specified server group.
        
        @param request: AddServersToServerGroupRequest
        @return: AddServersToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_servers_to_server_group_with_options_async(request, runtime)

    def associate_additional_certificates_with_listener_with_options(
        self,
        request: nlb_20220430_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener that uses SSL over TCP.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If the listener is in the **Associating** state, the additional certificates are being associated.
        If the listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
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
            action='AssociateAdditionalCertificatesWithListener',
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
            nlb_20220430_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_additional_certificates_with_listener_with_options_async(
        self,
        request: nlb_20220430_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener that uses SSL over TCP.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If the listener is in the **Associating** state, the additional certificates are being associated.
        If the listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
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
            action='AssociateAdditionalCertificatesWithListener',
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
            nlb_20220430_models.AssociateAdditionalCertificatesWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_additional_certificates_with_listener(
        self,
        request: nlb_20220430_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> nlb_20220430_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener that uses SSL over TCP.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If the listener is in the **Associating** state, the additional certificates are being associated.
        If the listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    async def associate_additional_certificates_with_listener_async(
        self,
        request: nlb_20220430_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> nlb_20220430_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener that uses SSL over TCP.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If the listener is in the **Associating** state, the additional certificates are being associated.
        If the listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_additional_certificates_with_listener_with_options_async(request, runtime)

    def attach_common_bandwidth_package_to_load_balancer_with_options(
        self,
        request: nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        """
        @summary 绑定带宽包
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
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
        """
        @summary 绑定带宽包
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
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
        """
        @summary 绑定带宽包
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_common_bandwidth_package_to_load_balancer_with_options(request, runtime)

    async def attach_common_bandwidth_package_to_load_balancer_async(
        self,
        request: nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> nlb_20220430_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        """
        @summary 绑定带宽包
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_common_bandwidth_package_to_load_balancer_with_options_async(request, runtime)

    def cancel_shift_load_balancer_zones_with_options(
        self,
        request: nlb_20220430_models.CancelShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to the DNS record.
        
        @description Before you call this operation, the zone of the Network Load Balancer (NLB) instance is removed from the DNS record by using the console or calling the [StartShiftLoadBalancerZones](https://help.aliyun.com/document_detail/2411999.html) API operation.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelShiftLoadBalancerZonesResponse
        """
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
            action='CancelShiftLoadBalancerZones',
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
            nlb_20220430_models.CancelShiftLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_shift_load_balancer_zones_with_options_async(
        self,
        request: nlb_20220430_models.CancelShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to the DNS record.
        
        @description Before you call this operation, the zone of the Network Load Balancer (NLB) instance is removed from the DNS record by using the console or calling the [StartShiftLoadBalancerZones](https://help.aliyun.com/document_detail/2411999.html) API operation.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelShiftLoadBalancerZonesResponse
        """
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
            action='CancelShiftLoadBalancerZones',
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
            nlb_20220430_models.CancelShiftLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_shift_load_balancer_zones(
        self,
        request: nlb_20220430_models.CancelShiftLoadBalancerZonesRequest,
    ) -> nlb_20220430_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to the DNS record.
        
        @description Before you call this operation, the zone of the Network Load Balancer (NLB) instance is removed from the DNS record by using the console or calling the [StartShiftLoadBalancerZones](https://help.aliyun.com/document_detail/2411999.html) API operation.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @return: CancelShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_shift_load_balancer_zones_with_options(request, runtime)

    async def cancel_shift_load_balancer_zones_async(
        self,
        request: nlb_20220430_models.CancelShiftLoadBalancerZonesRequest,
    ) -> nlb_20220430_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to the DNS record.
        
        @description Before you call this operation, the zone of the Network Load Balancer (NLB) instance is removed from the DNS record by using the console or calling the [StartShiftLoadBalancerZones](https://help.aliyun.com/document_detail/2411999.html) API operation.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @return: CancelShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_shift_load_balancer_zones_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        tmp_req: nlb_20220430_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateListenerResponse:
        """
        @summary Creates a TCP or UDP listener, or a listener that uses SSL over TCP for a Network Load Balancer (NLB) instance.
        
        @param tmp_req: CreateListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListenerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nlb_20220430_models.CreateListenerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
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
        if not UtilClient.is_unset(request.mss):
            body['Mss'] = request.mss
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        tmp_req: nlb_20220430_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateListenerResponse:
        """
        @summary Creates a TCP or UDP listener, or a listener that uses SSL over TCP for a Network Load Balancer (NLB) instance.
        
        @param tmp_req: CreateListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListenerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nlb_20220430_models.CreateListenerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
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
        if not UtilClient.is_unset(request.mss):
            body['Mss'] = request.mss
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        """
        @summary Creates a TCP or UDP listener, or a listener that uses SSL over TCP for a Network Load Balancer (NLB) instance.
        
        @param request: CreateListenerRequest
        @return: CreateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    async def create_listener_async(
        self,
        request: nlb_20220430_models.CreateListenerRequest,
    ) -> nlb_20220430_models.CreateListenerResponse:
        """
        @summary Creates a TCP or UDP listener, or a listener that uses SSL over TCP for a Network Load Balancer (NLB) instance.
        
        @param request: CreateListenerRequest
        @return: CreateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_listener_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: nlb_20220430_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateLoadBalancerResponse:
        """
        @summary Creates a Network Load Balancer (NLB) instance in a specified region.
        
        @description    When you create an NLB instance, the service-linked role AliyunServiceRoleForNlb is automatically created and assigned to you.
        **CreateLoadBalancer** is an asynchronous operation. After you send a request, the system returns an instance ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) to query the status of an NLB instance.
        If an NLB instance is in the **Provisioning** state, the NLB instance is being created.
        If an NLB instance is in the **Active** state, the NLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not UtilClient.is_unset(request.deletion_protection_config):
            body_flat['DeletionProtectionConfig'] = request.deletion_protection_config
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_billing_config):
            body_flat['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_type):
            body['LoadBalancerType'] = request.load_balancer_type
        if not UtilClient.is_unset(request.modification_protection_config):
            body_flat['ModificationProtectionConfig'] = request.modification_protection_config
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
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
        """
        @summary Creates a Network Load Balancer (NLB) instance in a specified region.
        
        @description    When you create an NLB instance, the service-linked role AliyunServiceRoleForNlb is automatically created and assigned to you.
        **CreateLoadBalancer** is an asynchronous operation. After you send a request, the system returns an instance ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) to query the status of an NLB instance.
        If an NLB instance is in the **Provisioning** state, the NLB instance is being created.
        If an NLB instance is in the **Active** state, the NLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ip_version):
            body['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            body['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.bandwidth_package_id):
            body['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        body_flat = {}
        if not UtilClient.is_unset(request.deletion_protection_config):
            body_flat['DeletionProtectionConfig'] = request.deletion_protection_config
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_billing_config):
            body_flat['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not UtilClient.is_unset(request.load_balancer_name):
            body['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_type):
            body['LoadBalancerType'] = request.load_balancer_type
        if not UtilClient.is_unset(request.modification_protection_config):
            body_flat['ModificationProtectionConfig'] = request.modification_protection_config
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            body_flat['ZoneMappings'] = request.zone_mappings
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
        """
        @summary Creates a Network Load Balancer (NLB) instance in a specified region.
        
        @description    When you create an NLB instance, the service-linked role AliyunServiceRoleForNlb is automatically created and assigned to you.
        **CreateLoadBalancer** is an asynchronous operation. After you send a request, the system returns an instance ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) to query the status of an NLB instance.
        If an NLB instance is in the **Provisioning** state, the NLB instance is being created.
        If an NLB instance is in the **Active** state, the NLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: nlb_20220430_models.CreateLoadBalancerRequest,
    ) -> nlb_20220430_models.CreateLoadBalancerResponse:
        """
        @summary Creates a Network Load Balancer (NLB) instance in a specified region.
        
        @description    When you create an NLB instance, the service-linked role AliyunServiceRoleForNlb is automatically created and assigned to you.
        **CreateLoadBalancer** is an asynchronous operation. After you send a request, the system returns an instance ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) to query the status of an NLB instance.
        If an NLB instance is in the **Provisioning** state, the NLB instance is being created.
        If an NLB instance is in the **Active** state, the NLB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_security_policy_with_options(
        self,
        request: nlb_20220430_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateSecurityPolicyResponse:
        """
        @summary Creates a custom security policy for a Network Load Balancer (NLB) instance.
        
        @param request: CreateSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityPolicyResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        """
        @summary Creates a custom security policy for a Network Load Balancer (NLB) instance.
        
        @param request: CreateSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityPolicyResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        """
        @summary Creates a custom security policy for a Network Load Balancer (NLB) instance.
        
        @param request: CreateSecurityPolicyRequest
        @return: CreateSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_security_policy_with_options(request, runtime)

    async def create_security_policy_async(
        self,
        request: nlb_20220430_models.CreateSecurityPolicyRequest,
    ) -> nlb_20220430_models.CreateSecurityPolicyResponse:
        """
        @summary Creates a custom security policy for a Network Load Balancer (NLB) instance.
        
        @param request: CreateSecurityPolicyRequest
        @return: CreateSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_security_policy_with_options_async(request, runtime)

    def create_server_group_with_options(
        self,
        request: nlb_20220430_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.CreateServerGroupResponse:
        """
        @summary Creates a server group in a region.
        
        @description    **protocol** specifies the protocol used to forward requests to the backend servers.
        NLB instances support only backend server groups that use TCP, UDP, or SSL over TCP.
        **CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the creation status of the task.
        If the task is in the **Succeeded** status, the server group is created.
        If the task is in the **Processing** status, the server group is being created.
        
        @param request: CreateServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ipversion):
            body['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.any_port_enabled):
            body['AnyPortEnabled'] = request.any_port_enabled
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        """
        @summary Creates a server group in a region.
        
        @description    **protocol** specifies the protocol used to forward requests to the backend servers.
        NLB instances support only backend server groups that use TCP, UDP, or SSL over TCP.
        **CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the creation status of the task.
        If the task is in the **Succeeded** status, the server group is created.
        If the task is in the **Processing** status, the server group is being created.
        
        @param request: CreateServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_ipversion):
            body['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.any_port_enabled):
            body['AnyPortEnabled'] = request.any_port_enabled
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
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
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
        """
        @summary Creates a server group in a region.
        
        @description    **protocol** specifies the protocol used to forward requests to the backend servers.
        NLB instances support only backend server groups that use TCP, UDP, or SSL over TCP.
        **CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the creation status of the task.
        If the task is in the **Succeeded** status, the server group is created.
        If the task is in the **Processing** status, the server group is being created.
        
        @param request: CreateServerGroupRequest
        @return: CreateServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_server_group_with_options(request, runtime)

    async def create_server_group_async(
        self,
        request: nlb_20220430_models.CreateServerGroupRequest,
    ) -> nlb_20220430_models.CreateServerGroupResponse:
        """
        @summary Creates a server group in a region.
        
        @description    **protocol** specifies the protocol used to forward requests to the backend servers.
        NLB instances support only backend server groups that use TCP, UDP, or SSL over TCP.
        **CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the creation status of the task.
        If the task is in the **Succeeded** status, the server group is created.
        If the task is in the **Processing** status, the server group is being created.
        
        @param request: CreateServerGroupRequest
        @return: CreateServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_server_group_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: nlb_20220430_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteListenerResponse:
        """
        @summary 删除监听
        
        @param request: DeleteListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListenerResponse
        """
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
        """
        @summary 删除监听
        
        @param request: DeleteListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListenerResponse
        """
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
        """
        @summary 删除监听
        
        @param request: DeleteListenerRequest
        @return: DeleteListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    async def delete_listener_async(
        self,
        request: nlb_20220430_models.DeleteListenerRequest,
    ) -> nlb_20220430_models.DeleteListenerResponse:
        """
        @summary 删除监听
        
        @param request: DeleteListenerRequest
        @return: DeleteListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_listener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: nlb_20220430_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteLoadBalancerResponse:
        """
        @summary 删除负载均衡
        
        @param request: DeleteLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerResponse
        """
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
        """
        @summary 删除负载均衡
        
        @param request: DeleteLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerResponse
        """
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
        """
        @summary 删除负载均衡
        
        @param request: DeleteLoadBalancerRequest
        @return: DeleteLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: nlb_20220430_models.DeleteLoadBalancerRequest,
    ) -> nlb_20220430_models.DeleteLoadBalancerResponse:
        """
        @summary 删除负载均衡
        
        @param request: DeleteLoadBalancerRequest
        @return: DeleteLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_security_policy_with_options(
        self,
        request: nlb_20220430_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteSecurityPolicyResponse:
        """
        @summary 删除安全策略
        
        @param request: DeleteSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityPolicyResponse
        """
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
        """
        @summary 删除安全策略
        
        @param request: DeleteSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityPolicyResponse
        """
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
        """
        @summary 删除安全策略
        
        @param request: DeleteSecurityPolicyRequest
        @return: DeleteSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_security_policy_with_options(request, runtime)

    async def delete_security_policy_async(
        self,
        request: nlb_20220430_models.DeleteSecurityPolicyRequest,
    ) -> nlb_20220430_models.DeleteSecurityPolicyResponse:
        """
        @summary 删除安全策略
        
        @param request: DeleteSecurityPolicyRequest
        @return: DeleteSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_policy_with_options_async(request, runtime)

    def delete_server_group_with_options(
        self,
        request: nlb_20220430_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DeleteServerGroupResponse:
        """
        @summary DeleteServerGroup
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerGroupResponse
        """
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
        """
        @summary DeleteServerGroup
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerGroupResponse
        """
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
        """
        @summary DeleteServerGroup
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @return: DeleteServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_server_group_with_options(request, runtime)

    async def delete_server_group_async(
        self,
        request: nlb_20220430_models.DeleteServerGroupRequest,
    ) -> nlb_20220430_models.DeleteServerGroupResponse:
        """
        @summary DeleteServerGroup
        
        @description You can delete server groups that are not associated with listeners.
        
        @param request: DeleteServerGroupRequest
        @return: DeleteServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_server_group_with_options_async(request, runtime)

    def describe_hd_monitor_region_config_with_options(
        self,
        request: nlb_20220430_models.DescribeHdMonitorRegionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeHdMonitorRegionConfigResponse:
        """
        @summary 查询秒级监控存储配置
        
        @param request: DescribeHdMonitorRegionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHdMonitorRegionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHdMonitorRegionConfig',
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
            nlb_20220430_models.DescribeHdMonitorRegionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hd_monitor_region_config_with_options_async(
        self,
        request: nlb_20220430_models.DescribeHdMonitorRegionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeHdMonitorRegionConfigResponse:
        """
        @summary 查询秒级监控存储配置
        
        @param request: DescribeHdMonitorRegionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHdMonitorRegionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHdMonitorRegionConfig',
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
            nlb_20220430_models.DescribeHdMonitorRegionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hd_monitor_region_config(
        self,
        request: nlb_20220430_models.DescribeHdMonitorRegionConfigRequest,
    ) -> nlb_20220430_models.DescribeHdMonitorRegionConfigResponse:
        """
        @summary 查询秒级监控存储配置
        
        @param request: DescribeHdMonitorRegionConfigRequest
        @return: DescribeHdMonitorRegionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hd_monitor_region_config_with_options(request, runtime)

    async def describe_hd_monitor_region_config_async(
        self,
        request: nlb_20220430_models.DescribeHdMonitorRegionConfigRequest,
    ) -> nlb_20220430_models.DescribeHdMonitorRegionConfigResponse:
        """
        @summary 查询秒级监控存储配置
        
        @param request: DescribeHdMonitorRegionConfigRequest
        @return: DescribeHdMonitorRegionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hd_monitor_region_config_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: nlb_20220430_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeRegionsResponse:
        """
        @summary Queries regions that support Network Load Balancer (NLB) instances.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        """
        @summary Queries regions that support Network Load Balancer (NLB) instances.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        """
        @summary Queries regions that support Network Load Balancer (NLB) instances.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: nlb_20220430_models.DescribeRegionsRequest,
    ) -> nlb_20220430_models.DescribeRegionsResponse:
        """
        @summary Queries regions that support Network Load Balancer (NLB) instances.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: nlb_20220430_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DescribeZonesResponse:
        """
        @summary Queries zones in a region that supports Network Load Balancer (NLB).
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
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
        """
        @summary Queries zones in a region that supports Network Load Balancer (NLB).
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
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
        """
        @summary Queries zones in a region that supports Network Load Balancer (NLB).
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: nlb_20220430_models.DescribeZonesRequest,
    ) -> nlb_20220430_models.DescribeZonesResponse:
        """
        @summary Queries zones in a region that supports Network Load Balancer (NLB).
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_common_bandwidth_package_from_load_balancer_with_options(
        self,
        request: nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        """
        @summary 解绑带宽包
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
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
        """
        @summary 解绑带宽包
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
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
        """
        @summary 解绑带宽包
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_common_bandwidth_package_from_load_balancer_with_options(request, runtime)

    async def detach_common_bandwidth_package_from_load_balancer_async(
        self,
        request: nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> nlb_20220430_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        """
        @summary 解绑带宽包
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_common_bandwidth_package_from_load_balancer_with_options_async(request, runtime)

    def disable_load_balancer_ipv_6internet_with_options(
        self,
        request: nlb_20220430_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the network type of an IPv6 Network Load Balancer (NLB) instance from Internet-facing to internal-facing.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLoadBalancerIpv6InternetResponse
        """
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
        """
        @summary Changes the network type of an IPv6 Network Load Balancer (NLB) instance from Internet-facing to internal-facing.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLoadBalancerIpv6InternetResponse
        """
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
        """
        @summary Changes the network type of an IPv6 Network Load Balancer (NLB) instance from Internet-facing to internal-facing.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @return: DisableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def disable_load_balancer_ipv_6internet_async(
        self,
        request: nlb_20220430_models.DisableLoadBalancerIpv6InternetRequest,
    ) -> nlb_20220430_models.DisableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the network type of an IPv6 Network Load Balancer (NLB) instance from Internet-facing to internal-facing.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @return: DisableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def disassociate_additional_certificates_with_listener_with_options(
        self,
        request: nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Disassociates additional certificates from a listener that uses SSL over TCP.
        
        @description *DisassociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated.
        If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DisassociateAdditionalCertificatesWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateAdditionalCertificatesWithListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
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
            action='DisassociateAdditionalCertificatesWithListener',
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
            nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_additional_certificates_with_listener_with_options_async(
        self,
        request: nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Disassociates additional certificates from a listener that uses SSL over TCP.
        
        @description *DisassociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated.
        If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DisassociateAdditionalCertificatesWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateAdditionalCertificatesWithListenerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.additional_certificate_ids):
            body['AdditionalCertificateIds'] = request.additional_certificate_ids
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
            action='DisassociateAdditionalCertificatesWithListener',
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
            nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_additional_certificates_with_listener(
        self,
        request: nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerRequest,
    ) -> nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Disassociates additional certificates from a listener that uses SSL over TCP.
        
        @description *DisassociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated.
        If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DisassociateAdditionalCertificatesWithListenerRequest
        @return: DisassociateAdditionalCertificatesWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_additional_certificates_with_listener_with_options(request, runtime)

    async def disassociate_additional_certificates_with_listener_async(
        self,
        request: nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerRequest,
    ) -> nlb_20220430_models.DisassociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Disassociates additional certificates from a listener that uses SSL over TCP.
        
        @description *DisassociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/615175.html) operation to query the status of the task:
        If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated.
        If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DisassociateAdditionalCertificatesWithListenerRequest
        @return: DisassociateAdditionalCertificatesWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_additional_certificates_with_listener_with_options_async(request, runtime)

    def enable_load_balancer_ipv_6internet_with_options(
        self,
        request: nlb_20220430_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the network type of the IPv6 address of a dual-stack NLB instance from private to the public.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLoadBalancerIpv6InternetResponse
        """
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
        """
        @summary Changes the network type of the IPv6 address of a dual-stack NLB instance from private to the public.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLoadBalancerIpv6InternetResponse
        """
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
        """
        @summary Changes the network type of the IPv6 address of a dual-stack NLB instance from private to the public.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @return: EnableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def enable_load_balancer_ipv_6internet_async(
        self,
        request: nlb_20220430_models.EnableLoadBalancerIpv6InternetRequest,
    ) -> nlb_20220430_models.EnableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the network type of the IPv6 address of a dual-stack NLB instance from private to the public.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @return: EnableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def get_job_status_with_options(
        self,
        request: nlb_20220430_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetJobStatusResponse:
        """
        @summary 获取工作流状态
        
        @param request: GetJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobStatusResponse
        """
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
        """
        @summary 获取工作流状态
        
        @param request: GetJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobStatusResponse
        """
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
        """
        @summary 获取工作流状态
        
        @param request: GetJobStatusRequest
        @return: GetJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    async def get_job_status_async(
        self,
        request: nlb_20220430_models.GetJobStatusRequest,
    ) -> nlb_20220430_models.GetJobStatusResponse:
        """
        @summary 获取工作流状态
        
        @param request: GetJobStatusRequest
        @return: GetJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_status_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: nlb_20220430_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetListenerAttributeResponse:
        """
        @summary Queries the details of a Network Load Balancer (NLB) listener.
        
        @param request: GetListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerAttributeResponse
        """
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
        """
        @summary Queries the details of a Network Load Balancer (NLB) listener.
        
        @param request: GetListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerAttributeResponse
        """
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
        """
        @summary Queries the details of a Network Load Balancer (NLB) listener.
        
        @param request: GetListenerAttributeRequest
        @return: GetListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_listener_attribute_with_options(request, runtime)

    async def get_listener_attribute_async(
        self,
        request: nlb_20220430_models.GetListenerAttributeRequest,
    ) -> nlb_20220430_models.GetListenerAttributeResponse:
        """
        @summary Queries the details of a Network Load Balancer (NLB) listener.
        
        @param request: GetListenerAttributeRequest
        @return: GetListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_attribute_with_options_async(request, runtime)

    def get_listener_health_status_with_options(
        self,
        request: nlb_20220430_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a Network Load Balancer (NLB) instance.
        
        @param request: GetListenerHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
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
        """
        @summary Queries the health check status of a Network Load Balancer (NLB) instance.
        
        @param request: GetListenerHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
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
        """
        @summary Queries the health check status of a Network Load Balancer (NLB) instance.
        
        @param request: GetListenerHealthStatusRequest
        @return: GetListenerHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_listener_health_status_with_options(request, runtime)

    async def get_listener_health_status_async(
        self,
        request: nlb_20220430_models.GetListenerHealthStatusRequest,
    ) -> nlb_20220430_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a Network Load Balancer (NLB) instance.
        
        @param request: GetListenerHealthStatusRequest
        @return: GetListenerHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_health_status_with_options_async(request, runtime)

    def get_load_balancer_attribute_with_options(
        self,
        request: nlb_20220430_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details about a Network Load Balancer (NLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoadBalancerAttributeResponse
        """
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
        """
        @summary Queries the details about a Network Load Balancer (NLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoadBalancerAttributeResponse
        """
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
        """
        @summary Queries the details about a Network Load Balancer (NLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @return: GetLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_load_balancer_attribute_with_options(request, runtime)

    async def get_load_balancer_attribute_async(
        self,
        request: nlb_20220430_models.GetLoadBalancerAttributeRequest,
    ) -> nlb_20220430_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details about a Network Load Balancer (NLB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @return: GetLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_load_balancer_attribute_with_options_async(request, runtime)

    def list_listener_certificates_with_options(
        self,
        request: nlb_20220430_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListListenerCertificatesResponse:
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @param request: ListListenerCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenerCertificatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
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
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @param request: ListListenerCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenerCertificatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.listener_id):
            body['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
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
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @param request: ListListenerCertificatesRequest
        @return: ListListenerCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    async def list_listener_certificates_async(
        self,
        request: nlb_20220430_models.ListListenerCertificatesRequest,
    ) -> nlb_20220430_models.ListListenerCertificatesResponse:
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @param request: ListListenerCertificatesRequest
        @return: ListListenerCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_listener_certificates_with_options_async(request, runtime)

    def list_listeners_with_options(
        self,
        request: nlb_20220430_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListListenersResponse:
        """
        @summary Queries listeners added to a Network Load Balancer (NLB) instance.
        
        @param request: ListListenersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenersResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Queries listeners added to a Network Load Balancer (NLB) instance.
        
        @param request: ListListenersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenersResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Queries listeners added to a Network Load Balancer (NLB) instance.
        
        @param request: ListListenersRequest
        @return: ListListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    async def list_listeners_async(
        self,
        request: nlb_20220430_models.ListListenersRequest,
    ) -> nlb_20220430_models.ListListenersResponse:
        """
        @summary Queries listeners added to a Network Load Balancer (NLB) instance.
        
        @param request: ListListenersRequest
        @return: ListListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_with_options_async(request, runtime)

    def list_load_balancers_with_options(
        self,
        request: nlb_20220430_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListLoadBalancersResponse:
        """
        @summary Queries Network Load Balancer (NLB) instances in a region based on specified conditions.
        
        @param request: ListLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.dnsname):
            query['DNSName'] = request.dnsname
        if not UtilClient.is_unset(request.ipv_6address_type):
            query['Ipv6AddressType'] = request.ipv_6address_type
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
        """
        @summary Queries Network Load Balancer (NLB) instances in a region based on specified conditions.
        
        @param request: ListLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.dnsname):
            query['DNSName'] = request.dnsname
        if not UtilClient.is_unset(request.ipv_6address_type):
            query['Ipv6AddressType'] = request.ipv_6address_type
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
        """
        @summary Queries Network Load Balancer (NLB) instances in a region based on specified conditions.
        
        @param request: ListLoadBalancersRequest
        @return: ListLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_load_balancers_with_options(request, runtime)

    async def list_load_balancers_async(
        self,
        request: nlb_20220430_models.ListLoadBalancersRequest,
    ) -> nlb_20220430_models.ListLoadBalancersResponse:
        """
        @summary Queries Network Load Balancer (NLB) instances in a region based on specified conditions.
        
        @param request: ListLoadBalancersRequest
        @return: ListLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_load_balancers_with_options_async(request, runtime)

    def list_security_policy_with_options(
        self,
        request: nlb_20220430_models.ListSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListSecurityPolicyResponse:
        """
        @summary Queries the TLS security policies set for a Network Load Balancer (NLB) instance.
        
        @param request: ListSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityPolicyResponse
        """
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
        """
        @summary Queries the TLS security policies set for a Network Load Balancer (NLB) instance.
        
        @param request: ListSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityPolicyResponse
        """
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
        """
        @summary Queries the TLS security policies set for a Network Load Balancer (NLB) instance.
        
        @param request: ListSecurityPolicyRequest
        @return: ListSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_security_policy_with_options(request, runtime)

    async def list_security_policy_async(
        self,
        request: nlb_20220430_models.ListSecurityPolicyRequest,
    ) -> nlb_20220430_models.ListSecurityPolicyResponse:
        """
        @summary Queries the TLS security policies set for a Network Load Balancer (NLB) instance.
        
        @param request: ListSecurityPolicyRequest
        @return: ListSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policy_with_options_async(request, runtime)

    def list_server_group_servers_with_options(
        self,
        request: nlb_20220430_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListServerGroupServersResponse:
        """
        @summary Queries the backend servers in a specified server group.
        
        @param request: ListServerGroupServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupServersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        """
        @summary Queries the backend servers in a specified server group.
        
        @param request: ListServerGroupServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupServersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        """
        @summary Queries the backend servers in a specified server group.
        
        @param request: ListServerGroupServersRequest
        @return: ListServerGroupServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_server_group_servers_with_options(request, runtime)

    async def list_server_group_servers_async(
        self,
        request: nlb_20220430_models.ListServerGroupServersRequest,
    ) -> nlb_20220430_models.ListServerGroupServersResponse:
        """
        @summary Queries the backend servers in a specified server group.
        
        @param request: ListServerGroupServersRequest
        @return: ListServerGroupServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_server_group_servers_with_options_async(request, runtime)

    def list_server_groups_with_options(
        self,
        request: nlb_20220430_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListServerGroupsResponse:
        """
        @summary Queries the server groups of a Network Load Balancer (NLB) instance.
        
        @param request: ListServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupsResponse
        """
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
        """
        @summary Queries the server groups of a Network Load Balancer (NLB) instance.
        
        @param request: ListServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupsResponse
        """
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
        """
        @summary Queries the server groups of a Network Load Balancer (NLB) instance.
        
        @param request: ListServerGroupsRequest
        @return: ListServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_server_groups_with_options(request, runtime)

    async def list_server_groups_async(
        self,
        request: nlb_20220430_models.ListServerGroupsRequest,
    ) -> nlb_20220430_models.ListServerGroupsResponse:
        """
        @summary Queries the server groups of a Network Load Balancer (NLB) instance.
        
        @param request: ListServerGroupsRequest
        @return: ListServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_server_groups_with_options_async(request, runtime)

    def list_system_security_policy_with_options(
        self,
        request: nlb_20220430_models.ListSystemSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListSystemSecurityPolicyResponse:
        """
        @summary Queries the default TLS policy.
        
        @param request: ListSystemSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSystemSecurityPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        """
        @summary Queries the default TLS policy.
        
        @param request: ListSystemSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSystemSecurityPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        """
        @summary Queries the default TLS policy.
        
        @param request: ListSystemSecurityPolicyRequest
        @return: ListSystemSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_system_security_policy_with_options(request, runtime)

    async def list_system_security_policy_async(
        self,
        request: nlb_20220430_models.ListSystemSecurityPolicyRequest,
    ) -> nlb_20220430_models.ListSystemSecurityPolicyResponse:
        """
        @summary Queries the default TLS policy.
        
        @param request: ListSystemSecurityPolicyRequest
        @return: ListSystemSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_system_security_policy_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: nlb_20220430_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
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
        """
        @summary Queries the tags of a resource.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
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
        """
        @summary Queries the tags of a resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: nlb_20220430_models.ListTagResourcesRequest,
    ) -> nlb_20220430_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of a resource.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def load_balancer_join_security_group_with_options(
        self,
        request: nlb_20220430_models.LoadBalancerJoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.LoadBalancerJoinSecurityGroupResponse:
        """
        @summary Associates a security group with a Network Load Balancer (NLB) instance.
        
        @description    Make sure that you have created a security group. For more information about how to create a security group, see [CreateSecurityGroup](https://help.aliyun.com/document_detail/25553.html).
        An NLB instance can be associated with up to four security groups.
        You can query the security groups that are associated with an NLB instance by calling the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation.
        LoadBalancerJoinSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is associated.
        If the task is in the **Processing** state, the security group is being associated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerJoinSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoadBalancerJoinSecurityGroupResponse
        """
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
        if not UtilClient.is_unset(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LoadBalancerJoinSecurityGroup',
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
            nlb_20220430_models.LoadBalancerJoinSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_balancer_join_security_group_with_options_async(
        self,
        request: nlb_20220430_models.LoadBalancerJoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.LoadBalancerJoinSecurityGroupResponse:
        """
        @summary Associates a security group with a Network Load Balancer (NLB) instance.
        
        @description    Make sure that you have created a security group. For more information about how to create a security group, see [CreateSecurityGroup](https://help.aliyun.com/document_detail/25553.html).
        An NLB instance can be associated with up to four security groups.
        You can query the security groups that are associated with an NLB instance by calling the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation.
        LoadBalancerJoinSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is associated.
        If the task is in the **Processing** state, the security group is being associated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerJoinSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoadBalancerJoinSecurityGroupResponse
        """
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
        if not UtilClient.is_unset(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LoadBalancerJoinSecurityGroup',
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
            nlb_20220430_models.LoadBalancerJoinSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_balancer_join_security_group(
        self,
        request: nlb_20220430_models.LoadBalancerJoinSecurityGroupRequest,
    ) -> nlb_20220430_models.LoadBalancerJoinSecurityGroupResponse:
        """
        @summary Associates a security group with a Network Load Balancer (NLB) instance.
        
        @description    Make sure that you have created a security group. For more information about how to create a security group, see [CreateSecurityGroup](https://help.aliyun.com/document_detail/25553.html).
        An NLB instance can be associated with up to four security groups.
        You can query the security groups that are associated with an NLB instance by calling the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation.
        LoadBalancerJoinSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is associated.
        If the task is in the **Processing** state, the security group is being associated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerJoinSecurityGroupRequest
        @return: LoadBalancerJoinSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.load_balancer_join_security_group_with_options(request, runtime)

    async def load_balancer_join_security_group_async(
        self,
        request: nlb_20220430_models.LoadBalancerJoinSecurityGroupRequest,
    ) -> nlb_20220430_models.LoadBalancerJoinSecurityGroupResponse:
        """
        @summary Associates a security group with a Network Load Balancer (NLB) instance.
        
        @description    Make sure that you have created a security group. For more information about how to create a security group, see [CreateSecurityGroup](https://help.aliyun.com/document_detail/25553.html).
        An NLB instance can be associated with up to four security groups.
        You can query the security groups that are associated with an NLB instance by calling the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation.
        LoadBalancerJoinSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is associated.
        If the task is in the **Processing** state, the security group is being associated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerJoinSecurityGroupRequest
        @return: LoadBalancerJoinSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.load_balancer_join_security_group_with_options_async(request, runtime)

    def load_balancer_leave_security_group_with_options(
        self,
        request: nlb_20220430_models.LoadBalancerLeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.LoadBalancerLeaveSecurityGroupResponse:
        """
        @summary Disassociates a security group from a Network Load Balancer (NLB) instance.
        
        @description LoadBalancerLeaveSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is disassociated.
        If the task is in the **Processing** state, the security group is being disassociated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerLeaveSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoadBalancerLeaveSecurityGroupResponse
        """
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
        if not UtilClient.is_unset(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LoadBalancerLeaveSecurityGroup',
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
            nlb_20220430_models.LoadBalancerLeaveSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def load_balancer_leave_security_group_with_options_async(
        self,
        request: nlb_20220430_models.LoadBalancerLeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.LoadBalancerLeaveSecurityGroupResponse:
        """
        @summary Disassociates a security group from a Network Load Balancer (NLB) instance.
        
        @description LoadBalancerLeaveSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is disassociated.
        If the task is in the **Processing** state, the security group is being disassociated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerLeaveSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoadBalancerLeaveSecurityGroupResponse
        """
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
        if not UtilClient.is_unset(request.security_group_ids):
            body['SecurityGroupIds'] = request.security_group_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LoadBalancerLeaveSecurityGroup',
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
            nlb_20220430_models.LoadBalancerLeaveSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def load_balancer_leave_security_group(
        self,
        request: nlb_20220430_models.LoadBalancerLeaveSecurityGroupRequest,
    ) -> nlb_20220430_models.LoadBalancerLeaveSecurityGroupResponse:
        """
        @summary Disassociates a security group from a Network Load Balancer (NLB) instance.
        
        @description LoadBalancerLeaveSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is disassociated.
        If the task is in the **Processing** state, the security group is being disassociated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerLeaveSecurityGroupRequest
        @return: LoadBalancerLeaveSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.load_balancer_leave_security_group_with_options(request, runtime)

    async def load_balancer_leave_security_group_async(
        self,
        request: nlb_20220430_models.LoadBalancerLeaveSecurityGroupRequest,
    ) -> nlb_20220430_models.LoadBalancerLeaveSecurityGroupResponse:
        """
        @summary Disassociates a security group from a Network Load Balancer (NLB) instance.
        
        @description LoadBalancerLeaveSecurityGroup is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the status of a task.
        If the task is in the **Succeeded** state, the security group is disassociated.
        If the task is in the **Processing** state, the security group is being disassociated. In this case, you can perform only query operations.
        
        @param request: LoadBalancerLeaveSecurityGroupRequest
        @return: LoadBalancerLeaveSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.load_balancer_leave_security_group_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: nlb_20220430_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.MoveResourceGroupResponse:
        """
        @summary Modify the group of resource.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
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
            nlb_20220430_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: nlb_20220430_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.MoveResourceGroupResponse:
        """
        @summary Modify the group of resource.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
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
            nlb_20220430_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: nlb_20220430_models.MoveResourceGroupRequest,
    ) -> nlb_20220430_models.MoveResourceGroupResponse:
        """
        @summary Modify the group of resource.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: nlb_20220430_models.MoveResourceGroupRequest,
    ) -> nlb_20220430_models.MoveResourceGroupResponse:
        """
        @summary Modify the group of resource.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def remove_servers_from_server_group_with_options(
        self,
        request: nlb_20220430_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from a server group of a Network Load Balancer (NLB) instance.
        
        @param request: RemoveServersFromServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServersFromServerGroupResponse
        """
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
        """
        @summary Removes backend servers from a server group of a Network Load Balancer (NLB) instance.
        
        @param request: RemoveServersFromServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServersFromServerGroupResponse
        """
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
        """
        @summary Removes backend servers from a server group of a Network Load Balancer (NLB) instance.
        
        @param request: RemoveServersFromServerGroupRequest
        @return: RemoveServersFromServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_servers_from_server_group_with_options(request, runtime)

    async def remove_servers_from_server_group_async(
        self,
        request: nlb_20220430_models.RemoveServersFromServerGroupRequest,
    ) -> nlb_20220430_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from a server group of a Network Load Balancer (NLB) instance.
        
        @param request: RemoveServersFromServerGroupRequest
        @return: RemoveServersFromServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_servers_from_server_group_with_options_async(request, runtime)

    def set_hd_monitor_region_config_with_options(
        self,
        request: nlb_20220430_models.SetHdMonitorRegionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.SetHdMonitorRegionConfigResponse:
        """
        @summary 配置秒级监控存储
        
        @param request: SetHdMonitorRegionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetHdMonitorRegionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.metric_store):
            query['MetricStore'] = request.metric_store
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHdMonitorRegionConfig',
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
            nlb_20220430_models.SetHdMonitorRegionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_hd_monitor_region_config_with_options_async(
        self,
        request: nlb_20220430_models.SetHdMonitorRegionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.SetHdMonitorRegionConfigResponse:
        """
        @summary 配置秒级监控存储
        
        @param request: SetHdMonitorRegionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetHdMonitorRegionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.metric_store):
            query['MetricStore'] = request.metric_store
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHdMonitorRegionConfig',
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
            nlb_20220430_models.SetHdMonitorRegionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_hd_monitor_region_config(
        self,
        request: nlb_20220430_models.SetHdMonitorRegionConfigRequest,
    ) -> nlb_20220430_models.SetHdMonitorRegionConfigResponse:
        """
        @summary 配置秒级监控存储
        
        @param request: SetHdMonitorRegionConfigRequest
        @return: SetHdMonitorRegionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_hd_monitor_region_config_with_options(request, runtime)

    async def set_hd_monitor_region_config_async(
        self,
        request: nlb_20220430_models.SetHdMonitorRegionConfigRequest,
    ) -> nlb_20220430_models.SetHdMonitorRegionConfigResponse:
        """
        @summary 配置秒级监控存储
        
        @param request: SetHdMonitorRegionConfigRequest
        @return: SetHdMonitorRegionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_hd_monitor_region_config_with_options_async(request, runtime)

    def start_listener_with_options(
        self,
        request: nlb_20220430_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StartListenerResponse:
        """
        @summary Enables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StartListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartListenerResponse
        """
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
        """
        @summary Enables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StartListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartListenerResponse
        """
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
        """
        @summary Enables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StartListenerRequest
        @return: StartListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_listener_with_options(request, runtime)

    async def start_listener_async(
        self,
        request: nlb_20220430_models.StartListenerRequest,
    ) -> nlb_20220430_models.StartListenerResponse:
        """
        @summary Enables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StartListenerRequest
        @return: StartListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_listener_with_options_async(request, runtime)

    def start_shift_load_balancer_zones_with_options(
        self,
        request: nlb_20220430_models.StartShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description > If a Network Load Balancer (NLB) instance is deployed only in one zone, you cannot remove the NLB instance from the zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartShiftLoadBalancerZonesResponse
        """
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
            action='StartShiftLoadBalancerZones',
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
            nlb_20220430_models.StartShiftLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_shift_load_balancer_zones_with_options_async(
        self,
        request: nlb_20220430_models.StartShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description > If a Network Load Balancer (NLB) instance is deployed only in one zone, you cannot remove the NLB instance from the zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartShiftLoadBalancerZonesResponse
        """
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
            action='StartShiftLoadBalancerZones',
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
            nlb_20220430_models.StartShiftLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_shift_load_balancer_zones(
        self,
        request: nlb_20220430_models.StartShiftLoadBalancerZonesRequest,
    ) -> nlb_20220430_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description > If a Network Load Balancer (NLB) instance is deployed only in one zone, you cannot remove the NLB instance from the zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @return: StartShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_shift_load_balancer_zones_with_options(request, runtime)

    async def start_shift_load_balancer_zones_async(
        self,
        request: nlb_20220430_models.StartShiftLoadBalancerZonesRequest,
    ) -> nlb_20220430_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description > If a Network Load Balancer (NLB) instance is deployed only in one zone, you cannot remove the NLB instance from the zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @return: StartShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_shift_load_balancer_zones_with_options_async(request, runtime)

    def stop_listener_with_options(
        self,
        request: nlb_20220430_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.StopListenerResponse:
        """
        @summary Disables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StopListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopListenerResponse
        """
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
        """
        @summary Disables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StopListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopListenerResponse
        """
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
        """
        @summary Disables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StopListenerRequest
        @return: StopListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_listener_with_options(request, runtime)

    async def stop_listener_async(
        self,
        request: nlb_20220430_models.StopListenerRequest,
    ) -> nlb_20220430_models.StopListenerResponse:
        """
        @summary Disables a listener for a Network Load Balancer (NLB) instance.
        
        @param request: StopListenerRequest
        @return: StopListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: nlb_20220430_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.TagResourcesResponse:
        """
        @summary Adds tags to specified resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        """
        @summary Adds tags to specified resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        """
        @summary Adds tags to specified resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: nlb_20220430_models.TagResourcesRequest,
    ) -> nlb_20220430_models.TagResourcesResponse:
        """
        @summary Adds tags to specified resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: nlb_20220430_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: nlb_20220430_models.UntagResourcesRequest,
    ) -> nlb_20220430_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_listener_attribute_with_options(
        self,
        tmp_req: nlb_20220430_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the attributes of a listener, such as the name and the idle connection timeout period.
        
        @param tmp_req: UpdateListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerAttributeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nlb_20220430_models.UpdateListenerAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
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
        if not UtilClient.is_unset(request.mss):
            body['Mss'] = request.mss
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
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
        tmp_req: nlb_20220430_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the attributes of a listener, such as the name and the idle connection timeout period.
        
        @param tmp_req: UpdateListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerAttributeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nlb_20220430_models.UpdateListenerAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proxy_protocol_v2config):
            request.proxy_protocol_v2config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proxy_protocol_v2config, 'ProxyProtocolV2Config', 'json')
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
        if not UtilClient.is_unset(request.mss):
            body['Mss'] = request.mss
        if not UtilClient.is_unset(request.proxy_protocol_enabled):
            body['ProxyProtocolEnabled'] = request.proxy_protocol_enabled
        if not UtilClient.is_unset(request.proxy_protocol_v2config_shrink):
            body['ProxyProtocolV2Config'] = request.proxy_protocol_v2config_shrink
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
        """
        @summary Updates the attributes of a listener, such as the name and the idle connection timeout period.
        
        @param request: UpdateListenerAttributeRequest
        @return: UpdateListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_listener_attribute_with_options(request, runtime)

    async def update_listener_attribute_async(
        self,
        request: nlb_20220430_models.UpdateListenerAttributeRequest,
    ) -> nlb_20220430_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the attributes of a listener, such as the name and the idle connection timeout period.
        
        @param request: UpdateListenerAttributeRequest
        @return: UpdateListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_attribute_with_options_async(request, runtime)

    def update_load_balancer_address_type_config_with_options(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse:
        """
        @summary Changes the network type of the IPv4 address of a Network Load Balancer (NLB) instance.
        
        @description    Make sure that an NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the **AddressType** value of an NLB instance after you change the network type.
        **UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the task status:
        If the task is in the **Succeeded** state, the network type of the IPv4 address of the NLB instance is changed.
        If the task is in the **Processing** state, the network type of the IPv4 address of the NLB instance is being changed. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
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
        """
        @summary Changes the network type of the IPv4 address of a Network Load Balancer (NLB) instance.
        
        @description    Make sure that an NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the **AddressType** value of an NLB instance after you change the network type.
        **UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the task status:
        If the task is in the **Succeeded** state, the network type of the IPv4 address of the NLB instance is changed.
        If the task is in the **Processing** state, the network type of the IPv4 address of the NLB instance is being changed. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
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
        """
        @summary Changes the network type of the IPv4 address of a Network Load Balancer (NLB) instance.
        
        @description    Make sure that an NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the **AddressType** value of an NLB instance after you change the network type.
        **UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the task status:
        If the task is in the **Succeeded** state, the network type of the IPv4 address of the NLB instance is changed.
        If the task is in the **Processing** state, the network type of the IPv4 address of the NLB instance is being changed. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_address_type_config_with_options(request, runtime)

    async def update_load_balancer_address_type_config_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerAddressTypeConfigResponse:
        """
        @summary Changes the network type of the IPv4 address of a Network Load Balancer (NLB) instance.
        
        @description    Make sure that an NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the **AddressType** value of an NLB instance after you change the network type.
        **UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation to query the task status:
        If the task is in the **Succeeded** state, the network type of the IPv4 address of the NLB instance is changed.
        If the task is in the **Processing** state, the network type of the IPv4 address of the NLB instance is being changed. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_address_type_config_with_options_async(request, runtime)

    def update_load_balancer_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Updates the attributes, including the name, of a Network Load Balancer (NLB) instance.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAttributeResponse
        """
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
        """
        @summary Updates the attributes, including the name, of a Network Load Balancer (NLB) instance.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAttributeResponse
        """
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
        """
        @summary Updates the attributes, including the name, of a Network Load Balancer (NLB) instance.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @return: UpdateLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_attribute_with_options(request, runtime)

    async def update_load_balancer_attribute_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerAttributeRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Updates the attributes, including the name, of a Network Load Balancer (NLB) instance.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @return: UpdateLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_attribute_with_options_async(request, runtime)

    def update_load_balancer_protection_with_options(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerProtectionResponse:
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @description > You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the details about deletion protection and the configuration read-only mode.
        
        @param request: UpdateLoadBalancerProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerProtectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection_enabled):
            body['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not UtilClient.is_unset(request.deletion_protection_reason):
            body['DeletionProtectionReason'] = request.deletion_protection_reason
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            body['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            body['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerProtection',
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
            nlb_20220430_models.UpdateLoadBalancerProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_protection_with_options_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerProtectionResponse:
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @description > You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the details about deletion protection and the configuration read-only mode.
        
        @param request: UpdateLoadBalancerProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerProtectionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection_enabled):
            body['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not UtilClient.is_unset(request.deletion_protection_reason):
            body['DeletionProtectionReason'] = request.deletion_protection_reason
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            body['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            body['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            body['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerProtection',
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
            nlb_20220430_models.UpdateLoadBalancerProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_protection(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerProtectionRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerProtectionResponse:
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @description > You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the details about deletion protection and the configuration read-only mode.
        
        @param request: UpdateLoadBalancerProtectionRequest
        @return: UpdateLoadBalancerProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_protection_with_options(request, runtime)

    async def update_load_balancer_protection_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerProtectionRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerProtectionResponse:
        """
        @summary Enables or disables deletion protection and the configuration read-only mode for a Network Load Balancer (NLB) instance.
        
        @description > You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the details about deletion protection and the configuration read-only mode.
        
        @param request: UpdateLoadBalancerProtectionRequest
        @return: UpdateLoadBalancerProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_protection_with_options_async(request, runtime)

    def update_load_balancer_zones_with_options(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Modifies the zones and zone attributes of a Network Load Balancer (NLB) instance.
        
        @description When you call this operation, make sure that you specify all the zones of the NLB instance, including the existing zones and new zones. If you do not specify the existing zones, the existing zones are removed.
        Prerequisites
        An NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the zones and zone attributes of an NLB instance.
        **UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation query to query the status of a task:
        If the task is in the **Succeeded** state, the zones and zone attributes are modified.
        If the task is in the **Processing** state, the zones and zone attributes are being modified. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerZonesResponse
        """
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
        """
        @summary Modifies the zones and zone attributes of a Network Load Balancer (NLB) instance.
        
        @description When you call this operation, make sure that you specify all the zones of the NLB instance, including the existing zones and new zones. If you do not specify the existing zones, the existing zones are removed.
        Prerequisites
        An NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the zones and zone attributes of an NLB instance.
        **UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation query to query the status of a task:
        If the task is in the **Succeeded** state, the zones and zone attributes are modified.
        If the task is in the **Processing** state, the zones and zone attributes are being modified. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerZonesResponse
        """
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
        """
        @summary Modifies the zones and zone attributes of a Network Load Balancer (NLB) instance.
        
        @description When you call this operation, make sure that you specify all the zones of the NLB instance, including the existing zones and new zones. If you do not specify the existing zones, the existing zones are removed.
        Prerequisites
        An NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the zones and zone attributes of an NLB instance.
        **UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation query to query the status of a task:
        If the task is in the **Succeeded** state, the zones and zone attributes are modified.
        If the task is in the **Processing** state, the zones and zone attributes are being modified. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerZonesRequest
        @return: UpdateLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_zones_with_options(request, runtime)

    async def update_load_balancer_zones_async(
        self,
        request: nlb_20220430_models.UpdateLoadBalancerZonesRequest,
    ) -> nlb_20220430_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Modifies the zones and zone attributes of a Network Load Balancer (NLB) instance.
        
        @description When you call this operation, make sure that you specify all the zones of the NLB instance, including the existing zones and new zones. If you do not specify the existing zones, the existing zones are removed.
        Prerequisites
        An NLB instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/445868.html).
        You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/445873.html) operation to query the zones and zone attributes of an NLB instance.
        **UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetJobStatus](https://help.aliyun.com/document_detail/445904.html) operation query to query the status of a task:
        If the task is in the **Succeeded** state, the zones and zone attributes are modified.
        If the task is in the **Processing** state, the zones and zone attributes are being modified. In this case, you can perform only query operations.
        
        @param request: UpdateLoadBalancerZonesRequest
        @return: UpdateLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_zones_with_options_async(request, runtime)

    def update_security_policy_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateSecurityPolicyAttributeResponse:
        """
        @summary Modifies the configurations of a security policy for a Network Load Balancer (NLB) instance.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecurityPolicyAttributeResponse
        """
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
        """
        @summary Modifies the configurations of a security policy for a Network Load Balancer (NLB) instance.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecurityPolicyAttributeResponse
        """
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
        """
        @summary Modifies the configurations of a security policy for a Network Load Balancer (NLB) instance.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @return: UpdateSecurityPolicyAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_security_policy_attribute_with_options(request, runtime)

    async def update_security_policy_attribute_async(
        self,
        request: nlb_20220430_models.UpdateSecurityPolicyAttributeRequest,
    ) -> nlb_20220430_models.UpdateSecurityPolicyAttributeResponse:
        """
        @summary Modifies the configurations of a security policy for a Network Load Balancer (NLB) instance.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @return: UpdateSecurityPolicyAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_security_policy_attribute_with_options_async(request, runtime)

    def update_server_group_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateServerGroupAttributeResponse:
        """
        @summary Modifies the configurations of a server group of Network Load Balancer (NLB).
        
        @param request: UpdateServerGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupAttributeResponse
        """
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
        """
        @summary Modifies the configurations of a server group of Network Load Balancer (NLB).
        
        @param request: UpdateServerGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupAttributeResponse
        """
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
        """
        @summary Modifies the configurations of a server group of Network Load Balancer (NLB).
        
        @param request: UpdateServerGroupAttributeRequest
        @return: UpdateServerGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_attribute_with_options(request, runtime)

    async def update_server_group_attribute_async(
        self,
        request: nlb_20220430_models.UpdateServerGroupAttributeRequest,
    ) -> nlb_20220430_models.UpdateServerGroupAttributeResponse:
        """
        @summary Modifies the configurations of a server group of Network Load Balancer (NLB).
        
        @param request: UpdateServerGroupAttributeRequest
        @return: UpdateServerGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_attribute_with_options_async(request, runtime)

    def update_server_group_servers_attribute_with_options(
        self,
        request: nlb_20220430_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlb_20220430_models.UpdateServerGroupServersAttributeResponse:
        """
        @summary Modifies the configurations of backend servers in a server group, such as the weight and description.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/445895.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, the server group is being modified.
        If a server group is in the **Available** state, the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/445896.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupServersAttributeResponse
        """
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
        """
        @summary Modifies the configurations of backend servers in a server group, such as the weight and description.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/445895.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, the server group is being modified.
        If a server group is in the **Available** state, the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/445896.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupServersAttributeResponse
        """
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
        """
        @summary Modifies the configurations of backend servers in a server group, such as the weight and description.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/445895.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, the server group is being modified.
        If a server group is in the **Available** state, the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/445896.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @return: UpdateServerGroupServersAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_servers_attribute_with_options(request, runtime)

    async def update_server_group_servers_attribute_async(
        self,
        request: nlb_20220430_models.UpdateServerGroupServersAttributeRequest,
    ) -> nlb_20220430_models.UpdateServerGroupServersAttributeResponse:
        """
        @summary Modifies the configurations of backend servers in a server group, such as the weight and description.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/445895.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, the server group is being modified.
        If a server group is in the **Available** state, the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/445896.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @return: UpdateServerGroupServersAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_servers_attribute_with_options_async(request, runtime)
