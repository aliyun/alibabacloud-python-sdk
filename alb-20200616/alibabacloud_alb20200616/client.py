# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alb20200616 import models as alb_20200616_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_entries_to_acl_with_options(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEntriesToAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddEntriesToAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_entries_to_acl_with_options_async(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEntriesToAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddEntriesToAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_entries_to_acl(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_entries_to_acl_with_options(request, runtime)

    async def add_entries_to_acl_async(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_entries_to_acl_with_options_async(request, runtime)

    def add_servers_to_server_group_with_options(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddServersToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_servers_to_server_group_with_options_async(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddServersToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_servers_to_server_group(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_servers_to_server_group_with_options(request, runtime)

    async def add_servers_to_server_group_async(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_servers_to_server_group_with_options_async(request, runtime)

    def apply_health_check_template_to_server_group_with_options(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyHealthCheckTemplateToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_health_check_template_to_server_group_with_options_async(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyHealthCheckTemplateToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_health_check_template_to_server_group(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_health_check_template_to_server_group_with_options(request, runtime)

    async def apply_health_check_template_to_server_group_async(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_health_check_template_to_server_group_with_options_async(request, runtime)

    def associate_acls_with_listener_with_options(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAclsWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAclsWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_acls_with_listener_with_options_async(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAclsWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAclsWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_acls_with_listener(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_acls_with_listener_with_options(request, runtime)

    async def associate_acls_with_listener_async(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_acls_with_listener_with_options_async(request, runtime)

    def associate_additional_certificates_with_listener_with_options(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAdditionalCertificatesWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_additional_certificates_with_listener_with_options_async(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAdditionalCertificatesWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_additional_certificates_with_listener(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    async def associate_additional_certificates_with_listener_async(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_additional_certificates_with_listener_with_options_async(request, runtime)

    def attach_common_bandwidth_package_to_load_balancer_with_options(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
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
            action='AttachCommonBandwidthPackageToLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_common_bandwidth_package_to_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
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
            action='AttachCommonBandwidthPackageToLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_common_bandwidth_package_to_load_balancer(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_common_bandwidth_package_to_load_balancer_with_options(request, runtime)

    async def attach_common_bandwidth_package_to_load_balancer_async(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_common_bandwidth_package_to_load_balancer_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: alb_20200616_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_with_options_async(
        self,
        request: alb_20200616_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl(
        self,
        request: alb_20200616_models.CreateAclRequest,
    ) -> alb_20200616_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: alb_20200616_models.CreateAclRequest,
    ) -> alb_20200616_models.CreateAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_health_check_template_with_options(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHealthCheckTemplate',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateHealthCheckTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_health_check_template_with_options_async(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHealthCheckTemplate',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateHealthCheckTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_health_check_template(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_health_check_template_with_options(request, runtime)

    async def create_health_check_template_async(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_health_check_template_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        request: alb_20200616_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_listener_with_options_async(
        self,
        request: alb_20200616_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_listener(
        self,
        request: alb_20200616_models.CreateListenerRequest,
    ) -> alb_20200616_models.CreateListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    async def create_listener_async(
        self,
        request: alb_20200616_models.CreateListenerRequest,
    ) -> alb_20200616_models.CreateListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_listener_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_allocated_mode):
            query['AddressAllocatedMode'] = request.address_allocated_mode
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection_enabled):
            query['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_billing_config):
            query['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_allocated_mode):
            query['AddressAllocatedMode'] = request.address_allocated_mode
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection_enabled):
            query['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_billing_config):
            query['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: alb_20200616_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: alb_20200616_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: alb_20200616_models.CreateRuleRequest,
    ) -> alb_20200616_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: alb_20200616_models.CreateRuleRequest,
    ) -> alb_20200616_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_rules_with_options(
        self,
        request: alb_20200616_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        request: alb_20200616_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rules(
        self,
        request: alb_20200616_models.CreateRulesRequest,
    ) -> alb_20200616_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    async def create_rules_async(
        self,
        request: alb_20200616_models.CreateRulesRequest,
    ) -> alb_20200616_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rules_with_options_async(request, runtime)

    def create_security_policy_with_options(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_policy_with_options_async(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_policy(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_security_policy_with_options(request, runtime)

    async def create_security_policy_async(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_security_policy_with_options_async(request, runtime)

    def create_server_group_with_options(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_group_with_options_async(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_group(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_server_group_with_options(request, runtime)

    async def create_server_group_async(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_server_group_with_options_async(request, runtime)

    def delete_acl_with_options(
        self,
        request: alb_20200616_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        request: alb_20200616_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl(
        self,
        request: alb_20200616_models.DeleteAclRequest,
    ) -> alb_20200616_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: alb_20200616_models.DeleteAclRequest,
    ) -> alb_20200616_models.DeleteAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_health_check_templates_with_options(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteHealthCheckTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_health_check_templates_with_options_async(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteHealthCheckTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_health_check_templates(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_health_check_templates_with_options(request, runtime)

    async def delete_health_check_templates_async(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_health_check_templates_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_listener_with_options_async(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_listener(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
    ) -> alb_20200616_models.DeleteListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    async def delete_listener_async(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
    ) -> alb_20200616_models.DeleteListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_listener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
    ) -> alb_20200616_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
    ) -> alb_20200616_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rules_with_options(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rules_with_options_async(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rules(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
    ) -> alb_20200616_models.DeleteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    async def delete_rules_async(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
    ) -> alb_20200616_models.DeleteRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rules_with_options_async(request, runtime)

    def delete_security_policy_with_options(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_policy_with_options_async(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_policy(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_policy_with_options(request, runtime)

    async def delete_security_policy_async(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_policy_with_options_async(request, runtime)

    def delete_server_group_with_options(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_server_group_with_options_async(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_server_group(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_server_group_with_options(request, runtime)

    async def delete_server_group_async(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_server_group_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeZonesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeZonesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(self) -> alb_20200616_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(runtime)

    async def describe_zones_async(self) -> alb_20200616_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(runtime)

    def detach_common_bandwidth_package_from_load_balancer_with_options(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
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
            action='DetachCommonBandwidthPackageFromLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_common_bandwidth_package_from_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
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
            action='DetachCommonBandwidthPackageFromLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_common_bandwidth_package_from_load_balancer(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_common_bandwidth_package_from_load_balancer_with_options(request, runtime)

    async def detach_common_bandwidth_package_from_load_balancer_async(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_common_bandwidth_package_from_load_balancer_with_options_async(request, runtime)

    def disable_deletion_protection_with_options(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_deletion_protection_with_options_async(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_deletion_protection(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_deletion_protection_with_options(request, runtime)

    async def disable_deletion_protection_async(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_deletion_protection_with_options_async(request, runtime)

    def disable_load_balancer_access_log_with_options(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_load_balancer_access_log_with_options_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_load_balancer_access_log(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_load_balancer_access_log_with_options(request, runtime)

    async def disable_load_balancer_access_log_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_load_balancer_access_log_with_options_async(request, runtime)

    def dissociate_acls_from_listener_with_options(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAclsFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAclsFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_acls_from_listener_with_options_async(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAclsFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAclsFromListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_acls_from_listener(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_acls_from_listener_with_options(request, runtime)

    async def dissociate_acls_from_listener_async(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_acls_from_listener_with_options_async(request, runtime)

    def dissociate_additional_certificates_from_listener_with_options(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAdditionalCertificatesFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_additional_certificates_from_listener_with_options_async(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAdditionalCertificatesFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_additional_certificates_from_listener(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)

    async def dissociate_additional_certificates_from_listener_async(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_additional_certificates_from_listener_with_options_async(request, runtime)

    def enable_deletion_protection_with_options(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_deletion_protection_with_options_async(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_deletion_protection(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_deletion_protection_with_options(request, runtime)

    async def enable_deletion_protection_async(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_deletion_protection_with_options_async(request, runtime)

    def enable_load_balancer_access_log_with_options(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_load_balancer_access_log_with_options_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_load_balancer_access_log(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_load_balancer_access_log_with_options(request, runtime)

    async def enable_load_balancer_access_log_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_load_balancer_access_log_with_options_async(request, runtime)

    def get_health_check_template_attribute_with_options(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetHealthCheckTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_health_check_template_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetHealthCheckTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_health_check_template_attribute(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_health_check_template_attribute_with_options(request, runtime)

    async def get_health_check_template_attribute_async(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_health_check_template_attribute_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_attribute(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_listener_attribute_with_options(request, runtime)

    async def get_listener_attribute_async(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_attribute_with_options_async(request, runtime)

    def get_listener_health_status_with_options(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_health_status_with_options_async(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_health_status(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_listener_health_status_with_options(request, runtime)

    async def get_listener_health_status_async(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_health_status_with_options_async(request, runtime)

    def get_load_balancer_attribute_with_options(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_load_balancer_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_load_balancer_attribute(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_load_balancer_attribute_with_options(request, runtime)

    async def get_load_balancer_attribute_async(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_load_balancer_attribute_with_options_async(request, runtime)

    def list_acl_entries_with_options(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclEntries',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_entries_with_options_async(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclEntries',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_entries(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acl_entries_with_options(request, runtime)

    async def list_acl_entries_async(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acl_entries_with_options_async(request, runtime)

    def list_acl_relations_with_options(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_relations_with_options_async(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_relations(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acl_relations_with_options(request, runtime)

    async def list_acl_relations_async(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acl_relations_with_options_async(request, runtime)

    def list_acls_with_options(
        self,
        request: alb_20200616_models.ListAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_names):
            query['AclNames'] = request.acl_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acls_with_options_async(
        self,
        request: alb_20200616_models.ListAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_names):
            query['AclNames'] = request.acl_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acls(
        self,
        request: alb_20200616_models.ListAclsRequest,
    ) -> alb_20200616_models.ListAclsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_acls_with_options(request, runtime)

    async def list_acls_async(
        self,
        request: alb_20200616_models.ListAclsRequest,
    ) -> alb_20200616_models.ListAclsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_acls_with_options_async(request, runtime)

    def list_asyn_jobs_with_options(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsynJobs',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAsynJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asyn_jobs_with_options_async(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsynJobs',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAsynJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_asyn_jobs(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_asyn_jobs_with_options(request, runtime)

    async def list_asyn_jobs_async(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_asyn_jobs_with_options_async(request, runtime)

    def list_health_check_templates_with_options(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        if not UtilClient.is_unset(request.health_check_template_names):
            query['HealthCheckTemplateNames'] = request.health_check_template_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListHealthCheckTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_health_check_templates_with_options_async(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        if not UtilClient.is_unset(request.health_check_template_names):
            query['HealthCheckTemplateNames'] = request.health_check_template_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListHealthCheckTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_health_check_templates(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_health_check_templates_with_options(request, runtime)

    async def list_health_check_templates_async(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_health_check_templates_with_options_async(request, runtime)

    def list_listener_certificates_with_options(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listener_certificates_with_options_async(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenerCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listener_certificates(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    async def list_listener_certificates_async(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listener_certificates_with_options_async(request, runtime)

    def list_listeners_with_options(
        self,
        request: alb_20200616_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenersResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_with_options_async(
        self,
        request: alb_20200616_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenersResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners(
        self,
        request: alb_20200616_models.ListListenersRequest,
    ) -> alb_20200616_models.ListListenersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    async def list_listeners_async(
        self,
        request: alb_20200616_models.ListListenersRequest,
    ) -> alb_20200616_models.ListListenersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_with_options_async(request, runtime)

    def list_load_balancers_with_options(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.load_balancer_bussiness_status):
            query['LoadBalancerBussinessStatus'] = request.load_balancer_bussiness_status
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
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
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_load_balancers_with_options_async(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.load_balancer_bussiness_status):
            query['LoadBalancerBussinessStatus'] = request.load_balancer_bussiness_status
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
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
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_load_balancers(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_load_balancers_with_options(request, runtime)

    async def list_load_balancers_async(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_load_balancers_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: alb_20200616_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: alb_20200616_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: alb_20200616_models.ListRulesRequest,
    ) -> alb_20200616_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: alb_20200616_models.ListRulesRequest,
    ) -> alb_20200616_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_security_policies_with_options(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        if not UtilClient.is_unset(request.security_policy_names):
            query['SecurityPolicyNames'] = request.security_policy_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policies_with_options_async(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        if not UtilClient.is_unset(request.security_policy_names):
            query['SecurityPolicyNames'] = request.security_policy_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policies(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_security_policies_with_options(request, runtime)

    async def list_security_policies_async(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policies_with_options_async(request, runtime)

    def list_security_policy_relations_with_options(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicyRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPolicyRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policy_relations_with_options_async(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicyRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPolicyRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policy_relations(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_security_policy_relations_with_options(request, runtime)

    async def list_security_policy_relations_async(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policy_relations_with_options_async(request, runtime)

    def list_server_group_servers_with_options(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_ids):
            query['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_group_servers_with_options_async(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_ids):
            query['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_group_servers(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_server_group_servers_with_options(request, runtime)

    async def list_server_group_servers_async(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_server_group_servers_with_options_async(request, runtime)

    def list_server_groups_with_options(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.server_group_ids):
            query['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            query['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_groups_with_options_async(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.server_group_ids):
            query['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            query['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_groups(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_server_groups_with_options(request, runtime)

    async def list_server_groups_async(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_server_groups_with_options_async(request, runtime)

    def list_system_security_policies_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSystemSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSystemSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_security_policies_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSystemSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSystemSecurityPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_security_policies(self) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_system_security_policies_with_options(runtime)

    async def list_system_security_policies_async(self) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_system_security_policies_with_options_async(runtime)

    def list_tag_keys_with_options(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
    ) -> alb_20200616_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
    ) -> alb_20200616_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
    ) -> alb_20200616_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
    ) -> alb_20200616_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def remove_entries_from_acl_with_options(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entries):
            query['Entries'] = request.entries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntriesFromAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveEntriesFromAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_entries_from_acl_with_options_async(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entries):
            query['Entries'] = request.entries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntriesFromAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveEntriesFromAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_entries_from_acl(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_entries_from_acl_with_options(request, runtime)

    async def remove_entries_from_acl_async(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_entries_from_acl_with_options_async(request, runtime)

    def remove_servers_from_server_group_with_options(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveServersFromServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_servers_from_server_group_with_options_async(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveServersFromServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_servers_from_server_group(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_servers_from_server_group_with_options(request, runtime)

    async def remove_servers_from_server_group_async(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_servers_from_server_group_with_options_async(request, runtime)

    def replace_servers_in_server_group_with_options(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.added_servers):
            query['AddedServers'] = request.added_servers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.removed_servers):
            query['RemovedServers'] = request.removed_servers
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceServersInServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ReplaceServersInServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_servers_in_server_group_with_options_async(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.added_servers):
            query['AddedServers'] = request.added_servers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.removed_servers):
            query['RemovedServers'] = request.removed_servers
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceServersInServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ReplaceServersInServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_servers_in_server_group(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_servers_in_server_group_with_options(request, runtime)

    async def replace_servers_in_server_group_async(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_servers_in_server_group_with_options_async(request, runtime)

    def start_listener_with_options(
        self,
        request: alb_20200616_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StartListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_listener_with_options_async(
        self,
        request: alb_20200616_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StartListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_listener(
        self,
        request: alb_20200616_models.StartListenerRequest,
    ) -> alb_20200616_models.StartListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_listener_with_options(request, runtime)

    async def start_listener_async(
        self,
        request: alb_20200616_models.StartListenerRequest,
    ) -> alb_20200616_models.StartListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_listener_with_options_async(request, runtime)

    def stop_listener_with_options(
        self,
        request: alb_20200616_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StopListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StopListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_listener_with_options_async(
        self,
        request: alb_20200616_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StopListenerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StopListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_listener(
        self,
        request: alb_20200616_models.StopListenerRequest,
    ) -> alb_20200616_models.StopListenerResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_listener_with_options(request, runtime)

    async def stop_listener_async(
        self,
        request: alb_20200616_models.StopListenerRequest,
    ) -> alb_20200616_models.StopListenerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alb_20200616_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: alb_20200616_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: alb_20200616_models.TagResourcesRequest,
    ) -> alb_20200616_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alb_20200616_models.TagResourcesRequest,
    ) -> alb_20200616_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_acl_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAclAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAclAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_acl_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAclAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAclAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_acl_attribute(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_acl_attribute_with_options(request, runtime)

    async def update_acl_attribute_async(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_acl_attribute_with_options_async(request, runtime)

    def update_health_check_template_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_health_check_template_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_health_check_template_attribute(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_health_check_template_attribute_with_options(request, runtime)

    async def update_health_check_template_attribute_async(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_health_check_template_attribute_with_options_async(request, runtime)

    def update_listener_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_attribute(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_listener_attribute_with_options(request, runtime)

    async def update_listener_attribute_async(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_attribute_with_options_async(request, runtime)

    def update_listener_log_config_with_options(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not UtilClient.is_unset(request.access_log_tracing_config):
            query['AccessLogTracingConfig'] = request.access_log_tracing_config
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerLogConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_log_config_with_options_async(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not UtilClient.is_unset(request.access_log_tracing_config):
            query['AccessLogTracingConfig'] = request.access_log_tracing_config
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerLogConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_log_config(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_listener_log_config_with_options(request, runtime)

    async def update_listener_log_config_async(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_log_config_with_options_async(request, runtime)

    def update_load_balancer_address_type_config_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAddressTypeConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_address_type_config_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAddressTypeConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_address_type_config(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_address_type_config_with_options(request, runtime)

    async def update_load_balancer_address_type_config_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_address_type_config_with_options_async(request, runtime)

    def update_load_balancer_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_attribute(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_attribute_with_options(request, runtime)

    async def update_load_balancer_attribute_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_attribute_with_options_async(request, runtime)

    def update_load_balancer_edition_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerEdition',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerEditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_edition_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerEdition',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerEditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_edition(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_edition_with_options(request, runtime)

    async def update_load_balancer_edition_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_edition_with_options_async(request, runtime)

    def update_load_balancer_zones_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_zones_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_zones(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_zones_with_options(request, runtime)

    async def update_load_balancer_zones_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_zones_with_options_async(request, runtime)

    def update_rule_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_attribute(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rule_attribute_with_options(request, runtime)

    async def update_rule_attribute_async(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_attribute_with_options_async(request, runtime)

    def update_rules_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRulesAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRulesAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rules_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRulesAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRulesAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rules_attribute(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_rules_attribute_with_options(request, runtime)

    async def update_rules_attribute_async(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rules_attribute_with_options_async(request, runtime)

    def update_security_policy_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecurityPolicyAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateSecurityPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_policy_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecurityPolicyAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateSecurityPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_policy_attribute(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_security_policy_attribute_with_options(request, runtime)

    async def update_security_policy_attribute_async(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_security_policy_attribute_with_options_async(request, runtime)

    def update_server_group_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_attribute(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_attribute_with_options(request, runtime)

    async def update_server_group_attribute_async(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_attribute_with_options_async(request, runtime)

    def update_server_group_servers_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupServersAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupServersAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_servers_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupServersAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupServersAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_servers_attribute(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_servers_attribute_with_options(request, runtime)

    async def update_server_group_servers_attribute_async(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_servers_attribute_with_options_async(request, runtime)
